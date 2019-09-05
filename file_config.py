# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2019

import os

def server_url(server):
    return '%s://%s:%s/' % (server.proto, server.ip, server.port)

class FileWriter(object):
    def __init__(self, location):
        self._location = location

    def clean(self):
        pass
  
    def create(self, jobid, config):
        entry = {}
        entry['location'] = '/streams/job/' + str(jobid) + '/'
        entry['servers'] = config['servers']
        config['config_file'] = self._write_file(jobid, [entry])

    def delete(self, jobid, config):
        if 'config_file' in config:
            os.remove(config['config_file'])

    def update(self, jobid, old_config, config):
        pass

    def _write_file(self, jobid, entries):
        cfn = 'nginx-streams-job-%s.conf' % jobid
        tfn = cfn + '.tmp'
        fcfn = os.path.join(self._location, cfn)
        ftfn = os.path.join(self._location, tfn)
        with open(ftfn, 'w') as f:
            for entry in entries:
                self._config_contents(f, jobid, entry)
        os.rename(ftfn, fcfn)
        return fcfn

    def _config_contents(self, f, jobid, entry):
        f.write('upstream streams_job_%s {\n' % jobid)
        proto = None
        for server in entry['servers']:
            proto = server.proto
            f.write('  server %s;\n' % server_url(server))
            f.write('}\n')

        f.write('location %s {\n' % entry['location'])
        f.write('  proxy_set_header Host $host;\n')
        f.write('  proxy_set_header X-Real-IP $remote_addr;\n')
        f.write('  proxy_set_header X-Forwarded-Proto %s ;\n' % proto)
        f.write('  proxy_pass %s://streams_job_%s/;\n' % (proto, jobid))
        f.write('}\n')

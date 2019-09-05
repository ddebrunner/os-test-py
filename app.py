import streamsx.scripts.info as info

from file_config import FileWriter
from endpoint_monitor import EndpointMonitor

info.main()

cfg = FileWriter(location='/opt/streams_job_configs')

em = EndpointMonitor(config=cfg, job_filter=lambda job: True)
em.run()




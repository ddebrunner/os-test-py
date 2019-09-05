import streamsx.scripts.info as info
import time
import datetime

info.main()

from file_config import FileWriter
cfg = FileWriter(location='/opt/streams_job_configs')

em = EndpointMonitor(config=cfg, job_filter=lambda job: True)
em.run()




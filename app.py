import streamsx.scripts.info as info
import time
import datetime

info.main()

while True:
    print('Now:', datetime.datetime.now())
    time.sleep(300)

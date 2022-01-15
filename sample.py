import time
import psutil
print('Hello World')
while True:
    print('CPU:', psutil.cpu_percent(1))
    print('Mem usage:', psutil.virtual_memory()[2])
    time.sleep(10)

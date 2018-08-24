import time
print(time.localtime())
time.sleep(5)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(1)
print(time.time())
time.sleep(1)
print(time.strftime("%Y", time.localtime()))

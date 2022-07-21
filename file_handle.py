# ref: https://www.geeksforgeeks.org/get-current-timestamp-using-python/

import time
import datetime

ts = time.time()

print(ts, 'current time')
print(datetime.datetime.fromtimestamp(ts), 'current time')

time.sleep(1) # 1 sec

import subprocess
import os

subprocess.run("touch Foo", shell=True)
#subprocess.run("echo Hello >> Foo", shell=True)

# ref: https://note.nkmk.me/en/python-os-stat-file-timestamp/
#      https://www.geeksforgeeks.org/file-timestamps-mtime-ctime-and-atime-in-linux/
foo_stat = os.stat('Foo')

print (foo_stat.st_ctime, 'ctime (Change/Creation)')
print (foo_stat.st_mtime, 'mtime (Modification)') # time coming with ls -l
print (foo_stat.st_atime, 'atime (Access)')


print(datetime.datetime.fromtimestamp(foo_stat.st_atime), 'atime')

print (ts < foo_stat.st_atime) # True
print (ts > foo_stat.st_atime) # False

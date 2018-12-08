#!/usr/bin/python3

# https://myenigma.hatenablog.com/entry/2016/04/09/184215
#
# for cpu_count() func:
# https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
# for debug:
# python3 -m pdb multiprocess.py

from time import time
import subprocess
import multiprocessing

start=time()
procs=[]

ncore = multiprocessing.cpu_count()

# Popen starts the execution of a command
for i in range (ncore):
    proc = subprocess.Popen(['./process_id_get.py'],shell=True)
    procs.append(proc)

# communicate waits for the termination
for proc in procs:
    proc.communicate()

end=time()
print("%f sec" %(end-start))

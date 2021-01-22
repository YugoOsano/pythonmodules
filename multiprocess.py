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
    proc = subprocess.Popen(['./subdirectory_crawl.py'],shell=True)
    procs.append(proc)

# communicate waits for the termination
for proc in procs:
    proc.communicate()

end=time()
print("%f sec" %(end-start))

# subprocess.call is used to simply run shell commands;
# it is better than os.system as stoppable by Ctrl+C
# https://methane.hatenablog.jp/entry/20110509/1304956974
print("--- test of subprocess.call ---")
cmd = "grep -n process *.py"
subprocess.call(cmd, shell=True)

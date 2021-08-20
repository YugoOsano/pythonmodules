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

# check_output returns stdout as a string
s = subprocess.check_output(cmd, shell=True)
print(s)

# have to pay attention to exit status when using subprocess
# How do I see exit status of the command?
# $ (any command)
# $ echo $?
# https://bash.cyberciti.biz/guide/The_exit_status_of_a_command
s=""
try:
    # this is equivalent to check_output
    # The recommended approach is to use the run() function for all use cases
    # https://docs.python.org/3/library/subprocess.html#call-function-trio
    # return type of run is subprocess.CompletedProcess
    s = subprocess.run(('diff', 'test_unittest.py', 'create_HDF5.py'),\
                       check=True, stdout=subprocess.PIPE).stdout
except subprocess.CalledProcessError as e:
    print("--- came to exception ---")
    # https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError
    print("return code: ", e.returncode) # 1 when there is difference, 2 when no file
    print(e.output) # type is 'bytes'
    #exit()
print(s)

print ("------------------")
try:
    s = subprocess.run(('./exit1'),\
                       check=True, stdout=subprocess.PIPE).stdout
except subprocess.CalledProcessError as e:
    print("--- exit1 exception ---")
    #import pdb; pdb.set_trace()
    print("return code: ", e.returncode)# type is int
    print(e.output)

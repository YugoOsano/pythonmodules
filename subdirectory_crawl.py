#!/usr/bin/python3

import os
import pathlib

pid = os.getpid()
print ("process id is: ", pid)

# recursively crawl subdirectories
# see StackOverFlow 13131497

# take the extension from a file (path)
# https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/

for root, dirs, files in os.walk('./'):
    filepaths = [os.path.join(root, f) for f in files]
    for filepath in filepaths:
        if (pathlib.Path(filepath).suffix == '.py'):
            print(filepath)

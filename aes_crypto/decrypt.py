# usage
# cat [encrypted text] | python3 decrypt.py

import sys
import getpass
import my_aes
import base64

password = getpass.getpass('password> ')

txt     = sys.stdin.buffer.read()
to_read = base64.b64decode(txt)
dec = my_aes.decrypt(to_read, password)
sys.stdout.buffer.write(dec)

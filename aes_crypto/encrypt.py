# usage
# cat [file to encrypt] | python3 encrypt.py > [file to save]

import sys
import getpass
import my_aes
import base64

password = getpass.getpass('password> ')
password2 = getpass.getpass('confirm> ')
if password != password2:
    print('Passwords do not match.')
    sys.exit(0)
enc = my_aes.encrypt(sys.stdin.buffer.read(), password)
to_write = base64.b64encode(enc)
sys.stdout.buffer.write(to_write)

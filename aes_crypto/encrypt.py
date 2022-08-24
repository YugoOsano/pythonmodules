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

# similar encryption gained by:
# cat [file to encrypt] | openssl aes-256-cbc -base64 -pbkdf2 > [file of encrypted text]

# decrypted by:
# cat [file of encrypted text] | openssl aes-256-cbc -d -base64 -pbkdf2 > [file of original text]

# options are shown by  openssl help

# append the following functions in .bashrc
# (see https://stackoverflow.com/questions/7131670/make-a-bash-alias-that-takes-a-parameter)
# aes_encrypt () {
#                cat $1 | openssl aes-256-cbc -base64 -pbkdf2
#                }
# aes_decrypt () {
#                cat $1 | openssl aes-256-cbc -d -base64 -pbkdf2
#                }

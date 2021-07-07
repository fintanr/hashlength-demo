#!/usr/bin/env python3
#
# Quick example of hash length versus password length and contents 
#
# July 7th 2021, @fintanr

import bcrypt
import string
import random

man_chars = string.ascii_letters + string.digits + string.punctuation

print("Random Password".ljust(60), "Length", "Hash Length")

for i in range(8, 64, 4):
    passwd = ( ''.join(random.choice(man_chars) for j in range(i)))
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd.encode('utf8'), salt)
    print(passwd.ljust(60), str(len(passwd.encode('utf8'))).ljust(7), len(hashed))

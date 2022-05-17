#!/usr/bin/env python3
#This is the decryption scrypt for loki.py
#For educational purposes only

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == "loki.py" or file == "thekey.key" or file == "thor.py":
    continue
  if os.path.isfile(file):
    files.append(file)
 
key = Fernet.generate_key()

with open("thekey.key", "rb") as key:
  secretkey = key.read()
  
for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_decrypted = fernet(secretkey).decrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_decrypted)

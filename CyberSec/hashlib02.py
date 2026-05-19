import hashlib

with open("wordlist.txt", "r") as f:
    for kelime in f:
        kelime = kelime.strip()
        
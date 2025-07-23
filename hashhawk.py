# HashHawk - Advanced Hash Cracker
# Coded by KRISHNA

import hashlib
import sys

BANNER = r"""
 _   _           _     _    _                 
| | | | __ _ ___| |__ | | _| |__   ___  _ __  
| |_| |/ _` / __| '_ \| |/ / '_ \ / _ \| '_ \ 
|  _  | (_| \__ \ | | |   <| | | | (_) | | | |
|_| |_|\__,_|___/_| |_|_|\_\_| |_|\___/|_| |_|

       HashHawk - Bruteforce Hash Cracker
                Coded by KRISHNA
"""

print(BANNER)

if len(sys.argv) != 4:
    print("Usage: python hashhawk.py <hash> <algorithm> <wordlist.txt>")
    print("Supported algorithms: md5, sha1, sha256, sha512")
    sys.exit(1)

target_hash = sys.argv[1]
algorithm = sys.argv[2].lower()
wordlist = sys.argv[3]

try:
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        passwords = f.read().splitlines()
except FileNotFoundError:
    print(f"[!] Wordlist not found: {wordlist}")
    sys.exit(1)

def hash_crack(hash_value, algo, words):
    for word in words:
        word = word.strip()
        if algo == "md5":
            hashed = hashlib.md5(word.encode()).hexdigest()
        elif algo == "sha1":
            hashed = hashlib.sha1(word.encode()).hexdigest()
        elif algo == "sha256":
            hashed = hashlib.sha256(word.encode()).hexdigest()
        elif algo == "sha512":
            hashed = hashlib.sha512(word.encode()).hexdigest()
        else:
            print("[!] Unsupported algorithm.")
            return

        if hashed == hash_value:
            print(f"[✔] Password found: {word}")
            return
    print("[✘] Password not found in wordlist.")

hash_crack(target_hash, algorithm, passwords)

import hashlib
from pathlib import Path

_WORDLIST = Path(__file__).resolve().parent.parent / "data" / "wordlists" / "wordlist.txt"
with open(_WORDLIST, "r") as f:
    for kelime in f:
        kelime = kelime.strip()
        
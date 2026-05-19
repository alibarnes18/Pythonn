import hashlib

def hash_kirici(hedef_hash, wordlist_dosya, algoritma="md5"):

    bulundu = False

    with open(wordlist_dosya, "r", encoding="utf-8") as f:
        for kelime in f:
            kelime = kelime.strip()

            if algoritma == "md5":
                hesaplanan = hashlib.md5(kelime.encode()).hexdigest()

            elif algoritma == "sha1":
                hesaplanan = hashlib.sha1(kelime.encode()).hexdigest()

            else:
                print("Desteklenmeyen algoritma")
                return

            if hesaplanan == hedef_hash:
                print(f"Şifre bulundu: {kelime}")
                bulundu = True
                return kelime

    if not bulundu:
        print("Şifre bulunamadı")
        return None



hash_kirici("482c811da5d5b4bc6d497ffa98491e38", "wordlist.txt", "md5")

hash_kirici(
    "cbfdac6008f9cab4083784cbd1874f76618d2a97",
    "wordlist.txt",
    "sha1"
)
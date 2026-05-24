import re

metin = "kullanıcı 42 kez denedi"
sonuc = re.search(r"\d+", metin)
print(sonuc.group())
 # Ekstra:#Özel karakter kontrolü ekle (!, @, # gibi) — puan 4'e çıksın //
#Süper ekstra:  Şifreyi liste olarak al, her birini analiz et ve en güçlüsünü bul


# Her şeyi fonksiyona böl!

def uzunluk_kontrol(sifre):
    return len(sifre) >= 8 # True/False

def buyuk_harf_var_mi(sifre):
    return any(c.isupper() for c in sifre)

def rakam_var_mi(sifre):
    return any(c.isdigit() for c in sifre)

def guc_hesapla(sifre):
    puan = 0
    if uzunluk_kontrol(sifre): puan += 1
    if buyuk_harf_var_mi(sifre): puan += 1
    if rakam_var_mi(sifre): puan += 1
    if puan == 3: return "💪 Güçlü"
    elif puan == 2: return "😐 Orta"
    else: return "😱 Zayıf"

# Test et
sifre = input("Şifre gir: ")
print(guc_hesapla(sifre))
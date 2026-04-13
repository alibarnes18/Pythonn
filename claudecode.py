# Şifre analiz aracı

def uzunluk_kontrol(sifre):
    return len(sifre) >= 8

def buyuk_harf_var_mi(sifre):
    return any(c.isupper() for c in sifre)

def rakam_var_mi(sifre):
    return any(c.isdigit() for c in sifre)

def ozel_karakter_var_mi(sifre):
    ozel_karakterler = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"
    return any(c in ozel_karakterler for c in sifre)

def puan_hesapla(sifre):
    puan = 0
    if uzunluk_kontrol(sifre):
        puan += 1
    if buyuk_harf_var_mi(sifre):
        puan += 1
    if rakam_var_mi(sifre):
        puan += 1
    if ozel_karakter_var_mi(sifre):
        puan += 1
    return puan

def guc_hesapla(sifre):
    puan = puan_hesapla(sifre)

    if puan == 4:
        return "💪 Güçlü"
    elif puan == 3:
        return "🙂 İyi"
    elif puan == 2:
        return "😐 Orta"
    else:
        return "😱 Zayıf"

def sifre_analiz_et(sifre):
    print(f"\nŞifre: {sifre}")
    print(f"Uzunluk yeterli mi? {'Evet' if uzunluk_kontrol(sifre) else 'Hayır'}")
    print(f"Büyük harf var mı? {'Evet' if buyuk_harf_var_mi(sifre) else 'Hayır'}")
    print(f"Rakam var mı? {'Evet' if rakam_var_mi(sifre) else 'Hayır'}")
    print(f"Özel karakter var mı? {'Evet' if ozel_karakter_var_mi(sifre) else 'Hayır'}")
    print(f"Puan: {puan_hesapla(sifre)}/4")
    print(f"Sonuç: {guc_hesapla(sifre)}")

def en_guclu_sifreyi_bul(sifreler):
    en_guclu = sifreler[0]
    en_yuksek_puan = puan_hesapla(en_guclu)

    for sifre in sifreler:
        mevcut_puan = puan_hesapla(sifre)
        if mevcut_puan > en_yuksek_puan:
            en_yuksek_puan = mevcut_puan
            en_guclu = sifre

    return en_guclu, en_yuksek_puan


# Kullanıcıdan şifreleri liste olarak al
sifreler = input("Şifreleri virgülle ayırarak gir: ").split(",")

# Baştaki ve sondaki boşlukları temizle
sifreler = [sifre.strip() for sifre in sifreler]

# Her bir şifreyi analiz et
for sifre in sifreler:
    sifre_analiz_et(sifre)

# En güçlü şifreyi bul
en_guclu, puan = en_guclu_sifreyi_bul(sifreler)
print("\n=== EN GÜÇLÜ ŞİFRE ===")
print(f"En güçlü şifre: {en_guclu}")
print(f"Puanı: {puan}/4")
print(f"Durumu: {guc_hesapla(en_guclu)}")
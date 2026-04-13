Tamam — bunu en doğru şekilde yapalım: **kod + mantık + mini quiz**.

Ama önemli: sadece “kopyala-yapıştır” değil, her parçayı anlayarak ilerleyeceğiz.

---

# 🔥 1. ADIM — THREADING (HIZLANDIRMA)

## 🧠 Mantık

Normalde:

* 1 port → dene → bekle

Threading ile:

* aynı anda birden fazla port dene

---

## 💻 KOD (öğrenme versiyonu)

```python
import socket
import threading

def port_ac_mi(ip, port, acik):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        s.close()
        print(f"✅ Port {port} — AÇIK")
        acik.append(port)
    except:
        print(f"❌ Port {port} — kapalı")


def scanner(ip, portlar):
    acik = []
    threads = []

    print(f"\n{ip} taranıyor...\n")

    for port in portlar:
        t = threading.Thread(target=port_ac_mi, args=(ip, port, acik))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return acik


hedef = "scanme.nmap.org"
portlar = range(1, 1025)

sonuc = scanner(hedef, portlar)

print(f"\nToplam {len(sonuc)} açık port bulundu")
```

---

# 🧠 ŞİMDİ ÖĞRENME KISMI (çok önemli)

## 🔹 Thread nedir?

👉 Aynı anda çalışan mini işlem

---

## 🔹 Şu satır ne yapıyor?

```python
t = threading.Thread(target=port_ac_mi, args=(ip, port, acik))
```

👉 “bu fonksiyonu ayrı bir worker gibi çalıştır”

---

## 🔹 join ne yapıyor?

```python
t.join()
```

👉 “hepsi bitmeden devam etme”

---

# ⚠️ KRİTİK NOKTA

```python
acik.append(port)
```

👉 bütün thread’ler aynı listeye yazıyor

---

# 🧪 QUIZ TIME (şimdi sana)

Cevaplarını yaz, ben kontrol edeceğim:

---

## ❓ Soru 1

Threading kullanmazsak program nasıl çalışır?

A) Aynı anda çalışır
B) Tek tek sırayla çalışır
C) Hiç çalışmaz

---

## ❓ Soru 2

`threading.Thread()` ne yapar?

A) Dosya açar
B) Yeni bir paralel işlem başlatır
C) Port kapatır

---

## ❓ Soru 3

`join()` ne işe yarar?

A) Thread başlatır
B) Programı hızlandırır
C) Tüm thread’ler bitmeden devam etmemeyi sağlar

---

## ❓ Soru 4 (mantık)

Neden threading kullanıyoruz?

👉 1 cümle ile açıkla

---

## ❓ Soru 5 (düşünme)

Eğer timeout = 5 saniye olursa ne olur?

---

# 🚀 SONRAKİ ADIM

Sen quiz’i cevapladıktan sonra:

👉 JSON output öğreteceğim
👉 sonra service detection
👉 sonra bunu “mini nmap tool” haline getireceğiz

Hazırsan cevaplarını yaz 👍

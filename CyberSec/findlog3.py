satirlar = [
    "192.168.1.1 POST /login 200 success\n",
    "10.0.0.2 POST /login 401 failed\n",
    "10.0.0.2 POST /login 401 failed\n",
    "10.0.0.2 POST /login 401 failed\n",
    "192.168.1.5 POST /login 200 success\n",
    "172.16.0.9 POST /login 401 failed\n",
    "10.0.0.2 POST /login 401 failed\n",
    "172.16.0.9 POST /login 401 failed\n",
    "10.0.0.2 POST /login 401 failed\n",
    "172.16.0.9 POST /login 401 failed\n",
    "172.16.0.9 POST /login 401 failed\n",
]

with open("web.log", "w") as f:
    f.writelines(satirlar)

print("Web.log oluşturuldu")

#web.log dosyasını oku
#401 failed geçen satırlardaki IP'leri say
#4 veya daha fazla hata yapan IP'leri tespit et
#Sonucu web_blocked.txt'e yaz


satirlar = [
    "INFO 192.168.1.1 login success\n",
    "ERROR 10.0.0.2 login failed\n",
    "ERROR 10.0.0.2 login failed\n",
    "ERROR 10.0.0.2 login failed\n",
    "ERROR 10.0.0.2 login failed\n",
    "INFO 192.168.1.5 login success\n",
    "ERROR 172.16.0.9 login failed\n",
    "ERROR 172.16.0.9 login failed\n",
    "INFO 192.168.1.1 login success\n",
    "ERROR 10.0.0.2 login failed\n",
]

with open("brute.log", "w") as f:
    f.writelines(satirlar)

print("brute.log oluşturuldu ")
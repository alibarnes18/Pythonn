satirlar = [
    "INFO 192.168.1.1 80 login success\n",
    "ERROR 10.0.0.2 22 login failed\n",
    "INFO 192.168.1.5 443 logout\n",
    "ERROR 172.16.0.9 21 login failed\n",
    "ERROR 10.0.0.2 22 login failed\n",
    "INFO 192.168.1.1 80 login success\n",
    "ERROR 172.16.0.9 22 login failed\n",
    "INFO 192.168.1.5 443 login success\n",
    "ERROR 10.0.0.2 21 login failed\n",
    "INFO 192.168.1.1 80 logout\n",
]

with open(r"c:\Users\alioz\Downloads\Funda. of Py\CyberSec\network.log", "w") as f:
    f.writelines(satirlar)

print("network.log oluşturuldu")
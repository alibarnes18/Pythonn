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

from pathlib import Path

_LOG = Path(__file__).resolve().parent / "network.log"
with open(_LOG, "w") as f:
    f.writelines(satirlar)

print("network.log oluşturuldu")
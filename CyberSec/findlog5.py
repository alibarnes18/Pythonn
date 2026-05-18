satirlar = [
    "May 18 10:01:01 server sshd: Failed password for root from 185.220.101.5 port 4444\n",
    "May 18 10:01:02 server sshd: Failed password for root from 185.220.101.5 port 4444\n",
    "May 18 10:01:03 server sshd: Failed password for admin from 192.168.1.9 port 2222\n",
    "May 18 10:01:04 server sshd: Accepted password for user from 192.168.1.1 port 22\n",
    "May 18 10:01:05 server sshd: Failed password for root from 185.220.101.5 port 4444\n",
    "May 18 10:01:06 server sshd: Failed password for admin from 45.33.32.156 port 1234\n",
    "May 18 10:01:07 server sshd: Failed password for root from 185.220.101.5 port 4444\n",
    "May 18 10:01:08 server sshd: Failed password for admin from 45.33.32.156 port 1234\n",
    "May 18 10:01:09 server sshd: Failed password for root from 185.220.101.5 port 4444\n",
    "May 18 10:01:10 server sshd: Failed password for admin from 45.33.32.156 port 1234\n",
]

with open("ssh.log", "w") as f:
    f.writelines(satirlar)
# -*- coding: utf-8 -*-
import os

ip = '10.120.11.11'
response = os.system("ping " + ip)

if response == 0:
        print(f"O host {ip} está ativo.")
else:
    print(f"O host {ip} está inativo ou não respondeu.")
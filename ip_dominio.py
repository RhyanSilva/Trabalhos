#!/usr/bin/python
#You can change the name this file , and Start with code : python <name.py> or python ip_dominio.py
from socket import *
while True:
    rb = int(input("\n0-Sair\n1-Ip Dominio\n\n>>"))
    if(rb==0):
        print("Saindo, Obrigado!")
        break
    else:
        vit= str(input("Site: "))
        p=gethostbyname(vit)
        print("\nIP do site é: ",p)


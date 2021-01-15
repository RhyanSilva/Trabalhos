#!/usr/bin/python
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


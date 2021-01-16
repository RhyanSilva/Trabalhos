#!/usr/bin/python
#You can change the name this file , and Start with code : python <name.py> or python coleta.py
from socket import *
import socket
import whois


def scan(dominios):
    try:
        dominio = dominios
        s_whois = whois.whois(dominio)
        print (s_whois.text)
        arquivo = open(dominios + '_whois.txt', 'w')
        arquivo.write(s_whois.text)
    except:
        pass

p=scan(input("Qual site para o Whois ? "))


while True:
    rb = int(input("\n0-Sair\n1-Ip do site\n\n>>"))
    if(rb==0):
        print("Saindo e entrando no Scan !")
        break
    else:
        vit= str(input("Site: "))
        p=gethostbyname(vit)
        print("\nIP do site é: ",p)



host=input("Ip do Alvo: ")
for porta in range(20, 100):
    net=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    net.settimeout(1)
    resultado=net.connect_ex((host, porta))
    net.close()
    if resultado == 0:
        print(f'Portas abertas: {porta}')


print('Script by : Silva')








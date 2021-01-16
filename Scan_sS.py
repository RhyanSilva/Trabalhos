#!/usr/bin/python3
import socket
ip = input("Ip alvo: ")
portas = []
ge = 0
while ge < 5:
    portas.append(int(input("porta: ")))
    ge += 1
for port in portas:
    neti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    neti.settimeout(0.05)
    cod = neti.connect_ex((ip, port)) 
    if cod == 0: #0 = Success
        print (str(port) + " -> Aberta")
    else:
        print (str(port) + " -> Fechada")


print ("Finalizado ... Script by : Silva")

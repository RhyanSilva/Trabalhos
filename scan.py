#!usr/bin/python
#You can change the name this file , and Start with code : python <name.py> or python scan.py
import socket
host=input("Ip do Alvo: ")
for porta in range(20, 1000):
    net=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    net.settimeout(1)
    resultado=net.connect_ex((host, porta))
    net.close()
    if resultado == 0:
        print(f'Portas abertas: {porta}')

print('Script by: Silva')

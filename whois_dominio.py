#usr/bin/python
##You can change the name this file , and Start with code : python <name.py> or python whois_dominio.py
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

print('Script by : Silva')

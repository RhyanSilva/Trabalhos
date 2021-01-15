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

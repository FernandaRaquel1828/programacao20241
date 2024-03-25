from pprint import pprint
lista = [ ]
for i in range (4):
    tempo = int(input("digite um ano:"))
    if (tempo % 4 == 0 and tempo % 100 != 0) or tempo % 400 == 0: 
        bissexto = True
        x = {"ano": tempo, "bissexto": bissexto}
        lista.append(x)
    else :
        bissexto = False
        x = {"ano": tempo, "bissexto": bissexto}
        lista.append(x)

pprint(lista)

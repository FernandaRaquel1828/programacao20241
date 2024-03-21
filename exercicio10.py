x = {"ano": tempo, "bissexto": bissexto}
lista = [ ]
for i in range (4):
    tempo = int(input("digite um ano:"))
    if tempo % 4 == 0 and tempo % 100 != 0 or tempo % 400 == 0: 
        bissexto = True
        lista.append(x)
    else :
        bissexto = False
        lista.append(x)

print(lista)

lista = []
x = 10

while x >= 0 :
    numero = int(input("digite 1 numeros diferentes: "))
    if numero not in lista:
        lista.append(numero)
    x = x - 1
print(lista)
  

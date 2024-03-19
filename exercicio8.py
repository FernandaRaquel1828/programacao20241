from random import choice
x = { }
lista = [ ]

sair = " "
while True: 
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    sair = input("deseja sair? digite 'fim' ")
    
    x = {'Nome': nome, 'Idade':idade}
    lista.append(x)
    if sair == "fim":
        break
idades = [pessoa['Idade'] for pessoa in lista]

print(lista)
print(len(lista))
print(sum(idades)/len(idades))
print(choice(lista))

       

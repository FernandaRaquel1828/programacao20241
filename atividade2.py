lista = []
maiorque170 = []

while True: 
  pessoa = input("digite nome, peso e altura do usuário ")
  nome = pessoa.split("-")[0]
  dados = [float(dado)for dado in pessoa.split("-")[1:]]
  imc = (dados[0])/(dados[1]**2)
  cadastro = {"nome": nome ,"peso":dados[0] ,"altura": dados[1], "IMC": imc }
  lista.append(cadastro)
  sair = input("deseja sair? digite nao para continuar ou FIM para sair").upper()

  if sair == "FIM":
    break

for i in lista:
    if i["altura"] > 1.70:
        maiorque170.append(i)

print('\nLISTA:')
print(*lista, sep='\n')

print('\nIMC:')
sorted_imc = sorted(lista, key=lambda x: x['IMC'])
print(*sorted_imc, sep='\n')

print('\nPeso:')
sorted_cad = sorted(lista, key=lambda x: x['peso'])
print(*sorted_cad, sep='\n')

print('\nMAIOR QUE 70:')
print(maiorque170)

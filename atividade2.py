lista = []
maiorque170 = []
def ord_peso(item):
  return("peso")
def ord_imc(item2):
  return("IMC")
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

cad = sorted(lista, key = ord_peso)
imc1 = sorted(lista,key = ord_imc)
print(lista)
print(imc1)
print(cad)
print(maiorque170)



saque = int(input("digite quanto vc quer sacar: "))
if saque <=1000: 
    cem = int(saque/100)
    saque = saque % 100

    cinquenta = int(saque/50)
    saque = saque % 50

    vinte = int(saque/20)
    saque = saque %20

    dez = int(saque/10)
    saque = saque % 10

    cinco = int(saque/5)
    saque = saque % 5

    print("notas 100", cem)
    print("notas 50", cinquenta)
    print("notas 20", vinte)
    print("notas 10", dez)
    print("notas 5", cinco)
else:
    print("não é possivel sacar esse valor")


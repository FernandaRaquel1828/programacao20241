sair =  " "
l1 = [ ]
while sair  != "fim" :
    sair  =  input("digite um numero ou fim para sair : ")
    if sair != "fim":
        l1.append(int(sair))
print(l1)
print([x * 3 for x in l1])
    
    

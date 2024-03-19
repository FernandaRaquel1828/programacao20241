lista = [ ]
for i in range (4):
    tempo = int(input("digite um ano:"))
    if tempo % 4 == 0 and tempo % 100 != 0 or tempo % 400 == 0: 
        print(f"o ano {tempo} é bissexto")
    else :
        print(f"o ano {tempo} não é bissexto")
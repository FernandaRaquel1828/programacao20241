def calendario (mes):
    meses = ["janeiro", "fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    return meses[int(mes)-1]



data = input("informe sua data de nascimento separado por '/'").split("/")
print (f"Voce nasceu em {data [0]} de {calendario (data[-1])} de {data[2]}")




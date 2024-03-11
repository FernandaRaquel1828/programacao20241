data = input("informe sua data de nascimento separado por '/'").split("/")
mes = ["janeiro", "fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

mesi = int(data[1])
print (f"Voce nasceu em {data [0]} de {mes[mesi -1]} de {data[2]}")


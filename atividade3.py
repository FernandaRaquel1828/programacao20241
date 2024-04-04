def montante(c,tj,t):
    m = c*(1 + tj)**t
    return m

def juros_aplicado(m,c):
    j = m - c
    return j
capital = float(input("Digite o valor inicial: "))
taxa_juros = float(input("digite a taxa de juros: "))
taxa_decimal = taxa_juros / 100
tempo = float(input("digite o tempo"))
montante_final = montante(capital,taxa_decimal,tempo)
juros_total = juros_aplicado(capital,montante_final)
print(f"o montante final é {montante_final}")
print(f"o juros aplicado foi de {juros_total}")
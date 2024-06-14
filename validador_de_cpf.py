cpf = input("digite seu cpf: ").replace('.','').replace('-','')
cpf_lista = []
while True:
    for a, b in enumerate(cpf):
        item = int(cpf[a])
        cpf_lista.append(item)
    break
cpf_lista.pop()
cpf_lista.pop()
lista_cpf_resultado_soma= []

rangi = range(10, 1,-1)
d = 10
for a, b in enumerate(cpf_lista):
    resultado  = b * d
    d -= 1
    lista_cpf_resultado_soma.append(resultado)

print(lista_cpf_resultado_soma)

soma =0
for a, b in enumerate(lista_cpf_resultado_soma):
    soma  += b

multiplicacao_por_10 = soma * 10
print(multiplicacao_por_10)
resto_divisão = multiplicacao_por_10 % 11
print(resto_divisão)

if resto_divisão > 9:
    resto_divisão = 0
else:
    resto_divisão = resto_divisão

print(resto_divisão)

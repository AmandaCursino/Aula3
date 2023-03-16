numeros = [10, 20, 30, 40, 50]

maior_numero = numeros[0]
#inicializando a variavel que irá armazenar o maior numero
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
#usando um loop for para percorrer a lista e encontrar maior numero

print('O maior numero na lista é: ', maior_numero)

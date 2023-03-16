lista_com_duplicatas = [1, 2, 3, 1, 4, 2, 5, 6, 3, 7, 8, 5, 9]

lista_sem_duplicatas = []
#inicializando uma lista vazia para armazenar os elementos unicos

while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) #pop é usado para remover o elemento
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
#usando um loop while para percorrer a lista e remover os elementos duplicados

    print('A lista sem duplicatas é:', lista_sem_duplicatas)
    
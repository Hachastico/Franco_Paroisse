#1.Desarrollar una función recursiva que permita listar los elementos de vector/lista de
#manera inversa al que están cargados. Preferentemente la función solo debe tener un
#parámetro que es la lista de elementos

def lista_inversa(lista):
    #lista vacia: no hay accion
    if not lista:
        return
    #lista inversa:
    lista_inversa(lista[1:])
    print(lista[0])

lista_test = [1,11,21,1211,111221,312211,13112221,1113213211,'segundo','primero']
lista_inversa(lista_test)
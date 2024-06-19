#Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar
from cola import Cola

def count_ocurrencia(cola, objetivo):
    cont = 0
    size = cola.size()
    for _ in range(size):
        element = cola.atention()
        if element == objetivo:
            cont += 1
    cola.arrive(element)
    return cont

TarElem = Cola()
ColaOcurren = [1,6,8,5,1,7,8,1,8,5,4,1,3,6,1]
for el in ColaOcurren:
    TarElem.arrive(el)

target = 8
print(f"Las ocurrencias de {target} en la cola es: {count_ocurrencia(TarElem, target)}")
#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire 
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que 
#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

from pila import Pila

def interseccion_pilas(pila1, pila2):
    elementos_pila1 = pila1.obtain_elements()
    elementos_pila2 = pila2.obtain_elements()

    conjunto1 = set(elementos_pila1)
    conjunto2 = set(elementos_pila2)

    interseccion = conjunto1.intersection(conjunto2)

    pila_interseccion = Pila()
    for elemento in interseccion:
        pila_interseccion.push(elemento)

    return pila_interseccion

PJ_EP_5 = Pila()
PJ_EP_5.push("Han Solo")
PJ_EP_5.push("Yoda")
PJ_EP_5.push("Obi-Wan Kenobi")
PJ_EP_5.push("Palpatine")
PJ_EP_5.push("Luke Skywalker")
PJ_EP_5.push("Leia Organa")

PJ_EP_7 = Pila()
PJ_EP_7.push("Rey")
PJ_EP_7.push("Kylo Ren")
PJ_EP_7.push("Luke Skywalker")
PJ_EP_7.push("Han Solo")
PJ_EP_7.push("Leia Organa")

pila_intersec = interseccion_pilas(PJ_EP_5,PJ_EP_7)
print("Los siguientes personajes aparecen en ambos episodios: ")
print(pila_intersec.obtain_elements())
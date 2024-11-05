#Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios 
#para resolver las siguientes tareas:

from grafo_star_wars import Grafo

#Grafo
grafo_star_wars = Grafo()

#Personajes (Punto (D) incluido)
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

#Agregar personajes
grafo_star_wars.agregar_arista("Luke Skywalker", "Yoda", 3)
grafo_star_wars.agregar_arista("Han Solo", "Chewbacca", 6)
grafo_star_wars.agregar_arista("Luke Skywalker", "Leia", 4)
grafo_star_wars.agregar_arista("Darth Vader", "Yoda", 2)
grafo_star_wars.agregar_arista("Luke Skywalker", "Darth Vader", 5)
grafo_star_wars.agregar_arista("Yoda", "Boba Fett", 1)
grafo_star_wars.agregar_arista("Yoda", "C-3PO", 1)
grafo_star_wars.agregar_arista("Leia", "Han Solo", 6)
grafo_star_wars.agregar_arista("C-3PO", "R2-D2", 5)
grafo_star_wars.agregar_arista("BB-8", "Rey", 2)
grafo_star_wars.agregar_arista("Kylo Ren", "Rey", 3)

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la 
#cantidad de episodios en los que aparecieron juntos ambos personajes que se
#relacionan;
print('A)')
arbol_expansion = grafo_star_wars.kruskal()
print("Arbol de expansion minima:")
for personaje1, personaje2, episodios in arbol_expansion:
    print(f"{personaje1} - {personaje2}: {episodios} episodios")

#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
print()
print('B)')
if grafo_star_wars.contiene_yoda(arbol_expansion):
    print("El arbol de expansion minima contiene a Yoda.")
else:
    print("El arbol de expansion minima no contiene a Yoda.")

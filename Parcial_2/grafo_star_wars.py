#Grafo modificado para parcial
class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_personaje(self, personaje):
        if personaje not in self.vertices:
            self.vertices[personaje] = {}

    def agregar_arista(self, personaje1, personaje2, episodios):
        self.agregar_personaje(personaje1)
        self.agregar_personaje(personaje2)
        self.vertices[personaje1][personaje2] = episodios
        self.vertices[personaje2][personaje1] = episodios

    def obtener_aristas(self):
        aristas = []
        for personaje, adyacentes in self.vertices.items():
            for adyacente, episodios in adyacentes.items():
                aristas.append((personaje, adyacente, episodios))
        return aristas

    def kruskal(self):
        aristas = self.obtener_aristas()
        aristas.sort(key=lambda x: x[2])

        padre = {}
        for vertice in self.vertices:
            padre[vertice] = vertice

        def encontrar(v):
            if padre[v] != v:
                padre[v] = encontrar(padre[v])
            return padre[v]

        def union(v1, v2):
            raiz1 = encontrar(v1)
            raiz2 = encontrar(v2)
            if raiz1 != raiz2:
                padre[raiz2] = raiz1

        arbol_expansion = []
        for personaje1, personaje2, episodios in aristas:
            if encontrar(personaje1) != encontrar(personaje2):
                union(personaje1, personaje2)
                arbol_expansion.append((personaje1, personaje2, episodios))

        return arbol_expansion

    def contiene_yoda(self, arbol_expansion):
        for personaje1, personaje2, episodios in arbol_expansion:
            if personaje1 == "Yoda" or personaje2 == "Yoda":
                return True
        return False

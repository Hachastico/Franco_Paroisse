#Cree una clase de arbol modificado dentro de la actividad por que la importacion me causaba problemas
class Nodo:
    def __init__(self, valor, data):
        self.valor = valor  # valor para ordenar el arbol
        self.data = data  # datos completos del pokemon
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, data):
        if not self.raiz:
            self.raiz = Nodo(valor, data)
        else:
            self._insertar_recursivo(self.raiz, valor, data)

    def _insertar_recursivo(self, nodo, valor, data):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor, data)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor, data)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor, data)
            else:
                self._insertar_recursivo(nodo.derecho, valor, data)

    def inorden(self, nodo, resultado=[]):
        if nodo:
            self.inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.data)
            self.inorden(nodo.derecho, resultado)
        return resultado
#b)
    def buscar_nombre(self, nombre):
        resultado = []
        self._buscar_nombre_recursivo(self.raiz, nombre, resultado)
        return resultado

    def _buscar_nombre_recursivo(self, nodo, nombre, resultado):
        if nodo is not None:
            if nombre.lower() in nodo.data['name'].lower():
                resultado.append(nodo.data)
            self._buscar_nombre_recursivo(nodo.izquierdo, nombre, resultado)
            self._buscar_nombre_recursivo(nodo.derecho, nombre, resultado)

    def buscar_numero(self, numero):
        return self._buscar_numero_recursivo(self.raiz, numero)

    def _buscar_numero_recursivo(self, nodo, numero):
        if nodo is None:
            return None
        if nodo.valor == numero:
            return nodo.data
        elif numero < nodo.valor:
            return self._buscar_numero_recursivo(nodo.izquierdo, numero)
        else:
            return self._buscar_numero_recursivo(nodo.derecho, numero)
#c)
    def buscar_tipo(self, tipo, resultado=[]):
        self._buscar_tipo_recursivo(self.raiz, tipo, resultado)
        return resultado

    def _buscar_tipo_recursivo(self, nodo, tipo, resultado):
        if nodo is not None:
            if tipo.lower() in nodo.data['tipo'].lower():
                resultado.append(nodo.data['name'])
            self._buscar_tipo_recursivo(nodo.izquierdo, tipo, resultado)
            self._buscar_tipo_recursivo(nodo.derecho, tipo, resultado)

    def mostrar_pokemons_por_tipo(self, tipo):
        resultado = []
        self.buscar_tipo(tipo, resultado)
        if resultado:
            print(f"Pokemon de tipo '{tipo}':")
            for nombre in resultado:
                print(nombre)
        else:
            print(f"No se encontraron pokemon de tipo '{tipo}'.")
#d)
    def buscar_nivel(self, nombre):
        return self._buscar_nivel_recursivo(self.raiz, nombre, 0)

    def _buscar_nivel_recursivo(self, nodo, nombre, nivel):
        if nodo is None:
            return None
        if nodo.valor == nombre:
            return nivel
        elif nombre < nodo.valor:
            return self._buscar_nivel_recursivo(nodo.izquierdo, nombre, nivel + 1)
        else:
            return self._buscar_nivel_recursivo(nodo.derecho, nombre, nivel + 1)
#e)
    def mostrar_datos_especificos(self, nombres):
        for nombre in nombres:
            pokemon = self.buscar_nombre(nombre)
            if pokemon:
                print(f"Datos del pokemon '{nombre}': {pokemon}")
            else:
                print(f"Pokemon '{nombre}' no encontrado.")
#f)
def contar_por_tipo(self, tipo):
        return self._contar_tipo_recursivo(self.raiz, tipo)

def _contar_tipo_recursivo(self, nodo, tipo):
        if nodo is None:
            return 0
        # Cuenta el nodo actual si su tipo coincide
        contar_actual = 1 if tipo.lower() in nodo.data['tipo'].lower() else 0
        # Recursion en subarboles
        return contar_actual + self._contar_tipo_recursivo(nodo.izquierdo, tipo) + self._contar_tipo_recursivo(nodo.derecho, tipo)

#Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:

lista_pokemones = [
    {'name': 'Charmander', 'number': 4, 'tipo': 'fire'},
    {'name': 'Squirtle', 'number': 7, 'tipo': 'water'},
    {'name': 'Weedle', 'number': 13, 'tipo': 'insect/poison'},
    {'name': 'Dugtrio', 'number': 51, 'tipo': 'earth'},
    {'name': 'Cyndaquil', 'number': 155, 'tipo': 'fire'},
    {'name': 'Lanturn', 'number': 171, 'tipo': 'water/electric'},
    {'name': 'Bibarel', 'number': 400, 'tipo': 'normal/water'},
    {'name': 'Honchcrow', 'number': 430, 'tipo': 'sinister/flying'},
    {'name': 'Samurott', 'number': 503, 'tipo': 'water'},
    {'name': 'Litwick', 'number': 607, 'tipo': 'ghost/fire'},
    {'name': 'Greninja', 'number': 658, 'tipo': 'water/sinister'},
    {'name': 'Mudbray', 'number': 749, 'tipo': 'earth'},
    {'name': 'Lurantis', 'number': 754, 'tipo': 'plant'},
    {'name': 'Grookey', 'number': 810, 'tipo': 'plant'},
    {'name': 'Corviknight', 'number': 823, 'tipo': 'steel'},
    {'name': 'Polteagist', 'number': 855, 'tipo': 'ghost'},
    {'name': 'Jolteon', 'number': 134,'tipo': 'electric'},
    {'name': 'Lycanroc', 'number': 744,'tipo': 'rock'},
    {'name': 'Tyrantrum', 'number': 697,'tipo': 'rock/dragon'},
]

#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;

arbol_nombres = ArbolBinario()
arbol_numeros = ArbolBinario()
arbol_tipos = ArbolBinario()

for pokemon in lista_pokemones:
    arbol_nombres.insertar(pokemon['name'], pokemon)
    arbol_numeros.insertar(pokemon['number'], pokemon)
    arbol_tipos.insertar(pokemon['tipo'], pokemon)
    

#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#caracteres–;

def buscar_pokemon_por_numero(numero):
    pokemon = arbol_numeros.buscar_numero(numero)
    if pokemon:
        print("Pokemon encontrado:", pokemon)
    else:
        print("Pokemon no encontrado.")

def buscar_pokemon_por_nombre(nombre):
    resultados = arbol_nombres.buscar_nombre(nombre)
    if resultados:
        print(f"Pokemones encontrados que contienen '{nombre}':")
        for pokemon in resultados:
            print(pokemon)
    else:
        print("No se encontraron pokemon.")

# ejemplos de busqueda
print('B)')
print('Busqueda por numero')
buscar_pokemon_por_numero(4)
buscar_pokemon_por_numero(999)  #Numero que no existe 
print() 
print('Busqueda por nombre aproximado')
buscar_pokemon_por_nombre("bul")  #Por proximidad
buscar_pokemon_por_nombre("Squirt")
print()
#c) mostrar todos los nombres de todos los pokemons de un determinado tipo agua, fuego, planta y eléctrico;
print('C)')
arbol_tipos.mostrar_pokemons_por_tipo('water')
print()
arbol_tipos.mostrar_pokemons_por_tipo('fire')
print()
arbol_tipos.mostrar_pokemons_por_tipo('plant')
print()
arbol_tipos.mostrar_pokemons_por_tipo('electric')
print()

#d)realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
print('D)')
print("Listado de pokemon por numero:")
pokemons_por_numero = arbol_numeros.inorden(arbol_numeros.raiz)
for pokemon in pokemons_por_numero:
    print(f"Numero: {pokemon['number']}, Nombre: {pokemon['name']}")
print()
print("\nListado de pokemon por nombre:")
pokemons_por_nombre = arbol_nombres.inorden(arbol_nombres.raiz)
for pokemon in pokemons_por_nombre:
    print(f"Nombre: {pokemon['name']}, Número: {pokemon['number']}")
print()
print("\nNiveles en el arbol de nombres:")
for pokemon in pokemons_por_nombre:
    nivel = arbol_nombres.buscar_nivel(pokemon['name'])
    print(f"Nombre: {pokemon['name']}, Nivel: {nivel}")
print()

#e)mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
print('E)')
print('Datos de pokemones especificos:')
arbol_nombres.mostrar_datos_especificos(['Jolteon', 'Lycanroc', 'Tyrantrum'])
print()
#f)Determina cuantos Pokémons hay de tipo eléctrico y acero.
print('F)')
print('Contando Pokemon de tipo electrico y acero:')
contador = arbol_tipos.buscar_tipo('electric')
contador = arbol_tipos.buscar_tipo('steel')

print(f"Numero de pokemon de tipo acero y electrico: {contador}")
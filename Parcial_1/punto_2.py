#Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
dinosaurios = [
    {"nombre": "Tyrannosaurus Rex", "especie": "Theropoda", "peso": 7000, "descubridor": "Barnum Brown", "ano_desc": 1902},
    {"nombre": "Triceratops", "especie": "Ceratopsidae", "peso": 6000, "descubridor": "Othniel Charles Marsh", "ano_desc": 1889},
    {"nombre": "Velociraptor", "especie": "Dromaeosauridae", "peso": 15, "descubridor": "Henry Fairfield Osborn", "ano_desc": 1924},
    {"nombre": "Brachiosaurus", "especie": "Sauropoda", "peso": 56000, "descubridor": "Elmer S. Riggs", "ano_desc": 1903},
    {"nombre": "Stegosaurus", "especie": "Stegosauridae", "peso": 5000, "descubridor": "Othniel Charles Marsh", "ano_desc": 1877},
    {"nombre": "Spinosaurus", "especie": "Spinosauridae", "peso": 10000, "descubridor": "Ernst Stromer", "ano_desc": 1912},
    {"nombre": "Allosaurus", "especie": "Theropoda", "peso": 2000, "descubridor": "Othniel Charles Marsh", "ano_desc": 1877},
    {"nombre": "Apatosaurus", "especie": "Sauropoda", "peso": 23000, "descubridor": "Othniel Charles Marsh", "ano_desc": 1877},
    {"nombre": "Diplodocus", "especie": "Sauropoda", "peso": 15000, "descubridor": "Othniel Charles Marsh", "ano_desc": 1878},
    {"nombre": "Ankylosaurus", "especie": "Ankylosauridae", "peso": 6000, "descubridor": "Barnum Brown", "ano_desc": 1908},
    {"nombre": "Parasaurolophus", "especie": "Hadrosauridae", "peso": 2500, "descubridor": "William Parks", "ano_desc": 1922},
    {"nombre": "Carnotaurus", "especie": "Theropoda", "peso": 1500, "descubridor": "José Bonaparte", "ano_desc": 1985},
    {"nombre": "Styracosaurus", "especie": "Ceratopsidae", "peso": 2700, "descubridor": "Lawrence Lambe", "ano_desc": 1913},
    {"nombre": "Therizinosaurus", "especie": "Therizinosauridae", "peso": 5000, "descubridor": "Evgeny Maleev", "ano_desc": 1954},
    {"nombre": "Pteranodon", "especie": "Pterosauria", "peso": 25, "descubridor": "Othniel Charles Marsh", "ano_desc": 1876},
    {"nombre": "Quetzalcoatlus", "especie": "Pterosauria", "peso": 200, "descubridor": "Douglas A. Lawson", "ano_desc": 1971},
    {"nombre": "Plesiosaurus", "especie": "Plesiosauria", "peso": 450, "descubridor": "Mary Anning", "ano_desc": 1824},
    {"nombre": "Mosasaurus", "especie": "Mosasauridae", "peso": 15000, "descubridor": "William Conybeare", "ano_desc": 1829}
]
#A) Contar cuantas especies hay;
print("NUMERO DE ESPECIES")
def contar_especies(dinosaurios):
    especies_unicas = set()
    for dinosaurio in dinosaurios:
        especies_unicas.add(dinosaurio["especie"])
    return len(especies_unicas)
numero_especies_unicas = contar_especies(dinosaurios)
print("A: Hay", numero_especies_unicas, "especies")
#B) Determinar cuantos descubridores distintos hay;
print("DESCUBRIDORES DISTINTOS")
def descubridores_unicos(dinosaurios):
    desc_unicos = set()
    for dinosaurio in dinosaurios:
        desc_unicos.add(dinosaurio["descubridor"])
    return len(desc_unicos)
descubridores = descubridores_unicos(dinosaurios)
print("B: Hay", descubridores, "descubridores distintos")
#C) Mostrar todos los dinosaurios que empiecen con T;
print("DINOS QUE EMPIEZAN CON T")
def dino_t(dinosaurios):
    resultados = []
    for dinosaurio in dinosaurios:
        if dinosaurio["nombre"].startswith("T"):
            resultados.append(dinosaurio)
    return resultados
dino_con_t = dino_t(dinosaurios)
for dinosaurio in dino_con_t:
   print(f"C: Nombre: {dinosaurio['nombre']}, Especie: {dinosaurio['especie']}, Peso: {dinosaurio['peso']} kg, Descubridor: {dinosaurio['descubridor']}, Año de Descubrimiento: {dinosaurio['ano_desc']}")
#D) Mostrar todos los dinosaurio que pesen menos de 275 Kg;
print("DINOS QUE PESAN MENOS DE 275KG")
def peso_275(dinosaurios):
    resultados = []
    for dinosaurio in dinosaurios:
        if dinosaurio["peso"] < 275:
            resultados.append(dinosaurio)
    return resultados
menos_que_275 = peso_275(dinosaurios)
for dinosaurio in menos_que_275:
    print(f"D: Nombre: {dinosaurio['nombre']}, Especie: {dinosaurio['especie']}, Peso: {dinosaurio['peso']} kg, Descubridor: {dinosaurio['descubridor']}, Año de Descubrimiento: {dinosaurio['ano_desc']}")
#E) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S
print("DINOS QUE COMIENZAN CON A, Q, S")
def pila_AQS(dinosaurios):
    resultados = []
    for dinosaurio in dinosaurios:
        if dinosaurio["nombre"].startswith("A"):
            resultados.append(dinosaurio)
        if dinosaurio["nombre"].startswith("Q"):
            resultados.append(dinosaurio)
        if dinosaurio["nombre"].startswith("S"):
            resultados.append(dinosaurio)
    return resultados
dino_AQS = pila_AQS(dinosaurios)
for dinosaurio in dino_AQS:
    print(f"E: Nombre: {dinosaurio['nombre']}, Especie: {dinosaurio['especie']}, Peso: {dinosaurio['peso']} kg, Descubridor: {dinosaurio['descubridor']}, Año de Descubrimiento: {dinosaurio['ano_desc']}")
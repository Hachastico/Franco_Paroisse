#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones
#necesarias para resolver las actividades enumeradas a continuación:
jedis = [
    {
        "name": "Qui-Gon Jinn",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Tera Sinube/Count Dooku",
        "lightsaber_color": "Green",
        "homeworld": "Coruscant",
        "birth_year": "79ABY",
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Obi-Wan Kenobi",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Qui-Gon Jinn/Yoda",
        "lightsaber_color": "Blue",
        "homeworld": "Stewjon",
        "birth_year": "57ABY",
        "height": 1.82,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Anakin Skywalker/Darth Vader",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Obi-Wan Kenobi",
        "lightsaber_color": "Blue",
        "homeworld": "Tatooine",
        "birth_year": "41ABY",
        "height": 1.88,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Quinlan Vos",
        "rank": "Jedi Master",
        "species": "Human/Kiffar",
        "master": "Tholme",
        "lightsaber_color": "Green",
        "homeworld": "Kiffu",
        "birth_year": "59ABY",
        "height": 1.91,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Yoda",
        "rank": "Grand Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "896ABY",
        "height": 0.66,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Mace Windu",
        "rank": "Jedi Master/Master of the Order",
        "species": "Human",
        "master": "Cyslin Myr",
        "lightsaber_color": "Purple",
        "homeworld": "Haruun Kal",
        "birth_year": "72ABY",
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ki-Adi-Mundi",
        "rank": "Jedi Master",
        "species": "Cerean",
        "master": None,
        "lightsaber_color": "Purple / Blue",
        "homeworld": "Cerea",
        "birth_year": "92ABY",
        "height": 1.98,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Plo Koon",
        "rank": "Jedi Master",
        "species": "Kel Dor",
        "master": None,
        "lightsaber_color": "Yellow / Blue / Orange",
        "homeworld": "Dorin",
        "birth_year": "71ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Saesee Tiin",
        "rank": "Jedi Master",
        "species": "Iktotchi",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Iktotch",
        "birth_year": None,
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yaddle",
        "rank": "Jedi Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "509AYB",
        "height": 0.61,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Even Piell",
        "rank": "Jedi Master",
        "species": "Lannik",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Lannik",
        "birth_year": None,
        "height": 1.22,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Oppo Rancisis",
        "rank": "Jedi Master",
        "species": "Thisspiasian",
        "master": "Yaddle",
        "lightsaber_color": "Green",
        "homeworld": "Thisspias",
        "birth_year": "206ABY",
        "height": 1.38,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Adi Gallia",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green / Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.84,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yarael Poof",
        "rank": "Jedi Master",
        "species": "Quermian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Quermia",
        "birth_year": None,
        "height": 2.64,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Eeth Koth",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green / Blue",
        "homeworld": "Iridonia",
        "birth_year": None,
        "height": 1.71,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Depa Billaba",
        "rank": "Jedi Master",
        "species": "Chalactan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Chalacta",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kit Fisto",
        "rank": "Jedi Master",
        "species": "Nautolan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Glee Anselm",
        "birth_year": None,
        "height": 1.96,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luminara Unduli",
        "rank": "Jedi Master",
        "species": "Mirialan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mirial",
        "birth_year": "58ABY",
        "height": 1.76,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Barriss Offee",
        "rank": "Padawan",
        "species": "Mirialan",
        "master": "Luminara Unduli",
        "lightsaber_color": "Blue",
        "homeworld": "Mirial",
        "birth_year": "40ABY",
        "height": 1.66,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Shaak Ti",
        "rank": "Jedi Master",
        "species": "Togruta",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Shili",
        "birth_year": None,
        "height": 1.87,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Coleman Trebor",
        "rank": "Jedi Master",
        "species": "Vurk",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Sembla",
        "birth_year": None,
        "height": 2.13,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Jocasta Nu",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.69,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Aayla Secura",
        "rank": "Jedi Knight",
        "species": "Twi'lek",
        "master": "Quinlan Vos",
        "lightsaber_color": "Blue",
        "homeworld": "Ryloth",
        "birth_year": "47ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Sifo-Dyas",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mundos Cassandranos",
        "birth_year": "75ABY",
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Count Dooku",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Yoda",
        "lightsaber_color": "Blue / Red",
        "homeworld": "Serenno",
        "birth_year": "102ABY",
        "height": 1.93,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Pablo-Jill",
        "rank": "Jedi Knight",
        "species": None,
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cúmulo Estelar Skustell",
        "birth_year": None,
        "height": 1.60,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bultar Swan",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Plo Koon",
        "lightsaber_color": "Green",
        "homeworld": "Kuat",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Agen Kolar",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green / Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Stass Allie",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Tholoth",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ahsoka Tano",
        "rank": "Padawan",
        "species": "Togruta",
        "master": "Anakin Skywalker",
        "lightsaber_color": "Green / Yellow / Blue / White",
        "homeworld": "Shili",
        "birth_year": "36ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Asajj Ventress",
        "rank": "Padawan",
        "species": "Dathomirian",
        "master": "Ky Narec",
        "lightsaber_color": "Yellow / Red",
        "homeworld": "Dathomir",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Ima-Gun Di",
        "rank": "Jedi Master",
        "species": "Nikto",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Nahdar Vebb",
        "rank": "Jedi Knight",
        "species": "Mon Calamari",
        "master": "Kit Fisto",
        "lightsaber_color": "Blue",
        "homeworld": "Dac",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bolla Ropal",
        "rank": "Jedi Master",
        "species": "Rodian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Rodia",
        "birth_year": None,
        "height": 1.75,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ord Enisence",
        "rank": "Jedi Master",
        "species": "Skrilling",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Agrimundo-2079",
        "birth_year": None,
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tera Sinube",
        "rank": "Jedi Master",
        "species": "Cosian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cosia",
        "birth_year": "102ABY",
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ky Narec",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Pong Krell",
        "rank": "Jedi Master",
        "species": "Besalisk",
        "master": None,
        "lightsaber_color": "Blue / Green",
        "homeworld": "Ojom",
        "birth_year": None,
        "height": 2.36,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Coleman Kcaj",
        "rank": "Jedi Master",
        "species": "Ongree",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Skustell",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplar",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplee",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tu-Anh",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": None,
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kanan Jarrus",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Depa Billaba",
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": "33ABY",
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ezra Bridger",
        "rank": "Padawan",
        "species": "Human",
        "master": "Kanan Jarrus",
        "lightsaber_color": "Blue",
        "homeworld": "Lothal",
        "birth_year": "19ABY",
        "height": 1.65,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luke Skywalker",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Obi-Wan Kenobi/Yoda",
        "lightsaber_color": "Green / Blue",
        "homeworld": "Tatooine",
        "birth_year": "19ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Leia Organa",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Blue",
        "homeworld": "Alderaan",
        "birth_year": "19ABY",
        "height": 1.50,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ben Solo/Kylo Ren",
        "rank": "Padawan",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Green / Blue",
        "homeworld": "Chandrila",
        "birth_year": "5DBY",
        "height": 1.89,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Rey Skywalker",
        "rank": "Jedi Sentinel",
        "species": "Human",
        "master": "Luke Skywalker / Leia Organa",
        "lightsaber_color": "Blue / Green / Yellow",
        "homeworld": "Jakku",
        "birth_year": "15DYB",
        "height": 1.70,
        "to_darkside": None,
        "come_lightside": None
    }
 ]

#A: listado ordenado por nombre y por especie;
print("A: ORDEN POR NOMBRE Y ESPECIE")
orden_nombre = sorted(jedis, key=lambda x: x['name'])
orden_especie = sorted(jedis, key=lambda x: (x['species'] if x['species'] else ''))
print("Ordenado por nombre:")
for jedi in orden_nombre:
    print(f"{jedi['name']} - {jedi['species']}")
print()
print("Ordenado por especie")
for jedi in orden_especie:
    print(f"{jedi['species']} - {jedi['name']}")
print("---------------------------------------------------------")
#B: mostrar toda la información de Ahsoka Tano y Kit Fisto;
print("B: INFO DE AHSOKA Y FISTO")
def jedi_info(jedis, name):
    return [jedi for jedi in jedis if jedi['name'] in name]
jedi_names = ["Ahsoka Tano", "Kit Fisto"]
chosen_jedi = jedi_info(jedis, jedi_names)
for jedi in chosen_jedi:
    print(f"B: Nombre: {jedi['name']}, Rango: {jedi['rank']}, Especie: {jedi['species']}, Maestro: {jedi['master']}, Color de Sable de Luz: {jedi['lightsaber_color']}, Planeta Natal: {jedi['homeworld']}, Año de Nacimiento: {jedi['birth_year']}, Altura: {jedi['height']} metros, Se Pasó al Lado Oscuro: {jedi['to_darkside']}, Regresó al Lado Luminoso: {jedi['come_lightside']}")
jedi_info(jedis, ["Ahsoka Tano", "Kit Fisto"])
print("---------------------------------------------------------")
#C: mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print("C: PADAWANS DE YODA Y LUKE")
def get_pad(lista_jedi, master_name):
    padawans = [jedi for jedi in lista_jedi if jedi['master'] and master_name in jedi['master']]
    return padawans
yoda_pad = get_pad(jedis, "Yoda")
luke_pad = get_pad(jedis, "Luke Skywalker")
print("Padawans de Yoda:")
for padawan in yoda_pad:
    print(f"C: Nombre: {padawan['name']}, Rango: {padawan['rank']}, Especie: {padawan['species']}, Color de Sable de Luz: {padawan['lightsaber_color']}, Planeta Natal: {padawan['homeworld']}, Año de Nacimiento: {padawan['birth_year']}, Altura: {padawan['height']} metros, Se Pasó al Lado Oscuro: {padawan['to_darkside']}, Regresó al Lado Luminoso: {padawan['come_lightside']}")
    print("\n")
print("Padawans de Luke:")
for padawan in luke_pad:
    print(f"C: Nombre: {padawan['name']}, Rango: {padawan['rank']}, Especie: {padawan['species']}, Color de Sable de Luz: {padawan['lightsaber_color']}, Planeta Natal: {padawan['homeworld']}, Año de Nacimiento: {padawan['birth_year']}, Altura: {padawan['height']} metros, Se Pasó al Lado Oscuro: {padawan['to_darkside']}, Regresó al Lado Luminoso: {padawan['come_lightside']}")
    print("\n")
print("---------------------------------------------------------")
#D: mostrar los Jedi de especie humana y twi'lek;
print("D: JEDIS HUMANOS Y TWI'LEK")
def jedi_hum_twi(jedis, species):
    jedis_humanos_twilek = [jedi for jedi in jedis if jedi['species'] in species]
    return jedis_humanos_twilek
humanos_y_twilek = ["Human", "Twi'lek"]
jedis_filtrados = jedi_hum_twi(jedis, humanos_y_twilek)
for jedi in jedis_filtrados:
    print(f"D: Nombre: {jedi['name']}, Rango: {jedi['rank']}, Especie: {jedi['species']}, Color de Sable de Luz: {jedi['lightsaber_color']}, Planeta Natal: {jedi['homeworld']}, Año de Nacimiento: {jedi['birth_year']}, Altura: {jedi['height']} metros, Se Pasó al Lado Oscuro: {jedi['to_darkside']}, Regresó al Lado Luminoso: {jedi['come_lightside']}")
    print("\n")
print("---------------------------------------------------------")
#E: listar todos los Jedi que comienzan con A;
print("E: JEDIS QUE COMIENZAN CON A")
def jedis_A(jedis, letra_A):
    jedis_con_A = [ jedi for jedi in jedis if jedi['name'].startswith(letra_A)]
    return jedis_con_A
start_A = "A"
jedis_con_A = jedis_A(jedis, start_A)
for jedi in jedis_con_A:
    print(f"E: Nombre: {jedi['name']}, Rango: {jedi['rank']}, Especie: {jedi['species']}, Color de Sable de Luz: {jedi['lightsaber_color']}, Planeta Natal: {jedi['homeworld']}, Año de Nacimiento: {jedi['birth_year']}, Altura: {jedi['height']} metros, Se Pasó al Lado Oscuro: {jedi['to_darkside']}, Regresó al Lado Luminoso: {jedi['come_lightside']}")
    print("\n")
print("---------------------------------------------------------")
#F: mostrar los Jedi que usaron sable de luz de más de un color;
print("F: JEDIS CON SABLES DE LUZ DE MAS DE UN COLOR")
def sable_multicolor(lista_jedi):
    multicolor_saber_jedis = []
    for jedi in lista_jedi:
         if jedi['lightsaber_color'] and '/' in jedi['lightsaber_color']:
            multicolor_saber_jedis.append(jedi)
    return multicolor_saber_jedis
multi_color_saber_jedis = sable_multicolor(jedis)
for jedi in multi_color_saber_jedis:
    print(f"F: Nombre: {jedi['name']}, Colores de Sable de Luz: {jedi['lightsaber_color']}")
    print("\n")
print("---------------------------------------------------------")
#G: indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print("G: JEDIS CON SABLES DE LUZ AMARILLO O VIOLETA")
def sable_amarillo_violeta(lista_jedi,color):
    jedi_color_especifico = []
    for jedi in lista_jedi:
        lightsaber_color = jedi.get('lightsaber_color')
        if lightsaber_color is not None:
            saber_colors = jedi['lightsaber_color'].split(' / ')
            if color in saber_colors:
                jedi_color_especifico.append(jedi)
    return jedi_color_especifico
violeta_amarillo = sable_amarillo_violeta(jedis, 'Yellow') + sable_amarillo_violeta(jedis, 'Violet')
for jedi in violeta_amarillo:
    print(f"G: Nombre: {jedi['name']}, Color de Sable de Luz: {jedi['lightsaber_color']}")
    print("\n")
print("---------------------------------------------------------")
#H: indicar los nombre de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron.
print("H: NOMBRES DE LOS PADAWANS DE QUI-GON JINN Y MACE WINDU")
qui_gon_pad = get_pad(jedis, 'Qui-Gon Jinn')
mace_pad = get_pad(jedis, 'Mace Windu')
print("Padawans de Qui-Gon Jinn")
if qui_gon_pad:
    for padawan in qui_gon_pad:
        print(f"H: Nombre: {padawan['name']}, Rango: {padawan['rank']}, Especie: {padawan['species']}, Color de Sable de Luz: {padawan['lightsaber_color']}, Planeta Natal: {padawan['homeworld']}, Año de Nacimiento: {padawan['birth_year']}, Altura: {padawan['height']} metros, Se Pasó al Lado Oscuro: {padawan['to_darkside']}, Regresó al Lado Luminoso: {padawan['come_lightside']}")
        print("\n")
else:
    print("Ningun padawan registrado")
print("\nPadawans de Mace Windu")
if mace_pad:
    for padawan in mace_pad:
        print(f"H: Nombre: {padawan['name']}, Rango: {padawan['rank']}, Especie: {padawan['species']}, Color de Sable de Luz: {padawan['lightsaber_color']}, Planeta Natal: {padawan['homeworld']}, Año de Nacimiento: {padawan['birth_year']}, Altura: {padawan['height']} metros, Se Pasó al Lado Oscuro: {padawan['to_darkside']}, Regresó al Lado Luminoso: {padawan['come_lightside']}")
        print("\n")
else:
    print("Ningún padawan registrado.")
print("---------------------------------------------------------")
#I: mostrar todos los Jedi que tengan el ranking de Grand Master.
print("I: JEDIS DE RANGO GRAND MASTER")
def get_grand_masters(lista_jedi):
    grand_masters = [jedi for jedi in lista_jedi if jedi.get('rank') == 'Grand Master']
    return grand_masters
grand_masters = get_grand_masters(jedis)
print("Jedis con el rango Grand Master:")
for jedi in grand_masters:
    print(f"I: Nombre: {jedi['name']}, Rango: {jedi['rank']}, Especie: {jedi['species']}, Color de Sable de Luz: {jedi['lightsaber_color']}, Planeta Natal: {jedi['homeworld']}, Año de Nacimiento: {jedi['birth_year']}, Altura: {jedi['height']} metros, Se Pasó al Lado Oscuro: {jedi['to_darkside']}, Regresó al Lado Luminoso: {jedi['come_lightside']}")
    print("\n")
print("---------------------------------------------------------")
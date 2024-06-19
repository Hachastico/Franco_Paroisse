#Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destructor Estelar y necesita localizar la base rebelde más cercana– y se tiene una cola con información de las bases
#rebeldes en la tierra de las cuales conoce su nombre, número de flota aérea, coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes tareas una vez que aterrice
#from cola import Cola
from RebelBase import Rebel
from cola import Cola
from copy import deepcopy
import math

ListaBases = [
Rebel("Base Alpha",400,31.9,-102.5),
Rebel("Base Beta",350,2.3,17.3),
Rebel("Base Charlie",150,-47.3,123.2),
Rebel("Base Delta",300,-10.6,167.4),
Rebel("Base Echo",150,65.7,-145),
Rebel("Base Foxtrot",100,73,-162.4),
Rebel("Base Gamma",50,-58.9,26.6),
]
ColaBases = Cola()
for rebel in ListaBases:
    ColaBases.arrive(rebel)

print("A/B: Determinar cuál es la base rebelde más cercana desde su posición actual, para el cálculo de la distancia deberá utilizar la fórmula de Haversine:")

def haversine(lon1, lat1, lon2, lat2):
    R = 6371  #Radio
    dlon = math.radians(lon2 - lon1)
    dlat = math.radians(lat2 - lat1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

ColaBases_A = deepcopy(ColaBases)
current_lat = -100.0
current_lon = 70.0
min_distance = float('inf')
closest_base = None

for base in ColaBases_A:
    distance = haversine(current_lat, current_lon, base.get_lat(), base.get_lon())
    if distance < min_distance:
        min_distance = distance
        closest_base = base

if closest_base:
    print(f"La base rebelde mas cercana es: {closest_base.get_nombre()}")
    print(f"Distancia: {min_distance:.2f} km")
else:
    print("No hay bases disponibles.")

print("-----------------------------")

print("C: Mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y determinar cual tiene mayor flota aérea")

ColaBases_C = deepcopy(ColaBases)
distances = []
current_lat = -100.0
current_lon = 70.0

for base in ColaBases_C:
    distance = haversine(current_lat, current_lon, base.get_lat(), base.get_lon())
    distances.append((base, distance))

distances.sort(key=lambda x: x[1])
closest_bases = distances[:3]

print("Las tres bases mas cercanas son:")
for base, distance in closest_bases:
    print(f"{base.get_nombre()}, Distancia: {distance:.2f} km")
max_fleet_base = max(closest_bases, key=lambda x: x[0].get_fleet())[0]
print(f"La base cercana con la mayor flota es la {max_fleet_base.get_nombre()} con {max_fleet_base.get_fleet()} aeronaves")

print("-----------------------------")

print("D: Determinar la distancia hasta la base rebelde con mayor flota aérea")
ColaBases_D = deepcopy(ColaBases)

current_lat = -100.0
current_lon = 70.0

max_fleet_base = max(ListaBases, key=lambda base: base.get_fleet())
distance_to_max_fleet_base = haversine(current_lat, current_lon, max_fleet_base.get_lat(), max_fleet_base.get_lon())
print(f"La base con la mayor flota aerea es la {max_fleet_base.get_nombre()} a una distancia de {distance_to_max_fleet_base:.2f} km con una flota de {max_fleet_base.get_fleet()}")
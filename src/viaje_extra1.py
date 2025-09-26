distancia1 = 0
total_paradas = 0
distancia2 = int(input("Introduce la distancia en kilómetros: "))  # distancia Tierra - Luna
velocidad_kmh = int(input("Introduce la velocidad en kilómetros/hora: "))
repostaje = 150000
tiempo_horas = distancia2 // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")
while distancia1 < distancia2 - 150000:
    distancia1 = distancia1 + 150000
    total_paradas = total_paradas + 1
    print(f"Parada en el km: {distancia1}")

print(f"Total paradas: {total_paradas}")
    
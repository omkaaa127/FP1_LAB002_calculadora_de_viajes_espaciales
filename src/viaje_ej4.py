distancia = 225000000

for velocidad in range(10000, 50001, 10000):
    tiempo = distancia / velocidad
    dias = tiempo / 24
    print(f"Velocidad: {velocidad}kmh -> Tiempo: {dias} dias")
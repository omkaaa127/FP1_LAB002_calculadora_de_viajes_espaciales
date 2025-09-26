distancia_km = int(input("Introduce la distancia en kilómetros: "))
velocidad_kmh = int(input("Introduce la velocidad en kilómetros/hora: "))
edad = int(input("Introduce tu edad: "))
fisico = int(input("Valora tu nivel físico del 1 al 10: "))
if edad < 18:
    print("Debes de ser mayor de edad")
elif fisico < 5:
    print("Debes estar en forma")
elif fisico >= 10:
    print("Introduce un valor del 1 al 10")
else:
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
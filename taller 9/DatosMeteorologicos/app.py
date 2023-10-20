from DatosMeteorologicos import DatosMeteorologicos

datos_meteorologicos = DatosMeteorologicos('datos.txt')
resultados = datos_meteorologicos.procesar_datos()

print(f"Temperatura promedio: {resultados[0]}")
print(f"Humedad promedio: {resultados[1]}")
print(f"Presión promedio: {resultados[2]}")
print(f"Velocidad promedio del viento: {resultados[3]}")
print(f"Dirección predominante del viento: {resultados[4]}")

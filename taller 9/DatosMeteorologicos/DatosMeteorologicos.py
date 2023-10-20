class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        promedio_temperatura, promedio_humedad, promedio_presion, promedio_velocidad_viento, direccion_viento_predominante = self.calcular_estadisticas()
        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_velocidad_viento, direccion_viento_predominante

    def leer_datos(self):
        datos_leidos = []
        with open(self.nombre_archivo, 'r') as archivo:
            datos_leidos = archivo.readlines()
        return datos_leidos

    def calcular_estadisticas(self):
        datos_leidos = self.leer_datos()
        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_velocidad_viento = 0
        direccion_viento_counts = {}

        for datos in datos_leidos:
            lines = datos.strip().split('\n')
            temperatura = float(lines[5].split(': ')[1])
            humedad = float(lines[6].split(': ')[1])
            presion = float(lines[7].split(': ')[1])
            velocidad_viento, direccion_viento = map(str, lines[8].split(': ')[1].split(','))

            total_temperatura += temperatura
            total_humedad += humedad
            total_presion += presion
            total_velocidad_viento += float(velocidad_viento)

            if direccion_viento in direccion_viento_counts:
                direccion_viento_counts[direccion_viento] += 1
            else:
                direccion_viento_counts[direccion_viento] = 1

        promedio_temperatura = total_temperatura / len(datos_leidos)
        promedio_humedad = total_humedad / len(datos_leidos)
        promedio_presion = total_presion / len(datos_leidos)
        promedio_velocidad_viento = total_velocidad_viento / len(datos_leidos)
        
        promedio_grados = self.direccion_predominante_en_grados(direccion_viento_counts.keys())
        direccion_viento_predominante = self.grados_a_abreviacion(promedio_grados)
        
        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_velocidad_viento, direccion_viento_predominante

    def direccion_predominante_en_grados(self, direcciones):
        abreviaciones_a_grados = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }

        grados = [abreviaciones_a_grados[direccion] for direccion in direcciones]
        promedio_grados = sum(grados) / len(grados)

        return promedio_grados

    def grados_a_abreviacion(self, grados):
        grados_a_abreviacion = {
            0: "N",
            22.5: "NNE",
            45: "NE",
            67.5: "ENE",
            90: "E",
            112.5: "ESE",
            135: "SE",
            157.5: "SSE",
            180: "S",
            202.5: "SSW",
            225: "SW",
            247.5: "WSW",
            270: "W",
            292.5: "WNW",
            315: "NW",
            337.5: "NNW"
        }

        abreviacion = min(grados_a_abreviacion, key=lambda x: abs(x - grados))
        
        return grados_a_abreviacion[abreviacion]

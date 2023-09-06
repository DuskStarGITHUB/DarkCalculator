"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones de operaciones de tiempo>
# autor: <DuskStar>
# Fecha de creación: <06/09/2023>
# Nota: <N/A>
#####################################################################################

class CalculadoraTiempo:
    """Estructura del objeto"""
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

    def ingresar_tiempo(self, horas, minutos, segundos):
        """Tiempo"""
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def sumar_tiempo(self, horas, minutos, segundos):
        """Operacion suma"""
        self.horas += horas
        self.minutos += minutos
        self.segundos += segundos
        self.normalizar_tiempo()

    def restar_tiempo(self, horas, minutos, segundos):
        """Operacion resta"""
        self.horas -= horas
        self.minutos -= minutos
        self.segundos -= segundos
        self.normalizar_tiempo()

    def normalizar_tiempo(self):
        """Normaliza los valores de los atributos"""
        if self.segundos >= 60:
            self.minutos += self.segundos // 60
            self.segundos %= 60
        if self.minutos >= 60:
            self.horas += self.minutos // 60
            self.minutos %= 60

    def obtener_resultado(self):
        """Devuelve el resultado"""
        return self.horas, self.minutos, self.segundos

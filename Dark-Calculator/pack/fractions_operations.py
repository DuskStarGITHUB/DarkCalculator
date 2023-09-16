"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones  de operaciones basicas con fracciones>
# autor: <DuskStar>
# Fecha de creación: <06/09/2023>
# Nota: <N/A>
#####################################################################################

from fractions import Fraction

class FraccionCalculadora:
    """Estructura del objeto"""
    def __init__(self, numerador, denominador, operacion):
        self.fraccion = Fraction(numerador, denominador)
        self.operacion = operacion
    def realizar_operacion(self, otra_fraccion):
        """Funcion de operaciones"""
        if self.operacion == '+':
            resultado = self.fraccion + otra_fraccion
        elif self.operacion == '-':
            resultado = self.fraccion - otra_fraccion
        elif self.operacion == '*':
            resultado = self.fraccion * otra_fraccion
        elif self.operacion == '/':
            resultado = self.fraccion / otra_fraccion
        else:
            raise ValueError("Operación no válida")
        return resultado

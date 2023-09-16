"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones de operaciones de calculos de area y volumen>
# autor: <DuskStar>
# Fecha de creación: <06/09/2023>
# Nota: <N/A>
#####################################################################################

# Libreria
import math

def calcular_area_figura(figura, *args):
    """Funcion de calculo"""
    if figura == "cuadrado":
        if len(args) == 1:
            lado = args[0]
            area = lado ** 2
            return area
        else:
            return "El cuadrado requiere un solo valor (lado)."
    elif figura == "triangulo":
        if len(args) == 2:
            base, altura = args
            area = (base * altura) / 2
            return area
        else:
            return "El triángulo requiere dos valores (base y altura)."
    elif figura == "circulo":
        if len(args) == 1:
            radio = args[0]
            area = math.pi * (radio ** 2)
            return area
        else:
            return "El círculo requiere un solo valor (radio)."
    elif figura == "rectangulo":
        if len(args) == 2:
            base, altura = args
            area = base * altura
            return area
        else:
            return "El rectángulo requiere dos valores (base y altura)."
    else:
        return "Figura no reconocida."

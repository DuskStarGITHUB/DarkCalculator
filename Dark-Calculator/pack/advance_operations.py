"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones de operaciones avanzadas>
# autor: <DuskStar>
# Fecha de creación: <05/09/2023>
# Nota: <N/A>
#####################################################################################

# Librerias
import math

def raiz(num_1):
    """Función que calcula la raiz cuadrada de un numero"""
    if num_1 < 0:
        raise ValueError("Raiz negativa")
    else:
        return math.sqrt(num_1)

def seno(num_1):
    """Función que calcula el seno de un numero"""
    if num_1 < 0:
        raise ValueError("Seno negativo")
    else:
        return math.sin(num_1)

def coseno(num_1):
    """Función que calcula el coseno de un numero"""
    if num_1 < 0:
        raise ValueError("Coseno negativo")
    else:
        return math.cos(num_1)

def tangente(num_1):
    """Función que calcula la tangente de un numero"""
    if num_1 < 0:
        raise ValueError("Tangente negativa")
    else:
        return math.tan(num_1)

def arco_seno(num_1):
    """Función que calcula el arco seno de un numero"""
    if num_1 < 0:
        raise ValueError("Arco seno negativo")
    else:
        return math.asin(num_1)

def arco_coseno(num_1):
    """Función que calcula el arco coseno de un numero"""
    if num_1 < 0:
        raise ValueError("Arco coseno negativo")
    else:
        return math.acos(num_1)

def arco_tangente(num_1):
    """Función que calcula el arco tangente de un numero"""
    if num_1 < 0:
        raise ValueError("Arco tangente negativo")
    else:
        return math.atan(num_1)

def arco_tangente_razon(num_1, num_2):
    """
    Funcion que calcula el arco tangente de la razon
    y/x devuelve el resultado en radianes
    """
    if num_1 < 0 or num_2 < 0:
        raise ValueError("Arco tangente razon negativo")
    else:
        return math.atan2(num_1,num_2)

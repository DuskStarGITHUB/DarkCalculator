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

def seno_hiperbolico(num_1):
    """Función que calcula el seno hiperbolico de un numero"""
    if num_1 < 0:
        raise ValueError("Seno hiperbolico negativo")
    else:
        return math.sinh(num_1)

def coseno_hiperbolico(num_1):
    """Función que calcula el coseno hiperbolico de un numero"""
    if num_1 < 0:
        raise ValueError("Coseno hiperbolico negativo")
    else:
        return math.cosh(num_1)

def tangente_hiperbolica(num_1):
    """Función que calcula la tangente hiperbolica de un numero"""
    if num_1 < 0:
        raise ValueError("Tangente hiperbolica negativa")
    else:
        return math.tanh(num_1)

def arco_seno_hiperbolico(num_1):
    """Función que calcula el arco seno hiperbolico de un numero"""
    if num_1 < 0:
        raise ValueError("Arco seno hiperbolico negativo")
    else:
        return math.asinh(num_1)

def arco_coseno_hiperbolico(num_1):
    """Función que calcula el arco coseno hiperbolico de un numero"""
    if num_1 < 0:
        raise ValueError("Arco coseno hiperbolico negativo")
    else:
        return math.acosh(num_1)

def arco_tangente_hiperbolica(num_1):
    """Función que calcula el arco tangente hiperbolica de un numero"""
    if num_1 < 0:
        raise ValueError("Arco tangente hiperbolica negativa")
    else:
        return math.atanh(num_1)

def exponencial(num_1):
    """Función que calcula el exponencial de un numero"""
    if num_1 < 0:
        raise ValueError("Exponencial negativo")
    else:
        return math.exp(num_1)

def elevacion(num_1, num_2):
    """Función que calcula la elevacion a la potencia de un numero"""
    if num_1 < 0 or num_2 < 0:
        raise ValueError("Elevacion a la potencia negativa")
    else:
        return math.pow(num_1, num_2)

def logaritmo(num_1):
    """Función que calcula el logaritmo de un numero"""
    if num_1 < 0:
        raise ValueError("Logaritmo negativo")
    else:
        return math.log(num_1)

def logartimo_perzonalizado(num_1, num_2):
    """Función que calcula el logaritmo perzonalizado de un numero"""
    if num_1 < 0 or num_2 < 0:
        raise ValueError("Logaritmo perzonalizado negativo")
    else:
        return math.log(num_1, num_2)

def logaritmo_natural(num_1):
    """Función que calcula el logaritmo natural de un numero"""
    if num_1 < 0:
        raise ValueError("Logaritmo natural negativo")
    else:
        return math.log10(num_1)

def redondeo_arriba(num_1):
    """Función que calcula el redondeo arriba de un numero"""
    return math.ceil(num_1)

def redondeo_abajo(num_1):
    """Función que calcula el redondeo abajo de un numero"""
    return math.floor(num_1)

def truncamiento(num_1):
    """Función que calcula el truncamiento de un numero"""
    return math.trunc(num_1)

def valor_absoluto(num_1):
    """Función que calcula el valor absoluto de un numero"""
    return math.fabs(num_1)
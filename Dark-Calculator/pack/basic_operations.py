"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones de operaciones basicas>
# autor: <DuskStar>
# Fecha de creación: <04/09/2023>
# Nota: <N/A>
#####################################################################################

# Funciones de operaciones

def suma(num_1,num_2):
    """Función que suma dos numeros"""
    return num_1+num_2

def resta(num_1,num_2):
    """Función que resta dos numeros"""
    return num_1-num_2

def multiplicacion(num_1,num_2):
    """Función que multiplica dos numeros"""
    return num_1*num_2

def division(num_1,num_2):
    """Función que divide dos numeros"""
    if num_2 == 0:
        raise ValueError("Division por cero")
    else:
        return num_1/num_2

def potencinum_1(num_1,num_2):
    """Función que eleva un numero a otro"""
    if num_2 < 0:
        raise ValueError("Potencia negativa")
    else:
        return num_1**num_2

def porcentaje(num_1,num_2):
    """Función que calcula el porcentaje de un numero"""
    if num_2 < 0:
        raise ValueError("Porcentaje negativo")
    else:
        return num_1*num_2/100

def cambio_signo(num_1):
    """Función que cambia el signo de un numero"""
    return -num_1

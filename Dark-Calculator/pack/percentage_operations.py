"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones de operacion de aumento o reduccion porcentual>
# autor: <DuskStar>
# Fecha de creación: <05/09/2023>
# Nota: <N/A>
#####################################################################################

# Funciones

def aumento_porcentual(valor, porcentaje):
    """Función que calcula el aumento porcentual de un numero"""
    aumento = (porcentaje / 100) * valor
    valor_aumentado = valor + aumento
    return valor_aumentado

def reduccion_porcentual(valor, porcentaje):
    """Función que calcula la reducción porcentual de un numero"""
    reduccion = (porcentaje / 100) * valor
    valor_reducido = valor - reduccion
    return valor_reducido

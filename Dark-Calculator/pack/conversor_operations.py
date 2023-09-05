"""Titulo: |Operations|"""
#####################################################################################
# Descripción: <Funciones de conversion de unidades>
# autor: <DuskStar>
# Fecha de creación: <05/09/2023>
# Nota: <N/A>
#####################################################################################

# Libreria
from decimal import Decimal

def convertir_longitud(valor, unidad_origen, unidad_destino):
    """Sistema: longitud"""
    conversiones = {
        'mm': Decimal('0.001'),
        'cm': Decimal('0.01'),
        'dm': Decimal('0.1'),
        'm': Decimal('1'),
        'dam': Decimal('10'),
        'hm': Decimal('100'),
        'km': Decimal('1000')
    }
    # Transformar el valor a deicmal
    valor_decimal = Decimal(str(valor))
    # Mapeado y operacion
    valor_convertido = valor_decimal * conversiones[unidad_origen] / conversiones[unidad_destino]
    # Retornar el resultado
    return valor_convertido

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    """Sistema: temperatura"""
    conversiones = {
        'C': (1.0, 0.0),
        'F': (1.8, 32.0)
    }
    factor_origen, desplazamiento_origen = conversiones[unidad_origen]
    factor_destino, desplazamiento_destino = conversiones[unidad_destino]
    valor_convertido = (valor - desplazamiento_origen) * factor_destino / factor_origen + desplazamiento_destino
    return valor_convertido

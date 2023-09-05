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


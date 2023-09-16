"""Titulo: |Interfaz|"""
#####################################################################################
# Descripción: <Interfaz de calculadora basica>
# autor: <DuskStar>
# Fecha de creación: <06/09/2023>
# Nota: <N/A>
#####################################################################################

# Importaciones
import tkinter as tk
from pack.basic_operations import *

# Codigo
def realizar_operacion():
    """Operaciones"""
    try:
        num_1 = float(entry_num_1.get())
        num_2 = float(entry_num_2.get())
        operacion = operacion_var.get()
        if operacion == "Suma":
            resultado.set(suma(num_1, num_2))
        elif operacion == "Resta":
            resultado.set(resta(num_1, num_2))
        elif operacion == "Multiplicación":
            resultado.set(multiplicacion(num_1, num_2))
        elif operacion == "División":
            resultado.set(division(num_1, num_2))
        elif operacion == "Potenciación":
            resultado.set(potencia(num_1, num_2))
        elif operacion == "Porcentaje":
            resultado.set(porcentaje(num_1, num_2))
    except ValueError as a_error:
        resultado.set(str(a_error))

def cambiar_signo():
    try:
        num_1 = float(entry_num_1.get())
        resultado_actual = float(resultado.get())
        resultado.set(cambio_signo(resultado_actual))
    except ValueError as a_error:
        resultado.set(str(a_error))


# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Variables para los números y el resultado
entry_num_1 = tk.Entry(root)
entry_num_2 = tk.Entry(root)
resultado = tk.StringVar()
resultado.set("Resultado")

# Radio buttons para seleccionar la operación
operacion_var = tk.StringVar()
operacion_var.set("Suma")
operaciones = ["Suma", "Resta", "Multiplicación", "División", "Potenciación", "Porcentaje"]
for operacion in operaciones:
    tk.Radiobutton(root, text=operacion, variable=operacion_var, value=operacion).pack()

# Botón para realizar la operación
tk.Button(root, text="Calcular", command=realizar_operacion).pack()

# Botón para cambiar el signo
tk.Button(root, text="Cambiar Signo", command=cambiar_signo).pack()

# Mostrar los resultados
tk.Label(root, text="Número 1:").pack()
entry_num_1.pack()
tk.Label(root, text="Número 2:").pack()
entry_num_2.pack()
tk.Label(root, text="Resultado:").pack()
tk.Label(root, textvariable=resultado).pack()

# Ejecutar la ventana
root.mainloop()

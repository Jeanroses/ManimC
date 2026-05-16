from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
PYTHON_COLOR = "#f1fa8c"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Python", font_size=60, color=PYTHON_COLOR).set_color_by_gradient(PYTHON_COLOR, ACCENT_COLOR)
        subtitle = Text("Lenguaje de programacion de proposito general", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class VariablesScene(Scene):
    def construct(self):
        title = Text("Variables y Tipos", font_size=48, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Variables (tipado dinamico)
nombre = "Maria"
edad = 28
altura = 1.65
activo = True

# Tipos de datos
entero = 42
flotante = 3.14159
cadena = "Hola mundo"
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3)  # inmutable
diccionario = {"nombre": "Juan", "edad": 30}
conjunto = {1, 2, 3, 4, 5}

# Verificar tipo
print(type(edad))  # <class "int">
print(isinstance(cadena, str))  # True'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ControlFlowScene(Scene):
    def construct(self):
        title = Text("Control de Flujo", font_size=48, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Condicionales
edad = 20

if edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")

# Operador ternario
mensaje = "Mayor" if edad >= 18 else "Menor"

# Match (Python 3.10+)
status = 200
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Otro")

# For loop
for i in range(10):  # 0-9
    print(i)

for item in lista:
    print(item)

# While
contador = 0
while contador < 5:
    contador += 1'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class FunctionsScene(Scene):
    def construct(self):
        title = Text("Funciones", font_size=48, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Definicion de funciones
def saludar(nombre):
    return f"Hola {nombre}"

# Parametros con valores por defecto
def potencia(base, exponente=2):
    return base ** exponente

# Args y Kwargs
def var_args(*args, **kwargs):
    print(f"Posicionales: {args}")
    print(f"Nombrados: {kwargs}")

var_args(1, 2, 3, nombre="Juan", edad=30)

# Funciones lambda
cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b

# Decoradores
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes")
        resultado = func(*args, **kwargs)
        print("Despues")
        return resultado
    return wrapper

@mi_decorador
def hola():
    print("Hola!")

# Generadores
def generador():
    for i in range(5):
        yield i'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class DataStructuresScene(Scene):
    def construct(self):
        title = Text("Estructuras de Datos", font_size=44, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Listas
frutas = ["manzana", "banana", "naranja"]
frutas.append("uva")
frutas.insert(1, "pera")
frutas.remove("banana")
ultimo = frutas.pop()

# List comprehensions
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
cuadrados = [n**2 for n in range(10)]

# Diccionarios
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Lima"}
persona["profesion"] = "Ingeniera"
del persona["ciudad"]
print(persona.get("nombre"))

# Dict comprehension
precios = {"manzana": 3, "banana": 2, "naranja": 4}
dupidos = {k: v*2 for k, v in precios.items()}

# Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union = A | B
interseccion = A & B
diferencia = A - B'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class OOPScene(Scene):
    def construct(self):
        title = Text("POO en Python", font_size=48, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

    def saludar(self):
        return f"Hola, soy {self.nombre}"

# Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def __str__(self):
        return f"{super().__str__()}, salario: {self.salario}"

# Encapsulamiento (convencion)
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # privado

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

# Polimorfismo
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ErrorHandlingScene(Scene):
    def construct(self):
        title = Text("Manejo de Excepciones", font_size=44, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Try-except
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error general: {e}")
else:
    print("Sin errores")
finally:
    print("Siempre se ejecuta")

# Lanzar excepciones
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# Excepciones personalizadas
class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)

# With (context manager)
with open("archivo.txt", "r") as f:
    contenido = f.read()
# El archivo se cierra automaticamente'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ModulesScene(Scene):
    def construct(self):
        title = Text("Modulos y Paquetes", font_size=44, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Importar modulos
import math
from datetime import datetime
from collections import Counter, defaultdict

# Alias
import numpy as np
import pandas as pd

# Modulo personalizado (mi_modulo.py)
"""
# mi_modulo.py
def saludar(nombre):
    return f"Hola {nombre}"

CONSTANTE = 42
"""
import mi_modulo
print(mi_modulo.saludar("Juan"))

# Paquetes
"""
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
"""
from mi_paquete import modulo1

# Instalar paquetes
# pip install requests numpy pandas

# Virtual environment
# python -m venv venv
# venv\\Scripts\\activate'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class FileIOScene(Scene):
    def construct(self):
        title = Text("Lectura y Escritura de Archivos", font_size=38, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Archivos de texto
with open("datos.txt", "w") as f:
    f.write("Hola mundo\\n")
    f.write("Segunda linea")

with open("datos.txt", "r") as f:
    lineas = f.readlines()
    contenido = f.read()

# JSON
import json

datos = {"nombre": "Ana", "edad": 30, "ciudad": "Lima"}
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)

with open("datos.json", "r") as f:
    datos = json.load(f)

# CSV
import csv

with open("datos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Ana", 30])
    writer.writerow(["Juan", 25])

with open("datos.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AsyncScene(Scene):
    def construct(self):
        title = Text("Async/Await", font_size=48, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''import asyncio

# Funcion asincrona
async def obtener_datos():
    await asyncio.sleep(1)
    return {"id": 1, "nombre": "Producto"}

# Ejecutar coroutine
async def main():
    resultado = await obtener_datos()
    print(resultado)

asyncio.run(main())

# Tareas concurrentes
async def tarea1():
    await asyncio.sleep(1)
    return "Tarea 1"

async def tarea2():
    await asyncio.sleep(2)
    return "Tarea 2"

async def main():
    # Ejecutar en paralelo
    resultados = await asyncio.gather(
        tarea1(),
        tarea2()
    )
    print(resultados)

asyncio.run(main())

# Create task
async def demo():
    task = asyncio.create_task(tarea1())
    resultado = await task'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Python", font_size=38, color=PYTHON_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Variables y tipos de datos", font_size=22, color=TEXT_COLOR),
            Text("Control de flujo: if, for, while", font_size=22, color=TEXT_COLOR),
            Text("Funciones: lambda, decoradores, generadores", font_size=22, color=TEXT_COLOR),
            Text("Estructuras: listas, diccionarios, sets", font_size=22, color=TEXT_COLOR),
            Text("POO: clases, herencia, encapsulamiento", font_size=22, color=TEXT_COLOR),
            Text("Manejo de excepciones", font_size=22, color=TEXT_COLOR),
            Text("Modulos y paquetes", font_size=22, color=TEXT_COLOR),
            Text("Lectura/escritura de archivos", font_size=22, color=TEXT_COLOR),
            Text("Async/await para concurrencia", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Lenguaje versatilidad y simplicidad", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class PythonFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        VariablesScene.construct(self)
        ControlFlowScene.construct(self)
        FunctionsScene.construct(self)
        DataStructuresScene.construct(self)
        OOPScene.construct(self)
        ErrorHandlingScene.construct(self)
        ModulesScene.construct(self)
        FileIOScene.construct(self)
        AsyncScene.construct(self)
        ConclusionScene.construct(self)
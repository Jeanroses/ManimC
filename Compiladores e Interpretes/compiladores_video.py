from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
COMP_COLOR = "#e91e63"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Compiladores e Interpretes", font_size=60, color=COMP_COLOR).set_color_by_gradient(COMP_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class LexerScene(Scene):
    def construct(self):
        title = Text("Analisis Lexico", font_size=48, color=COMP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Analisis Lexico - Tokenizacion

# Token types
TOKENS = {
    "KEYWORD": ["if", "else", "while", "for", "return", "int", "float", "void"],
    "OPERATOR": ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="],
    "DELIMITER": ["(", ")", "{", "}", ";", ",", "["],
    "LITERAL": ["123", "3.14", '"hola"', "true", "false"],
}

# Lexer simple en Python
import re

class Token:
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1
        self.columna = 1

    def tokenizar(self):
        tokens = []
        while self.pos < len(self.codigo):
            char = self.codigo[self.pos]

            # Saltar whitespace
            if char in " \t\n":
                if char == "\n":
                    self.linea += 1
                    self.columna = 1
                else:
                    self.columna += 1
                self.pos += 1
                continue

            # Identificadores y keywords
            if char.isalpha() or char == "_":
                start = self.pos
                while self.pos < len(self.codigo) and (self.codigo[self.pos].isalnum() or self.codigo[self.pos] == "_"):
                    self.pos += 1
                valor = self.codigo[start:self.pos]
                tipo = "KEYWORD" if valor in TOKENS["KEYWORD"] else "IDENTIFIER"
                tokens.append(Token(tipo, valor, self.linea, self.columna))
                self.columna += len(valor)
                continue

            # Numeros
            if char.isdigit():
                start = self.pos
                while self.pos < len(self.codigo) and self.codigo[self.pos].isdigit():
                    self.pos += 1
                tokens.append(Token("NUMBER", self.codigo[start:self.pos], self.linea, self.columna))
                self.columna += self.pos - start
                continue

            # Operadores y delimitadores
            ...
        return tokens'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ParserScene(Scene):
    def construct(self):
        title = Text("Analisis Sintactico", font_size=48, color=COMP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Analisis Sintactico - Parser

# Gramatica de ejemplo (expr = expression)
# expr -> term (("+" | "-") term)*
# term -> factor (("*" | "/") factor)*
# factor -> NUMBER | "(" expr ")"

class AST:
    pass

class Numero(AST):
    def __init__(self, valor):
        self.valor = valor

class BinOp(AST):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

# Recursive Descent Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.expr()

    def expr(self):
        nodo = self.term()
        while self.pos < len(self.tokens) and self.es_operador(["+", "-"]):
            op = self.consumir()
            derecha = self.term()
            nodo = BinOp(nodo, op, derecha)
        return nodo

    def term(self):
        nodo = self.factor()
        while self.pos < len(self.tokens) and self.es_operador(["*", "/"]):
            op = self.consumir()
            derecha = self.factor()
            nodo = BinOp(nodo, op, derecha)
        return nodo

    def factor(self):
        token = self.tokens[self.pos]
        if token.tipo == "NUMBER":
            self.pos += 1
            return Numero(int(token.valor))
        elif token.valor == "(":
            self.pos += 1  # consumir (
            nodo = self.expr()
            self.consumir(")")  # consumir )
            return nodo
        raise SyntaxError(f"Token inesperado: {token}")

# AST para: 3 + 4 * 2
#     (+)
#    /   \
#   3    (*)
#       /   \
#      4     2'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class EvalScene(Scene):
    def construct(self):
        title = Text("Evaluacion y Codegen", font_size=48, color=COMP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Evaluacion de AST

class Evaluador:
    def visitar(self, nodo):
        if isinstance(nodo, Numero):
            return nodo.valor
        elif isinstance(nodo, BinOp):
            izquierda = self.visitar(nodo.izquierda)
            derecha = self.visitar(nodo.derecha)
            if nodo.operador.valor == "+":
                return izquierda + derecha
            elif nodo.operador.valor == "-":
                return izquierda - derecha
            elif nodo.operador.valor == "*":
                return izquierda * derecha
            elif nodo.operador.valor == "/":
                return izquierda / derecha
        raise ValueError(f"Nodo desconocido: {type(nodo)}")

# Code Generation (bytecode simple)
class Generador:
    def __init__(self):
        self.bytecode = []

    def generar(self, nodo):
        if isinstance(nodo, Numero):
            self.bytecode.append(f"PUSH {nodo.valor}")
        elif isinstance(nodo, BinOp):
            self.generar(nodo.derecha)
            self.generar(nodo.izquierda)
            ops = {"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}
            self.bytecode.append(ops[nodo.operador.valor])

    def get_code(self):
        return self.bytecode

# Para 3 + 4 * 2:
# PUSH 2
# PUSH 4
# MUL
# PUSH 3
# ADD

# Stack-based VM
class VM:
    def ejecutar(self, bytecode):
        pila = []
        for instruccion in bytecode:
            if instruccion.startswith("PUSH"):
                pila.append(int(instruccion.split()[1]))
            elif instruccion == "ADD":
                pila.append(pila.pop() + pila.pop())
            elif instruccion == "SUB":
                a, b = pila.pop(), pila.pop()
                pila.append(b - a)
            elif instruccion == "MUL":
                pila.append(pila.pop() * pila.pop())
            elif instruccion == "DIV":
                a, b = pila.pop(), pila.pop()
                pila.append(b // a)
        return pila[-1]'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class OptimizacionScene(Scene):
    def construct(self):
        title = Text("Optimizacion de Codigo", font_size=48, color=COMP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Optimizaciones de Compiladores

# 1. Constant Folding
# Antes:  x = 3 + 4 + 5
# Despues: x = 12

# 2. Constant Propagation
# Antes:  x = 5; y = x + 2
# Despues: y = 7

# 3. Dead Code Elimination
# Antes:
#   x = 5
#   y = 3  # x nunca se usa
#   z = x + 1
# Despues: z = 6

# 4. Common Subexpression Elimination
# Antes:
#   a = b * c + d
#   e = b * c + f
# Despues:
#   t = b * c
#   a = t + d
#   e = t + f

# 5. Loop Invariant Code Motion
# Antes:
#   for i in range(n):
#       x = y * z  # No cambia en el loop
#       a[i] = x + i
# Despues:
#   x = y * z
#   for i in range(n):
#       a[i] = x + i

# 6. Strength Reduction
# Antes:  x = y * 2
# Despues: x = y << 1
# Antes:  x = y / 4
# Despues: x = y >> 2

# 7. Inlining
# Antes:
#   def cuadrado(x): return x * x
#   y = cuadrado(5)
# Despues: y = 5 * 5

# 8. Tail Call Optimization
# Antes:
#   def fact(n): return n * fact(n-1)
# Despues (tail recursion):
#   def fact(n, acc=1):
#       if n <= 1: return acc
#       return fact(n-1, n * acc)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class IRScene(Scene):
    def construct(self):
        title = Text("IR y Backend", font_size=48, color=COMP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Intermediate Representation (IR)

# Three Address Code (TAC)
# Formato: resultado = arg1 OP arg2
# t1 = a + b
# t2 = t1 * c
# t3 = t2 - d

# SSA Form (Static Single Assignment)
# Cada variable se asigna exactamente una vez
# Variables con versiones: a1, a2, b1, etc.
# Phi functions en puntos de convergencia

# Ejemplo con if:
# a1 = 5
# if x:
#   a2 = a1 + 1
# else:
#   a3 = a1 - 1
# a4 = phi(a2, a3)

# Basic Blocks
# Secuencia lineal de instrucciones
# Un punto de entrada, un punto de salida
# Terminan en: branch, jump, return

# Control Flow Graph (CFG)
# Nodos = basic blocks
# Aristas = transfers de control

# Register Allocation (Graph Coloring)
# - Construir grafo de interferencia
# - Colorear con N colores (registros)
# - Spill a memoria si no hay suficientes

# Peephole Optimization
# Optimizaciones locales en ventana pequena
# Ejemplos:
#   PUSH 0; POP x -> MOV x, 0
#   JMP L; L: -> eliminar salto redundante
#   ADD 0 -> eliminar

# Code Generation
# x86-64 / ARM / WebAssembly / LLVM IR
# Pattern matching del IR a instrucciones nativas

# LLVM - Low Level Virtual Machine
# Frontend (Clang) -> LLVM IR -> Backend (x86, ARM, etc.)
# llc: LLVM static compiler
# opt: LLVM optimizer'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Compiladores e Interpretes", font_size=38, color=COMP_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Lexer: tokenizacion y regex", font_size=22, color=TEXT_COLOR),
            Text("Parser: gramaticas y AST", font_size=22, color=TEXT_COLOR),
            Text("Evaluacion y code generation", font_size=22, color=TEXT_COLOR),
            Text("Optimizacion de codigo", font_size=22, color=TEXT_COLOR),
            Text("IR, SSA y CFG", font_size=22, color=TEXT_COLOR),
            Text("LLVM y backends", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("El puente entre humanos y maquinas", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class CompiladoreseInterpretesFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        LexerScene.construct(self)
        ParserScene.construct(self)
        EvalScene.construct(self)
        OptimizacionScene.construct(self)
        IRScene.construct(self)
        ConclusionScene.construct(self)

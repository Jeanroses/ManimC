from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
EDA_COLOR = "#aa00ff"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Estructuras de Datos y Algoritmos", font_size=60, color=EDA_COLOR).set_color_by_gradient(EDA_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class ArraysScene(Scene):
    def construct(self):
        title = Text("Arrays y Listas", font_size=48, color=EDA_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Arrays - Arreglos

# Array estatico (tamano fijo)
arr = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Acceso O(1)
arr[5] = 42
print(arr[5])  # 42

# Array dinamico (ArrayList/Python list)
lista = []
lista.append(1)      # O(1) amortizado
lista.insert(0, 0)   # O(n)
lista.pop()          # O(1)
lista.pop(0)         # O(n)

# Sliding Window
def max_subarray_sum(arr, k):
    max_sum = sum(arr[:k])
    window_sum = max_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Two Pointers
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        suma = arr[left] + arr[right]
        if suma == target:
            return [left, right]
        elif suma < target:
            left += 1
        else:
            right -= 1
    return []

# Prefix Sum
def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i, val in enumerate(arr):
        prefix[i + 1] = prefix[i] + val
    return prefix
# suma(i..j) = prefix[j + 1] - prefix[i]'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class LinkedListScene(Scene):
    def construct(self):
        title = Text("Listas Enlazadas", font_size=48, color=EDA_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, valor):
        if not self.cabeza:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def detectar_ciclo(self):
        lento = self.cabeza
        rapido = self.cabeza
        while rapido and rapido.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
            if lento == rapido:
                return True  # Floyd's cycle detection
        return False

# Lista doblemente enlazada
class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

# Aplicaciones: LRU Cache, Undo/Redo, Navegador'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class TreesScene(Scene):
    def construct(self):
        title = Text("Arboles y Grafos", font_size=48, color=EDA_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Arbol Binario de Busqueda (BST)
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    def insertar(self, raiz, valor):
        if not raiz:
            return NodoArbol(valor)
        if valor < raiz.valor:
            raiz.izquierdo = self.insertar(raiz.izquierdo, valor)
        else:
            raiz.derecho = self.insertar(raiz.derecho, valor)
        return raiz

    def buscar(self, raiz, valor):
        if not raiz or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izquierdo, valor)
        return self.buscar(raiz.derecho, valor)

    def recorridos(self, raiz):
        # In-order: izquierdo, raiz, derecho (ordenado)
        if raiz:
            self.recorridos(raiz.izquierdo)
            print(raiz.valor)
            self.recorridos(raiz.derecho)

        # Pre-order: raiz, izquierdo, derecho
        # Post-order: izquierdo, derecho, raiz

    def altura(self, raiz):
        if not raiz:
            return 0
        return 1 + max(self.altura(raiz.izquierdo),
                       self.altura(raiz.derecho))

# Grafos - Representacion
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# DFS (Depth-First Search)
def dfs(grafo, inicio):
    visitados = set()
    pila = [inicio]
    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            pila.extend(grafo[nodo] - visitados)
    return visitados

# BFS (Breadth-First Search)
from collections import deque
def bfs(grafo, inicio):
    visitados = set([inicio])
    cola = deque([inicio])
    while cola:
        nodo = cola.popleft()
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return visitados'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class SortingScene(Scene):
    def construct(self):
        title = Text("Algoritmos de Ordenamiento", font_size=48, color=EDA_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Bubble Sort O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimizacion
    return arr

# Merge Sort O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort O(n log n) promedio
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Heap Sort O(n log n)
import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Counting Sort O(n + k)
def counting_sort(arr):
    counts = [0] * (max(arr) + 1)
    for num in arr:
        counts[num] += 1
    result = []
    for i, count in enumerate(counts):
        result.extend([i] * count)
    return result'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class DynamicScene(Scene):
    def construct(self):
        title = Text("Programacion Dinamica", font_size=48, color=EDA_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Programacion Dinamica

# 1. Fibonacci (Top-down con memoization)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# 2. Fibonacci (Bottom-up)
def fib_iterativo(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# 3. Knapsack - Mochila 0/1
def mochila(capacidad, pesos, valores, n):
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(
                    valores[i - 1] + dp[i - 1][w - pesos[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]

# 4. Longest Common Subsequence (LCS)
def lcs(texto1, texto2):
    m, n = len(texto1), len(texto2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if texto1[i - 1] == texto2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# 5. Coin Change - Minimum Coins
def monedas(monedas, cantidad):
    dp = [float("inf")] * (cantidad + 1)
    dp[0] = 0
    for i in range(1, cantidad + 1):
        for moneda in monedas:
            if moneda <= i:
                dp[i] = min(dp[i], dp[i - moneda] + 1)
    return dp[cantidad] if dp[cantidad] != float("inf") else -1'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Estructuras de Datos y Algoritmos", font_size=38, color=EDA_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Arrays, sliding window, two pointers", font_size=22, color=TEXT_COLOR),
            Text("Listas enlazadas y deteccion de ciclos", font_size=22, color=TEXT_COLOR),
            Text("Arboles binarios y BST", font_size=22, color=TEXT_COLOR),
            Text("Grafos: DFS y BFS", font_size=22, color=TEXT_COLOR),
            Text("Sorting: Merge, Quick, Heap Sort", font_size=22, color=TEXT_COLOR),
            Text("Programacion dinamica y DP clasicos", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Fundamento de todo buen programador", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class EstructurasdeDatosyAlgoritmosFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        ArraysScene.construct(self)
        LinkedListScene.construct(self)
        TreesScene.construct(self)
        SortingScene.construct(self)
        DynamicScene.construct(self)
        ConclusionScene.construct(self)

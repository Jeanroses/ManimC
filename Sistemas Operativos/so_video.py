from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
SO_COLOR = "#00bfa5"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Sistemas Operativos", font_size=60, color=SO_COLOR).set_color_by_gradient(SO_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class ProcesosScene(Scene):
    def construct(self):
        title = Text("Procesos y Scheduling", font_size=48, color=SO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Procesos en Linux

# Ver procesos
ps aux  # Todos los procesos
ps -ef  # Formato completo
top     # Monitor interactivo
htop    # Version mejorada

# Arbol de procesos
pstree -p

# Estados de un proceso
# R (Running): ejecutandose
# S (Sleeping): esperando I/O
# D (Uninterruptible): esperando disco
# Z (Zombie): terminado, padre no recogio
# T (Stopped): detenido con SIGSTOP

# Scheduling - Algoritmos clasicos
# FCFS: First Come First Served
# SJF: Shortest Job First
# Round Robin: quantum de tiempo
# Priority: prioridades estaticas/dinamicas

# Priorities en Linux
# -20 a 19 (menor = mayor prioridad)
nice -n -10 ./programa  # Alta prioridad
renice -n 5 -p 1234     # Cambiar prioridad PID 1234

# Fork - Crear procesos
import os

pid = os.fork()
if pid == 0:
    # Proceso hijo
    print(f"Hijo: PID={os.getpid()}, Padre={os.getppid()}")
else:
    # Proceso padre
    print(f"Padre: PID={os.getpid()}, Hijo={pid}")
    os.wait()  # Esperar hijo

# Signals
import signal, time

def handler(signum, frame):
    print(f"Recibida senal: {signum}")

signal.signal(signal.SIGINT, handler)  # Ctrl+C
signal.signal(signal.SIGTERM, handler) # kill
print("Esperando... (PID:", os.getpid(), ")")
signal.pause()'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ThreadsScene(Scene):
    def construct(self):
        title = Text("Hilos y Concurrencia", font_size=48, color=SO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Threads en Python
import threading
import time

contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        with lock:  # Exclusion mutua
            contador += 1

# Crear hilos
hilos = []
for _ in range(10):
    h = threading.Thread(target=incrementar)
    hilos.append(h)
    h.start()

# Esperar todos
for h in hilos:
    h.join()

print(f"Contador final: {contador} (esperado: 1000000)")

# Thread Pool
from concurrent.futures import ThreadPoolExecutor

def tarea(n):
    time.sleep(0.1)
    return n * n

with ThreadPoolExecutor(max_workers=4) as executor:
    resultados = list(executor.map(tarea, range(10)))
print(resultados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Race Condition
# Ocurre cuando dos hilos acceden a recurso compartido sin sincronizacion

# Deadlock
# Dos hilos esperan recursos que el otro tiene
# Estrategias: lock jerarquico, timeout, deteccion

# Condition Variable
cond = threading.Condition()
cola = []

def productor():
    with cond:
        cola.append("item")
        cond.notify()  # Despertar consumidor

def consumidor():
    with cond:
        while not cola:
            cond.wait()  # Esperar item
        item = cola.pop()'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class MemoriaScene(Scene):
    def construct(self):
        title = Text("Gestion de Memoria", font_size=48, color=SO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Memoria Virtual y Paginacion

# Segmentacion de memoria
# .text: codigo del programa (solo lectura)
# .data: variables globales inicializadas
# .bss: variables globales no inicializadas
# .heap: memoria dinamica (malloc/new)
# .stack: variables locales y call stack

# Paginacion
# Pagina: unidad de memoria virtual (4KB tipicamente)
# Marco: unidad de memoria fisica
# Tabla de paginas: mapeo virtual -> fisico
# TLB: Translation Lookaside Buffer (cache)

# Reemplazo de paginas
# FIFO: First In First Out
# LRU: Least Recently Used
# Optimal: futuro conocido (teorico)
# Clock: aproximacion a LRU

# Alocacion de memoria en C
# malloc, calloc, realloc, free
# mmap: mapear archivos a memoria

# Memory leak
# Ocurre cuando no liberamos memoria alocada
# Herramientas: valgrind, address sanitizer

# swap
cat /proc/swaps
free -h  # Memoria y swap

# Page cache
cat /proc/meminfo | grep -E "^(Cached|Buffers|Active|Inactive)"

# /proc - Filesystem virtual
cat /proc/self/status  # Estado del proceso actual
cat /proc/cpuinfo      # Informacion CPU
cat /proc/meminfo      # Informacion memoria

# Segmentacion (x86-64)
# CS: Code Segment
# DS: Data Segment
# SS: Stack Segment
# ES, FS, GS: Extra segments'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class FileSystemScene(Scene):
    def construct(self):
        title = Text("Sistemas de Archivos", font_size=48, color=SO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Sistemas de Archivos

# ext4 (Linux)
# - Journaling (metadatos)
# - Soporte hasta 1EB
# - Extensiones (extents)
# - Fragmentacion reducida

# Inodos
# Cada archivo tiene un inodo con metadatos
# - permisos, propietario, tamano
# - timestamps (atime, mtime, ctime)
# - bloques de datos

stat archivo.txt
ls -li  # Ver inodos

# Permisos UNIX
# rwx rwx rwx
# user group other
chmod 755 script.sh    # rwxr-xr-x
chmod u+x script.sh    # Agregar ejecucion al owner
chown user:group file  # Cambiar propietario

# Links
ln -s target link      # Symlink (acceso directo)
ln target link         # Hard link (mismo inodo)

# Mount points
mount | grep "^/"
df -h                  # Espacio en discos
du -sh directorio/     # Tamano de directorio

# VFS - Virtual File System
# Capa de abstraccion que unifica:
# ext4, XFS, Btrfs, NFS, tmpfs, procfs

# FUSE - Filesystem in Userspace
# sshfs: montar SFTP como FS local
# s3fs: montar S3 como FS local

# Journaling
# Write-ahead logging para consistencia
# Modos: journal, ordered, writeback

# RAID
# RAID 0: striping (rendimiento)
# RAID 1: mirroring (redundancia)
# RAID 5: striping + paridad
# RAID 6: doble paridad
# RAID 10: mirror + stripe'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class IPCScene(Scene):
    def construct(self):
        title = Text("IPC y Sincronizacion", font_size=48, color=SO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# IPC - Inter-Process Communication

# 1. Pipes (tuberias)
# Comunicacion unidireccional padre-hijo
import os

r, w = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(w)
    r = os.fdopen(r)
    print(f"Hijo recibe: {r.read()}")
else:
    os.close(r)
    w = os.fdopen(w, "w")
    w.write("Hola desde el padre!")
    w.close()

# Named Pipes (FIFO)
# mkfifo /tmp/mi_pipe
# Comunicacion entre procesos no relacionados

# 2. Shared Memory
# Memoria compartida entre procesos
# mas rapido que pipes/sockets
# Sincronizacion necesaria (semaphores)

# 3. Message Queues
# System V / POSIX message queues
# Comunicacion asincrona con prioridades

# 4. Sockets
# Comunicacion en red o local (Unix sockets)

# 5. Semaphores
# Sincronizacion entre procesos
import threading
sem = threading.Semaphore(3)  # Maximo 3 concurrentes

def tarea():
    with sem:
        print("Ejecutando...")
        time.sleep(1)

# 6. Mutex (Mutual Exclusion)
lock = threading.Lock()
with lock:
    # Seccion critica

# 7. Barriers
# Esperar a N procesos antes de continuar
barrier = threading.Barrier(5)
def tarea():
    print("Preparando...")
    time.sleep(random.random())
    barrier.wait()  # Esperar los 5
    print("Todos listos!")

# Problemas clasicos
# - Productor-Consumidor
# - Filosofos comensales (dining philosophers)
# - Lectores-Escritores
# - El barbero dormilon'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Sistemas Operativos", font_size=38, color=SO_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Procesos y scheduling en Linux", font_size=22, color=TEXT_COLOR),
            Text("Hilos y concurrencia con locks", font_size=22, color=TEXT_COLOR),
            Text("Gestion de memoria y paginacion", font_size=22, color=TEXT_COLOR),
            Text("Sistemas de archivos y permisos", font_size=22, color=TEXT_COLOR),
            Text("IPC: pipes, colas, memoria compartida", font_size=22, color=TEXT_COLOR),
            Text("Semaphores y sincronizacion", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("La base sobre la que corre todo el software", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class SistemasOperativosFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        ProcesosScene.construct(self)
        ThreadsScene.construct(self)
        MemoriaScene.construct(self)
        FileSystemScene.construct(self)
        IPCScene.construct(self)
        ConclusionScene.construct(self)

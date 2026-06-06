from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
ARCH_COLOR = "#7c3aed"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Arquitectura de Software", font_size=60, color=ARCH_COLOR).set_color_by_gradient(ARCH_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class PatronesScene(Scene):
    def construct(self):
        title = Text("Patrones de Diseno", font_size=48, color=ARCH_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Singleton
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = cls._connect()
        return cls._instance

    @classmethod
    def _connect(cls):
        return "Connected to DB"

# Factory Method
from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def crear(self): pass

class PDF(Documento):
    def crear(self): return "PDF creado"

class Word(Documento):
    def crear(self): return "Word creado"

class FactoryDocumento:
    @staticmethod
    def crear(tipo):
        factories = {"pdf": PDF, "word": Word}
        return factories[tipo]()

# Observer
class Sujeto:
    def __init__(self):
        self._observadores = []

    def attach(self, obs):
        self._observadores.append(obs)

    def notificar(self, datos):
        for obs in self._observadores:
            obs.actualizar(datos)

# Strategy
class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto): pass

class TarjetaCredito(EstrategiaPago):
    def pagar(self, m): return f"Pagado {m} con TC"

class PayPal(EstrategiaPago):
    def pagar(self, m): return f"Pagado {m} con PayPal"

# Decorator
def log_transaccion(func):
    def wrapper(*args, **kwargs):
        print(f"Transaccion iniciada: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class CleanArchScene(Scene):
    def construct(self):
        title = Text("Clean Architecture", font_size=48, color=ARCH_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# CAPAS DE CLEAN ARCHITECTURE

# 1. Domain - Entidades y reglas de negocio
class Usuario:
    def __init__(self, id: str, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

    def cambiar_email(self, nuevo: str):
        if "@" not in nuevo:
            raise ValueError("Email invalido")
        self.email = nuevo

class RepositorioUsuario(ABC):
    @abstractmethod
    def guardar(self, usuario: Usuario): pass
    @abstractmethod
    def buscar_por_id(self, id: str) -> Usuario: pass

# 2. Application - Casos de uso
class CrearUsuario:
    def __init__(self, repo: RepositorioUsuario):
        self.repo = repo

    def ejecutar(self, nombre: str, email: str) -> Usuario:
        usuario = Usuario(id=str(uuid4()), nombre=nombre, email=email)
        self.repo.guardar(usuario)
        return usuario

# 3. Infrastructure - Adaptadores
class RepositorioPostgres(RepositorioUsuario):
    def guardar(self, usuario: Usuario):
        db.execute("INSERT INTO usuarios VALUES (%s, %s, %s)",
                   (usuario.id, usuario.nombre, usuario.email))

    def buscar_por_id(self, id: str) -> Usuario:
        row = db.execute("SELECT * FROM usuarios WHERE id = %s", (id,)).fetchone()
        return Usuario(row[0], row[1], row[2])

# 4. Presentation - Controllers
class ControladorUsuario:
    def __init__(self, caso_uso: CrearUsuario):
        self.caso_uso = caso_uso

    def crear(self, request):
        user = self.caso_uso.ejecutar(request["nombre"], request["email"])
        return {"id": user.id, "nombre": user.nombre}

# Principio de Inversion de Dependencias
# Las capas externas dependen de las internas (no al reves)
# Domain no sabe nada de Infrastructure'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class DDDScene(Scene):
    def construct(self):
        title = Text("Domain-Driven Design", font_size=48, color=ARCH_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Value Object - Inmutable
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Dinero:
    cantidad: Decimal
    moneda: str

    def __add__(self, otro: "Dinero") -> "Dinero":
        if self.moneda != otro.moneda:
            raise ValueError("Moneda diferente")
        return Dinero(self.cantidad + otro.cantidad, self.moneda)

# Entity - Identidad unica
@dataclass
class Orden:
    id: str
    items: list
    estado: str
    total: Dinero

    def agregar_item(self, producto, cantidad):
        item = ItemOrden(producto, cantidad, producto.precio * cantidad)
        self.items.append(item)
        self.total += item.subtotal

    def enviar(self):
        if not self.items:
            raise ValueError("Orden vacia")
        self.estado = "ENVIADA"

# Aggregate Root
class Cliente:
    def __init__(self, id: str, nombre: str):
        self.id = id
        self.nombre = nombre
        self.ordenes = []

    def crear_orden(self, items) -> Orden:
        total = sum(i.subtotal for i in items)
        orden = Orden(id=str(uuid4()), items=items, estado="PENDIENTE", total=total)
        self.ordenes.append(orden)
        return orden

# Domain Service
class ServicioPrecios:
    def calcular_descuento(self, cliente, orden) -> Dinero:
        if len(cliente.ordenes) > 10:
            return orden.total * Decimal("0.9")
        return orden.total

# Repository
class RepositorioOrden(ABC):
    @abstractmethod
    def guardar(self, orden: Orden): pass
    @abstractmethod
    def buscar_por_id(self, id: str) -> Orden: pass
    @abstractmethod
    def buscar_por_cliente(self, id: str) -> list: pass'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class CQRSScene(Scene):
    def construct(self):
        title = Text("CQRS y Event Sourcing", font_size=48, color=ARCH_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# CQRS - Segregacion de Responsabilidad

# COMMAND (Escritura)
class ComandoCrearOrden:
    def __init__(self, cliente_id: str, items: list):
        self.cliente_id = cliente_id
        self.items = items

class ManejadorCrearOrden:
    def __init__(self, repo: RepositorioOrden):
        self.repo = repo

    def manejar(self, cmd: ComandoCrearOrden):
        orden = Orden.crear(cmd.cliente_id, cmd.items)
        self.repo.guardar(orden)
        return orden.id

# QUERY (Lectura) - Modelo separado
class ConsultaOrden:
    def __init__(self, orden_id: str):
        self.orden_id = orden_id

class ManejadorConsultaOrden:
    def __init__(self, db_lectura):
        self.db = db_lectura

    async def manejar(self, query: ConsultaOrden):
        return await self.db.obtener_orden(query.orden_id)

# Event Sourcing
class EventoAlmacen:
    def __init__(self):
        self.eventos = {}

    def agregar(self, id_agregado: str, evento):
        if id_agregado not in self.eventos:
            self.eventos[id_agregado] = []
        self.eventos[id_agregado].append(evento)

    def obtener_eventos(self, id_agregado: str) -> list:
        return self.eventos.get(id_agregado, [])

    def reconstruir(self, id_agregado: str):
        orden = None
        for evento in self.obtener_eventos(id_agregado):
            if isinstance(evento, OrdenCreada):
                orden = Orden(evento.id, evento.cliente_id, evento.items)
            elif isinstance(evento, OrdenEnviada):
                orden.enviar(evento.numero_seguimiento)
        return orden

# Beneficios:
# - Escalabilidad (lectura != escritura)
# - Auditoria completa
# - Historial de cambios'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class HexagonalScene(Scene):
    def construct(self):
        title = Text("Arquitectura Hexagonal", font_size=48, color=ARCH_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# PUERTO (Interface)
class PuertoUsuario:
    def crear_usuario(self, datos): pass
    def obtener_usuario(self, id): pass

# PUERTO (Interface) para repositorio
class PuertoRepositorioUsuario(ABC):
    @abstractmethod
    def guardar(self, usuario): pass
    @abstractmethod
    def buscar(self, id): pass

# CASO DE USO (Core)
class ServicioUsuario:
    def __init__(self, repo: PuertoRepositorioUsuario):
        self.repo = repo

    def registrar(self, nombre, email):
        usuario = Usuario(id=str(uuid4()), nombre=nombre, email=email)
        self.repo.guardar(usuario)
        return usuario

# ADAPTADOR DE ENTRADA (REST)
from flask import Flask, request, jsonify

app = Flask(__name__)
servicio = ServicioUsuario(RepositorioPostgres())

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.json
    usuario = servicio.registrar(datos["nombre"], datos["email"])
    return jsonify({"id": usuario.id, "nombre": usuario.nombre}), 201

@app.route("/usuarios/<id>", methods=["GET"])
def obtener_usuario(id):
    usuario = servicio.repo.buscar(id)
    return jsonify({"id": usuario.id, "nombre": usuario.nombre})

# ADAPTADOR DE SALIDA (Postgres)
class RepositorioPostgres(PuertoRepositorioUsuario):
    def guardar(self, usuario):
        pool.execute("INSERT INTO usuarios VALUES ($1, $2, $3)",
                     usuario.id, usuario.nombre, usuario.email)

    def buscar(self, id):
        row = pool.fetch("SELECT * FROM usuarios WHERE id = $1", id)
        return Usuario(row[0], row[1], row[2])

# Ventajas: testeas el core sin infraestructura'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Arquitectura de Software", font_size=38, color=ARCH_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Patrones de diseno creacionales y estructurales", font_size=22, color=TEXT_COLOR),
            Text("Clean Architecture y hexagonal", font_size=22, color=TEXT_COLOR),
            Text("Domain-Driven Design (DDD)", font_size=22, color=TEXT_COLOR),
            Text("CQRS y Event Sourcing", font_size=22, color=TEXT_COLOR),
            Text("Arquitectura en capas", font_size=22, color=TEXT_COLOR),
            Text("Principio de inversion de dependencias", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("La base de todo sistema de software exitoso", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class ArquitecturadeSoftwareFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        PatronesScene.construct(self)
        CleanArchScene.construct(self)
        DDDScene.construct(self)
        CQRSScene.construct(self)
        HexagonalScene.construct(self)
        ConclusionScene.construct(self)

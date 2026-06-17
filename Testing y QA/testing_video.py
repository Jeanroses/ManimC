from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
TEST_COLOR = "#00c853"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Testing y QA", font_size=60, color=TEST_COLOR).set_color_by_gradient(TEST_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class UnitTestScene(Scene):
    def construct(self):
        title = Text("Pruebas Unitarias", font_size=48, color=TEST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# pytest - Pruebas unitarias
import pytest
from src.calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

class TestCalculadora:
    def test_sumar(self, calc):
        assert calc.sumar(2, 3) == 5
        assert calc.sumar(-1, 1) == 0
        assert calc.sumar(0, 0) == 0

    def test_dividir(self, calc):
        assert calc.dividir(10, 2) == 5
        assert calc.dividir(7, 2) == 3.5

    def test_dividir_por_cero(self, calc):
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.dividir(10, 0)

    @pytest.mark.parametrize("a, b, esperado", [
        (1, 2, 3),
        (0, 5, 5),
        (-3, 3, 0),
        (100, 200, 300),
    ])
    def test_sumar_parametrizado(self, calc, a, b, esperado):
        assert calc.sumar(a, b) == esperado

# Mocking
from unittest.mock import Mock, patch

def test_enviar_email():
    servicio_email = Mock()
    servicio_email.enviar.return_value = True

    resultado = notificar_usuario(servicio_email, "test@test.com")

    servicio_email.enviar.assert_called_once_with(
        "test@test.com",
        "Bienvenido",
        "Contenido..."
    )
    assert resultado == True

# Cobertura
# pytest --cov=src --cov-report=html tests/'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class IntegrationScene(Scene):
    def construct(self):
        title = Text("Pruebas de Integracion", font_size=48, color=TEST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Pruebas de integracion con base de datos
import pytest
from src.repositorio import RepositorioUsuario
from src.modelos import Usuario

@pytest.fixture
def db_session():
    # Base de datos en memoria para testing
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def repo(db_session):
    return RepositorioUsuario(db_session)

def test_guardar_usuario(repo):
    usuario = Usuario(nombre="Juan", email="juan@test.com")
    repo.guardar(usuario)

    resultado = repo.buscar_por_email("juan@test.com")
    assert resultado is not None
    assert resultado.nombre == "Juan"

def test_actualizar_usuario(repo):
    usuario = Usuario(nombre="Ana", email="ana@test.com")
    repo.guardar(usuario)

    usuario.nombre = "Ana Maria"
    repo.actualizar(usuario)

    resultado = repo.buscar_por_email("ana@test.com")
    assert resultado.nombre == "Ana Maria"

# Testcontainers
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="module")
def postgres():
    with PostgresContainer("postgres:16") as postgres:
        yield postgres

def test_conexion_db(postgres):
    connection_url = postgres.get_connection_url()
    # Usar para pruebas reales con PostgreSQL'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class E2EScene(Scene):
    def construct(self):
        title = Text("Pruebas E2E", font_size=48, color=TEST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Cypress - Pruebas End-to-End
describe("Login Flow", () => {
    beforeEach(() => {
        cy.visit("/login");
    });

    it("should display login form", () => {
        cy.get("[data-testid=email-input]").should("be.visible");
        cy.get("[data-testid=password-input]").should("be.visible");
        cy.get("[data-testid=submit-button]")
          .should("be.visible")
          .and("contain", "Iniciar Sesion");
    });

    it("should show error on invalid credentials", () => {
        cy.get("[data-testid=email-input]").type("invalid@email.com");
        cy.get("[data-testid=password-input]").type("wrong");
        cy.get("[data-testid=submit-button]").click();
        cy.get("[data-testid=error-message]")
          .should("be.visible")
          .and("contain", "Credenciales invalidas");
    });

    it("should login successfully", () => {
        cy.intercept("POST", "/api/login", {
            statusCode: 200,
            body: { token: "jwt-token", user: { name: "Juan" } }
        });

        cy.get("[data-testid=email-input]").type("user@test.com");
        cy.get("[data-testid=password-input]").type("password123");
        cy.get("[data-testid=submit-button]").click();

        cy.url().should("include", "/dashboard");
        cy.get("[data-testid=welcome]").should("contain", "Bienvenido Juan");
    });
});

// Playwright
test("completar formulario", async ({ page }) => {
    await page.goto("https://example.com/form");
    await page.fill("[name=nombre]", "Juan");
    await page.fill("[name=email]", "juan@test.com");
    await page.selectOption("[name=pais]", "PE");
    await page.click("button[type=submit]");
    await expect(page.locator(".success")).toBeVisible();
});'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class TDDScene(Scene):
    def construct(self):
        title = Text("TDD y BDD", font_size=48, color=TEST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# TDD - Test Driven Development
# Red -> Green -> Refactor

# 1. RED: Escribir prueba que falla
def test_calcular_precio_con_descuento():
    carrito = Carrito()
    carrito.agregar(Producto("Laptop", 1000))
    carrito.agregar(Producto("Mouse", 50))

    # Descuento del 10% para compras > 500
    total = carrito.calcular_total()
    assert total == 945  # (1000 + 50) * 0.9

# 2. GREEN: Implementacion minima
class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, producto):
        self.items.append(producto)

    def calcular_total(self):
        subtotal = sum(p.precio for p in self.items)
        if subtotal > 500:
            return subtotal * 0.9
        return subtotal

# 3. REFACTOR: Mejorar sin cambiar comportamiento
# Continuar ciclo para mas funcionalidad

# BDD - Behavior Driven Development (Behave)
Feature: Gestion de Carrito
  Scenario: Aplicar descuento por monto
    Given un carrito vacio
    When agrego un producto de $1000
    And agrego un producto de $50
    Then el total debe ser $945

  Scenario: Sin descuento para montos bajos
    Given un carrito vacio
    When agrego un producto de $50
    Then el total debe ser $50

# Step definitions
@given("un carrito vacio")
def step_carrito_vacio(context):
    context.carrito = Carrito()

@when("agrego un producto de ${precio}")
def step_agregar_producto(context, precio):
    context.carrito.agregar(Producto("Test", float(precio)))'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class TestingToolsScene(Scene):
    def construct(self):
        title = Text("Herramientas de Testing", font_size=48, color=TEST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Cobertura de codigo
# pytest --cov=src --cov-report=term-missing --cov-report=html

# Tipos de cobertura:
# - Line coverage: lineas ejecutadas
# - Branch coverage: ramas condicionales
# - Function coverage: funciones llamadas

# Mutation Testing (mutmut)
# Introduce mutaciones y verifica que tests fallen
# Mutation score: mutaciones detectadas / total

# Property-Based Testing (hypothesis)
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_suma_conmutativa(a, b):
    assert Calculadora().sumar(a, b) == Calculadora().sumar(b, a)

@given(st.lists(st.integers()))
def test_ordenamiento(lista):
    resultado = sorted(lista)
    assert len(resultado) == len(lista)
    assert all(resultado[i] <= resultado[i + 1] for i in range(len(resultado) - 1))

# Load Testing (locust)
from locust import HttpUser, task, between

class UsuarioSimulado(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def ver_pagina_principal(self):
        self.client.get("/")

    @task(2)
    def buscar_productos(self):
        self.client.get("/productos?q=laptop")

    @task(1)
    def crear_usuario(self):
        self.client.post("/api/usuarios", json={
            "nombre": "Test",
            "email": "test@test.com"
        })

# py -m locust -f locustfile.py'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Testing y QA", font_size=38, color=TEST_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Pruebas unitarias con pytest", font_size=22, color=TEXT_COLOR),
            Text("Pruebas de integracion con DB", font_size=22, color=TEXT_COLOR),
            Text("E2E con Cypress y Playwright", font_size=22, color=TEXT_COLOR),
            Text("TDD: Red-Green-Refactor", font_size=22, color=TEXT_COLOR),
            Text("BDD con Behave", font_size=22, color=TEXT_COLOR),
            Text("Cobertura y mutation testing", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Calidad no es negociable", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class TestingyQAFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        UnitTestScene.construct(self)
        IntegrationScene.construct(self)
        E2EScene.construct(self)
        TDDScene.construct(self)
        TestingToolsScene.construct(self)
        ConclusionScene.construct(self)

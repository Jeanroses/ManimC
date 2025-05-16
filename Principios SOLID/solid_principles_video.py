from manim import *
import numpy as np

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
WARNING_COLOR = "#fab387"
SUCCESS_COLOR = "#a6e3a1"
ITER_COLOR = "#cba6f7"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Principios SOLID",
            font_size=52,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "Diseño orientado a objetos robusto y mantenible",
            font_size=26,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
        ])
        dots.arrange(RIGHT, buff=0.4).next_to(subtitle, DOWN, buff=0.6)

        self.play(Write(title, run_time=2.2))
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2),
            run_time=1.2,
        )
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(dots),
            run_time=1.0,
        )


class SRPIntroScene(Scene):
    def construct(self):
        title = Text(
            "S - Single Responsibility Principle",
            font_size=42,
            color=HIGHLIGHT_COLOR,
        )
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Una clase debe tener una única razón para cambiar",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        bad_code = '''// Violacion de SRP - Clase con multiples responsabilidades
class UserManager {
  validateUser(user) { /* ... */ }
  saveToDatabase(user) { /* ... */ }
  sendEmail(user) { /* ... */ }
  generateReport(user) { /* ... */ }
  createBackup() { /* ... */ }
}

// Esta clase cambia por:
// 1. Cambios en validacion
// 2. Cambios en base de datos
// 3. Cambios en emails
// 4. Cambios en reportes
// 5. Cambios en backups'''

        bad = Code(
            code_string=bad_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        bad.scale(0.75).next_to(definition, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(Create(bad), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SRPSolutionScene(Scene):
    def construct(self):
        title = Text("SRP - Solución", font_size=44, color=HIGHLIGHT_COLOR)
        title.to_edge(UP, buff=0.5)

        good_code = '''// Cumpliendo SRP - Una responsabilidad por clase
class UserValidator {
  validate(user: User): boolean { /* ... */ }
}

class UserRepository {
  save(user: User): void { /* ... */ }
}

class EmailService {
  sendEmail(user: User, message: string): void { /* ... */ }
}

class ReportGenerator {
  generateReport(user: User): Report { /* ... */ }
}

class BackupService {
  createBackup(): void { /* ... */ }
}

// Cada clase ahora tiene una sola razon para cambiar
// UserValidator cambia solo por reglas de validacion
// UserRepository cambia solo por cambios en DB
// etc.'''

        good = Code(
            code_string=good_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        good.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(good), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class OCPIntroScene(Scene):
    def construct(self):
        title = Text(
            "O - Open/Closed Principle",
            font_size=42,
            color=ACCENT_COLOR,
        )
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Las entidades de software deben estar abiertas para extensión pero cerradas para modificación",
            font_size=22,
            color=TEXT_COLOR,
            line_spacing=1.3,
        )
        definition.next_to(title, DOWN, buff=0.5)

        bad_code = '''// Violacion de OCP - Modificar clase existente para cada nuevo tipo
class PaymentProcessor {
  processPayment(order: Order, paymentType: string): void {
    if (paymentType === "credit") {
      // Process credit card
    } else if (paymentType === "debit") {
      // Process debit card
    } else if (paymentType === "paypal") {
      // Process PayPal
    } else if (paymentType === "crypto") {
      // Process Crypto
    }
    // Cada vez que agregamos un metodo de pago
    //，我们必须修改 esta clase
  }
}'''

        bad = Code(
            code_string=bad_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        bad.scale(0.75).next_to(definition, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(Create(bad), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class OCPSolutionScene(Scene):
    def construct(self):
        title = Text("OCP - Solución con Polimorfismo", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)

        good_code = '''// Cumpliendo OCP - Extender sin modificar
interface PaymentMethod {
  processPayment(amount: number): void;
}

class CreditCardPayment implements PaymentMethod {
  processPayment(amount: number): void {
    // Process credit card
  }
}

class DebitCardPayment implements PaymentMethod {
  processPayment(amount: number): void {
    // Process debit card
  }
}

class PayPalPayment implements PaymentMethod {
  processPayment(amount: number): void {
    // Process PayPal
  }
}

class CryptoPayment implements PaymentMethod {
  processPayment(amount: number): void {
    // Process Crypto
  }
}

// Agregar nuevo metodo de pago sin modificar codigo existente
class PaymentProcessor {
  processPayment(paymentMethod: PaymentMethod): void {
    paymentMethod.processPayment(100);
  }
}

// Ahora podemos agregar BitcoinPayment sin cambiar PaymentProcessor'''

        good = Code(
            code_string=good_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        good.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(good), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LSPIntroScene(Scene):
    def construct(self):
        title = Text(
            "L - Liskov Substitution Principle",
            font_size=42,
            color=SUCCESS_COLOR,
        )
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Los objetos de una clase derivada deben poder remplacer a objetos de la clase base sin alterar el comportamiento",
            font_size=20,
            color=TEXT_COLOR,
            line_spacing=1.3,
        )
        definition.next_to(title, DOWN, buff=0.5)

        bad_code = '''// Violacion de LSP
class Rectangle {
  protected width: number;
  protected height: number;

  setWidth(width: number): void { this.width = width; }
  setHeight(height: number): void { this.height = height; }
  area(): number { return this.width * this.height; }
}

class Square extends Rectangle {
  setWidth(width: number): void {
    this.width = width;
    this.height = width;  // Square fuerza ambas dimensiones iguales
  }

  setHeight(height: number): void {
    this.width = height;
    this.height = height;
  }
}

// Problema
function calculateArea(rect: Rectangle): number {
  rect.setWidth(5);
  rect.setHeight(4);
  return rect.area();  // Espera 20, pero Square retorna 16!
}

let square = new Square();
calculateArea(square); // Comportamiento inesperado!'''

        bad = Code(
            code_string=bad_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        bad.scale(0.8).next_to(definition, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(Create(bad), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LSPSolutionScene(Scene):
    def construct(self):
        title = Text("LSP - Solución", font_size=44, color=SUCCESS_COLOR)
        title.to_edge(UP, buff=0.5)

        good_code = '''// Cumpliendo LSP - Jerarquia correcta
interface Shape {
  area(): number;
}

class Rectangle implements Shape {
  constructor(protected width: number, protected height: number) {}

  area(): number { return this.width * this.height; }

  setDimensions(width: number, height: number): void {
    this.width = width;
    this.height = height;
  }
}

class Square implements Shape {
  constructor(private side: number) {}

  area(): number { return this.side * this.side; }

  setSide(side: number): void {
    this.side = side;
  }
}

// Funcion que trabaja con cualquier Shape
function printArea(shape: Shape): void {
  console.log(`Area: ${shape.area()}`);
}

let rect = new Rectangle(5, 4);
let square = new Square(5);

printArea(rect);   // 20 - Correcto
printArea(square); // 25 - Correcto

// Ambos pueden substituirse indistintamente'''

        good = Code(
            code_string=good_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        good.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(good), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ISPIntroScene(Scene):
    def construct(self):
        title = Text(
            "I - Interface Segregation Principle",
            font_size=42,
            color=CURVE_COLOR,
        )
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Los clientes no deben depender de interfaces que no utilizan",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        bad_code = '''// Violacion de ISP - Interfazgada肥胖
interface Worker {
  work(): void;
  eat(): void;
  sleep(): void;
  attendMeeting(): void;
  writeReport(): void;
}

class HumanWorker implements Worker {
  work(): void { /* ... */ }
  eat(): void { /* ... */ }
  sleep(): void { /* ... */ }
  attendMeeting(): void { /* ... */ }
  writeReport(): void { /* ... */ }
}

class RobotWorker implements Worker {
  work(): void { /* ... */ }
  eat(): void { /* Robot no come! */ }
  sleep(): void { /* Robot no duerme! */ }
  attendMeeting(): void { /* Robot no asiste! */ }
  writeReport(): void { /* Robot no escribe! */ }
}

// Robot esta forzado a implementar metodos que no necesita'''

        bad = Code(
            code_string=bad_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        bad.scale(0.8).next_to(definition, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(Create(bad), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ISPSolutionScene(Scene):
    def construct(self):
        title = Text("ISP - Solución con Interfaces Especificas", font_size=38, color=CURVE_COLOR)
        title.to_edge(UP, buff=0.5)

        good_code = '''// Cumpliendo ISP - Interfaces pequenas y especificas
interface Workable {
  work(): void;
}

interface Eatable {
  eat(): void;
}

interface Sleepable {
  sleep(): void;
}

interface MeetingAttendee {
  attendMeeting(): void;
}

interface ReportWriter {
  writeReport(): void;
}

// HumanWorker implementa todas las interfaces relevantes
class HumanWorker implements Workable, Eatable, Sleepable,
                                MeetingAttendee, ReportWriter {
  work(): void { /* ... */ }
  eat(): void { /* ... */ }
  sleep(): void { /* ... */ }
  attendMeeting(): void { /* ... */ }
  writeReport(): void { /* ... */ }
}

// RobotWorker solo implementa lo que necesita
class RobotWorker implements Workable {
  work(): void { /* ... */ }
}

// Cliente solo depende de lo que necesita
function assignWork(worker: Workable): void {
  worker.work();
}

function provideBreak(eatable: Eatable): void {
  eatable.eat();
}

assignWork(new HumanWorker()); // OK
assignWork(new RobotWorker()); // OK
provideBreak(new HumanWorker()); // OK
// Robot no tiene metodo eat(), no puede ser pasado'''

        good = Code(
            code_string=good_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        good.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(good), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DIPIntroScene(Scene):
    def construct(self):
        title = Text(
            "D - Dependency Inversion Principle",
            font_size=42,
            color=ITER_COLOR,
        )
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Los modulos de alto nivel no deben depender de modulos de bajo nivel. Ambos deben depender de abstracciones",
            font_size=20,
            color=TEXT_COLOR,
            line_spacing=1.3,
        )
        definition.next_to(title, DOWN, buff=0.5)

        bad_code = '''// Violacion de DIP - Dependencia directa de implementaciones
class MySQLConnection {
  connect(): void { /* Conexion MySQL */ }
  query(sql: string): void { /* ... */ }
}

class UserRepository {
  private db: MySQLConnection;

  constructor() {
    this.db = new MySQLConnection(); // Dependencia directa
  }

  saveUser(user: User): void {
    this.db.connect();
    this.db.query("INSERT INTO users ...");
  }
}

// Problemas:
// 1. UserRepository depende de implementacion concreta
// 2. Si queremos cambiar a PostgreSQL, debemos modificar UserRepository
// 3. Dificil de testear (no podemos mockear facilmente)
// 4. Acoplamiento fuerte entre capas'''

        bad = Code(
            code_string=bad_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        bad.scale(0.75).next_to(definition, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(Create(bad), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DIPSolutionScene(Scene):
    def construct(self):
        title = Text("DIP - Solución con Inyección de Dependencias", font_size=36, color=ITER_COLOR)
        title.to_edge(UP, buff=0.5)

        good_code = '''// Cumpliendo DIP - Dependencia de abstracciones
// 1. Definir interfaz abstracta
interface DatabaseConnection {
  connect(): void;
  query(sql: string): void;
}

// 2. Implementaciones concretas
class MySQLConnection implements DatabaseConnection {
  connect(): void { /* MySQL */ }
  query(sql: string): void { /* ... */ }
}

class PostgreSQLConnection implements DatabaseConnection {
  connect(): void { /* PostgreSQL */ }
  query(sql: string): void { /* ... */ }
}

class SQLiteConnection implements DatabaseConnection {
  connect(): void { /* SQLite */ }
  query(sql: string): void { /* ... */ }
}

// 3. Depender de la abstraccion, no de la implementacion
class UserRepository {
  private db: DatabaseConnection;

  // Inyeccion por constructor
  constructor(db: DatabaseConnection) {
    this.db = db;
  }

  saveUser(user: User): void {
    this.db.connect();
    this.db.query("INSERT INTO users ...");
  }
}

// Uso
const mysql = new MySQLConnection();
const userRepo = new UserRepository(mysql);

// Cambiar implementacion sin modificar UserRepository
const postgres = new PostgreSQLConnection();
const userRepo2 = new UserRepository(postgres);

// Test facilmente con mock
const mockDb = new MockDatabase();
const testRepo = new UserRepository(mockDb);'''

        good = Code(
            code_string=good_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        good.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(good), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SRPMetricsScene(Scene):
    def construct(self):
        title = Text("Como detectar violaciones de SRP", font_size=38, color=HIGHLIGHT_COLOR)
        title.to_edge(UP, buff=0.5)

        indicators = VGroup(
            Text("Señales de alerta:", font_size=24, color=HIGHLIGHT_COLOR),
            Text("- Nombre de clase con múltiples conceptos (UserManager, DataHandler)", font_size=18, color=TEXT_COLOR),
            Text("- Métodos que cambian por diferentes razones", font_size=18, color=TEXT_COLOR),
            Text("- Dificultad para describir la clase en una oración", font_size=18, color=TEXT_COLOR),
            Text("- Pruebas unitarias complejas y acopladas", font_size18, color=TEXT_COLOR),
            Text("- Cambios frecuentes en la clase", font_size18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        indicators.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(indicators), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class OCPMetricsScene(Scene):
    def construct(self):
        title = Text("Como detectar violaciones de OCP", font_size=38, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)

        indicators = VGroup(
            Text("Señales de alerta:", font_size=24, color=ACCENT_COLOR),
            Text("- Cambios frecuentes en clases existentes", font_size18, color=TEXT_COLOR),
            Text("- Uso extensivo de if/else o switch para nuevos tipos", font_size18, color=TEXT_COLOR),
            Text("- Miedo a agregar nuevas funcionalidades", font_size18, color=TEXT_COLOR),
            Text("- Tests que requieren modificar cuando se agrega funcionalidad", font_size18, color=TEXT_COLOR),
            Text("- Comentarios tipo 'no agregar mas casos aqui'", font_size18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        indicators.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(indicators), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LSPMetricsScene(Scene):
    def construct(self):
        title = Text("Como detectar violaciones de LSP", font_size=38, color=SUCCESS_COLOR)
        title.to_edge(UP, buff=0.5)

        indicators = VGroup(
            Text("Señales de alerta:", font_size=24, color=SUCCESS_COLOR),
            Text("- Métodos que lanzan excepciones no definidas en clase base", font_size18, color=TEXT_COLOR),
            Text("- Comportamiento diferente en subclase (override que cambia logica)", font_size18, color=TEXT_COLOR),
            Text("- Precondiciones mas fuertes en subclase", font_size18, color=TEXT_COLOR),
            Text("- Postcondiciones mas debiles en subclase", font_size18, color=TEXT_COLOR),
            Text("- Tests que fallan con objetos de subclase", font_size18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        indicators.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(indicators), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ISPMetricsScene(Scene):
    def construct(self):
        title = Text("Como detectar violaciones de ISP", font_size=38, color=CURVE_COLOR)
        title.to_edge(UP, buff=0.5)

        indicators = VGroup(
            Text("Señales de alerta:", font_size=24, color=CURVE_COLOR),
            Text("- Interfaces con muchos metodos (god interfaces)", font_size18, color=TEXT_COLOR),
            Text("- Clases que implementan interfaces pero usan pocos metodos", font_size18, color=TEXT_COLOR),
            Text("- Dependencia de metodos no utilizados", font_size18, color=TEXT_COLOR),
            Text("-Cambios en interfaz afectan muchas clases no relacionadas", font_size18, color=TEXT_COLOR),
            Text("- Tests que requieren mocks de metodos no usados", font_size18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        indicators.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(indicators), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DIPMetricsScene(Scene):
    def construct(self):
        title = Text("Como detectar violaciones de DIP", font_size=38, color=ITER_COLOR)
        title.to_edge(UP, buff=0.5)

        indicators = VGroup(
            Text("Señales de alerta:", font_size=24, color=ITER_COLOR),
            Text("- new Keyword en clases de alto nivel", font_size18, color=TEXT_COLOR),
            Text("- Dependencia de clases concretas en lugar de interfaces", font_size18, color=TEXT_COLOR),
            Text("- Dificultad para testing unitario", font_size18, color=TEXT_COLOR),
            Text("- Cambios en modulo bajo nivel rompen modulo alto nivel", font_size18, color=TEXT_COLOR),
            Text("- Acoplamiento fuerte entre capas", font_size18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        indicators.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(indicators), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SOLIDSummaryScene(Scene):
    def construct(self):
        title = Text("Resumen de Principios SOLID", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        summary = VGroup(
            Text("S - Single Responsibility", font_size=22, color=HIGHLIGHT_COLOR),
            Text("   Una clase = una responsabilidad", font_size=18, color=TEXT_COLOR),

            Text("O - Open/Closed", font_size=22, color=ACCENT_COLOR),
            Text("   Extender sin modificar", font_size=18, color=TEXT_COLOR),

            Text("L - Liskov Substitution", font_size=22, color=SUCCESS_COLOR),
            Text("   Subclases substituibles por base", font_size=18, color=TEXT_COLOR),

            Text("I - Interface Segregation", font_size=22, color=CURVE_COLOR),
            Text("   Interfaces pequenas y especificas", font_size=18, color=TEXT_COLOR),

            Text("D - Dependency Inversion", font_size=22, color=ITER_COLOR),
            Text("   Depender de abstracciones, no concreciones", font_size18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for s in summary:
            self.play(FadeIn(s, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class BenefitsScene(Scene):
    def construct(self):
        title = Text("Beneficios de aplicar SOLID", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        benefits = VGroup(
            Text("Mantenibilidad - Cambios localizados", font_size=22, color=SUCCESS_COLOR),
            Text("Testabilidad - Componentes aisladamente probables", font_size22, color=TEXT_COLOR),
            Text("Reusabilidad - Componentes reutilizables", font_size22, color=TEXT_COLOR),
            Text("Flexibilidad - Cambios con minimo impacto", font_size22, color=TEXT_COLOR),
            Text("Legibilidad - Codigo mas limpio y entendible", font_size22, color=TEXT_COLOR),
            Text("Colaboracion - Equipos pueden trabajar en paralelo", font_size22, color=TEXT_COLOR),
            Text("Escalabilidad - Sistema crece sin complejidad", font_size22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        benefits.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for b in benefits:
            self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Principios SOLID", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("SRP: Una responsabilidad por clase", font_size=24, color=TEXT_COLOR),
            Text("OCP: Abierto para extensión, cerrado para modificación", font_size24, color=TEXT_COLOR),
            Text("LSP: Subclases substituibles por base class", font_size24, color=TEXT_COLOR),
            Text("ISP: Interfaces pequeñas especializadas", font_size24, color=TEXT_COLOR),
            Text("DIP: Depender de abstracciones, no concreciones", font_size24, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        self.wait(1)

        final_msg = Text(
            "Fundamentos para software orientado a objetos de calidad",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SOLIDFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        SRPIntroScene.construct(self)
        SRPSolutionScene.construct(self)
        OCPIntroScene.construct(self)
        OCPSolutionScene.construct(self)
        LSPIntroScene.construct(self)
        LSPSolutionScene.construct(self)
        ISPIntroScene.construct(self)
        ISPSolutionScene.construct(self)
        DIPIntroScene.construct(self)
        DIPSolutionScene.construct(self)
        SRPMetricsScene.construct(self)
        OCPMetricsScene.construct(self)
        LSPMetricsScene.construct(self)
        ISPMetricsScene.construct(self)
        DIPMetricsScene.construct(self)
        SOLIDSummaryScene.construct(self)
        BenefitsScene.construct(self)
        ConclusionScene.construct(self)
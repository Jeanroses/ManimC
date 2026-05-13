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
            "Programacion Orientada\na Objetos en Java",
            font_size=52,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "Principios y tecnicas de diseno orientado a objetos",
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


class WhatIsOOP(Scene):
    def construct(self):
        title = Text("Que es POO?", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        definition = Text(
            "Paradigma de programacion que usa objetos como bloques fundamentales",
            font_size=26,
            color=TEXT_COLOR,
            line_spacing=1.3,
        )
        definition.next_to(title, DOWN, buff=0.7)

        pillars = VGroup(
            Text("Los 4 pilares:", font_size=28, color=HIGHLIGHT_COLOR),
            Text("1. Encapsulamiento", font_size=24, color=CURVE_COLOR),
            Text("2. Herencia", font_size=24, color=SECONDARY_COLOR),
            Text("3. Polimorfismo", font_size=24, color=ACCENT_COLOR),
            Text("4. Abstraccion", font_size=24, color=HIGHLIGHT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        pillars.next_to(definition, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=1)
        self.play(FadeIn(pillars, shift=RIGHT * 0.2), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ClassesAndObjects(Scene):
    def construct(self):
        title = Text("Clases y Objetos", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        class_code = '''public class Persona {
    // Atributos (estado)
    private String nombre;
    private int edad;

    // Constructor
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Metodos (comportamiento)
    public void saludar() {
        System.out.println("Hola, soy " + nombre);
    }
}'''

        java_code = Code(
            code_string=class_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        java_code.scale(0.85).to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)

        explanation = VGroup(
            Text("Clase: plantilla o molde", font_size=22, color=HIGHLIGHT_COLOR),
            Text("Objeto: instancia de una clase", font_size=22, color=ACCENT_COLOR),
            Text("this: referencia al objeto actual", font_size=20, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.2)
        explanation.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EncapsulationScene(Scene):
    def construct(self):
        title = Text("Encapsulamiento", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Ocultar el estado interno y exponer solo operaciones seguras",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        code_example = '''public class CuentaBancaria {
    private double saldo;  // Oculto

    public void depositar(double monto) {
        if (monto > 0) {
            saldo += monto;
        }
    }

    public double getSaldo() {
        return saldo;
    }
}'''

        code = Code(
            code_string=code_example,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.8).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)

        benefits = VGroup(
            Text("Beneficios:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("- Control de acceso", font_size=20, color=ACCENT_COLOR),
            Text("- Validacion de datos", font_size=20, color=ACCENT_COLOR),
            Text("- Mantenimiento facil", font_size=20, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.15)
        benefits.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(code), run_time=1.2)
        self.play(FadeIn(benefits, shift=UP * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class GettersSettersScene(Scene):
    def construct(self):
        title = Text("Getters y Setters", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''private String nombre;

public String getNombre() {
    return nombre;
}

public void setNombre(String nombre) {
    this.nombre = nombre;
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=24,
        )
        java_code.next_to(title, DOWN, buff=0.7)

        explanation = VGroup(
            Text("getNombre(): acceso de lectura", font_size=22, color=HIGHLIGHT_COLOR),
            Text("setNombre(): acceso de escritura con posible validacion", font_size=22, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.3)
        explanation.next_to(java_code, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.2)
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class InheritanceScene(Scene):
    def construct(self):
        title = Text("Herencia", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Mecanismo para crear nuevas clases basadas en clases existentes",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        parent_code = '''public class Animal {
    protected String nombre;

    public void eat() {
        System.out.println("Comiendo...");
    }
}'''

        child_code = '''public class Perro extends Animal {
    public void ladrar() {
        System.out.println("Guau!");
    }
}'''

        parent = Code(
            code_string=parent_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        parent.scale(0.75).to_edge(LEFT, buff=0.4).shift(DOWN * 0.3)

        child = Code(
            code_string=child_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        child.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.3)

        keywords = VGroup(
            Text("extends: palabra clave para heredar", font_size=20, color=HIGHLIGHT_COLOR),
            Text("super: referencia a la clase padre", font_size=20, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2)
        keywords.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(parent), run_time=1)
        self.play(Create(child), run_time=1)
        self.play(FadeIn(keywords), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConstructorsScene(Scene):
    def construct(self):
        title = Text("Constructores", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public class Estudiante {
    private String nombre;
    private int edad;

    // Constructor default
    public Estudiante() {
        this.nombre = "Sin nombre";
        this.edad = 0;
    }

    // Constructor con parametros
    public Estudiante(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Constructor copia
    public Estudiante(Estudiante otro) {
        this.nombre = otro.nombre;
        this.edad = otro.edad;
    }
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.8).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PolymorphismScene(Scene):
    def construct(self):
        title = Text("Polimorfismo", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Capacidad de un objeto de tomar multiples formas",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        example_code = '''// Sobrecarga (mismo metodo, diferentes parametros)
class Calculadora {
    public int sumar(int a, int b) { return a + b; }
    public double sumar(double a, double b) { return a + b; }
    public String sumar(String a, String b) { return a + b; }
}'''

        code = Code(
            code_string=example_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.75).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)

        override_code = '''// Sobrescritura (Runtime Polymorphism)
class Animal {
    public void sonido() { System.out.println("..."); }
}

class Perro extends Animal {
    @Override
    public void sonido() { System.out.println("Guau"); }
}'''

        code2 = Code(
            code_string=override_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code2.scale(0.7).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(code), run_time=1)
        self.play(Create(code2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AbstractionScene(Scene):
    def construct(self):
        title = Text("Abstraccion", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Ocultar detalles complejos y mostrar solo lo esencial",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        abstract_code = '''public abstract class Figura {
    // Metodo abstracto (sin implementacion)
    public abstract double area();

    // Metodo concreto (con implementacion)
    public void mostrar() {
        System.out.println("Soy una figura");
    }
}'''

        code = Code(
            code_string=abstract_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.8).next_to(definition, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(code), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class InterfaceScene(Scene):
    def construct(self):
        title = Text("Interfaces", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        interface_code = '''public interface Volable {
    void volar();  // Implicitamente abstracto
    int getAltitudMaxima();  // Puede tener implementacion default
}

public interface Nadable {
    void nadar();
}'''

        impl_code = '''public class Avion implements Volable {
    @Override
    public void volar() {
        System.out.println("El avion vuela");
    }

    @Override
    public int getAltitudMaxima() {
        return 10000;
    }
}'''

        interface_java = Code(
            code_string=interface_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        interface_java.scale(0.75).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)

        impl_java = Code(
            code_string=impl_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        impl_java.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)

        note = Text("implements: una clase puede implementar multiples interfaces", font_size=22, color=HIGHLIGHT_COLOR)
        note.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(interface_java), run_time=1)
        self.play(Create(impl_java), run_time=1)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AccessModifiersScene(Scene):
    def construct(self):
        title = Text("Modificadores de Acceso", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        table = VGroup(
            Text("Modificador", font_size=22, color=PRIMARY_COLOR),
            Text("Clase", font_size=22, color=PRIMARY_COLOR),
            Text("Paquete", font_size=22, color=PRIMARY_COLOR),
            Text("Subclase", font_size=22, color=PRIMARY_COLOR),
            Text("Todo", font_size=22, color=PRIMARY_COLOR),

            Text("public", font_size=20, color=TEXT_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),

            Text("protected", font_size=20, color=TEXT_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("NO", font_size, color=WARNING_COLOR),

            Text("default", font_size=20, color=TEXT_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("NO", font_size, color=WARNING_COLOR),
            Text("NO", font_size, color=WARNING_COLOR),

            Text("private", font_size=20, color=TEXT_COLOR),
            Text("SI", font_size=20, color=SUCCESS_COLOR),
            Text("NO", font_size, color=WARNING_COLOR),
            Text("NO", font_size, color=WARNING_COLOR),
            Text("NO", font_size, color=WARNING_COLOR),
        )
        table.arrange_in_grid(rows=5, cols=5, buff=(0.5, 0.25))
        table.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(table, shift=UP * 0.2), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class StaticFinalScene(Scene):
    def construct(self):
        title = Text("Static y Final", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        static_code = '''public class Contador {
    private static int instancia = 0;  // Compartida por todas las instancias

    public Contador() {
        instancia++;
    }

    public static int getInstancias() {
        return instancia;
    }
}'''

        static_java = Code(
            code_string=static_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        static_java.scale(0.8).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)

        final_code = '''public class Constantes {
    public static final double PI = 3.14159;
    public static final String VERSION = "1.0";
}

// Metodo final: no se puede sobrescribir
public final class MiClase { }

// Variable final: no puede cambiar
final int x = 10;'''

        final_java = Code(
            code_string=final_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        final_java.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(static_java), run_time=1)
        self.play(Create(final_java), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CompositionScene(Scene):
    def construct(self):
        title = Text("Composicion: tiene-un", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        explanation = Text(
            "Un objeto contiene a otro como parte de su estado",
            font_size=24,
            color=TEXT_COLOR,
        )
        explanation.next_to(title, DOWN, buff=0.5)

        code = '''public class Auto {
    private Motor motor;  // Componente obligatorio

    public Auto() {
        this.motor = new Motor();  // Creacion interna
    }

    public void conducir() {
        motor.encender();
    }
}

public class Motor {
    public void encendcer() { }
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        java_code.scale(0.8).next_to(explanation, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(explanation), run_time=0.8)
        self.play(Create(java_code), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AggregationScene(Scene):
    def construct(self):
        title = Text("Agregacion: tiene-un (independiente)", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public class Universidad {
    private List<Estudiante> estudiantes;

    public Universidad() {
        this.estudiantes = new ArrayList<>();
    }

    public void agregarEstudiante(Estudiante e) {
        estudiantes.add(e);
    }
}  // Los estudiantes existen independientemente'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        difference = Text(
            "Diferencia: en composicion el todo controla la vida del componente",
            font_size=22,
            color=HIGHLIGHT_COLOR,
        )
        difference.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.2)
        self.play(FadeIn(difference), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AssociationScene(Scene):
    def construct(self):
        title = Text("Asociacion: conoce-a", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Relacion debil donde un objeto usa a otro temporalmente",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        code = '''public class Piloto {
    private Avion avion;

    public Piloto(Avion avion) {
        this.avion = avion;
    }

    public void volar() {
        avion.despegar();
    }
}  // El piloto conoce al avion pero no lo posee'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        java_code.scale(0.85).next_to(definition, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(java_code), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ThisSuperScene(Scene):
    def construct(self):
        title = Text("this y super", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        this_code = '''// this: referencia al objeto actual
public class Ejemplo {
    private int valor;

    public void setValor(int valor) {
        this.valor = valor;  // diferencia parametro de atributo
    }
}'''

        super_code = '''// super: referencia a la clase padre
public class Perro extends Animal {
    public Perro(String nombre) {
        super(nombre);  // llamar al constructor padre
    }

    @Override
    public void sonido() {
        super.sonido();  // llamar al metodo padre
        System.out.println("Guau!");
    }
}'''

        this_java = Code(
            code_string=this_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        this_java.scale(0.75).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)

        super_java = Code(
            code_string=super_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        super_java.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)

        self.play(Write(title), run_time=1)
        self.play(Create(this_java), run_time=1)
        self.play(Create(super_java), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class OverridingScene(Scene):
    def construct(self):
        title = Text("Sobrescritura de Metodos (Override)", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        parent = '''public class Figura {
    public double area() {
        return 0;
    }
}'''

        child = '''public class Circulo extends Figura {
    private double radio;

    @Override  // Anotacion de seguridad
    public double area() {
        return Math.PI * radio * radio;
    }
}'''

        parent_code = Code(
            code_string=parent,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        parent_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)

        child_code = Code(
            code_string=child,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        child_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)

        rules = VGroup(
            Text("Reglas:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("- Misma firma que el metodo padre", font_size=18, color=TEXT_COLOR),
            Text("- No puede ser menos restrictivo", font_size=18, color=TEXT_COLOR),
            Text("- @Override es opcional pero recomendado", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1)
        rules.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(parent_code), run_time=1)
        self.play(Create(child_code), run_time=1)
        self.play(FadeIn(rules), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class OverloadingScene(Scene):
    def construct(self):
        title = Text("Sobrecarga de Metodos (Overload)", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public class Calculadora {
    // Mismo nombre, diferentes parametros
    public int sumar(int a, int b) {
        return a + b;
    }

    public double sumar(double a, double b) {
        return a + b;
    }

    public int sumar(int a, int b, int c) {
        return a + b + c;
    }

    public String sumar(String a, String b) {
        return a + b;
    }
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ObjectClassScene(Scene):
    def construct(self):
        title = Text("La clase Object", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        methods = VGroup(
            Text("Metodos de Object:", font_size=24, color=HIGHLIGHT_COLOR),
            Text("toString(): representacion en cadena", font_size=22, color=TEXT_COLOR),
            Text("equals(): comparacion de objetos", font_size=22, color=TEXT_COLOR),
            Text("hashCode(): codigo hash unico", font_size=22, color=TEXT_COLOR),
            Text("clone(): copiar objeto", font_size=22, color=TEXT_COLOR),
            Text("getClass(): informacion de la clase", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.2)
        methods.next_to(title, DOWN, buff=0.6)

        code = '''@Override
public String toString() {
    return "Persona{nombre='" + nombre + "'}";
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        java_code.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(methods, shift=RIGHT * 0.2), run_time=1)
        self.play(Create(java_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ExceptionHandlingScene(Scene):
    def construct(self):
        title = Text("Excepciones en POO", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''try {
    int resultado = dividir(10, 0);
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Siempre se ejecuta");
}

// Throws: declaracion de excepciones
public int dividir(int a, int b) throws ArithmeticException {
    if (b == 0) throw new ArithmeticException("Divisor cero");
    return a / b;
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class GenericsScene(Scene):
    def construct(self):
        title = Text("Genericos", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        generic_class = '''public class Caja<T> {
    private T elemento;

    public void set(T elemento) {
        this.elemento = elemento;
    }

    public T get() {
        return elemento;
    }
}'''

        generic_usage = '''Caja<String> cajaStrings = new Caja<>();
cajaStrings.set("Hola");
String texto = cajaStrings.get();

Caja<Integer> cajaNumeros = new Caja<>();
cajaNumeros.set(42);
Integer numero = cajaNumeros.get();'''

        class_code = Code(
            code_string=generic_class,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        class_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(DOWN * 0.2)

        use_code = Code(
            code_string=generic_usage,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        use_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(class_code), run_time=1)
        self.play(Create(use_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CollectionsScene(Scene):
    def construct(self):
        title = Text("Colecciones en Java", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        hierarchy = VGroup(
            Text("Jerarquia de Collections:", font_size=24, color=HIGHLIGHT_COLOR),
            Text("List (ordenado, duplicados)", font_size=20, color=CURVE_COLOR),
            Text("  - ArrayList, LinkedList", font_size=18, color=TEXT_COLOR),
            Text("Set (sin duplicados)", font_size=20, color=SECONDARY_COLOR),
            Text("  - HashSet, TreeSet", font_size=18, color=TEXT_COLOR),
            Text("Map (clave-valor)", font_size=20, color=ACCENT_COLOR),
            Text("  - HashMap, TreeMap", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        hierarchy.next_to(title, DOWN, buff=0.6)

        code = '''List<String> lista = new ArrayList<>();
lista.add("Manzana");
lista.add("Banano");
System.out.println(lista.get(0));  // "Manzana"

Map<Integer, String> mapa = new HashMap<>();
mapa.put(1, "Uno");
mapa.put(2, "Dos");'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(hierarchy, shift=RIGHT * 0.2), run_time=1)
        self.play(Create(java_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class UMLScene(Scene):
    def construct(self):
        title = Text("Diagramas UML", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        uml_diagram = VGroup()

        rectangle_1 = RoundedRectangle(width=2.5, height=0.8, corner_radius=0.1, color=PRIMARY_COLOR, stroke_width=2)
        rectangle_2 = RoundedRectangle(width=2.5, height=1.2, corner_radius=0.1, color=TEXT_COLOR, stroke_width=1)
        rectangle_3 = RoundedRectangle(width=2.5, height=0.6, corner_radius=0.1, color=TEXT_COLOR, stroke_width=1)

        class_box = VGroup(rectangle_1, rectangle_2, rectangle_3).arrange(DOWN, buff=0)
        class_box.shift(LEFT * 2.5)

        class_name = Text("Animal", font_size=20, color=BACKGROUND_COLOR).move_to(rectangle_1)
        attr = Text("-nombre: String", font_size=14, color=CURVE_COLOR).move_to(rectangle_2)
        methods = Text("+eat(): void", font_size=14, color=TEXT_COLOR).move_to(rectangle_3)

        class_box.add(class_name, attr, methods)

        rectangle_4 = RoundedRectangle(width=2.5, height=0.8, corner_radius=0.1, color=SECONDARY_COLOR, stroke_width=2)
        rectangle_5 = RoundedRectangle(width=2.5, height=1.0, corner_radius=0.1, color=TEXT_COLOR, stroke_width=1)
        rectangle_6 = RoundedRectangle(width=2.5, height=0.6, corner_radius=0.1, color=TEXT_COLOR, stroke_width=1)

        child_box = VGroup(rectangle_4, rectangle_5, rectangle_6).arrange(DOWN, buff=0)
        child_box.shift(RIGHT * 2.5)

        child_name = Text("Perro", font_size=20, color=BACKGROUND_COLOR).move_to(rectangle_4)
        child_attr = Text("+raza: String", font_size=14, color=HIGHLIGHT_COLOR).move_to(rectangle_5)
        child_methods = Text("+ladrar(): void", font_size=14, color=TEXT_COLOR).move_to(rectangle_6)

        child_box.add(child_name, child_attr, child_methods)

        arrow = Arrow(
            class_box.get_right() + RIGHT * 0.3,
            child_box.get_left() + LEFT * 0.3,
            color=WARNING_COLOR,
            buff=0.1,
        )
        arrow.add(Text("extends", font_size=16, color=WARNING_COLOR).next_to(arrow, UP, buff=0.1))

        self.play(Write(title), run_time=1)
        self.play(Create(class_box), run_time=1)
        self.play(Create(child_box), run_time=1)
        self.play(Create(arrow), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SingletonPatternScene(Scene):
    def construct(self):
        title = Text("Patron Singleton", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public class Singleton {
    private static Singleton instancia;

    private Singleton() { }  // Constructor privado

    public static Singleton getInstancia() {
        if (instancia == null) {
            instancia = new Singleton();
        }
        return instancia;
    }
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=22,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        explanation = Text("Garantiza una sola instancia de la clase", font_size=24, color=HIGHLIGHT_COLOR)
        explanation.next_to(java_code, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.play(FadeIn(explanation), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FactoryPatternScene(Scene):
    def construct(self):
        title = Text("Patron Factory", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public interface Shape {
    void draw();
}

public class Circle implements Shape {
    public void draw() { System.out.println("Circle"); }
}

public class Square implements Shape {
    public void draw() { System.out.println("Square"); }
}

public class ShapeFactory {
    public Shape getShape(String tipo) {
        if (tipo.equals("circle")) return new Circle();
        if (tipo.equals("square")) return new Square();
        return null;
    }
}'''

        java_code = Code(
            code_string=code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: POO en Java", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Clase: plantilla; Objeto: instancia", font_size=24, color=TEXT_COLOR),
            Text("Encapsulamiento: ocultamiento con getters/setters", font_size=24, color=TEXT_COLOR),
            Text("Herencia: extends para reutilizar codigo", font_size=24, color=TEXT_COLOR),
            Text("Polimorfismo: overload y override", font_size=24, color=TEXT_COLOR),
            Text("Abstraccion: clases e interfaces abstractas", font_size=24, color=TEXT_COLOR),
            Text("Composicion, Agregacion, Asociacion", font_size=24, color=TEXT_COLOR),
            Text("Modificadores: public, protected, private, default", font_size=24, color=TEXT_COLOR),
            Text("Patrones: Singleton, Factory", font_size=24, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Fundamento para desarrollo de software escalable",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class JavaOOPFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        WhatIsOOP.construct(self)
        ClassesAndObjects.construct(self)
        EncapsulationScene.construct(self)
        GettersSettersScene.construct(self)
        InheritanceScene.construct(self)
        ConstructorsScene.construct(self)
        PolymorphismScene.construct(self)
        AbstractionScene.construct(self)
        InterfaceScene.construct(self)
        AccessModifiersScene.construct(self)
        StaticFinalScene.construct(self)
        CompositionScene.construct(self)
        AggregationScene.construct(self)
        AssociationScene.construct(self)
        ThisSuperScene.construct(self)
        OverridingScene.construct(self)
        OverloadingScene.construct(self)
        ObjectClassScene.construct(self)
        ExceptionHandlingScene.construct(self)
        GenericsScene.construct(self)
        CollectionsScene.construct(self)
        UMLScene.construct(self)
        SingletonPatternScene.construct(self)
        FactoryPatternScene.construct(self)
        ConclusionScene.construct(self)
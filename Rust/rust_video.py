from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
RUST_COLOR = "#dea584"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Rust", font_size=60, color=RUST_COLOR).set_color_by_gradient(RUST_COLOR, ACCENT_COLOR)
        subtitle = Text("Lenguaje de sistemas seguro y rapido", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Sintaxis Basica", font_size=48, color=RUST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''fn main() {
    // Variables
    let nombre = "Ana";
    let mut edad = 28;
    edad += 1;

    // Constantes
    const PI: f64 = 3.1416;

    // Tipos
    let entero: i32 = 42;
    let flotante: f64 = 3.14;
    let booleano: bool = true;
    let caracter: char = 'A';

    // Tuplas
    let tupla: (i32, f64, &str) = (1, 3.14, "hola");
    let (x, y, z) = tupla;

    // Arrays
    let arr: [i32; 3] = [1, 2, 3];
    let slice = &arr[0..2];

    // Vectores
    let mut vec = Vec::new();
    vec.push(1);
    vec.push(2);

    // String vs &str
    let texto: &str = "hola"; // string slice
    let string: String = String::from("hola");

    // Control
    if edad >= 18 {
        println!("Mayor");
    }

    for i in 0..5 {
        println!("{}", i);
    }

    // Match
    match edad {
        18 => println!("Justo"),
        19..=64 => println!("Adulto"),
        _ => println!("Otro"),
    }
}'''

        code = Code(code=code_str, language="rust", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class OwnershipScene(Scene):
    def construct(self):
        title = Text("Ownership y Borrowing", font_size=40, color=RUST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Ownership
fn main() {
    let s1 = String::from("hola");
    let s2 = s1; // s1 se mueve a s2
    // println!("{}", s1); // error!

    // Clone
    let s3 = s2.clone();
    println!("{}", s2); // ok
}

// Borrowing (referencias)
fn calcular_longitud(s: &String) -> usize {
    s.len()
}

// Mutable reference
fn agregar_exclamacion(s: &mut String) {
    s.push_str("!");
}

// Slice
fn primera_palabra(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}

// Lifetime
fn mas_largo<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}'''

        code = Code(code=code_str, language="rust", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class StructsEnumsScene(Scene):
    def construct(self):
        title = Text("Structs y Enums", font_size=44, color=RUST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Struct
struct Usuario {
    nombre: String,
    edad: u32,
    activo: bool,
}

impl Usuario {
    fn saludar(&self) -> String {
        format!("Hola, soy {}", self.nombre)
    }

    fn cumpleanios(&mut self) {
        self.edad += 1;
    }

    fn new(nombre: &str, edad: u32) -> Self {
        Self {
            nombre: String::from(nombre),
            edad,
            activo: true,
        }
    }
}

// Tuple struct
struct Color(i32, i32, i32);

// Enum
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}

// Pattern matching
fn procesar(opcion: Option<i32>) {
    match opcion {
        Some(valor) => println!("{}", valor),
        None => println!("Nada"),
    }
}

// if let
if let Some(valor) = opcion {
    println!("{}", valor);
}'''

        code = Code(code=code_str, language="rust", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ErrorHandlingScene(Scene):
    def construct(self):
        title = Text("Manejo de Errores", font_size=44, color=RUST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Result
use std::fs::File;
use std::io::{self, Read};

fn leer_archivo(ruta: &str) -> Result<String, io::Error> {
    let mut archivo = File::open(ruta)?;
    let mut contenido = String::new();
    archivo.read_to_string(&mut contenido)?;
    Ok(contenido)
}

// Custom error
#[derive(Debug)]
enum AppError {
    NotFound(String),
    InvalidInput(String),
    DatabaseError(String),
}

impl std::fmt::Display for AppError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            AppError::NotFound(msg) => write!(f, "No encontrado: {}", msg),
            AppError::InvalidInput(msg) => write!(f, "Invalido: {}", msg),
            AppError::DatabaseError(msg) => write!(f, "DB error: {}", msg),
        }
    }
}

// Try operator
fn procesar() -> Result<(), AppError> {
    let data = leer_archivo("data.txt")
        .map_err(|e| AppError::NotFound(e.to_string()))?;
    Ok(())
}

// Panic
fn dividir(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Division por cero");
    }
    a / b
}

// Option
fn encontrar(id: i32) -> Option<Usuario> {
    users.iter().find(|u| u.id == id).cloned()
}'''

        code = Code(code=code_str, language="rust", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class CollectionsScene(Scene):
    def construct(self):
        title = Text("Colecciones y Traits", font_size=44, color=RUST_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Iterator
fn main() {
    let nums = vec![1, 2, 3, 4, 5];

    let pares: Vec<i32> = nums
        .iter()
        .filter(|x| *x % 2 == 0)
        .map(|x| x * 2)
        .collect();

    let suma: i32 = nums.iter().sum();
    let productos: Vec<String> = nums
        .iter()
        .map(|n| format!("Producto {}", n))
        .collect();
}

// Trait
trait Animal {
    fn sonido(&self) -> String;

    fn dormir(&self) -> String {
        String::from("Zzz")
    }
}

struct Perro;
impl Animal for Perro {
    fn sonido(&self) -> String {
        String::from("Guau")
    }
}

// Generic con trait bound
fn imprimir<T: Display>(item: T) {
    println!("{}", item);
}

fn mayor<T: PartialOrd>(a: T, b: T) -> T {
    if a > b { a } else { b }
}

// impl Trait
fn devolver_animal() -> impl Animal {
    Perro
}'''

        code = Code(code=code_str, language="rust", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Rust", font_size=38, color=RUST_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Sintaxis expresiva y segura", font_size=22, color=TEXT_COLOR),
            Text("Ownership y borrowing sin GC", font_size=22, color=TEXT_COLOR),
            Text("Structs, enums y pattern matching", font_size=22, color=TEXT_COLOR),
            Text("Manejo de errores con Result/Option", font_size=22, color=TEXT_COLOR),
            Text("Traits y generics", font_size=22, color=TEXT_COLOR),
            Text("Iterators y closures", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Rendimiento de C con seguridad de memoria", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class RustFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        OwnershipScene.construct(self)
        StructsEnumsScene.construct(self)
        ErrorHandlingScene.construct(self)
        CollectionsScene.construct(self)
        ConclusionScene.construct(self)
from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
TS_COLOR = "#3178c6"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("TypeScript", font_size=60, color=TS_COLOR).set_color_by_gradient(TS_COLOR, PRIMARY_COLOR)
        subtitle = Text("JavaScript con tipos estaticos", font_size=28, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class TypesScene(Scene):
    def construct(self):
        title = Text("Tipos Basicos", font_size=48, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Tipos primitivos
let nombre: string = "Juan";
let edad: number = 25;
let activo: boolean = true;

// Arrays
let numeros: number[] = [1, 2, 3];
let nombres: Array<string> = ["Ana", "Pedro"];

// Any y Unknown
let cualquier: any = "hola";
let desconocido: unknown = "valor";

// Void y Null
function saludar(): void {
  console.log("Hola");
}
let vacio: void = undefined;

// Never y Enum
function error(): never {
  throw new Error("Error");
}
enum Color { Rojo, Verde, Azul }
let color: Color = Color.Rojo;'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=20)
        code.scale(0.9).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class InterfacesScene(Scene):
    def construct(self):
        title = Text("Interfaces y Types", font_size=44, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Interface
interface Usuario {
  id: number;
  nombre: string;
  email: string;
  edad?: number;  // opcional
}

const usuario: Usuario = {
  id: 1,
  nombre: "Maria",
  email: "maria@email.com"
};

// Type alias
type ID = string | number;
type Estado = "pendiente" | "completado";

type Tarea = {
  id: ID;
  titulo: string;
  estado: Estado;
};

// Extender interfaces
interface Empleado extends Usuario {
  departamento: string;
  salary: number;
}

// Readonly
interface Config {
  readonly apiUrl: string;
  readonly apiKey: string;
}'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class GenericsScene(Scene):
    def construct(self):
        title = Text("Generics", font_size=48, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Funcion generica
function identidad<T>(valor: T): T {
  return valor;
}
const num = identidad<number>(5);
const texto = identidad<string>("Hola");

// Generic constraints
interface ConLength {
  length: number;
}
function logger<T extends ConLength>(item: T): void {
  console.log(item.length);
}

// Generic classes
class Contenedor<T> {
  private contenido: T;
  constructor(valor: T) {
    this.contenido = valor;
  }
  getContenido(): T {
    return this.contenido;
  }
}
const caja = new Contenedor<string>("datos");

// Multiple generics
function pares<T, U>(a: T, b: U): [T, U] {
  return [a, b];
}'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AdvancedTypesScene(Scene):
    def construct(self):
        title = Text("Tipos Avanzados", font_size=44, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Union types
type ID = number | string;
let userId: ID = 1;
userId = "abc123";

// Intersection types
type Empleado = { nombre: string };
type Manager = { departamento: string };
type Director = Empleado & Manager;

// Type guards
function isString(val: any): val is string {
  return typeof val === "string";
}

// Literal types
type Direccion = "norte" | "sur" | "este" | "oeste";
let dir: Direccion = "norte";

// Mapped types
type SoloLectura<T> = {
  readonly [K in keyof T]: T[K];
};
type Nullable<T> = {
  [K in keyof T]: T[K] | null;
};

// Utility types
type Parcial = Partial<Usuario>;
type Completo = Required<Usuario>;
type Pick = Pick<Usuario, "id" | "nombre">;'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class DecoratorsScene(Scene):
    def construct(self):
        title = Text("Decorators", font_size=48, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Decorator de clase
function logged(constructor: Function) {
  console.log("Clase creada:", constructor.name);
}

@logged
class Usuario {
  constructor(public nombre: string) {}
}

// Decorator de metodo
function readonly(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
) {
  descriptor.writable = false;
}

class Servicio {
  @readonly
  metodoImportante() { return "datos"; }
}

// Decorator de propiedad
function defaultValue(value: any) {
  return function(target: any, key: string) {
    target[key] = value;
  };
}

class Config {
  @defaultValue("localhost")
  apiUrl: string;
}

// Factory decorators
function color(color: string) {
  return function(target: any) {
    target.color = color;
  };
}'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ModulesScene(Scene):
    def construct(self):
        title = Text("Modulos y Namespaces", font_size=44, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Export/Import
export classUsuario {
  constructor(public nombre: string) {}
}
export function saludar(nombre: string): string {
  return `Hola ${nombre}`;
}
export default class DefaultUser {}

// Import
import { Usuario, saludar } from "./usuario";
import DefaultUser from "./default";
import * as utils from "./utils";

// Re-export
export { Usuario } from "./usuario";
export * from "./helpers";

// Namespace
namespace Geometria {
  export function areaRect(width: number, height: number): number {
    return width * height;
  }
  export function perimetroRect(w: number, h: number): number {
    return 2 * (w + h);
  }
}
console.log(Geometria.areaRect(5, 3));'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AsyncScene(Scene):
    def construct(self):
        title = Text("Async/Await y Promesas", font_size=42, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Promesas
function fetchUsuario(id: number): Promise<Usuario> {
  return new Promise((resolve, reject) => {
    // Simular API call
    if (id > 0) {
      resolve({ id, nombre: "Usuario" + id });
    } else {
      reject(new Error("ID invalido"));
    }
  });
}

// Async/Await
async function getUserData(id: number): Promise<Usuario> {
  try {
    const user = await fetchUsuario(id);
    return user;
  } catch (error) {
    console.error("Error:", error);
    throw error;
  }
}

// Multiple async
async function getDatos(): Promise<[Usuario, Post[]]> {
  const usuario = await fetchUsuario(1);
  const posts = await fetchPosts(1);
  return [usuario, posts];
}

// Promise.all
async function paralelo() {
  const resultados = await Promise.all([
    fetchUsuario(1),
    fetchUsuario(2),
    fetchUsuario(3)
  ]);
  return resultados;
}'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class TypeGuardsScene(Scene):
    def construct(self):
        title = Text("Type Guards", font_size=48, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// typeof guard
function process(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  }
  return value.toFixed(2);
}

// instanceof guard
class Perro {
  ladrar() { console.log("Guau"); }
}
class Gato {
  maullar() { console.log("Miau"); }
}

function ruido(animal: Perro | Gato) {
  if (animal instanceof Perro) {
    animal.ladrar();
  } else {
    animal.maullar();
  }
}

// Custom type guard
interface Pez {
  nadar(): void;
}
interface Pajaro {
  volar(): void;
}

function esPez(animal: any): animal is Pez {
  return "nadar" in animal;
}

function mover(animal: Pez | Pajaro) {
  if (esPez(animal)) {
    animal.nadar();
  } else {
    animal.volar();
  }
}'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ErrorHandlingScene(Scene):
    def construct(self):
        title = Text("Manejo de Errores", font_size=44, color=TS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Custom error class
class ApiError extends Error {
  constructor(
    public statusCode: number,
    message: string
  ) {
    super(message);
    this.name = "ApiError";
  }
}

// Try-catch con tipos
async function fetchData(): Promise<string> {
  try {
    const response = await api.get("/data");
    return response.data;
  } catch (error) {
    if (error instanceof ApiError) {
      console.error("API Error:", error.statusCode);
    } else {
      console.error("Unknown Error:", error);
    }
    throw error;
  }
}

// Result type pattern
type Result<T> = { success: true; data: T } | { success: false; error: string };

function safeDivide(a: number, b: number): Result<number> {
  if (b === 0) {
    return { success: false, error: "Division por cero" };
  }
  return { success: true, data: a / b };
}

// Never throw
function assert(val: never): never {
  throw new Error("Unexpected value: " + val);
}'''

        code = Code(code=code_str, language="typescript", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: TypeScript", font_size=38, color=TS_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Tipos basicos: string, number, boolean, array", font_size=22, color=TEXT_COLOR),
            Text("Interfaces y Type aliases", font_size=22, color=TEXT_COLOR),
            Text("Generics: funciones y clases tipadas", font_size=22, color=TEXT_COLOR),
            Text("Tipos avanzados: union, intersection, utility types", font_size=22, color=TEXT_COLOR),
            Text("Decorators: clase, metodo, propiedad", font_size=22, color=TEXT_COLOR),
            Text("Modulos y exports", font_size=22, color=TEXT_COLOR),
            Text("Async/Await y Promesas", font_size=22, color=TEXT_COLOR),
            Text("Type Guards personalizados", font_size=22, color=TEXT_COLOR),
            Text("Manejo de errores tipado", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("JavaScript con superpoderes de tipos", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class TypeScriptFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        TypesScene.construct(self)
        InterfacesScene.construct(self)
        GenericsScene.construct(self)
        AdvancedTypesScene.construct(self)
        DecoratorsScene.construct(self)
        ModulesScene.construct(self)
        AsyncScene.construct(self)
        TypeGuardsScene.construct(self)
        ErrorHandlingScene.construct(self)
        ConclusionScene.construct(self)
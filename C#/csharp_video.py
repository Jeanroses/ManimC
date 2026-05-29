from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
CSHARP_COLOR = "#68217a"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("C#", font_size=60, color=CSHARP_COLOR).set_color_by_gradient(CSHARP_COLOR, ACCENT_COLOR)
        subtitle = Text("Lenguaje moderno del ecosistema .NET", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Sintaxis Basica", font_size=48, color=CSHARP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''using System;

class Program
{
    static void Main()
    {
        // Variables
        string nombre = "Ana";
        int edad = 28;
        bool activo = true;
        decimal precio = 19.99m;

        // Constantes
        const double PI = 3.1416;

        // Inferencia
        var ciudad = "Lima";
        var numeros = new int[] { 1, 2, 3, 4, 5 };

        // String interpolation
        Console.WriteLine($"Hola {nombre}, tienes {edad} anos");

        // Nullable
        int? nullable = null;

        // Control
        if (edad >= 18)
        {
            Console.WriteLine("Mayor");
        }

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine(i);
        }

        // Switch expression
        var categoria = edad switch
        {
            < 18 => "Menor",
            >= 18 and < 65 => "Adulto",
            _ => "Adulto mayor"
        };

        // LINQ
        var pares = numeros.Where(n => n % 2 == 0).ToList();

        // Null-conditional
        string? texto = null;
        var longitud = texto?.Length ?? 0;
    }
}'''

        code = Code(code=code_str, language="csharp", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class OOPScene(Scene):
    def construct(self):
        title = Text("POO en C#", font_size=48, color=CSHARP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Clase
public class Persona
{
    // Propiedades
    public string Nombre { get; set; }
    public int Edad { get; private set; }
    public readonly string Email;

    // Constructor
    public Persona(string nombre, int edad, string email)
    {
        Nombre = nombre;
        Edad = edad;
        Email = email;
    }

    // Metodo
    public virtual string Saludar()
    {
        return $"Hola, soy {Nombre}";
    }
}

// Herencia
public class Empleado : Persona
{
    public decimal Salario { get; set; }

    public Empleado(string nombre, int edad, string email, decimal salario)
        : base(nombre, edad, email)
    {
        Salario = salario;
    }

    public override string Saludar()
    {
        return $"{base.Saludar()}, gano {Salario:C}";
    }
}

// Interfaz
public interface IAnimal
{
    string Sonido();
}

public class Perro : IAnimal
{
    public string Sonido() => "Guau";
}

// Abstract
public abstract class Figura
{
    public abstract double Area();
}

public class Circulo : Figura
{
    public double Radio { get; set; }
    public override double Area() => Math.PI * Radio * Radio;
}'''

        code = Code(code=code_str, language="csharp", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AsyncScene(Scene):
    def construct(self):
        title = Text("Async/Await", font_size=48, color=CSHARP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''using System.Net.Http;
using System.Threading.Tasks;

public class ApiService
{
    private readonly HttpClient _http;

    public ApiService()
    {
        _http = new HttpClient();
    }

    // Async method
    public async Task<string> GetDataAsync(string url)
    {
        var response = await _http.GetStringAsync(url);
        return response;
    }

    // Multiple tasks
    public async Task<string[]> GetAllDataAsync()
    {
        var t1 = GetDataAsync("https://api.com/data1");
        var t2 = GetDataAsync("https://api.com/data2");
        var t3 = GetDataAsync("https://api.com/data3");

        return await Task.WhenAll(t1, t2, t3);
    }

    // Parallel.ForEachAsync
    public async Task ProcessItemsAsync(List<int> items)
    {
        await Parallel.ForEachAsync(items, async (item, ct) =>
        {
            await ProcessItemAsync(item);
        });
    }

    // CancellationToken
    public async Task<string> GetWithCancelAsync(
        string url, CancellationToken ct)
    {
        var response = await _http.GetStringAsync(url, ct);
        return response;
    }
}

// async void (solo eventos)
private async void OnButtonClick(object sender, EventArgs e)
{
    await LoadDataAsync();
}'''

        code = Code(code=code_str, language="csharp", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class CollectionsScene(Scene):
    def construct(self):
        title = Text("LINQ y Colecciones", font_size=44, color=CSHARP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''using System.Collections.Generic;
using System.Linq;

class Demo
{
    static void Main()
    {
        var numeros = new List<int> { 1, 2, 3, 4, 5, 6 };

        // LINQ method syntax
        var pares = numeros.Where(n => n % 2 == 0);
        var cuadrados = numeros.Select(n => n * n);
        var ordenados = numeros.OrderByDescending(n => n);

        // LINQ query syntax
        var query = from n in numeros
                    where n > 3
                    select n * 2;

        // Agregacion
        var suma = numeros.Sum();
        var promedio = numeros.Average();
        var maximo = numeros.Max();
        var agrupados = numeros.GroupBy(n => n % 2 == 0);

        // Dictionary
        var dic = new Dictionary<string, int>
        {
            {"a", 1},
            {"b", 2}
        };

        // HashSet
        var set = new HashSet<int> { 1, 2, 2, 3 };

        // Stack / Queue
        var pila = new Stack<int>();
        pila.Push(1);
        var cola = new Queue<int>();
        cola.Enqueue(1);

        // Tuplas modernas
        var tupla = (Id: 1, Nombre: "Ana");
        Console.WriteLine(tupla.Nombre);
    }
}'''

        code = Code(code=code_str, language="csharp", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class FeaturesScene(Scene):
    def construct(self):
        title = Text("Caracteristicas Modernas", font_size=40, color=CSHARP_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Records (inmutable por defecto)
public record Persona(string Nombre, int Edad);

// Init-only properties
public class Config
{
    public string ApiUrl { get; init; }
    public int Timeout { get; init; }
}

// Pattern matching avanzado
string Clasificar(int edad) => edad switch
{
    0 => "Bebe",
    >= 1 and < 13 => "Nino",
    >= 13 and < 20 => "Adolescente",
    >= 20 and < 65 => "Adulto",
    _ => "Adulto mayor"
};

// Nullable reference types
#nullable enable
public string? GetEmail(int id) { ... }
#nullable disable

// Top-level statements (Program.cs)
Console.WriteLine("Hola Mundo");

// using global
global using System.Console;

// Primary constructors
public class Cliente(string nombre, string email)
{
    public string Nombre { get; } = nombre;
    public string Email { get; } = email;
}'''

        code = Code(code=code_str, language="csharp", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: C#", font_size=38, color=CSHARP_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Sintaxis moderna y tipado fuerte", font_size=22, color=TEXT_COLOR),
            Text("POO: clases, interfaces, herencia", font_size=22, color=TEXT_COLOR),
            Text("Async/await y paralelismo", font_size=22, color=TEXT_COLOR),
            Text("LINQ para consultas de datos", font_size=22, color=TEXT_COLOR),
            Text("Records, pattern matching, nullables", font_size=22, color=TEXT_COLOR),
            Text("Ecosistema .NET completo", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Lenguaje versatil para web, desktop, mobile y cloud", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class CSharpFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        OOPScene.construct(self)
        AsyncScene.construct(self)
        CollectionsScene.construct(self)
        FeaturesScene.construct(self)
        ConclusionScene.construct(self)
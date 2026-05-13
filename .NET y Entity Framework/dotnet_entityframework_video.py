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
DOTNET_COLOR = "#68217a"
EF_COLOR = "#00618a"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            ".NET y Entity Framework",
            font_size=52,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "Ecosistema de desarrollo y acceso a datos",
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


class DotNetHistoryScene(Scene):
    def construct(self):
        title = Text("Historia de .NET", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        timeline = VGroup(
            Text("2002: .NET Framework 1.0", font_size=22, color=HIGHLIGHT_COLOR),
            Text("2008: LINQ, Entity Framework 1.0", font_size=22, color=TEXT_COLOR),
            Text("2010: .NET 4.0, Parallel Extensions", font_size=22, color=TEXT_COLOR),
            Text("2016: .NET Core 1.0 (cross-platform)", font_size=22, color=SECONDARY_COLOR),
            Text("2019: .NET 5 (unificacion)", font_size=22, color=ACCENT_COLOR),
            Text("2021: .NET 6 LTS", font_size=22, color=ACCENT_COLOR),
            Text("2023: .NET 8 (actual)", font_size=22, color=SUCCESS_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        timeline.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        for t in timeline:
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DotNetArchitectureScene(Scene):
    def construct(self):
        title = Text("Arquitectura de .NET", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        layers = VGroup()

        app_layer = RoundedRectangle(
            width=8, height=1.2, corner_radius=0.15,
            color=HIGHLIGHT_COLOR, stroke_width=2, fill_opacity=0.3
        )
        app_label = Text("Aplicaciones (Web, Desktop, Mobile, Games)", font_size=22, color=HIGHLIGHT_COLOR)
        app_label.move_to(app_layer.get_center())

        lang_layer = RoundedRectangle(
            width=8, height=1.0, corner_radius=0.15,
            color=CURVE_COLOR, stroke_width=2, fill_opacity=0.3
        ).next_to(app_layer, DOWN, buff=0.1)
        lang_label = Text("Lenguajes: C#, F#, VB.NET", font_size=22, color=CURVE_COLOR)
        lang_label.move_to(lang_layer.get_center())

        runtime_layer = RoundedRectangle(
            width=8, height=1.2, corner_radius=0.15,
            color=ACCENT_COLOR, stroke_width=2, fill_opacity=0.3
        ).next_to(lang_layer, DOWN, buff=0.1)
        runtime_label = Text("Runtime: CLR, JIT, Garbage Collector", font_size=20, color=ACCENT_COLOR)
        runtime_label.move_to(runtime_layer.get_center())

        base_layer = RoundedRectangle(
            width=8, height=1.0, corner_radius=0.15,
            color=SECONDARY_COLOR, stroke_width=2, fill_opacity=0.3
        ).next_to(runtime_layer, DOWN, buff=0.1)
        base_label = Text("BCL: Collections, IO, Networking, Security", font_size=20, color=SECONDARY_COLOR)
        base_label.move_to(base_layer.get_center())

        layers.add(app_layer, app_label, lang_layer, lang_label, runtime_layer, runtime_label, base_layer, base_label)
        layers.shift(DOWN * 0.3)

        self.play(Write(title), run_time=1)
        for l in layers:
            self.play(FadeIn(l), run_time=0.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DotNetPlatformsScene(Scene):
    def construct(self):
        title = Text("Plataformas .NET", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        platforms = VGroup(
            VGroup(
                Text("ASP.NET Core", font_size=26, color=SUCCESS_COLOR),
                Text("Web APIs, MVC, Blazor, SignalR", font_size=20, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),

            VGroup(
                Text("WPF / Windows Forms", font_size=26, color=CURVE_COLOR),
                Text("Aplicaciones de escritorio Windows", font_size=20, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),

            VGroup(
                Text("Xamarin / .NET MAUI", font_size=26, color=SECONDARY_COLOR),
                Text("Aplicaciones moviles (iOS, Android)", font_size=20, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),

            VGroup(
                Text("Unity / Godot", font_size=26, color=HIGHLIGHT_COLOR),
                Text("Desarrollo de videojuegos", font_size=20, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),

            VGroup(
                Text("ML.NET", font_size=26, color=ACCENT_COLOR),
                Text("Machine Learning", font_size=20, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.35)
        platforms.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for p in platforms:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CSharpFeaturesScene(Scene):
    def construct(self):
        title = Text("C# Caracteristicas Principales", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        features = VGroup(
            Text("Tipos de datos: int, double, string, bool, decimal, var", font_size=20, color=TEXT_COLOR),
            Text("POO: class, interface, struct, record, enum", font_size=20, color=TEXT_COLOR),
            Text("Modificadores: public, private, protected, internal, sealed", font_size=20, color=TEXT_COLOR),
            Text("Genericos: List<T>, Dictionary<K,V>, Task<T>", font_size=20, color=TEXT_COLOR),
            Text("LINQ: consultas integradas al lenguaje", font_size=20, color=HIGHLIGHT_COLOR),
            Text("Async/Await: programacion asincrona", font_size=20, color=ACCENT_COLOR),
            Text("Pattern Matching: switch expressions", font_size=20, color=SECONDARY_COLOR),
            Text("Records: tipos inmutables", font_size=20, color=CURVE_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        features.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for f in features:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LINQScene(Scene):
    def construct(self):
        title = Text("LINQ: Language Integrated Query", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Coleccion de ejemplo
var productos = new List<Producto> {
    new Producto { Nombre = "Laptop", Precio = 999, Categoria = "Electronica" },
    new Producto { Nombre = "Telefono", Precio = 599, Categoria = "Electronica" },
    new Producto { Nombre = "Silla", Precio = 150, Categoria = "Muebles" }
};

// Consulta LINQ
var electronica = from p in productos
                  where p.Categoria == "Electronica"
                  orderby p.Precio descending
                  select p;

// Sintaxis de metodo
var pricey = productos
    .Where(p => p.Precio > 500)
    .OrderBy(p => p.Nombre)
    .Select(p => p.Nombre);'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AsyncAwaitScene(Scene):
    def construct(self):
        title = Text("Async/Await en C#", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public async Task<string> ObtenerDatosAsync()
{
    // Simular llamada a API
    var cliente = new HttpClient();
    string resultado = await cliente
        .GetStringAsync("https://api.ejemplo.com/datos");
    return resultado;
}

// Uso
var datos = await ObtenerDatosAsync();
Console.WriteLine(datos);

// Multiples tareas en paralelo
var tarea1 = ObtenerDatosAsync();
var tarea2 = ObtenerOtroDatoAsync();
var resultados = await Task.WhenAll(tarea1, tarea2);'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EntityFrameworkIntroScene(Scene):
    def construct(self):
        title = Text("Que es Entity Framework?", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "ORM (Object-Relational Mapping) de Microsoft para acceso a datos",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        orm_diagram = VGroup()

        app_box = RoundedRectangle(
            width=2.5, height=1.5, corner_radius=0.1,
            color=CURVE_COLOR, stroke_width=2, fill_opacity=0.2
        )
        app_label = Text("C# Objects", font_size=18, color=TEXT_COLOR).move_to(app_box.get_center())

        db_box = RoundedRectangle(
            width=2.5, height=1.5, corner_radius=0.1,
            color=ACCENT_COLOR, stroke_width=2, fill_opacity=0.2
        )
        db_label = Text("SQL Tables", font_size=18, color=TEXT_COLOR).move_to(db_box.get_center())

        orm_box = RoundedRectangle(
            width=2.0, height=1.0, corner_radius=0.1,
            color=HIGHLIGHT_COLOR, stroke_width=2, fill_opacity=0.3
        )
        orm_label = Text("EF Core", font_size=18, color=HIGHLIGHT_COLOR).move_to(orm_box.get_center())

        app_box.to_edge(LEFT, buff=1.5).shift(DOWN * 0.3)
        db_box.to_edge(RIGHT, buff=1.5).shift(DOWN * 0.3)
        orm_box.move_to(ORIGIN)

        arrow1 = Arrow(app_box.get_right(), orm_box.get_left(), color=SUCCESS_COLOR, buff=0.1)
        arrow2 = Arrow(orm_box.get_right(), db_box.get_left(), color=SUCCESS_COLOR, buff=0.1)

        orm_diagram.add(app_box, app_label, db_box, db_label, orm_box, orm_label, arrow1, arrow2)

        benefits = VGroup(
            Text("Beneficios:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("- Consulta con LINQ", font_size=18, color=TEXT_COLOR),
            Text("- Cambio de base de datos sin codigo", font_size=18, color=TEXT_COLOR),
            Text("- Migration automatico", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15)
        benefits.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(orm_diagram), run_time=1.5)
        self.play(FadeIn(benefits), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFModelsScene(Scene):
    def construct(self):
        title = Text("Modelos en Entity Framework", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        entity_code = '''public class Estudiante
{
    public int Id { get; set; }           // Clave primaria
    public string Nombre { get; set; }
    public string Email { get; set; }
    public DateTime FechaNacimiento { get; set; }

    // Relaciones
    public int? CarreraId { get; set; }
    public virtual Carrera Carrera { get; set; }

    public virtual ICollection<Matricula> Matriculas { get; set; }
}

public class Matricula
{
    public int Id { get; set; }
    public int EstudianteId { get; set; }
    public int CursoId { get; set; }
    public DateTime Fecha { get; set; }

    public virtual Estudiante Estudiante { get; set; }
    public virtual Curso Curso { get; set; }
}'''

        java_code = Code(
            code_string=entity_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DbContextScene(Scene):
    def construct(self):
        title = Text("DbContext: Punto de entrada", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''public class UniversidadContext : DbContext
{
    public DbSet<Estudiante> Estudiantes { get; set; }
    public DbSet<Carrera> Carreras { get; set; }
    public DbSet<Curso> Cursos { get; set; }
    public DbSet<Matricula> Matriculas { get; set; }

    protected override void OnConfiguring(
        DbContextOptionsBuilder options)
    {
        options.UseSqlServer(
            "Server=localhost;Database=Universidad;Trusted_Connection=True");
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Configuracion Fluent API
        modelBuilder.Entity<Estudiante>()
            .HasIndex(e => e.Email)
            .IsUnique();

        modelBuilder.Entity<Matricula>()
            .HasOne(m => m.Estudiante)
            .WithMany(e => e.Matriculas)
            .HasForeignKey(m => m.EstudianteId);
    }
}'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFCRUDScene(Scene):
    def construct(self):
        title = Text("CRUD con Entity Framework", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        create_code = '''// CREATE - Insertar
using var context = new UniversidadContext();

var nuevoEstudiante = new Estudiante
{
    Nombre = "Juan Perez",
    Email = "juan@universidad.edu",
    FechaNacimiento = new DateTime(2000, 5, 15),
    CarreraId = 1
};

context.Estudiantes.Add(nuevoEstudiante);
await context.SaveChangesAsync();'''

        read_code = '''// READ - Consultar
var estudiante = await context.Estudiantes
    .Where(e => e.Id == 1)
    .FirstOrDefaultAsync();

var todos = await context.Estudiantes
    .Where(e => e.CarreraId == 1)
    .OrderBy(e => e.Nombre)
    .ToListAsync();

// Include para relaciones
var conCarrera = await context.Estudiantes
    .Include(e => e.Carrera)
    .FirstOrDefaultAsync();'''

        update_code = '''// UPDATE - Actualizar
var estudiante = await context.Estudiantes.FindAsync(1);
estudiante.Email = "nuevo@email.com";
await context.SaveChangesAsync();'''

        delete_code = '''// DELETE - Eliminar
var estudiante = await context.Estudiantes.FindAsync(1);
context.Estudiantes.Remove(estudiante);
await context.SaveChangesAsync();'''

        create_java = Code(
            code_string=create_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        create_java.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.5)

        read_java = Code(
            code_string=read_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        read_java.scale(0.75).to_edge(RIGHT, buff=0.3).shift(UP * 0.5)

        update_java = Code(
            code_string=update_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        update_java.scale(0.75).to_edge(LEFT, buff=0.3).shift(DOWN * 1.5)

        delete_java = Code(
            code_string=delete_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        delete_java.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 1.5)

        self.play(Write(title), run_time=1)
        self.play(Create(create_java), run_time=1)
        self.play(Create(read_java), run_time=1)
        self.play(Create(update_java), run_time=1)
        self.play(Create(delete_java), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFLazyEagerScene(Scene):
    def construct(self):
        title = Text("Carga de Relaciones: Eager vs Lazy", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        eager = VGroup(
            Text("Eager Loading (Include)", font_size=24, color=ACCENT_COLOR),
            Code(
                code_string='''var estudiantes = context.Estudiantes
    .Include(e => e.Carrera)
    .Include(e => e.Matriculas)
        .ThenInclude(m => m.Curso)
    .ToList();''',
                language="csharp",
                formatter_style="monokai",
                background="rectangle",
                font_size=18,
            ).scale(0.8),
        ).arrange(DOWN, buff=0.15)

        lazy = VGroup(
            Text("Lazy Loading (automatico con virtual)", font_size=24, color=HIGHLIGHT_COLOR),
            Code(
                code_string='''// Requires: Microsoft.EntityFrameworkCore.Proxies
// y UseLazyLoadingProxies()

var estudiante = context.Estudiantes.First();
// Se carga automaticamente al acceder
var carrera = estudiante.Carrera.Nombre;''',
                language="csharp",
                formatter_style="monokai",
                background="rectangle",
                font_size=18,
            ).scale(0.8),
        ).arrange(DOWN, buff=0.15)

        eager.to_edge(LEFT, buff=0.5).shift(UP * 0.3)
        lazy.to_edge(RIGHT, buff=0.5).shift(UP * 0.3)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(eager), run_time=1)
        self.play(FadeIn(lazy), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFMigrationsScene(Scene):
    def construct(self):
        title = Text("Migrations en EF Core", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        commands = VGroup(
            Text("Comandos de Migration:", font_size=24, color=HIGHLIGHT_COLOR),
            Text("1. dotnet ef migrations add InitialCreate", font_size=20, color=TEXT_COLOR),
            Text("2. dotnet ef migrations add AddPhoneToStudent", font_size=20, color=TEXT_COLOR),
            Text("3. dotnet ef database update", font_size=20, color=ACCENT_COLOR),
            Text("4. dotnet ef migrations list", font_size=20, color=TEXT_COLOR),
            Text("5. dotnet ef migrations remove", font_size=20, color=WARNING_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        commands.next_to(title, DOWN, buff=0.6)

        explanation = Text(
            "Las migrations mantienen el schema sincronizado con el codigo",
            font_size=22,
            color=SECONDARY_COLOR,
        )
        explanation.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(commands, shift=RIGHT * 0.2), run_time=1)
        self.play(FadeIn(explanation), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFRelationshipsScene(Scene):
    def construct(self):
        title = Text("Tipos de Relaciones en EF", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        one_to_one = VGroup(
            Text("One-to-One", font_size=22, color=CURVE_COLOR),
            Code(
                code_string='''modelBuilder.Entity<Usuario>()
    .HasOne(u => u.Perfil)
    .WithOne(p => p.Usuario)
    .HasForeignKey<Perfil>(p => p.UsuarioId);''',
                language="csharp",
                formatter_style="monokai",
                background="rectangle",
                font_size=16,
            ).scale(0.9),
        ).arrange(DOWN, buff=0.1)

        one_to_many = VGroup(
            Text("One-to-Many", font_size=22, color=ACCENT_COLOR),
            Code(
                code_string='''modelBuilder.Entity<Curso>()
    .HasMany(c => c.Estudiantes)
    .WithOne(e => e.Curso)
    .HasForeignKey(e => e.CursoId);''',
                language="csharp",
                formatter_style="monokai",
                background="rectangle",
                font_size=16,
            ).scale(0.9),
        ).arrange(DOWN, buff=0.1)

        many_to_many = VGroup(
            Text("Many-to-Many", font_size=22, color=SECONDARY_COLOR),
            Code(
                code_string='''// En EF Core 5+ automatico
modelBuilder.Entity<Estudiante>()
    .HasMany(e => e.Cursos)
    .WithMany(c => c.Estudiantes)
    .UsingEntity(j => j.ToTable("Matricula"));''',
                language="csharp",
                formatter_style="monokai",
                background="rectangle",
                font_size=16,
            ).scale(0.9),
        ).arrange(DOWN, buff=0.1)

        one_to_one.to_edge(LEFT, buff=0.5).shift(UP * 0.8)
        one_to_many.to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)
        many_to_many.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(one_to_one), run_time=0.8)
        self.play(FadeIn(one_to_many), run_time=0.8)
        self.play(FadeIn(many_to_many), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFFluentAPIScene(Scene):
    def construct(self):
        title = Text("Fluent API Configuration", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''protected override void OnModelCreating(ModelBuilder mb)
{
    // Entidad
    mb.Entity<Producto>(entity =>
    {
        // Tabla
        entity.ToTable("Productos", "Inventario");

        // Clave primaria
        entity.HasKey(p => p.ProductoId);

        // Propiedades
        entity.Property(p => p.Nombre)
            .IsRequired()
            .HasMaxLength(100);

        entity.Property(p => p.Precio)
            .HasColumnType("decimal(18,2)");

        // Indice
        entity.HasIndex(p => p.CodigoBarras)
            .IsUnique();

        // Ignorar propiedad
        entity.Ignore(p => p.CodigoCalculado);
    });
}'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFQueryingScene(Scene):
    def construct(self):
        title = Text("Consultas Avanzadas en EF", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        projection = '''// Projection - Seleccionar campos especificos
var nombres = await context.Estudiantes
    .Where(e => e.CarreraId == 1)
    .Select(e => new { e.Nombre, e.Email })
    .ToListAsync();'''

        grouping = '''// GroupBy - Agrupacion
var porCarrera = await context.Estudiantes
    .GroupBy(e => e.Carrera.Nombre)
    .Select(g => new {
        Carrera = g.Key,
        Cantidad = g.Count()
    })
    .ToListAsync();'''

        join = '''// Join - Union de tablas
var conInfo = await context.Matriculas
    .Join(context.Estudiantes,
        m => m.EstudianteId,
        e => e.Id,
        (m, e) => new { m.Fecha, e.Nombre, e.Email })
    .ToListAsync();'''

        proj_code = Code(
            code_string=projection,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        proj_code.scale(0.8).to_edge(LEFT, buff=0.3).shift(UP * 0.8)

        group_code = Code(
            code_string=grouping,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        group_code.scale(0.8).to_edge(RIGHT, buff=0.3).shift(UP * 0.8)

        join_code = Code(
            code_string=join,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        join_code.scale(0.75).to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(proj_code), run_time=1)
        self.play(Create(group_code), run_time=1)
        self.play(Create(join_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFTrackingScene(Scene):
    def construct(self):
        title = Text("Change Tracking en EF", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        tracking_code = '''// AsNoTracking - Optimizacion de lectura
var estudiantes = await context.Estudiantes
    .AsNoTracking()
    .Where(e => e.Activo)
    .ToListAsync();

// Para actualizar, usar el tracked entity
var est = await context.Estudiantes.FindAsync(1);
est.Nombre = "Nuevo Nombre";
// No necesita explicit SaveChanges, EF detecta el cambio

// Entry - Acceso al estado
var entry = context.Entry(estudiante);
Console.WriteLine(entry.State);  // Modified
Console.WriteLine(entry.OriginalValues["Nombre"]);  // Valor original''''''

        java_code = Code(
            code_string=tracking_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFSplitQueriesScene(Scene):
    def construct(self):
        title = Text("Split Queries en EF Core", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        explanation = Text(
            "Carga datos en multiples consultas en lugar de un JOIN grande",
            font_size=24,
            color=TEXT_COLOR,
        )
        explanation.next_to(title, DOWN, buff=0.5)

        code = '''// Evitar problema N+1 y Cartesian Explosion
var estudiantes = context.Estudiantes
    .Include(e => e.Matriculas)
        .ThenInclude(m => m.Curso)
    .AsSplitQuery()  // Divide en multiples queries
    .ToList();

// O configurarlo globalmente en DbContext
optionsBuilder.UseSqlServer(
    "...",
    o => o.UseQuerySplittingBehavior(QuerySplittingBehavior.SplitQuery));'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(explanation, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(explanation), run_time=0.8)
        self.play(Create(java_code), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFGlobalQueryFiltersScene(Scene):
    def construct(self):
        title = Text("Global Query Filters", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Aplicar filtros automaticamente a todas las consultas
protected override void OnModelCreating(ModelBuilder mb)
{
    mb.Entity<Estudiante>()
        .HasQueryFilter(e => !e.Eliminado);  // Soft delete automatico
}

// Uso normal - filtro aplicado automaticamente
var activos = context.Estudiantes.ToList();  // Solo no eliminados

// Ignorar filtro para audit/Admin
var todos = context.Estudiantes
    .IgnoreQueryFilters()
    .ToList();'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFShadowPropertiesScene(Scene):
    def construct(self):
        title = Text("Shadow Properties", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Propiedades no definidas en la entidad, pero existentes en la DB",
            font_size=22,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        code = '''// Definir propiedades shadow
protected override void OnModelCreating(ModelBuilder mb)
{
    mb.Entity<Estudiante>()
        .Property<DateTime>("FechaCreacion")
        .HasDefaultValueSql("GETDATE()");

    mb.Entity<Estudiante>()
        .Property<string>("UsuarioCreacion")
        .HasMaxLength(50);
}

// Acceder desde DbContext
var fecha = context.Entry(estudiante)
    .Property<DateTime>("FechaCreacion").CurrentValue;'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.85).next_to(definition, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(java_code), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFStoredProceduresScene(Scene):
    def construct(self):
        title = Text("Stored Procedures y Raw SQL", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Ejecutar Stored Procedure
var resultados = context.Set<Resultado>()
    .FromSqlRaw("EXEC sp_ObtenerEstadisticas @Anio={0}", anio)
    .ToList();

// SQL plano con parametros
var estudiante = context.Estudiantes
    .FromSqlRaw("SELECT * FROM Estudiantes WHERE Id = {0}", id)
    .FirstOrDefault();

// Ejecute Non-Query (INSERT/UPDATE/DELETE)
await context.Database
    .ExecuteSqlRawAsync("DELETE FROM Matriculas WHERE EstudianteId = {0}", id);

// interpolation (protegido contra SQL Injection)
var nombre = "Juan";
await context.Database.ExecuteSqlInterpolatedAsync(
    $"DELETE FROM Estudiantes WHERE Nombre = {nombre}");'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EFDatabaseProvidersScene(Scene):
    def construct(self):
        title = Text("Proveedores de Base de Datos", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        providers = VGroup(
            Text("SQL Server", font_size=22, color=SUCCESS_COLOR),
            Text("Install-Package Microsoft.EntityFrameworkCore.SqlServer", font_size=18, color=TEXT_COLOR),
            Text("UseSqlServer(connectionString)", font_size=18, color=HIGHLIGHT_COLOR),

            Text("PostgreSQL", font_size=22, color=ACCENT_COLOR),
            Text("Install-Package Npgsql.EntityFrameworkCore.PostgreSQL", font_size=18, color=TEXT_COLOR),
            Text("UseNpgsql(connectionString)", font_size=18, color=HIGHLIGHT_COLOR),

            Text("MySQL", font_size=22, color=SECONDARY_COLOR),
            Text("Install-Package Pomelo.EntityFrameworkCore.MySql", font_size=18, color=TEXT_COLOR),
            Text("UseMySql(connectionString)", font_size=18, color=HIGHLIGHT_COLOR),

            Text("SQLite", font_size=22, color=CURVE_COLOR),
            Text("Install-Package Microsoft.EntityFrameworkCore.Sqlite", font_size=18, color=TEXT_COLOR),
            Text("UseSqlite(connectionString)", font_size=18, color=HIGHLIGHT_COLOR),

            Text("In-Memory (Testing)", font_size=22, color=HIGHLIGHT_COLOR),
            Text("Install-Package Microsoft.EntityFrameworkCore.InMemory", font_size=18, color=TEXT_COLOR),
            Text("UseInMemoryDatabase(databaseName)", font_size=18, color=HIGHLIGHT_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        providers.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for p in providers:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.3)
            self.wait(0.1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ASPNETCoreIntroScene(Scene):
    def construct(self):
        title = Text("ASP.NET Core", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Framework para crear Web APIs y aplicaciones web modernas",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        features = VGroup(
            Text("Cross-platform: Windows, Linux, macOS", font_size=20, color=ACCENT_COLOR),
            Text("High-performance: fastest web framework", font_size=20, color=ACCENT_COLOR),
            Text("Modular: Middleware pipeline", font_size=20, color=SECONDARY_COLOR),
            Text("Dependency Injection built-in", font_size=20, color=HIGHLIGHT_COLOR),
            Text("Razor Pages, MVC, Blazor, Web APIs", font_size=20, color=CURVE_COLOR),
        ).arrange(DOWN, buff=0.25)
        features.next_to(definition, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(FadeIn(features, shift=RIGHT * 0.2), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WebAPIExampleScene(Scene):
    def construct(self):
        title = Text("Web API con .NET", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        controller_code = '''[ApiController]
[Route("api/[controller]")]
public class EstudiantesController : ControllerBase
{
    private readonly UniversidadContext _context;

    public EstudiantesController(UniversidadContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<Estudiante>>>
        GetEstudiantes()
    {
        return await _context.Estudiantes.ToListAsync();
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Estudiante>>
        GetEstudiante(int id)
    {
        var estudiante = await _context.Estudiantes
            .Include(e => e.Carrera)
            .FirstOrDefaultAsync(e => e.Id == id);

        if (estudiante == null)
            return NotFound();

        return estudiante;
    }

    [HttpPost]
    public async Task<ActionResult<Estudiante>> PostEstudiante(
        Estudiante estudiante)
    {
        _context.Estudiantes.Add(estudiante);
        await _context.SaveChangesAsync();

        return CreatedAtAction(nameof(GetEstudiante),
            new { id = estudiante.Id }, estudiante);
    }
}'''

        java_code = Code(
            code_string=controller_code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DependencyInjectionScene(Scene):
    def construct(self):
        title = Text("Inyeccion de Dependencias en .NET", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        registration = '''// Program.cs
builder.Services.AddDbContext<UniversidadContext>(
    options => options.UseSqlServer(
        builder.Configuration.GetConnectionString("Default")));

builder.Services.AddScoped<IEstudianteRepository, EstudianteRepository>();
builder.Services.AddTransient<IEmailService, EmailService>();
builder.Services.AddSingleton<ILoggerService, LoggerService>();'''

        usage = '''// Constructor Injection
public class EstudiantesController : ControllerBase
{
    private readonly UniversidadContext _context;
    private readonly IEstudianteRepository _repo;
    private readonly IEmailService _emailSvc;

    public EstudiantesController(
        UniversidadContext context,
        IEstudianteRepository repo,
        IEmailService emailSvc)
    {
        _context = context;
        _repo = repo;
        _emailSvc = emailSvc;
    }
}'''

        reg_code = Code(
            code_string=registration,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        reg_code.scale(0.85).to_edge(LEFT, buff=0.4).shift(UP * 0.5)

        use_code = Code(
            code_string=usage,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        use_code.scale(0.85).to_edge(RIGHT, buff=0.4).shift(UP * 0.5)

        lifetimes = VGroup(
            Text("Transient: nueva instancia cada vez", font_size=18, color=HIGHLIGHT_COLOR),
            Text("Scoped: una instancia por peticion HTTP", font_size=18, color=ACCENT_COLOR),
            Text("Singleton: una instancia para toda la app", font_size=18, color=CURVE_COLOR),
        ).arrange(DOWN, buff=0.15)
        lifetimes.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(reg_code), run_time=1)
        self.play(Create(use_code), run_time=1)
        self.play(FadeIn(lifetimes), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class MiddlewareScene(Scene):
    def construct(self):
        title = Text("Middleware en ASP.NET Core", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Middleware personalizado
public class RequestLoggingMiddleware
{
    private readonly RequestDelegate _next;

    public RequestLoggingMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        Console.WriteLine($"Peticion: {context.Request.Method} {context.Request.Path}");
        await _next(context);  // Llamar al siguiente middleware
        Console.WriteLine($"Respuesta: {context.Response.StatusCode}");
    }
}

// Registro en Program.cs
app.UseMiddleware<RequestLoggingMiddleware>();
app.Use(async (context, next) => {
    // Codigo antes
    await next();
    // Codigo despues
});'''

        java_code = Code(
            code_string=code,
            language="csharp",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: .NET y Entity Framework", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text(".NET: framework multiplataforma de Microsoft", font_size=24, color=TEXT_COLOR),
            Text("C#: lenguaje moderno y tipado seguro", font_size=24, color=TEXT_COLOR),
            Text("LINQ: consultas integradas al lenguaje", font_size=24, color=TEXT_COLOR),
            Text("Async/Await: programacion asincrona no bloqueante", font_size=24, color=TEXT_COLOR),
            Text("EF Core: ORM para acceso a datos con migrations", font_size=24, color=TEXT_COLOR),
            Text("ASP.NET Core: framework web moderno y de alto rendimiento", font_size=24, color=TEXT_COLOR),
            Text("DI: inyeccion de dependencias integrada", font_size=24, color=TEXT_COLOR),
            Text("Middleware: pipeline de procesamiento de peticiones", font_size=24, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Ecosistema completo para desarrollo empresarial",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DotNetEntityFrameworkFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        DotNetHistoryScene.construct(self)
        DotNetArchitectureScene.construct(self)
        DotNetPlatformsScene.construct(self)
        CSharpFeaturesScene.construct(self)
        LINQScene.construct(self)
        AsyncAwaitScene.construct(self)
        EntityFrameworkIntroScene.construct(self)
        EFModelsScene.construct(self)
        DbContextScene.construct(self)
        EFCRUDScene.construct(self)
        EFLazyEagerScene.construct(self)
        EFMigrationsScene.construct(self)
        EFRelationshipsScene.construct(self)
        EFFluentAPIScene.construct(self)
        EFQueryingScene.construct(self)
        EFTrackingScene.construct(self)
        EFSplitQueriesScene.construct(self)
        EFGlobalQueryFiltersScene.construct(self)
        EFShadowPropertiesScene.construct(self)
        EFStoredProceduresScene.construct(self)
        EFDatabaseProvidersScene.construct(self)
        ASPNETCoreIntroScene.construct(self)
        WebAPIExampleScene.construct(self)
        DependencyInjectionScene.construct(self)
        MiddlewareScene.construct(self)
        ConclusionScene.construct(self)
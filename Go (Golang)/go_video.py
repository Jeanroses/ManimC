from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
GO_COLOR = "#00add8"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Go (Golang)", font_size=60, color=GO_COLOR).set_color_by_gradient(GO_COLOR, ACCENT_COLOR)
        subtitle = Text("Lenguaje compilado, concurrente y eficiente", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Sintaxis Basica", font_size=48, color=GO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''package main

import "fmt"

func main() {
    // Variables
    var nombre string = "Ana"
    edad := 28
    activo := true

    // Constantes
    const PI = 3.1416

    // Tipos basicos
    var entero int = 42
    var flotante float64 = 3.14
    var texto string = "Hola"
    var booleano bool = false

    // Array y Slice
    var arr [3]int{1, 2, 3}
    slice := []int{4, 5, 6}
    slice = append(slice, 7)

    // Map
    mapa := map[string]int{
        "a": 1,
        "b": 2,
    }

    // Control
    if edad >= 18 {
        fmt.Println("Mayor")
    }

    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }

    // Switch
    switch edad {
    case 18:
        fmt.Println("Adulto")
    default:
        fmt.Println("Otro")
    }
}'''

        code = Code(code=code_str, language="go", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class FunctionsScene(Scene):
    def construct(self):
        title = Text("Funciones", font_size=48, color=GO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Funcion simple
func sumar(a int, b int) int {
    return a + b
}

// Multiple retorno
func dividir(a, b int) (int, error) {
    if b == 0 {
        return 0, fmt.Errorf("division por cero")
    }
    return a / b, nil
}

// Nombres en retorno
func operar(a, b int) (suma, resta, producto int) {
    suma = a + b
    resta = a - b
    producto = a * b
    return
}

// Variadic
func sumarTodos(numeros ...int) int {
    total := 0
    for _, n := range numeros {
        total += n
    }
    return total
}

// Funcion como parametro
func aplicar(f func(int) int, val int) int {
    return f(val)
}

// Defer
func leerArchivo() {
    f, _ := os.Open("archivo.txt")
    defer f.Close()
    // ...
}

// Closures
func contador() func() int {
    i := 0
    return func() int {
        i++
        return i
    }
}'''

        code = Code(code=code_str, language="go", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class StructsScene(Scene):
    def construct(self):
        title = Text("Structs e Interfaces", font_size=44, color=GO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Struct
type Persona struct {
    Nombre string
    Edad   int
    Email  string
}

// Metodo
func (p Persona) Saludar() string {
    return "Hola, soy " + p.Nombre
}

func (p *Persona) CumplirAnios() {
    p.Edad++
}

// Constructor
func NuevaPersona(nombre string, edad int) *Persona {
    return &Persona{Nombre: nombre, Edad: edad}
}

// Interface
type Animal interface {
    Sonido() string
}

type Perro struct{}
func (p Perro) Sonido() string { return "Guau" }

type Gato struct{}
func (g Gato) Sonido() string { return "Miau" }

// Interface vacia (any)
func imprimir(valor interface{}) {
    fmt.Println(valor)
}

// Type assertion
func obtenerEdad(val interface{}) {
    if edad, ok := val.(int); ok {
        fmt.Println(edad)
    }
}'''

        code = Code(code=code_str, language="go", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConcurrencyScene(Scene):
    def construct(self):
        title = Text("Concurrencia", font_size=48, color=GO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Goroutines
func tarea(id int) {
    for i := 0; i < 5; i++ {
        fmt.Printf("Tarea %d: %d\\n", id, i)
        time.Sleep(time.Millisecond * 100)
    }
}

func main() {
    go tarea(1)
    go tarea(2)
    time.Sleep(time.Second)
}

// Channels
func main() {
    ch := make(chan string)

    go func() {
        ch <- "Hola"
    }()

    msg := <-ch
    fmt.Println(msg)
}

// Channel con buffer
ch := make(chan int, 3)

// Select
select {
case msg := <-ch1:
    fmt.Println(msg)
case <-time.After(time.Second):
    fmt.Println("Timeout")
}

// WaitGroup
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Println(id)
    }(i)
}
wg.Wait()

// Mutex
var mu sync.Mutex
mu.Lock()
contador++
mu.Unlock()'''

        code = Code(code=code_str, language="go", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class WebScene(Scene):
    def construct(self):
        title = Text("HTTP y Web", font_size=48, color=GO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Servidor HTTP simple
func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hola %s", r.URL.Path)
}

// Router con middleware
func logging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s", r.Method, r.URL.Path)
        next.ServeHTTP(w, r)
    })
}

// JSON API
type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
}

func getUsers(w http.ResponseWriter, r *http.Request) {
    users := []User{{1, "Ana"}, {2, "Juan"}}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(users)
}

// Gin framework
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/api/users", getUsers)
    r.Run(":8080")
}

// Cliente HTTP
resp, _ := http.Get("https://api.com/data")
body, _ := ioutil.ReadAll(resp.Body)
defer resp.Body.Close()'''

        code = Code(code=code_str, language="go", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class TestScene(Scene):
    def construct(self):
        title = Text("Testing", font_size=48, color=GO_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// archivo: main_test.go
package main

import "testing"

// Test unitario
func TestSumar(t *testing.T) {
    resultado := sumar(2, 3)
    esperado := 5
    if resultado != esperado {
        t.Errorf("sumar(2,3) = %d; esperado %d", resultado, esperado)
    }
}

// Tabla de tests
func TestDividir(t *testing.T) {
    casos := []struct {
        a, b, esperado int
    }{
        {10, 2, 5},
        {9, 3, 3},
        {7, 0, 0},
    }
    for _, c := range casos {
        res, _ := dividir(c.a, c.b)
        if res != c.esperado {
            t.Errorf("dividir(%d, %d) = %d", c.a, c.b, res)
        }
    }
}

// Benchmark
func BenchmarkSumar(b *testing.B) {
    for i := 0; i < b.N; i++ {
        sumar(i, i+1)
    }
}

// TestMain
func TestMain(m *testing.M) {
    setup()
    codigo := m.Run()
    teardown()
    os.Exit(codigo)
}

// Ejecutar
// go test ./...
// go test -v
// go test -bench .'''

        code = Code(code=code_str, language="go", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Go", font_size=38, color=GO_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Sintaxis simple y rapida compilacion", font_size=22, color=TEXT_COLOR),
            Text("Structs, interfaces y metodos", font_size=22, color=TEXT_COLOR),
            Text("Goroutines y channels para concurrencia", font_size=22, color=TEXT_COLOR),
            Text("Servidores HTTP nativos", font_size=22, color=TEXT_COLOR),
            Text("Testing integrado en la stdlib", font_size=22, color=TEXT_COLOR),
            Text("Ecosistema minimalista pero potente", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Lenguaje eficiente para microservicios y cloud", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class GoFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        FunctionsScene.construct(self)
        StructsScene.construct(self)
        ConcurrencyScene.construct(self)
        WebScene.construct(self)
        TestScene.construct(self)
        ConclusionScene.construct(self)
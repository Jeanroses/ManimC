from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
KOTLIN_COLOR = "#7f52ff"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Kotlin", font_size=60, color=KOTLIN_COLOR).set_color_by_gradient(KOTLIN_COLOR, ACCENT_COLOR)
        subtitle = Text("Lenguaje moderno para JVM y multiplataforma", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Sintaxis Basica", font_size=48, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Variables
val nombre: String = "Ana"     // inmutable
var edad: Int = 28              // mutable

// Inferencia de tipos
val activo = true
val pi = 3.1416

// Null safety
var email: String? = null
val longitud = email?.length ?: 0

// Strings
val mensaje = "Hola, $nombre"
val multilinea = """
  Linea 1
  Linea 2
""".trimIndent()

// Control de flujo
if (edad >= 18) {
  println("Mayor")
} else {
  println("Menor")
}

// When
when (edad) {
  in 0..17 -> println("Menor")
  in 18..64 -> println("Adulto")
  else -> println("Adulto mayor")
}

// Ranges
for (i in 1..5) println(i)
for (i in 10 downTo 1 step 2) println(i)'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class FunctionsScene(Scene):
    def construct(self):
        title = Text("Funciones", font_size=48, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Funciones
fun sumar(a: Int, b: Int): Int {
  return a + b
}

// Expression body
fun multiplicar(a: Int, b: Int) = a * b

// Default params
fun saludar(nombre: String = "Mundo") {
  println("Hola $nombre")
}

// Named arguments
saludar(nombre = "Juan")

// Lambda
val cuadrado: (Int) -> Int = { x -> x * x }

// Higher-order
fun operar(a: Int, b: Int, op: (Int, Int) -> Int): Int {
  return op(a, b)
}
val resultado = operar(2, 3) { x, y -> x + y }

// Extension function
fun String.esEmail(): Boolean = contains("@")
"test@mail.com".esEmail()

// Inline + reified
inline fun <reified T> tipo(): String = T::class.java.simpleName'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class OOPScene(Scene):
    def construct(self):
        title = Text("POO en Kotlin", font_size=46, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Clase basica
class Persona(val nombre: String, var edad: Int) {
  fun saludar() = "Hola, soy $nombre"
}

// Data class
data class Usuario(val id: Int, val email: String)

// Herencia
open class Animal(open val nombre: String) {
  open fun sonido() = "..."
}

class Perro(override val nombre: String): Animal(nombre) {
  override fun sonido() = "Guau"
}

// Interfaces
interface Conducible {
  fun conducir()
}

class Auto: Conducible {
  override fun conducir() = println("Conduciendo")
}

// Sealed classes
sealed class Resultado {
  data class Exito(val data: String): Resultado()
  data class Error(val msg: String): Resultado()
}

// Object / Singleton
object Config {
  const val API_URL = "https://api.com"
}

// Companion object
class Factory {
  companion object {
    fun crear() = Factory()
  }
}'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class CollectionsScene(Scene):
    def construct(self):
        title = Text("Colecciones", font_size=48, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Colecciones
val lista = listOf(1, 2, 3, 4)
val mutable = mutableListOf("a", "b")

// Map y Set
val mapa = mapOf("a" to 1, "b" to 2)
val conjunto = setOf(1, 2, 2, 3)

// Operadores funcionales
val pares = lista.filter { it % 2 == 0 }
val dobles = lista.map { it * 2 }
val suma = lista.reduce { acc, i -> acc + i }
val total = lista.fold(0) { acc, i -> acc + i }

// Sorting
val orden = lista.sortedDescending()

// Grouping
val grupos = lista.groupBy { it % 2 == 0 }

// Sequences
val secuencia = generateSequence(1) { it + 1 }
  .take(5)
  .toList()

// Null-safe collections
val nullable: List<Int?> = listOf(1, null, 3)
val sinNull = nullable.filterNotNull()'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class CoroutinesScene(Scene):
    def construct(self):
        title = Text("Coroutines", font_size=48, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Coroutines
import kotlinx.coroutines.*

fun main() = runBlocking {
  launch {
    delay(1000)
    println("Coroutine 1")
  }
  async {
    delay(500)
    println("Coroutine 2")
  }.await()
}

// Scope y dispatcher
val scope = CoroutineScope(Dispatchers.IO)
scope.launch {
  val data = fetchData()
}

// Suspending function
suspend fun fetchData(): String {
  delay(1000)
  return "data"
}

// Structured concurrency
suspend fun cargarTodo() = coroutineScope {
  val a = async { fetchData() }
  val b = async { fetchData() }
  a.await() + b.await()
}

// Flow
val flow = flow {
  emit(1)
  emit(2)
  emit(3)
}
flow.collect { println(it) }'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AndroidScene(Scene):
    def construct(self):
        title = Text("Android y Kotlin", font_size=44, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Android con Kotlin

// Jetpack Compose
@Composable
fun Greeting(name: String) {
  Text(text = "Hola $name")
}

// ViewModel
class MainViewModel: ViewModel() {
  private val _state = MutableStateFlow(0)
  val state: StateFlow<Int> = _state

  fun incrementar() {
    _state.value += 1
  }
}

// Room (DB local)
@Entity
data class User(
  @PrimaryKey val id: Int,
  val nombre: String
)

@Dao
interface UserDao {
  @Query("SELECT * FROM user")
  fun getAll(): Flow<List<User>>

  @Insert
  suspend fun insert(user: User)
}

// Retrofit
interface ApiService {
  @GET("users")
  suspend fun getUsers(): List<User>
}

// Hilt DI
@HiltAndroidApp
class MyApp: Application()'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class MultiplatformScene(Scene):
    def construct(self):
        title = Text("Kotlin Multiplatform", font_size=40, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Multiplatform
// Compartir logica entre Android, iOS, JVM, JS

// build.gradle.kts
kotlin {
  android()
  iosX64()
  iosArm64()
  js(IR) {
    browser()
  }

  sourceSets {
    val commonMain by getting {
      dependencies {
        implementation("io.ktor:ktor-client-core")
      }
    }
    val androidMain by getting
    val iosMain by creating
  }
}

// Expect / Actual
expect fun plataforma(): String

// androidMain
actual fun plataforma() = "Android"

// iosMain
actual fun plataforma() = "iOS"'''

        code = Code(code=code_str, language="kotlin", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Kotlin", font_size=38, color=KOTLIN_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Sintaxis concisa y null safety", font_size=22, color=TEXT_COLOR),
            Text("Funciones, lambdas y extensiones", font_size=22, color=TEXT_COLOR),
            Text("POO + sealed classes", font_size=22, color=TEXT_COLOR),
            Text("Colecciones y APIs funcionales", font_size=22, color=TEXT_COLOR),
            Text("Coroutines y Flow", font_size=22, color=TEXT_COLOR),
            Text("Android moderno con Compose", font_size=22, color=TEXT_COLOR),
            Text("Multiplatform: compartir logica", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Lenguaje moderno, seguro y productivo", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class KotlinFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        FunctionsScene.construct(self)
        OOPScene.construct(self)
        CollectionsScene.construct(self)
        CoroutinesScene.construct(self)
        AndroidScene.construct(self)
        MultiplatformScene.construct(self)
        ConclusionScene.construct(self)

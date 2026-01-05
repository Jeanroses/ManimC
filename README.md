<p align="center">
  <img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png" alt="Manim Logo" width="300"/>
</p>

<h1 align="center">🎬 Manim — Mathematical Animation Engine</h1>

<p align="center">
  <strong>Guía completa para crear animaciones matemáticas profesionales con Python</strong>
</p>

<p align="center">
  <a href="#-qué-es-manim">¿Qué es?</a> •
  <a href="#-instalación">Instalación</a> •
  <a href="#-renderizado">Renderizado</a> •
  <a href="#-objetos-mobjects">Objetos</a> •
  <a href="#-animaciones">Animaciones</a> •
  <a href="#-matemáticas-latex">LaTeX</a> •
  <a href="#-recursos">Recursos</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Manim-Community%20Edition-58B5F0?style=for-the-badge" alt="Manim CE"/>
  <img src="https://img.shields.io/badge/LaTeX-Supported-008080?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
</p>

---

## 🎥 ¿Qué es Manim?

**Manim** (Mathematical Animation Engine) es una biblioteca de Python para crear animaciones matemáticas precisas y de alta calidad. Fue originalmente desarrollada por **Grant Sanderson** ([3Blue1Brown](https://www.youtube.com/c/3blue1brown)) para sus famosos videos educativos.

### 🔀 Versiones Disponibles

| Versión | Descripción | Estado |
|---------|-------------|--------|
| **[Manim Community (CE)](https://www.manim.community/)** | Fork mantenido por la comunidad | ✅ **Recomendado** |
| **[ManimGL](https://github.com/3b1b/manim)** | Versión de 3Blue1Brown con OpenGL | ⚡ Renderizado en tiempo real |

> 💡 **Este repositorio utiliza Manim Community Edition**, la versión más estable y mejor documentada.

### 🌟 Características Principales

| Característica | Descripción |
|----------------|-------------|
| 📐 **Precisión Matemática** | Renderizado exacto de fórmulas y gráficos |
| 🎨 **Control Total** | Personalización pixel-perfect de cada elemento |
| ⚡ **Animaciones Fluidas** | Hasta 60 FPS de calidad profesional |
| 📝 **LaTeX Integrado** | Soporte nativo para ecuaciones matemáticas |
| 🔧 **Extensible** | Fácil de modificar y crear componentes custom |
| 🐍 **100% Python** | Aprovecha todo el ecosistema de Python |

---

## ⚙️ Instalación

### 📋 Prerrequisitos

| Dependencia | Descripción | Obligatorio |
|-------------|-------------|-------------|
| **Python 3.8+** | Lenguaje base | ✅ Sí |
| **FFmpeg** | Codificación de video | ✅ Sí |
| **LaTeX** | Ecuaciones matemáticas | ⚠️ Opcional* |

> *LaTeX es necesario solo si usas `MathTex` o `Tex` para ecuaciones.

---

### 🪟 Windows

#### Opción 1: Chocolatey (Recomendado)

```powershell
# Instalar Chocolatey (si no lo tienes) - Ejecutar como Administrador
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar dependencias
choco install python ffmpeg miktex -y

# Instalar Manim
pip install manim
```

#### Opción 2: Manual

```powershell
# 1. Descargar e instalar Python desde python.org
# 2. Descargar FFmpeg desde ffmpeg.org y agregar al PATH
# 3. Descargar MiKTeX desde miktex.org (opcional)

# Instalar Manim
pip install manim
```

---

### 🐧 Linux (Ubuntu/Debian)

```bash
# Dependencias del sistema
sudo apt update
sudo apt install -y build-essential python3-dev libcairo2-dev \
    libpango1.0-dev ffmpeg

# LaTeX (opcional, pero recomendado)
sudo apt install -y texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science dvipng

# Instalar Manim
pip3 install manim
```

---

### 🍎 macOS

```bash
# Usando Homebrew
brew install python ffmpeg

# LaTeX (opcional)
brew install --cask mactex-no-gui

# Instalar Manim
pip3 install manim
```

---

### ✅ Verificar Instalación

```bash
manim --version
# Output esperado: Manim Community v0.18.x
```

```bash
# Test rápido
manim -pql -s test.py TestScene
```

---

## 🎬 Renderizado

### 📊 Comando Básico

```bash
manim [OPCIONES] <archivo.py> <NombreEscena>
```

### 🎚️ Calidades de Renderizado

| Flag | Nombre | Resolución | FPS | Tiempo | Uso |
|------|--------|------------|-----|--------|-----|
| `-ql` | Low | 854×480 | 15 | ⚡ Rápido | Desarrollo/Preview |
| `-qm` | Medium | 1280×720 | 30 | 🔄 Moderado | Pruebas |
| `-qh` | High | 1920×1080 | 60 | 🐢 Lento | Producción |
| `-qp` | Production | 1920×1080 | 60 | 🐢 Lento | Producción |
| `-qk` | 4K | 3840×2160 | 60 | 🐌 Muy lento | Ultra calidad |

### 🔧 Opciones de CLI

| Opción | Descripción |
|--------|-------------|
| `-p` | **Preview** — Abre el video automáticamente al terminar |
| `-s` | **Screenshot** — Guarda solo la última imagen (PNG) |
| `-a` | **All** — Renderiza todas las escenas del archivo |
| `-o <nombre>` | **Output** — Nombre personalizado del archivo |
| `--format gif` | Exportar como GIF animado |
| `--format webm` | Exportar como WebM |
| `-n <num>` | Renderiza desde la animación número `<num>` |
| `--disable_caching` | Desactiva el caché (útil para debugging) |
| `-t` | **Transparent** — Fondo transparente |

### 💡 Ejemplos de Uso

```bash
# 🎯 Preview rápido durante desarrollo
manim -pql archivo.py MiEscena

# 🎥 Producción HD (1080p, 60fps)
manim -pqh archivo.py MiEscena

# 📸 Capturar solo la última imagen
manim -pqh -s archivo.py MiEscena

# 🔄 Renderizar TODAS las escenas
manim -ql archivo.py -a

# 🎞️ Exportar como GIF
manim -ql --format gif archivo.py MiEscena

# 📁 Nombre de salida personalizado
manim -qh archivo.py MiEscena -o "video_final"

# 🖥️ Renderizado en 4K
manim -qk archivo.py MiEscena

# 🎨 Fondo transparente (para composición)
manim -qh -t archivo.py MiEscena

# ⏭️ Empezar desde la animación #5
manim -pql -n 5 archivo.py MiEscena
```

### 📂 Estructura de Salida

```
media/
├── videos/
│   └── archivo/
│       ├── 480p15/          # -ql
│       │   └── MiEscena.mp4
│       ├── 720p30/          # -qm
│       ├── 1080p60/         # -qh
│       └── 2160p60/         # -qk
├── images/                  # Screenshots (-s)
└── Tex/                     # Archivos LaTeX compilados
```

---

## 🎭 Objetos (Mobjects)

Los **Mobjects** (Mathematical Objects) son los elementos visuales fundamentales de Manim.

### 📐 Formas Geométricas

```python
from manim import *

class FormasBasicas(Scene):
    def construct(self):
        # Círculo
        circulo = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        
        # Cuadrado
        cuadrado = Square(side_length=2, color=RED)
        
        # Rectángulo
        rectangulo = Rectangle(width=3, height=1, color=GREEN)
        
        # Línea
        linea = Line(start=LEFT*2, end=RIGHT*2, color=YELLOW)
        
        # Flecha
        flecha = Arrow(start=ORIGIN, end=UP*2, color=PURPLE)
        
        # Polígono
        triangulo = Polygon(
            [-1, -1, 0], [1, -1, 0], [0, 1, 0],
            color=ORANGE
        )
        
        # Arco
        arco = Arc(radius=2, angle=PI/2, color=PINK)
        
        # Punto
        punto = Dot(point=ORIGIN, color=WHITE)
```

### 📝 Texto

```python
class TextoEjemplos(Scene):
    def construct(self):
        # Texto simple
        texto = Text("¡Hola Manim!", font_size=48)
        
        # Texto con fuente personalizada
        texto_font = Text("Fuente Custom", font="Arial")
        
        # Texto con color
        texto_color = Text("Colores", color=BLUE)
        
        # Texto con gradiente
        texto_grad = Text("Gradiente").set_color_by_gradient(BLUE, GREEN)
        
        # Texto con estilos
        texto_bold = Text("Negrita", weight=BOLD)
        texto_italic = Text("Itálica", slant=ITALIC)
        
        # MarkupText para formato avanzado (Pango)
        markup = MarkupText(
            '<span foreground="blue">Azul</span> y <b>negrita</b>'
        )
```

### ➗ Matemáticas (LaTeX)

```python
class MatematicasEjemplos(Scene):
    def construct(self):
        # Ecuación simple
        ecuacion = MathTex(r"E = mc^2")
        
        # Ecuación compleja
        integral = MathTex(
            r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}"
        )
        
        # Fracción
        fraccion = MathTex(r"\frac{a}{b} = \frac{c}{d}")
        
        # Matriz
        matriz = MathTex(r"""
            \begin{bmatrix}
            a & b \\
            c & d
            \end{bmatrix}
        """)
        
        # Texto con matemáticas mezcladas
        mixto = Tex(r"El área es $A = \pi r^2$")
        
        # Colorear partes específicas
        formula = MathTex(r"a^2", "+", r"b^2", "=", r"c^2")
        formula[0].set_color(RED)
        formula[2].set_color(BLUE)
        formula[4].set_color(GREEN)
```

### 📊 Gráficos y Ejes

```python
class GraficosEjemplos(Scene):
    def construct(self):
        # Ejes 2D
        ejes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        )
        
        # Graficar función
        grafica = ejes.plot(lambda x: np.sin(x), color=BLUE)
        
        # Etiquetas
        etiqueta = ejes.get_graph_label(grafica, label="\\sin(x)")
        
        # Plano numérico
        plano = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1]
        )
        
        # Gráfico de barras
        barras = BarChart(
            values=[3, 5, 2, 8, 4],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 10, 2]
        )
```

### 🔲 Grupos y Layouts

```python
class GruposEjemplos(Scene):
    def construct(self):
        # VGroup - Grupo vertical
        grupo_v = VGroup(
            Circle(),
            Square(),
            Triangle()
        ).arrange(DOWN, buff=0.5)
        
        # HGroup - Grupo horizontal
        grupo_h = VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT)
        
        # Posicionamiento relativo
        circulo = Circle()
        cuadrado = Square().next_to(circulo, RIGHT, buff=1)
        
        # Alineación
        objetos = VGroup(
            Circle(radius=0.3),
            Square(side_length=0.8),
            Circle(radius=0.5)
        ).arrange(RIGHT, aligned_edge=DOWN)
```

---

## ✨ Animaciones

### 🎬 Animaciones de Creación

```python
class AnimacionesCreacion(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        texto = Text("Manim")
        ecuacion = MathTex(r"E = mc^2")
        
        # Create - Dibuja el contorno
        self.play(Create(circulo))
        
        # Write - Para texto y ecuaciones
        self.play(Write(texto))
        self.play(Write(ecuacion))
        
        # FadeIn - Aparecer gradualmente
        self.play(FadeIn(circulo))
        self.play(FadeIn(texto, shift=UP))  # Con dirección
        
        # GrowFromCenter - Crecer desde el centro
        self.play(GrowFromCenter(circulo))
        
        # DrawBorderThenFill - Dibujar borde y rellenar
        self.play(DrawBorderThenFill(circulo))
        
        # SpinInFromNothing - Aparecer girando
        self.play(SpinInFromNothing(circulo))
```

### 🔄 Animaciones de Transformación

```python
class AnimacionesTransformacion(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        cuadrado = Square(color=RED)
        
        # Transform - Transformar un objeto en otro
        self.play(Transform(circulo, cuadrado))
        
        # ReplacementTransform - Similar pero reemplaza el objeto
        self.play(ReplacementTransform(circulo, cuadrado))
        
        # MoveToTarget - Mover a posición objetivo
        circulo.generate_target()
        circulo.target.shift(RIGHT * 2)
        circulo.target.set_color(GREEN)
        self.play(MoveToTarget(circulo))
        
        # TransformMatchingShapes - Para texto
        texto1 = Text("ABC")
        texto2 = Text("ABCD")
        self.play(TransformMatchingShapes(texto1, texto2))
```

### 🏃 Animaciones de Movimiento

```python
class AnimacionesMovimiento(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        
        # Shift - Mover relativo
        self.play(circulo.animate.shift(RIGHT * 2))
        
        # Move_to - Mover a posición absoluta
        self.play(circulo.animate.move_to(UP * 2))
        
        # Rotate - Rotar
        self.play(Rotate(circulo, angle=PI))
        self.play(circulo.animate.rotate(PI/4))
        
        # Scale - Escalar
        self.play(circulo.animate.scale(2))
        
        # Encadenar animaciones
        self.play(
            circulo.animate
            .shift(LEFT)
            .rotate(PI/2)
            .set_color(RED)
            .scale(0.5)
        )
```

### 🚪 Animaciones de Salida

```python
class AnimacionesSalida(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        self.add(circulo)
        
        # FadeOut - Desvanecer
        self.play(FadeOut(circulo))
        self.play(FadeOut(circulo, shift=DOWN))
        
        # Uncreate - Inverso de Create
        self.play(Uncreate(circulo))
        
        # Unwrite - Inverso de Write
        texto = Text("Adiós")
        self.play(Unwrite(texto))
        
        # ShrinkToCenter - Encoger al centro
        self.play(ShrinkToCenter(circulo))
```

### ⏱️ Control de Tiempo

```python
class ControlTiempo(Scene):
    def construct(self):
        c1 = Circle(color=BLUE)
        c2 = Square(color=RED).shift(RIGHT*2)
        
        # run_time - Duración de la animación
        self.play(Create(c1), run_time=3)
        
        # rate_func - Curva de velocidad
        from manim import rate_functions
        self.play(Create(c2), rate_func=rate_functions.ease_in_out_bounce)
        # Otras: linear, smooth, rush_into, rush_from, there_and_back
        
        # Animaciones simultáneas
        self.play(
            Create(c1),
            Create(c2)
        )
        
        # Animaciones secuenciales con Succession
        self.play(Succession(
            Create(c1),
            Create(c2),
            lag_ratio=0.5
        ))
        
        # AnimationGroup con lag
        self.play(AnimationGroup(
            Create(c1),
            Create(c2),
            lag_ratio=0.3
        ))
        
        # Pausa
        self.wait(2)
```

---

## 📐 Matemáticas (LaTeX)

### 📝 Sintaxis Básica

```python
class LaTeXBasico(Scene):
    def construct(self):
        # Usar r"" para raw strings (evita problemas con \)
        
        # Exponentes y subíndices
        exp = MathTex(r"x^2, x^{10}, x_1, x_{12}")
        
        # Fracciones
        frac = MathTex(r"\frac{a}{b}, \dfrac{1}{2}")
        
        # Raíces
        sqrt = MathTex(r"\sqrt{x}, \sqrt[3]{x}")
        
        # Sumatorias e integrales
        sum_int = MathTex(r"\sum_{i=1}^{n} i, \int_0^1 x\,dx")
        
        # Límites
        lim = MathTex(r"\lim_{x \to \infty} f(x)")
        
        # Letras griegas
        greek = MathTex(r"\alpha, \beta, \gamma, \theta, \pi, \omega")
        
        # Símbolos
        symbols = MathTex(r"\infty, \partial, \nabla, \times, \cdot")
```

### 🎨 Colorear Ecuaciones

```python
class ColorearEcuaciones(Scene):
    def construct(self):
        # Método 1: Separar en partes
        eq = MathTex(r"a^2", "+", r"b^2", "=", r"c^2")
        eq[0].set_color(RED)      # a^2
        eq[2].set_color(BLUE)     # b^2
        eq[4].set_color(GREEN)    # c^2
        
        # Método 2: set_color_by_tex
        eq2 = MathTex(r"E", "=", "m", "c^2")
        eq2.set_color_by_tex("E", YELLOW)
        eq2.set_color_by_tex("m", BLUE)
        
        # Método 3: substrings_to_isolate
        eq3 = MathTex(
            r"f(x) = ax^2 + bx + c",
            substrings_to_isolate=["a", "b", "c"]
        )
        eq3.set_color_by_tex("a", RED)
        eq3.set_color_by_tex("b", GREEN)
        eq3.set_color_by_tex("c", BLUE)
```

### 🔄 Transformar Ecuaciones

```python
class TransformarEcuaciones(Scene):
    def construct(self):
        eq1 = MathTex(r"x^2 + 2x + 1")
        eq2 = MathTex(r"(x + 1)^2")
        
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
```

---

## 🎨 Configuración y Estilos

### ⚙️ Archivo de Configuración

Crea un archivo `manim.cfg` en tu directorio de proyecto:

```ini
[CLI]
# Calidad por defecto
quality = low_quality

# Preview automático
preview = True

# Directorio de salida
media_dir = ./media

[renderer]
# Color de fondo
background_color = #000000

[output]
# Formato de video
format = mp4
```

### 🎨 Paleta de Colores Recomendada

```python
# Catppuccin Mocha (Tema oscuro elegante)
BACKGROUND   = "#000000"  # Negro
PRIMARY      = "#89b4fa"  # Azul
SECONDARY    = "#f5c2e7"  # Rosa
ACCENT       = "#a6e3a1"  # Verde
HIGHLIGHT    = "#f9e2af"  # Amarillo
WARNING      = "#fab387"  # Naranja
TEXT         = "#cdd6f4"  # Blanco cálido
ERROR        = "#f38ba8"  # Rojo

# Aplicar
config.background_color = BACKGROUND
```

### 📐 Plantilla de Escena

```python
from manim import *

# Configuración global
config.background_color = "#000000"

class MiEscena(Scene):
    def construct(self):
        self.play_intro()
        self.play_contenido()
        self.play_conclusion()
    
    def play_intro(self):
        titulo = Text("Mi Animación", font_size=72, color="#89b4fa")
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
    
    def play_contenido(self):
        # Tu contenido aquí
        pass
    
    def play_conclusion(self):
        thanks = Text("¡Gracias!", font_size=48)
        self.play(FadeIn(thanks))
        self.wait(2)
```

---

## 🔧 Tips y Trucos

### ⚡ Optimización de Renderizado

```python
# Usar run_time más cortos durante desarrollo
self.play(Create(obj), run_time=0.5)

# Desactivar preview para batch rendering
manim -ql archivo.py -a  # Sin -p

# Usar caché efectivamente
# (Manim cachea animaciones - cambios pequeños son rápidos)
```

### 🐛 Debugging

```python
# Agregar objeto sin animación (instant)
self.add(objeto)

# Mostrar punto para debugging
self.add(Dot(punto, color=RED))

# Imprimir posición
print(objeto.get_center())

# Mostrar bounding box
self.add(SurroundingRectangle(objeto))
```

### 📏 Posicionamiento

```python
# Constantes de posición
UP, DOWN, LEFT, RIGHT, ORIGIN
UL, UR, DL, DR  # Esquinas

# Ejemplo
objeto.to_edge(UP)           # Al borde superior
objeto.to_corner(UL)         # Esquina superior izquierda
objeto.next_to(otro, RIGHT)  # A la derecha de otro objeto
objeto.move_to(ORIGIN)       # Al centro
```

---

## 📚 Recursos

### 📖 Documentación

| Recurso | Enlace |
|---------|--------|
| 📘 Documentación Oficial | [docs.manim.community](https://docs.manim.community/) |
| 🎓 Tutorial Quickstart | [Quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html) |
| 📚 Referencia de API | [Reference](https://docs.manim.community/en/stable/reference.html) |
| 🖼️ Galería de Ejemplos | [Examples](https://docs.manim.community/en/stable/examples.html) |

### 🎬 Canales de YouTube

| Canal | Contenido |
|-------|-----------|
| [3Blue1Brown](https://www.youtube.com/c/3blue1brown) | Creador original, matemáticas |
| [Theorem of Beethoven](https://www.youtube.com/c/TheoremofBeethoven) | Tutoriales de Manim |
| [Reducible](https://www.youtube.com/c/Reducible) | Ciencias de la computación |

### 💬 Comunidad

| Plataforma | Enlace |
|------------|--------|
| 🗨️ Discord | [discord.gg/mMRrZQW](https://discord.gg/mMRrZQW) |
| 📝 Reddit | [r/manim](https://www.reddit.com/r/manim/) |
| 🐙 GitHub | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) |

---

## 📋 Cheat Sheet Rápido

```bash
# Renderizado
manim -pql archivo.py Escena    # Preview rápido
manim -pqh archivo.py Escena    # Alta calidad
manim -pqh -s archivo.py Escena # Solo imagen

# Formatos
manim --format gif archivo.py Escena  # GIF
manim -t archivo.py Escena            # Transparente
```

```python
# Básicos
self.play(Create(obj))          # Crear
self.play(Write(texto))         # Escribir
self.play(FadeIn(obj))          # Aparecer
self.play(FadeOut(obj))         # Desaparecer
self.play(Transform(a, b))      # Transformar
self.wait(2)                    # Esperar

# Movimiento
obj.animate.shift(RIGHT*2)      # Mover
obj.animate.rotate(PI/2)        # Rotar
obj.animate.scale(2)            # Escalar
obj.animate.set_color(RED)      # Cambiar color
```

---

<p align="center">
  <strong>⭐ Happy Animating! ⭐</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Manim-58B5F0?style=for-the-badge" alt="Made with Manim"/>
  <img src="https://img.shields.io/badge/Powered%20by-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

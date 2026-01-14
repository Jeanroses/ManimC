<p align="center">
  <img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png" alt="Manim Logo" width="400"/>
</p>

<h1 align="center">Manim — Mathematical Animation Engine</h1>

<p align="center">
  <strong>Guía para crear animaciones matemáticas profesionales con Python</strong>
</p>

<p align="center">
  <a href="#qué-es-manim">Qué es</a> •
  <a href="#instalación">Instalación</a> •
  <a href="#renderizado">Renderizado</a> •
  <a href="#objetos-mobjects">Objetos</a> •
  <a href="#animaciones">Animaciones</a> •
  <a href="#matemáticas-latex">LaTeX</a> •
  <a href="#recursos">Recursos</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Manim-Community%20Edition-58B5F0?style=for-the-badge" alt="Manim CE"/>
  <img src="https://img.shields.io/badge/LaTeX-Supported-008080?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
</p>

---

## Qué es Manim

**Manim** (Mathematical Animation Engine) es una biblioteca de Python para crear animaciones matemáticas de alta calidad. Desarrollada originalmente por Grant Sanderson ([3Blue1Brown](https://www.youtube.com/c/3blue1brown)).

### Versiones

| Versión                                         | Descripción                       | Estado                     |
| ----------------------------------------------- | --------------------------------- | -------------------------- |
| [Manim Community](https://www.manim.community/) | Fork mantenido por la comunidad   | Recomendado                |
| [ManimGL](https://github.com/3b1b/manim)        | Versión de 3Blue1Brown con OpenGL | Renderizado en tiempo real |

> Este repositorio utiliza **Manim Community Edition**.

### Características

- **Precisión matemática**: Renderizado exacto de fórmulas y gráficos
- **Control total**: Personalización de cada elemento visual
- **Animaciones fluidas**: Hasta 60 FPS
- **LaTeX integrado**: Soporte nativo para ecuaciones
- **Extensible**: Fácil de modificar y crear componentes
- **100% Python**: Aprovecha todo el ecosistema

---

## Instalación

### Prerrequisitos

| Dependencia | Descripción            | Obligatorio |
| ----------- | ---------------------- | ----------- |
| Python 3.8+ | Lenguaje base          | Sí          |
| FFmpeg      | Codificación de video  | Sí          |
| LaTeX       | Ecuaciones matemáticas | Opcional\*  |

\*LaTeX es necesario solo para `MathTex` o `Tex`.

---

### Windows

**Opción 1: Chocolatey (Recomendado)**

```powershell
# Instalar Chocolatey (ejecutar como Administrador)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar dependencias
choco install python ffmpeg miktex -y

# Instalar Manim
pip install manim
```

**Opción 2: Manual**

```powershell
# 1. Descargar Python desde python.org
# 2. Descargar FFmpeg desde ffmpeg.org y agregar al PATH
# 3. Descargar MiKTeX desde miktex.org (opcional)

pip install manim
```

---

### Linux (Ubuntu/Debian)

```bash
# Dependencias del sistema
sudo apt update
sudo apt install -y build-essential python3-dev libcairo2-dev \
    libpango1.0-dev ffmpeg

# LaTeX (opcional)
sudo apt install -y texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science dvipng

pip3 install manim
```

---

### macOS

```bash
brew install python ffmpeg

# LaTeX (opcional)
brew install --cask mactex-no-gui

pip3 install manim
```

---

### Verificar instalación

```bash
manim --version
```

---

## Renderizado

### Comando básico

```bash
manim [OPCIONES] <archivo.py> <NombreEscena>
```

### Calidades

| Flag  | Resolución | FPS | Uso           |
| ----- | ---------- | --- | ------------- |
| `-ql` | 854x480    | 15  | Desarrollo    |
| `-qm` | 1280x720   | 30  | Pruebas       |
| `-qh` | 1920x1080  | 60  | Producción    |
| `-qk` | 3840x2160  | 60  | Ultra calidad |

### Opciones principales

| Opción         | Descripción                      |
| -------------- | -------------------------------- |
| `-p`           | Abre el video al terminar        |
| `-s`           | Guarda solo la última imagen     |
| `-a`           | Renderiza todas las escenas      |
| `-o <nombre>`  | Nombre personalizado del archivo |
| `--format gif` | Exportar como GIF                |
| `-t`           | Fondo transparente               |

### Ejemplos

```bash
# Preview rápido
manim -pql archivo.py MiEscena

# Producción HD
manim -pqh archivo.py MiEscena

# Capturar imagen
manim -pqh -s archivo.py MiEscena

# Exportar como GIF
manim -ql --format gif archivo.py MiEscena

# Renderizado 4K
manim -qk archivo.py MiEscena
```

### Estructura de salida

```
media/
├── videos/
│   └── archivo/
│       ├── 480p15/
│       ├── 720p30/
│       ├── 1080p60/
│       └── 2160p60/
├── images/
└── Tex/
```

---

## Objetos (Mobjects)

Los **Mobjects** son los elementos visuales de Manim.

### Formas geométricas

```python
from manim import *

class FormasBasicas(Scene):
    def construct(self):
        circulo = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        cuadrado = Square(side_length=2, color=RED)
        rectangulo = Rectangle(width=3, height=1, color=GREEN)
        linea = Line(start=LEFT*2, end=RIGHT*2, color=YELLOW)
        flecha = Arrow(start=ORIGIN, end=UP*2, color=PURPLE)
        triangulo = Polygon([-1, -1, 0], [1, -1, 0], [0, 1, 0], color=ORANGE)
        arco = Arc(radius=2, angle=PI/2, color=PINK)
        punto = Dot(point=ORIGIN, color=WHITE)
```

### Texto

```python
class TextoEjemplos(Scene):
    def construct(self):
        texto = Text("Hola Manim", font_size=48)
        texto_font = Text("Fuente Custom", font="Arial")
        texto_color = Text("Colores", color=BLUE)
        texto_grad = Text("Gradiente").set_color_by_gradient(BLUE, GREEN)
        texto_bold = Text("Negrita", weight=BOLD)
```

### Matemáticas (LaTeX)

```python
class MatematicasEjemplos(Scene):
    def construct(self):
        ecuacion = MathTex(r"E = mc^2")
        integral = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        fraccion = MathTex(r"\frac{a}{b} = \frac{c}{d}")
        matriz = MathTex(r"\begin{bmatrix} a & b \\ c & d \end{bmatrix}")
        mixto = Tex(r"El área es $A = \pi r^2$")

        # Colorear partes
        formula = MathTex(r"a^2", "+", r"b^2", "=", r"c^2")
        formula[0].set_color(RED)
        formula[2].set_color(BLUE)
        formula[4].set_color(GREEN)
```

### Gráficos

```python
class GraficosEjemplos(Scene):
    def construct(self):
        ejes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4
        )
        grafica = ejes.plot(lambda x: np.sin(x), color=BLUE)
        etiqueta = ejes.get_graph_label(grafica, label="\\sin(x)")

        plano = NumberPlane(x_range=[-5, 5, 1], y_range=[-5, 5, 1])

        barras = BarChart(
            values=[3, 5, 2, 8, 4],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 10, 2]
        )
```

### Grupos

```python
class GruposEjemplos(Scene):
    def construct(self):
        grupo_v = VGroup(Circle(), Square(), Triangle()).arrange(DOWN, buff=0.5)
        grupo_h = VGroup(*[Dot() for _ in range(5)]).arrange(RIGHT)

        circulo = Circle()
        cuadrado = Square().next_to(circulo, RIGHT, buff=1)
```

---

## Animaciones

### Creación

```python
class AnimacionesCreacion(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        texto = Text("Manim")

        self.play(Create(circulo))        # Dibuja contorno
        self.play(Write(texto))           # Escribe texto
        self.play(FadeIn(circulo))        # Aparece gradualmente
        self.play(GrowFromCenter(circulo))
        self.play(DrawBorderThenFill(circulo))
```

### Transformación

```python
class AnimacionesTransformacion(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        cuadrado = Square(color=RED)

        self.play(Transform(circulo, cuadrado))
        self.play(ReplacementTransform(circulo, cuadrado))

        circulo.generate_target()
        circulo.target.shift(RIGHT * 2).set_color(GREEN)
        self.play(MoveToTarget(circulo))
```

### Movimiento

```python
class AnimacionesMovimiento(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)

        self.play(circulo.animate.shift(RIGHT * 2))
        self.play(circulo.animate.move_to(UP * 2))
        self.play(Rotate(circulo, angle=PI))
        self.play(circulo.animate.scale(2))

        # Encadenar
        self.play(
            circulo.animate
            .shift(LEFT)
            .rotate(PI/2)
            .set_color(RED)
            .scale(0.5)
        )
```

### Salida

```python
class AnimacionesSalida(Scene):
    def construct(self):
        circulo = Circle(color=BLUE)
        self.add(circulo)

        self.play(FadeOut(circulo))
        self.play(Uncreate(circulo))
        self.play(ShrinkToCenter(circulo))
```

### Control de tiempo

```python
class ControlTiempo(Scene):
    def construct(self):
        c1 = Circle(color=BLUE)
        c2 = Square(color=RED).shift(RIGHT*2)

        self.play(Create(c1), run_time=3)
        self.play(Create(c2), rate_func=rate_functions.ease_in_out_bounce)

        # Simultáneas
        self.play(Create(c1), Create(c2))

        # Secuenciales
        self.play(Succession(Create(c1), Create(c2), lag_ratio=0.5))

        self.wait(2)
```

---

## Matemáticas (LaTeX)

### Sintaxis básica

```python
class LaTeXBasico(Scene):
    def construct(self):
        exp = MathTex(r"x^2, x^{10}, x_1, x_{12}")
        frac = MathTex(r"\frac{a}{b}, \dfrac{1}{2}")
        sqrt = MathTex(r"\sqrt{x}, \sqrt[3]{x}")
        sum_int = MathTex(r"\sum_{i=1}^{n} i, \int_0^1 x\,dx")
        lim = MathTex(r"\lim_{x \to \infty} f(x)")
        greek = MathTex(r"\alpha, \beta, \gamma, \theta, \pi, \omega")
        symbols = MathTex(r"\infty, \partial, \nabla, \times, \cdot")
```

### Colorear ecuaciones

```python
class ColorearEcuaciones(Scene):
    def construct(self):
        # Separar en partes
        eq = MathTex(r"a^2", "+", r"b^2", "=", r"c^2")
        eq[0].set_color(RED)
        eq[2].set_color(BLUE)
        eq[4].set_color(GREEN)

        # Por texto
        eq2 = MathTex(r"E", "=", "m", "c^2")
        eq2.set_color_by_tex("E", YELLOW)
        eq2.set_color_by_tex("m", BLUE)
```

---

## Configuración

### Archivo manim.cfg

```ini
[CLI]
quality = low_quality
preview = True
media_dir = ./media

[renderer]
background_color = #000000

[output]
format = mp4
```

### Plantilla de escena

```python
from manim import *

config.background_color = "#000000"

class MiEscena(Scene):
    def construct(self):
        self.play_intro()
        self.play_contenido()
        self.play_conclusion()

    def play_intro(self):
        titulo = Text("Mi Animación", font_size=72)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))

    def play_contenido(self):
        pass

    def play_conclusion(self):
        thanks = Text("Gracias", font_size=48)
        self.play(FadeIn(thanks))
        self.wait(2)
```

---

## Tips

### Optimización

```python
# Tiempos cortos durante desarrollo
self.play(Create(obj), run_time=0.5)

# Batch rendering
manim -ql archivo.py -a
```

### Debugging

```python
self.add(objeto)                      # Agregar sin animación
self.add(Dot(punto, color=RED))       # Punto de referencia
print(objeto.get_center())            # Imprimir posición
self.add(SurroundingRectangle(objeto))# Bounding box
```

### Posicionamiento

```python
# Constantes
UP, DOWN, LEFT, RIGHT, ORIGIN
UL, UR, DL, DR  # Esquinas

objeto.to_edge(UP)
objeto.to_corner(UL)
objeto.next_to(otro, RIGHT)
objeto.move_to(ORIGIN)
```

---

## Recursos

### Documentación

| Recurso               | Enlace                                                                         |
| --------------------- | ------------------------------------------------------------------------------ |
| Documentación Oficial | [docs.manim.community](https://docs.manim.community/)                          |
| Tutorial Quickstart   | [Quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html) |
| Referencia de API     | [Reference](https://docs.manim.community/en/stable/reference.html)             |
| Galería de Ejemplos   | [Examples](https://docs.manim.community/en/stable/examples.html)               |

### Canales de YouTube

| Canal                                                                | Contenido                  |
| -------------------------------------------------------------------- | -------------------------- |
| [3Blue1Brown](https://www.youtube.com/c/3blue1brown)                 | Creador original           |
| [Theorem of Beethoven](https://www.youtube.com/c/TheoremofBeethoven) | Tutoriales de Manim        |
| [Reducible](https://www.youtube.com/c/Reducible)                     | Ciencias de la computación |

### Comunidad

| Plataforma | Enlace                                                          |
| ---------- | --------------------------------------------------------------- |
| Discord    | [discord.gg/mMRrZQW](https://discord.gg/mMRrZQW)                |
| Reddit     | [r/manim](https://www.reddit.com/r/manim/)                      |
| GitHub     | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) |

---

## Referencia rápida

```bash
manim -pql archivo.py Escena    # Preview
manim -pqh archivo.py Escena    # Alta calidad
manim -pqh -s archivo.py Escena # Solo imagen
manim --format gif archivo.py Escena
```

```python
self.play(Create(obj))          # Crear
self.play(Write(texto))         # Escribir
self.play(FadeIn(obj))          # Aparecer
self.play(FadeOut(obj))         # Desaparecer
self.play(Transform(a, b))      # Transformar
self.wait(2)                    # Esperar

obj.animate.shift(RIGHT*2)      # Mover
obj.animate.rotate(PI/2)        # Rotar
obj.animate.scale(2)            # Escalar
obj.animate.set_color(RED)      # Color
```

---

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Manim-58B5F0?style=for-the-badge" alt="Made with Manim"/>
  <img src="https://img.shields.io/badge/Powered%20by-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

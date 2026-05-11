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
            "Transformada de Laplace",
            font_size=52,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "De ecuaciones diferenciales a algebraicas",
            font_size=28,
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


class DefinitionScene(Scene):
    def construct(self):
        title = Text("Definicion formal", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        formula = MathTex(
            r"\mathcal{L}\{f(t)\}(s) = \int_0^\infty e^{-st} f(t) \, dt",
            font_size=42,
            color=ACCENT_COLOR,
        )
        formula.next_to(title, DOWN, buff=0.8)

        parts = VGroup(
            Text("f(t): funcion original en tiempo", font_size=24, color=TEXT_COLOR),
            Text("s: variable compleja (s = sigma + iomega)", font_size=24, color=TEXT_COLOR),
            Text("L{f(t)}: transformada en variable s", font_size=24, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        parts.next_to(formula, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.5)
        self.wait(0.8)

        for p in parts:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SimpleTransformsScene(Scene):
    def construct(self):
        title = Text("Transformadas basicas", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        transforms = VGroup(
            MathTex(r"\mathcal{L}\{1\} = \frac{1}{s}", font_size=32, color=HIGHLIGHT_COLOR),
            MathTex(r"\mathcal{L}\{t\} = \frac{1}{s^2}", font_size=32, color=HIGHLIGHT_COLOR),
            MathTex(r"\mathcal{L}\{e^{at}\} = \frac{1}{s-a}", font_size=32, color=HIGHLIGHT_COLOR),
            MathTex(r"\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2 + \omega^2}", font_size=28, color=HIGHLIGHT_COLOR),
            MathTex(r"\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2 + \omega^2}", font_size=28, color=HIGHLIGHT_COLOR),
        ).arrange(DOWN, buff=0.4)
        transforms.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        for t in transforms:
            self.play(Write(t), run_time=0.8)
            self.wait(0.4)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PropertiesScene(Scene):
    def construct(self):
        title = Text("Propiedades fundamentales", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        prop1 = VGroup(
            Text("1. Linealidad", font_size=26, color=CURVE_COLOR),
            MathTex(r"\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)", font_size=28, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        prop2 = VGroup(
            Text("2. Primera derivada", font_size=26, color=SECONDARY_COLOR),
            MathTex(r"\mathcal{L}\{f'(t)\} = sF(s) - f(0)", font_size=28, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        prop3 = VGroup(
            Text("3. Segunda derivada", font_size=26, color=ACCENT_COLOR),
            MathTex(r"\mathcal{L}\{f''(t)\} = s^2F(s) - sf(0) - f'(0)", font_size=28, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        prop4 = VGroup(
            Text("4. Desplazamiento en tiempo", font_size=26, color=HIGHLIGHT_COLOR),
            MathTex(r"\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)", font_size=28, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)

        properties = VGroup(prop1, prop2, prop3, prop4).arrange(DOWN, buff=0.4)
        properties.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.7)
            self.wait(0.4)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class Transform1ExampleScene(Scene):
    def construct(self):
        title = Text("Ejemplo 1: Transformada de t", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        problem = MathTex(r"\mathcal{L}\{t\} = \int_0^\infty t e^{-st} \, dt", font_size=36, color=HIGHLIGHT_COLOR)
        problem.next_to(title, DOWN, buff=0.7)

        step1 = MathTex(r"= \left[ -\frac{t e^{-st}}{s} \right]_0^\infty + \frac{1}{s}\int_0^\infty e^{-st} \, dt", font_size=28, color=TEXT_COLOR)
        step1.next_to(problem, DOWN, buff=0.4)

        step2 = MathTex(r"= 0 + \frac{1}{s} \left[ -\frac{e^{-st}}{s} \right]_0^\infty", font_size=28, color=TEXT_COLOR)
        step2.next_to(step1, DOWN, buff=0.3)

        result = MathTex(r"= \frac{1}{s^2}", font_size=40, color=SUCCESS_COLOR)
        result.next_to(step2, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Write(problem), run_time=1)
        self.wait(0.8)
        self.play(Write(step1), run_time=1.2)
        self.wait(0.6)
        self.play(Write(step2), run_time=1.2)
        self.wait(0.6)
        self.play(Write(result), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class Transform2ExampleScene(Scene):
    def construct(self):
        title = Text("Ejemplo 2: Transformada de sen", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        problem = MathTex(r"\mathcal{L}\{\sin(\omega t)\}", font_size=36, color=HIGHLIGHT_COLOR)
        problem.next_to(title, DOWN, buff=0.7)

        hint = Text("Usando integracion por partes dos veces", font_size=22, color=WARNING_COLOR)
        hint.next_to(problem, DOWN, buff=0.3)

        step1 = MathTex(r"= \frac{\omega}{s^2 + \omega^2}", font_size=40, color=SUCCESS_COLOR)
        step1.next_to(hint, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Write(problem), run_time=1)
        self.play(FadeIn(hint), run_time=0.8)
        self.wait(0.8)
        self.play(Write(step1), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class InverseTransformScene(Scene):
    def construct(self):
        title = Text("Transformada inversa", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = MathTex(
            r"f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{2\pi i}\int_{\gamma - i\infty}^{\gamma + i\infty} e^{st} F(s) \, ds",
            font_size=24,
            color=HIGHLIGHT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.7)

        practical_title = Text("En la practica: fracciones parciales", font_size=26, color=SECONDARY_COLOR)
        practical_title.next_to(definition, DOWN, buff=0.5)

        example = MathTex(
            r"\mathcal{L}^{-1}\left\{ \frac{1}{s(s+1)} \right\} = 1 - e^{-t}",
            font_size=32,
            color=ACCENT_COLOR,
        )
        example.next_to(practical_title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Write(definition), run_time=1.2)
        self.play(FadeIn(practical_title), run_time=0.8)
        self.play(Write(example), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PartialFractionsScene(Scene):
    def construct(self):
        title = Text("Fracciones parciales", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        problem = MathTex(
            r"\mathcal{L}^{-1}\left\{ \frac{s+1}{s(s-2)} \right\}",
            font_size=36,
            color=HIGHLIGHT_COLOR,
        )
        problem.next_to(title, DOWN, buff=0.7)

        decomposition = MathTex(
            r"\frac{s+1}{s(s-2)} = \frac{A}{s} + \frac{B}{s-2}",
            font_size=32,
            color=TEXT_COLOR,
        )
        decomposition.next_to(problem, DOWN, buff=0.5)

        solving = Text("Resolviendo: A = -1/2, B = 3/2", font_size=24, color=SECONDARY_COLOR)
        solving.next_to(decomposition, DOWN, buff=0.4)

        result = MathTex(
            r"= -\frac{1}{2}(1) + \frac{3}{2}e^{2t}",
            font_size=32,
            color=SUCCESS_COLOR,
        )
        result.next_to(solving, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Write(problem), run_time=1)
        self.play(Write(decomposition), run_time=1.2)
        self.play(FadeIn(solving), run_time=0.8)
        self.play(Write(result), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SolvingODEScene(Scene):
    def construct(self):
        title = Text("Resolver EDOs con Laplace", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        problem_title = Text("y'' + y = sen(t),  y(0)=0, y'(0)=1", font_size=28, color=HIGHLIGHT_COLOR)
        problem_title.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Write(problem_title), run_time=1)
        self.wait(0.8)

        step1 = MathTex(r"\mathcal{L}\{y''\} + \mathcal{L}\{y\} = \mathcal{L}\{\sin(t)\}", font_size=26, color=TEXT_COLOR)
        step1.next_to(problem_title, DOWN, buff=0.5)
        self.play(Write(step1), run_time=1)

        step2 = MathTex(r"(s^2Y - s\cdot0 - 1) + Y = \frac{1}{s^2+1}", font_size=28, color=TEXT_COLOR)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2), run_time=1)
        self.wait(0.6)

        step3 = MathTex(r"(s^2 + 1)Y = \frac{1}{s^2+1} + 1", font_size=28, color=TEXT_COLOR)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3), run_time=1)
        self.wait(0.6)

        step4 = MathTex(r"Y(s) = \frac{s^2+2}{(s^2+1)^2}", font_size=32, color=SECONDARY_COLOR)
        step4.next_to(step3, DOWN, buff=0.4)
        self.play(Write(step4), run_time=1)
        self.wait(0.8)

        final = Text("Ahora aplicar transformada inversa...", font_size=24, color=ACCENT_COLOR)
        final.next_to(step4, DOWN, buff=0.4)
        self.play(FadeIn(final), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConvolutionScene(Scene):
    def construct(self):
        title = Text("Convolucion en Laplace", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = MathTex(
            r"(f * g)(t) = \int_0^t f(\tau)g(t-\tau) \, d\tau",
            font_size=32,
            color=HIGHLIGHT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.7)

        property_formula = MathTex(
            r"\mathcal{L}\{f * g\} = \mathcal{L}\{f\} \cdot \mathcal{L}\{g\}",
            font_size=36,
            color=ACCENT_COLOR,
        )
        property_formula.next_to(definition, DOWN, buff=0.6)

        example = Text("Convolucion en el tiempo = Multiplicacion en s", font_size=26, color=SECONDARY_COLOR)
        example.next_to(property_formula, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Write(definition), run_time=1.2)
        self.play(Write(property_formula), run_time=1)
        self.play(FadeIn(example), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class HeavisideScene(Scene):
    def construct(self):
        title = Text("Funcion de Heaviside (escalon)", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = MathTex(
            r"u(t-a) = \begin{cases} 0 & t < a \\ 1 & t \geq a \end{cases}",
            font_size=36,
            color=HIGHLIGHT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.7)

        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-0.5, 1.5, 1],
            x_length=5.5,
            y_length=3.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        step_graph = VGroup(
            Line(axes.c2p(-0.5, 0), axes.c2p(2, 0), color=CURVE_COLOR, stroke_width=3),
            Dot(axes.c2p(2, 0), color=CURVE_COLOR),
            Dot(axes.c2p(2, 1), color=CURVE_COLOR),
            Line(axes.c2p(2, 1), axes.c2p(4.5, 1), color=CURVE_COLOR, stroke_width=3),
        )

        self.play(Write(title), run_time=1)
        self.play(Write(definition), run_time=1.2)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(step_graph), run_time=1)

        formula = MathTex(r"\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)", font_size=30, color=ACCENT_COLOR)
        formula.to_edge(LEFT, buff=0.6).shift(DOWN * 1.5)
        self.play(FadeIn(formula, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DiracDeltaScene(Scene):
    def construct(self):
        title = Text("Delta de Dirac", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = VGroup(
            MathTex(r"\delta(t-a) = 0 \text{ para } t \neq a", font_size=28, color=TEXT_COLOR),
            MathTex(r"\int_{-\infty}^{\infty} \delta(t-a) \, dt = 1", font_size=28, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.3)

        definition.next_to(title, DOWN, buff=0.7)

        transform = MathTex(r"\mathcal{L}\{\delta(t-a)\} = e^{-as}", font_size=36, color=ACCENT_COLOR)
        transform.next_to(definition, DOWN, buff=0.6)

        special = MathTex(r"\mathcal{L}\{\delta(t)\} = 1", font_size=32, color=SUCCESS_COLOR)
        special.next_to(transform, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=1)
        self.play(Write(transform), run_time=1)
        self.play(Write(special), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ApplicationCircuitScene(Scene):
    def construct(self):
        title = Text("Aplicacion: Circuitos RC", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        circuit_eq = Text("RC V' + V = V_fuente(t)", font_size=26, color=HIGHLIGHT_COLOR)
        circuit_eq.next_to(title, DOWN, buff=0.5)

        with_laplace = MathTex(
            r"RC(sV(s) - V(0)) + V(s) = V_f(s)",
            font_size=28,
            color=TEXT_COLOR,
        )
        with_laplace.next_to(circuit_eq, DOWN, buff=0.4)

        solve = MathTex(
            r"V(s) = \frac{V_f(s) + RCV_0}{RCs + 1}",
            font_size=30,
            color=SECONDARY_COLOR,
        )
        solve.next_to(with_laplace, DOWN, buff=0.4)

        inverse = Text("Aplicando L^{-1} se obtiene V(t) en dominio temporal", font_size=22, color=ACCENT_COLOR)
        inverse.next_to(solve, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(Write(circuit_eq), run_time=1)
        self.play(Write(with_laplace), run_time=1)
        self.play(Write(solve), run_time=1)
        self.play(FadeIn(inverse), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ApplicationControlScene(Scene):
    def construct(self):
        title = Text("Aplicacion: Control Automatico", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        transfer = MathTex(
            r"G(s) = \frac{Y(s)}{U(s)} = \frac{K}{\tau s + 1}",
            font_size=32,
            color=HIGHLIGHT_COLOR,
        )
        transfer.next_to(title, DOWN, buff=0.7)

        step = Text("Respuesta a escalon unitario:", font_size=24, color=SECONDARY_COLOR)
        step.next_to(transfer, DOWN, buff=0.5)

        response = MathTex(
            r"y(t) = K(1 - e^{-t/\tau})",
            font_size=32,
            color=ACCENT_COLOR,
        )
        response.next_to(step, DOWN, buff=0.4)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 1.5, 0.5],
            x_length=5.0,
            y_length=3.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        response_curve = axes.plot(lambda t: 1 - np.exp(-t), x_range=[0, 5.5], color=SUCCESS_COLOR, stroke_width=3)

        self.play(Write(title), run_time=1)
        self.play(Write(transfer), run_time=1)
        self.play(FadeIn(step), run_time=0.8)
        self.play(Write(response), run_time=1)
        self.play(Create(axes), Create(response_curve), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TableScene(Scene):
    def construct(self):
        title = Text("Tabla resumen de transformadas", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        table = VGroup(
            MathTex(r"f(t)", font_size=24, color=PRIMARY_COLOR),
            MathTex(r"F(s) = \mathcal{L}\{f(t)\}", font_size=24, color=PRIMARY_COLOR),
            MathTex(r"1", font_size=22, color=TEXT_COLOR),
            MathTex(r"\frac{1}{s}", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"t", font_size=22, color=TEXT_COLOR),
            MathTex(r"\frac{1}{s^2}", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"e^{at}", font_size=22, color=TEXT_COLOR),
            MathTex(r"\frac{1}{s-a}", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"\sin(\omega t)", font_size=22, color=TEXT_COLOR),
            MathTex(r"\frac{\omega}{s^2+\omega^2}", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"\cos(\omega t)", font_size=22, color=TEXT_COLOR),
            MathTex(r"\frac{s}{s^2+\omega^2}", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"t^n", font_size=22, color=TEXT_COLOR),
            MathTex(r"\frac{n!}{s^{n+1}}", font_size=22, color=HIGHLIGHT_COLOR),
        )
        table.arrange_in_grid(rows=5, cols=2, buff=(0.4, 0.25))
        table.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(table, shift=UP * 0.2), run_time=1.5)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Transformada de Laplace", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Convierte EDOs en ecuaciones algebraicas", font_size=26, color=TEXT_COLOR),
            Text("Propiedades: linealidad, derivadas, convolucion", font_size=26, color=TEXT_COLOR),
            Text("Permite resolver sistemas lineales con condiciones iniciales", font_size=26, color=TEXT_COLOR),
            Text("Esencial en control, circuitos y senales", font_size=26, color=TEXT_COLOR),
            Text("Transformada inversa usa fracciones parciales", font_size=26, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        self.wait(1.2)

        final_msg = Text(
            "Herramienta fundamental en ingenieria",
            font_size=28,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LaplaceTransformFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        DefinitionScene.construct(self)
        SimpleTransformsScene.construct(self)
        PropertiesScene.construct(self)
        Transform1ExampleScene.construct(self)
        Transform2ExampleScene.construct(self)
        InverseTransformScene.construct(self)
        PartialFractionsScene.construct(self)
        SolvingODEScene.construct(self)
        ConvolutionScene.construct(self)
        HeavisideScene.construct(self)
        DiracDeltaScene.construct(self)
        ApplicationCircuitScene.construct(self)
        ApplicationCircuitScene.construct(self)
        TableScene.construct(self)
        ConclusionScene.construct(self)
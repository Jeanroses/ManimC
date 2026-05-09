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

PLANE_STYLE = {
    "stroke_color": "#2a2a2a",
    "stroke_width": 1,
    "stroke_opacity": 0.6,
}

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Derivadas parciales\ny gradiente",
            font_size=56,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "Una lectura geometrica",
            font_size=30,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.06, color=c)
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
        title = Text("Definiciones clave", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        mapping = MathTex(r"f: \mathbb{R}^2 \to \mathbb{R}", font_size=36, color=TEXT_COLOR)

        fx = MathTex(
            r"\frac{\partial f}{\partial x}(x_0,y_0) = \lim_{h\to 0}"
            r"\frac{f(x_0+h,y_0) - f(x_0,y_0)}{h}",
            font_size=28,
            color=TEXT_COLOR,
        )

        fy = MathTex(
            r"\frac{\partial f}{\partial y}(x_0,y_0) = \lim_{h\to 0}"
            r"\frac{f(x_0,y_0+h) - f(x_0,y_0)}{h}",
            font_size=28,
            color=TEXT_COLOR,
        )

        grad = MathTex(
            r"\nabla f(x_0,y_0) = \left(\frac{\partial f}{\partial x},"
            r"\frac{\partial f}{\partial y}\right)",
            font_size=30,
            color=ACCENT_COLOR,
        )

        group = VGroup(mapping, fx, fy, grad).arrange(DOWN, buff=0.35)
        group.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(mapping, shift=UP * 0.2), run_time=0.8)
        self.play(Write(fx), run_time=1.4)
        self.play(Write(fy), run_time=1.4)
        self.play(FadeIn(grad, shift=UP * 0.2), run_time=0.8)
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PartialXScene(Scene):
    def construct(self):
        title = Text("Derivada parcial en x", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        x0 = 1.0
        y0 = 1.0

        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4.6,
            y_length=4.6,
            background_line_style=PLANE_STYLE,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.6)

        fixed_y = Line(
            plane.c2p(-3, y0),
            plane.c2p(3, y0),
            color=SECONDARY_COLOR,
            stroke_width=3,
        )

        point = Dot(plane.c2p(x0, y0), color=HIGHLIGHT_COLOR)
        point_label = MathTex(r"(x_0,y_0)", font_size=24, color=HIGHLIGHT_COLOR)
        point_label.next_to(point, UP, buff=0.1)

        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 6, 1],
            x_length=4.8,
            y_length=3.2,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(RIGHT, buff=0.6)

        graph = axes.plot(lambda x: x**2 + y0**2, x_range=[-2.5, 2.5], color=CURVE_COLOR)
        graph_label = MathTex(r"g(x) = f(x,y_0)", font_size=24, color=CURVE_COLOR)
        graph_label.next_to(axes, UP, buff=0.2)

        slope = 2 * x0
        tangent = axes.plot(
            lambda x: slope * (x - x0) + (x0**2 + y0**2),
            x_range=[x0 - 1.2, x0 + 1.2],
            color=HIGHLIGHT_COLOR,
        )
        dot_graph = Dot(axes.c2p(x0, x0**2 + y0**2), color=HIGHLIGHT_COLOR)

        label = MathTex(r"\frac{\partial f}{\partial x}(x_0,y_0)", font_size=28, color=HIGHLIGHT_COLOR)
        label.next_to(axes, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(plane), FadeIn(axes), run_time=1.2)
        self.play(Create(fixed_y), FadeIn(point), FadeIn(point_label), run_time=0.8)
        self.play(Create(graph), FadeIn(graph_label), run_time=1)
        self.play(Create(tangent), FadeIn(dot_graph), run_time=0.8)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.6)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PartialYScene(Scene):
    def construct(self):
        title = Text("Derivada parcial en y", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        x0 = 1.2
        y0 = 0.8

        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4.6,
            y_length=4.6,
            background_line_style=PLANE_STYLE,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.6)

        fixed_x = Line(
            plane.c2p(x0, -3),
            plane.c2p(x0, 3),
            color=SECONDARY_COLOR,
            stroke_width=3,
        )

        point = Dot(plane.c2p(x0, y0), color=HIGHLIGHT_COLOR)
        point_label = MathTex(r"(x_0,y_0)", font_size=24, color=HIGHLIGHT_COLOR)
        point_label.next_to(point, UP, buff=0.1)

        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 6, 1],
            x_length=4.8,
            y_length=3.2,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(RIGHT, buff=0.6)

        graph = axes.plot(lambda y: x0**2 + y**2, x_range=[-2.5, 2.5], color=CURVE_COLOR)
        graph_label = MathTex(r"h(y) = f(x_0,y)", font_size=24, color=CURVE_COLOR)
        graph_label.next_to(axes, UP, buff=0.2)

        slope = 2 * y0
        tangent = axes.plot(
            lambda y: slope * (y - y0) + (x0**2 + y0**2),
            x_range=[y0 - 1.2, y0 + 1.2],
            color=HIGHLIGHT_COLOR,
        )
        dot_graph = Dot(axes.c2p(y0, x0**2 + y0**2), color=HIGHLIGHT_COLOR)

        label = MathTex(r"\frac{\partial f}{\partial y}(x_0,y_0)", font_size=28, color=HIGHLIGHT_COLOR)
        label.next_to(axes, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(plane), FadeIn(axes), run_time=1.2)
        self.play(Create(fixed_x), FadeIn(point), FadeIn(point_label), run_time=0.8)
        self.play(Create(graph), FadeIn(graph_label), run_time=1)
        self.play(Create(tangent), FadeIn(dot_graph), run_time=0.8)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.6)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class GradientScene(Scene):
    def construct(self):
        title = Text("Gradiente y curvas de nivel", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=8.0,
            y_length=5.0,
            background_line_style=PLANE_STYLE,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).shift(DOWN * 0.2)

        levels = VGroup(
            Circle(radius=0.8, color=CURVE_COLOR, stroke_width=2),
            Circle(radius=1.4, color=SECONDARY_COLOR, stroke_width=2),
            Circle(radius=2.0, color=ACCENT_COLOR, stroke_width=2),
        )

        x0, y0 = 1.0, 0.8
        point = Dot(plane.c2p(x0, y0), color=HIGHLIGHT_COLOR)

        grad_vec = np.array([2 * x0, 2 * y0, 0])
        scale = 0.35
        grad_arrow = Arrow(
            plane.c2p(x0, y0),
            plane.c2p(x0 + scale * grad_vec[0], y0 + scale * grad_vec[1]),
            color=ACCENT_COLOR,
            buff=0,
            stroke_width=4,
        )

        grad_label = MathTex(r"\nabla f(x_0,y_0)", font_size=28, color=ACCENT_COLOR)
        grad_label.next_to(grad_arrow, UP, buff=0.2)

        formula = MathTex(r"\nabla f = (2x, 2y)", font_size=30, color=TEXT_COLOR)
        formula.to_edge(DOWN, buff=0.4)

        note = Text(
            "Direccion de mayor crecimiento",
            font_size=24,
            color=HIGHLIGHT_COLOR,
        ).next_to(formula, UP, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(plane), run_time=1)
        self.play(FadeIn(levels, shift=UP * 0.1), run_time=1)
        self.play(FadeIn(point), run_time=0.4)
        self.play(GrowArrow(grad_arrow), FadeIn(grad_label), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.2), FadeIn(formula), run_time=0.8)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DirectionalDerivativeScene(Scene):
    def construct(self):
        title = Text("Derivada direccional", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=8.0,
            y_length=5.0,
            background_line_style=PLANE_STYLE,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).shift(DOWN * 0.2)

        x0, y0 = 1.0, 0.6
        point = Dot(plane.c2p(x0, y0), color=HIGHLIGHT_COLOR)

        grad_vec = np.array([2 * x0, 2 * y0, 0])
        grad_arrow = Arrow(
            plane.c2p(x0, y0),
            plane.c2p(x0 + 0.35 * grad_vec[0], y0 + 0.35 * grad_vec[1]),
            color=ACCENT_COLOR,
            buff=0,
            stroke_width=4,
        )

        theta = 35 * DEGREES
        u = np.array([np.cos(theta), np.sin(theta), 0])
        u_arrow = Arrow(
            plane.c2p(x0, y0),
            plane.c2p(x0 + 1.1 * u[0], y0 + 1.1 * u[1]),
            color=SECONDARY_COLOR,
            buff=0,
            stroke_width=4,
        )

        u_label = MathTex(r"\vec{u}", font_size=26, color=SECONDARY_COLOR)
        u_label.next_to(u_arrow.get_end(), UP, buff=0.15)

        formula = MathTex(r"D_{\vec{u}} f = \nabla f \cdot \vec{u}", font_size=32, color=TEXT_COLOR)
        formula.to_edge(DOWN, buff=0.5)

        note = Text(
            "Proyeccion del gradiente sobre la direccion u",
            font_size=24,
            color=HIGHLIGHT_COLOR,
        ).next_to(formula, UP, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(plane), run_time=1)
        self.play(FadeIn(point), run_time=0.4)
        self.play(GrowArrow(grad_arrow), run_time=0.6)
        self.play(GrowArrow(u_arrow), FadeIn(u_label), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.2), FadeIn(formula), run_time=0.8)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen", font_size=46, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Las derivadas parciales miden cambio en x o y", font_size=26, color=TEXT_COLOR),
            Text("El gradiente apunta al crecimiento mas rapido", font_size=26, color=TEXT_COLOR),
            Text("La derivada direccional es una proyeccion", font_size=26, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.7)

        closing = Text(
            "Listo para aplicar en optimizacion y fisica",
            font_size=28,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.7)
        self.play(FadeIn(closing, shift=UP * 0.2), run_time=0.8)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PartialsGradientFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        DefinitionScene.construct(self)
        PartialXScene.construct(self)
        PartialYScene.construct(self)
        GradientScene.construct(self)
        DirectionalDerivativeScene.construct(self)
        ConclusionScene.construct(self)

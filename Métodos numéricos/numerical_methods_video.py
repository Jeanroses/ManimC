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
            "Metodos numericos",
            font_size=58,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "Aproximando soluciones con precision",
            font_size=30,
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


class WhyNumericalScene(Scene):
    def construct(self):
        title = Text("Por que metodos numericos?", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        reasons = VGroup(
            Text("1. Ecuaciones sin solucion analitica exacta", font_size=26, color=TEXT_COLOR),
            Text("2. Sistemas grandes que requieren eficiencia", font_size=26, color=TEXT_COLOR),
            Text("3. Datos discretos (mediciones experimentales)", font_size=26, color=TEXT_COLOR),
            Text("4. Optimizacion y simulacion numerica", font_size=26, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        reasons.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1.2)
        for r in reasons:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class BisectionMethodScene(Scene):
    def construct(self):
        title = Text("Metodo de Biseccion", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        subtitle = Text("Reduccion del intervalo por la mitad", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)

        axes = Axes(
            x_range=[0, 4, 0.5],
            y_range=[-2, 3, 1],
            x_length=5.5,
            y_length=4.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)

        def f(x):
            return x**3 - 4*x - 2

        graph = axes.plot(f, x_range=[0, 4], color=CURVE_COLOR, stroke_width=3)

        x_axis_label = Text("x", font_size=24, color=TEXT_COLOR).next_to(axes.x_axis, RIGHT)
        y_axis_label = Text("f(x)", font_size=24, color=TEXT_COLOR).next_to(axes.y_axis, UP)

        self.play(Write(title), FadeIn(subtitle), run_time=1)
        self.play(Create(axes), FadeIn(x_axis_label), FadeIn(y_axis_label), run_time=1)
        self.play(Create(graph), run_time=1)

        a, b = 2.0, 3.0
        for i in range(4):
            c = (a + b) / 2
            fc = f(c)

            left_line = Line(axes.c2p(a, 0), axes.c2p(b, 0), color=WARNING_COLOR, stroke_width=4)
            point_a = Dot(axes.c2p(a, 0), color=WARNING_COLOR)
            point_b = Dot(axes.c2p(b, 0), color=WARNING_COLOR)

            label_text = f"Iteracion {i+1}: c={c:.2f}, f(c)={fc:.2f}"
            label = Text(label_text, font_size=22, color=HIGHLIGHT_COLOR if fc > 0 else SUCCESS_COLOR)
            label.to_edge(DOWN, buff=0.4)

            if i == 0:
                self.play(Create(left_line), FadeIn(point_a), FadeIn(point_b), run_time=0.8)

            mid_point = Dot(axes.c2p(c, 0), color=ITER_COLOR)

            self.play(FadeIn(mid_point), FadeIn(label), run_time=0.8)
            self.wait(0.6)

            if f(c) * f(a) < 0:
                b = c
            else:
                a = c

            self.play(
                FadeOut(left_line),
                FadeOut(point_a),
                FadeOut(point_b),
                FadeOut(mid_point),
                FadeOut(label),
                run_time=0.4,
            )

        formula = MathTex(r"x \approx \frac{a+b}{2}", font_size=32, color=SUCCESS_COLOR)
        formula.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(formula), run_time=0.8)
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class NewtonRaphsonScene(Scene):
    def construct(self):
        title = Text("Metodo de Newton-Raphson", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        subtitle = Text("Tangentes como aproximacion", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-2, 4, 1],
            x_length=5.5,
            y_length=4.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)

        def f(x):
            return x**3 - 4*x - 2

        def df(x):
            return 3*x**2 - 4

        graph = axes.plot(f, x_range=[0.5, 4.5], color=CURVE_COLOR, stroke_width=3)

        x0 = 3.5

        self.play(Write(title), FadeIn(subtitle), run_time=1)
        self.play(Create(axes), Create(graph), run_time=1)

        points = []
        labels = []
        tangents = []

        for i in range(4):
            x_curr = x0 if i == 0 else points[-1][0]
            y_curr = f(x_curr)
            slope = df(x_curr)

            pt = Dot(axes.c2p(x_curr, y_curr), color=HIGHLIGHT_COLOR)
            points.append((x_curr, y_curr))

            label_text = f"x{i+1}={x_curr:.3f}"
            lbl = Text(label_text, font_size=18, color=HIGHLIGHT_COLOR)
            lbl.next_to(pt, UP, buff=0.15)
            labels.append(lbl)

            if i == 0:
                self.play(FadeIn(pt), FadeIn(lbl), run_time=0.6)

            x_new = x_curr - f(x_curr) / slope
            y_intercept = y_curr - slope * x_curr

            tangent = axes.plot(
                lambda x, m=slope, b=y_intercept, xc=x_curr: m * (x - xc) + f(x_curr),
                x_range=[x_curr - 1.5, x_curr + 0.5],
                color=ITER_COLOR,
                stroke_width=2,
            )
            tangents.append(tangent)

            x_intersection = Dot(axes.c2p(x_new, 0), color=SUCCESS_COLOR)

            if i > 0:
                self.play(FadeIn(pt), FadeIn(lbl), run_time=0.6)

            self.play(Create(tangent), run_time=0.5)
            self.play(FadeIn(x_intersection), run_time=0.5)

            new_label = Text(f"x{i+2}={x_new:.3f}", font_size=18, color=SUCCESS_COLOR)
            new_label.next_to(x_intersection, DOWN, buff=0.15)
            labels.append(new_label)
            self.play(FadeIn(new_label), run_time=0.5)

            self.wait(0.6)

            x0 = x_new

        formula = MathTex(r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}", font_size=32, color=ACCENT_COLOR)
        formula.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(formula), run_time=0.8)
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SecantMethodScene(Scene):
    def construct(self):
        title = Text("Metodo de la Secante", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        subtitle = Text("Dos puntos, una recta secante", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)

        axes = Axes(
            x_range=[0, 4, 0.5],
            y_range=[-2, 3, 1],
            x_length=5.5,
            y_length=4.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)

        def f(x):
            return x**3 - 4*x - 2

        graph = axes.plot(f, x_range=[0.2, 4], color=CURVE_COLOR, stroke_width=3)

        self.play(Write(title), FadeIn(subtitle), run_time=1)
        self.play(Create(axes), Create(graph), run_time=1)

        x0, x1 = 2.5, 3.5

        for i in range(4):
            f0, f1 = f(x0), f(x1)

            secant = Line(
                axes.c2p(x0 - 0.5, f0 - 0.5 * (f1 - f0) / (x1 - x0)),
                axes.c2p(x1 + 0.5, f1 + 0.5 * (f1 - f0) / (x1 - x0)),
                color=ITER_COLOR,
                stroke_width=2,
            )

            p0 = Dot(axes.c2p(x0, f0), color=WARNING_COLOR)
            p1 = Dot(axes.c2p(x1, f1), color=WARNING_COLOR)

            if i == 0:
                self.play(FadeIn(p0), FadeIn(p1), run_time=0.6)

            self.play(Create(secant), run_time=0.6)

            x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
            x_int = Dot(axes.c2p(x_new, 0), color=SUCCESS_COLOR)

            label_text = f"Iter {i+1}: x={x_new:.3f}"
            label = Text(label_text, font_size=20, color=SUCCESS_COLOR)
            label.next_to(x_int, DOWN, buff=0.2)

            self.play(FadeIn(x_int), FadeIn(label), run_time=0.6)
            self.wait(0.7)

            x0, x1 = x1, x_new

            self.play(
                FadeOut(secant),
                FadeOut(label),
                run_time=0.4,
            )

        formula = MathTex(r"x_{n+1} = x_n - f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}", font_size=26, color=ACCENT_COLOR)
        formula.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(formula), run_time=0.8)
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ComparisonScene(Scene):
    def construct(self):
        title = Text("Comparacion de metodos", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        table = VGroup(
            Text("Metodo", font_size=22, color=PRIMARY_COLOR),
            Text("Convergencia", font_size=22, color=PRIMARY_COLOR),
            Text("Derivada necesaria", font_size=22, color=PRIMARY_COLOR),
            Text("Biseccion", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(n)", font_size=24, color=WARNING_COLOR),
            Text("No", font_size=20, color=ACCENT_COLOR),
            Text("Newton", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(c^n)", font_size=24, color=SUCCESS_COLOR),
            Text("Si", font_size=20, color=WARNING_COLOR),
            Text("Secante", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(c^n)", font_size=24, color=SUCCESS_COLOR),
            Text("No", font_size=20, color=ACCENT_COLOR),
        )
        table.arrange_in_grid(rows=4, cols=3, buff=(0.5, 0.3))
        table.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(table, shift=UP * 0.2), run_time=1.5)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TrapezoidalRuleScene(Scene):
    def construct(self):
        title = Text("Regla del Trapecio", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)

        def f(x):
            return 0.5 * x**2 + 0.5

        a, b = 1.0, 3.0

        graph = axes.plot(f, x_range=[0.8, 3.2], color=CURVE_COLOR, stroke_width=3)

        area_points = [
            axes.c2p(a, 0),
            axes.c2p(a, f(a)),
            axes.c2p(b, f(b)),
            axes.c2p(b, 0),
        ]
        area_polygon = Polygon(*area_points, color=ACCENT_COLOR, fill_opacity=0.3, stroke_width=0)

        trapezoid = Polygon(
            axes.c2p(a, 0),
            axes.c2p(a, f(a)),
            axes.c2p(b, f(b)),
            axes.c2p(b, 0),
            color=HIGHLIGHT_COLOR,
            stroke_width=3,
            fill_opacity=0,
        )

        self.play(Write(title), run_time=1)
        self.play(Create(axes), Create(graph), run_time=1)
        self.play(FadeIn(area_polygon), Create(trapezoid), run_time=1)

        labels = VGroup(
            MathTex(r"a", font_size=28, color=WARNING_COLOR).next_to(axes.c2p(a, 0), DOWN, buff=0.1),
            MathTex(r"b", font_size=28, color=WARNING_COLOR).next_to(axes.c2p(b, 0), DOWN, buff=0.1),
        )
        self.play(FadeIn(labels), run_time=0.6)

        formula = MathTex(
            r"\int_a^b f(x)dx \approx \frac{b-a}{2}(f(a)+f(b))",
            font_size=30,
            color=ACCENT_COLOR,
        ).to_edge(RIGHT, buff=0.6).shift(UP * 1.2)

        self.play(FadeIn(formula, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SimpsonRuleScene(Scene):
    def construct(self):
        title = Text("Regla de Simpson (1/3)", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 3, 1],
            x_length=5.0,
            y_length=3.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)

        def f(x):
            return 0.4 * (x - 1.5)**2 + 0.8

        a, b = 0.5, 3.5
        c = (a + b) / 2

        graph = axes.plot(f, x_range=[0.3, 3.7], color=CURVE_COLOR, stroke_width=3)

        parabola_approx = axes.plot(
            lambda x: f(a) + (f(b) - f(a)) / (b - a) * (x - a) + 
                     ((f(c) - f(a)) / (c - a) - (f(b) - f(a)) / (b - a)) / (c - a) * (x - a) * (x - c),
            x_range=[a, b],
            color=ITER_COLOR,
            stroke_width=2,
        )

        self.play(Write(title), run_time=1)
        self.play(Create(axes), Create(graph), run_time=1)
        self.play(Create(parabola_approx), run_time=0.8)

        points = VGroup(
            Dot(axes.c2p(a, f(a)), color=WARNING_COLOR),
            Dot(axes.c2p(c, f(c)), color=HIGHLIGHT_COLOR),
            Dot(axes.c2p(b, f(b)), color=WARNING_COLOR),
        )
        self.play(FadeIn(points), run_time=0.6)

        formula = MathTex(
            r"\int_a^b f(x)dx \approx \frac{b-a}{6}[f(a)+4f(c)+f(b)]",
            font_size=28,
            color=ACCENT_COLOR,
        ).to_edge(RIGHT, buff=0.6).shift(UP * 1.0)

        self.play(FadeIn(formula, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EulerMethodScene(Scene):
    def construct(self):
        title = Text("Metodo de Euler (EDOs)", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        subtitle = Text("y' = f(t, y)", font_size=26, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 4, 1],
            x_length=5.5,
            y_length=4.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
            x_axis_config={"label": "t"},
            y_axis_config={"label": "y"},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)

        def f(t, y):
            return 0.5 * y

        exact = axes.plot(lambda t: 2 * np.exp(0.5 * t), x_range=[0, 4.5], color=SECONDARY_COLOR, stroke_width=3)

        t0, y0 = 0.0, 2.0
        h = 0.5
        steps = 8

        points = [(t0, y0)]
        for _ in range(steps):
            t, y = points[-1]
            y_new = y + h * f(t, y)
            t_new = t + h
            points.append((t_new, y_new))

        euler_path = VGroup()
        for i in range(len(points) - 1):
            seg = Line(
                axes.c2p(points[i][0], points[i][1]),
                axes.c2p(points[i + 1][0], points[i + 1][1]),
                color=HIGHLIGHT_COLOR,
                stroke_width=3,
            )
            euler_path.add(seg)

        euler_dots = VGroup(*[
            Dot(axes.c2p(p[0], p[1]), color=HIGHLIGHT_COLOR)
            for p in points
        ])

        self.play(Write(title), FadeIn(subtitle), run_time=1)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(exact), run_time=0.8)
        self.play(Create(euler_path), FadeIn(euler_dots), run_time=1)

        formula = MathTex(
            r"y_{n+1} = y_n + h \cdot f(t_n, y_n)",
            font_size=30,
            color=ACCENT_COLOR,
        ).to_edge(RIGHT, buff=0.6).shift(UP * 1.5)

        error_note = Text("Diferencia con solucion exacta", font_size=20, color=WARNING_COLOR)
        error_note.next_to(formula, DOWN, buff=0.3)

        self.play(FadeIn(formula, shift=RIGHT * 0.2), FadeIn(error_note), run_time=1)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class InterpolationScene(Scene):
    def construct(self):
        title = Text("Interpolacion de Lagrange", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=5.5,
            y_length=4.0,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)

        data_points = [(1, 1), (2, 2.5), (4, 3), (5, 4)]

        dots = VGroup(*[
            Dot(axes.c2p(p[0], p[1]), color=WARNING_COLOR)
            for p in data_points
        ])

        def lagrange_poly(x):
            result = 0
            for i, (xi, yi) in enumerate(data_points):
                term = yi
                for j, (xj, _) in enumerate(data_points):
                    if i != j:
                        term *= (x - xj) / (xi - xj)
                result += term
            return result

        interp_curve = axes.plot(lagrange_poly, x_range=[0.5, 5.5], color=ITER_COLOR, stroke_width=3)

        self.play(Write(title), run_time=1)
        self.play(Create(axes), run_time=0.8)
        self.play(FadeIn(dots), run_time=0.6)
        self.play(Create(interp_curve), run_time=1)

        formula = MathTex(
            r"P(x) = \sum_{i=0}^n y_i L_i(x), \quad L_i(x) = \prod_{j \neq i}\frac{x-x_j}{x_i-x_j}",
            font_size=22,
            color=ACCENT_COLOR,
        ).to_edge(RIGHT, buff=0.6).shift(UP * 1.0)

        self.play(FadeIn(formula, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen de metodos numericos", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Biseccion: seguro pero lento", font_size=26, color=TEXT_COLOR),
            Text("Newton-Raphson: rapido, requiere derivada", font_size=26, color=TEXT_COLOR),
            Text("Secante: rapido sin derivada", font_size=26, color=TEXT_COLOR),
            Text("Trapecio/Simpson: integracion numerica", font_size=26, color=TEXT_COLOR),
            Text("Euler: resolver EDOs basico", font_size=26, color=TEXT_COLOR),
            Text("Lagrange: interpolar datos discretos", font_size=26, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.2)

        final_msg = Text(
            "Esenciales en ingenieria y ciencia computacional",
            font_size=28,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.6)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class NumericalMethodsFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        WhyNumericalScene.construct(self)
        BisectionMethodScene.construct(self)
        NewtonRaphsonScene.construct(self)
        SecantMethodScene.construct(self)
        ComparisonScene.construct(self)
        TrapezoidalRuleScene.construct(self)
        SimpsonRuleScene.construct(self)
        EulerMethodScene.construct(self)
        InterpolationScene.construct(self)
        ConclusionScene.construct(self)
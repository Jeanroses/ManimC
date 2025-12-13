from manim import *
import numpy as np
import random

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
REGION_COLOR = "#74c7ec"
TEXT_COLOR = "#cdd6f4"
FORMULA_COLOR = "#fab387"
PIVOT_COLOR = "#cba6f7"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        particles = VGroup()
        for _ in range(20):
            p = Dot(
                point=np.array([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0]),
                radius=0.03,
                color=random.choice([PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR]),
                fill_opacity=0.5
            )
            particles.add(p)
        
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in particles], lag_ratio=0.05), run_time=1.5)
        
        title = Text(
            "Teorema de Green",
            font_size=72,
            color=PRIMARY_COLOR,
            weight=BOLD
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR)
        title.shift(UP * 1.5)
        
        self.play(Write(title, run_time=2.5))
        self.wait(0.3)
        
        subtitle = Text(
            "Conectando integrales de línea con integrales dobles",
            font_size=30,
            color=TEXT_COLOR
        ).next_to(title, DOWN, buff=0.6)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=1)
        self.wait(0.5)
        
        formula = MathTex(
            r"\oint_C", r"\vec{F}", r"\cdot", r"d\vec{r}",
            r"=", r"\iint_D", 
            r"\left(", r"\frac{\partial Q}{\partial x}", r"-", 
            r"\frac{\partial P}{\partial y}", r"\right)", r"dA",
            font_size=42
        ).next_to(subtitle, DOWN, buff=0.7)
        
        formula[0].set_color(CURVE_COLOR)
        formula[1:4].set_color(ACCENT_COLOR)
        formula[5].set_color(REGION_COLOR)
        formula[7].set_color(SECONDARY_COLOR)
        formula[9].set_color(PRIMARY_COLOR)
        
        self.play(Write(formula), run_time=2)
        self.wait(0.3)
        
        self.play(formula.animate.scale(1.05), rate_func=there_and_back, run_time=0.8)
        self.wait(0.5)
        
        curve = Circle(radius=0.6, color=CURVE_COLOR, stroke_width=3)
        curve.next_to(formula, DOWN, buff=0.5)
        
        arrow = Arrow(
            curve.point_from_proportion(0.1),
            curve.point_from_proportion(0.15),
            color=HIGHLIGHT_COLOR, buff=0, stroke_width=3
        )
        
        self.play(Create(curve), run_time=0.8)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.wait(0.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
        self.wait(0.2)


class DefinitionScene(Scene):
    def construct(self):
        title = Text("Definición del Teorema", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        underline = Line(LEFT * 3, RIGHT * 3, color=PRIMARY_COLOR, stroke_width=2)
        underline.next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title), Create(underline), run_time=1.5)
        self.wait(0.5)
        
        def_box = RoundedRectangle(
            width=12, height=2.5, corner_radius=0.2,
            color=TEXT_COLOR, stroke_width=1, fill_opacity=0.05
        ).next_to(underline, DOWN, buff=0.6)
        
        definition = VGroup(
            Text("Sea C una curva cerrada, simple, suave a trozos,", font_size=24, color=TEXT_COLOR),
            Text("orientada positivamente (sentido antihorario),", font_size=24, color=TEXT_COLOR),
            Text("que encierra una región D en el plano ℝ².", font_size=24, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.2)
        definition.move_to(def_box.get_center())
        
        self.play(Create(def_box), run_time=0.8)
        for line in definition:
            self.play(Write(line), run_time=1)
            self.wait(0.3)
        
        self.wait(0.5)
        
        conditions_title = Text("Condiciones:", font_size=26, color=HIGHLIGHT_COLOR)
        conditions_title.next_to(def_box, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        conditions = VGroup(
            MathTex(r"\bullet \; P(x,y), Q(x,y) \text{ continuas en } D", font_size=24, color=TEXT_COLOR),
            MathTex(r"\bullet \; \frac{\partial P}{\partial y}, \frac{\partial Q}{\partial x} \text{ continuas en } D", font_size=24, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        conditions.next_to(conditions_title, DOWN, buff=0.3).align_to(conditions_title, LEFT)
        
        self.play(Write(conditions_title), run_time=0.6)
        self.play(Write(conditions), run_time=1.5)
        self.wait(0.5)
        
        formula_title = Text("Entonces:", font_size=24, color=ACCENT_COLOR)
        formula_title.next_to(conditions, DOWN, buff=0.3).align_to(conditions_title, LEFT)
        
        main_formula = MathTex(
            r"\oint_C", r"(P \, dx + Q \, dy)", r"=", 
            r"\iint_D", r"\left(", r"\frac{\partial Q}{\partial x}", 
            r"-", r"\frac{\partial P}{\partial y}", r"\right)", r"dA",
            font_size=32
        ).next_to(formula_title, RIGHT, buff=0.3)
        
        main_formula[0].set_color(CURVE_COLOR)
        main_formula[1].set_color(ACCENT_COLOR)
        main_formula[3].set_color(REGION_COLOR)
        main_formula[5].set_color(SECONDARY_COLOR)
        main_formula[7].set_color(PRIMARY_COLOR)
        
        box = SurroundingRectangle(main_formula, color=FORMULA_COLOR, buff=0.2, stroke_width=2)
        
        self.play(Write(formula_title), run_time=0.5)
        self.play(Write(main_formula), run_time=2.5)
        self.play(Create(box), run_time=0.8)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class GeometricIntuitionScene(Scene):
    def construct(self):
        title = Text("Intuición Geométrica", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.2)
        
        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=9, y_length=6,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
            tips=True
        ).shift(DOWN * 0.3)
        
        x_label = MathTex("x", font_size=28, color=TEXT_COLOR).next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y", font_size=28, color=TEXT_COLOR).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.5)
        
        region = Ellipse(width=5, height=3.5, color=REGION_COLOR, fill_opacity=0.2, stroke_width=0)
        region.shift(DOWN * 0.3)
        
        self.play(FadeIn(region), run_time=1)
        
        d_label = MathTex("D", font_size=44, color=REGION_COLOR).move_to(region.get_center())
        self.play(FadeIn(d_label), run_time=0.6)
        self.wait(0.5)
        
        curve = Ellipse(width=5, height=3.5, color=CURVE_COLOR, stroke_width=5)
        curve.shift(DOWN * 0.3)
        
        self.play(Create(curve), run_time=2)
        
        c_label = MathTex("C", font_size=36, color=CURVE_COLOR)
        c_label.next_to(curve, RIGHT, buff=0.2).shift(UP * 0.5)
        self.play(FadeIn(c_label), run_time=0.5)
        
        arrows = VGroup()
        for t in [0.1, 0.35, 0.6, 0.85]:
            p1 = curve.point_from_proportion(t)
            p2 = curve.point_from_proportion(t + 0.03)
            arr = Arrow(p1, p2, color=HIGHLIGHT_COLOR, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.5)
            arrows.add(arr)
        
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), run_time=1.2)
        self.wait(0.5)
        
        vectors = VGroup()
        for i in np.linspace(-1.8, 1.8, 5):
            for j in np.linspace(-1.2, 1.2, 4):
                pos = axes.c2p(i, j)
                dx, dy = -j * 0.15, i * 0.15
                vec = Arrow(
                    pos, pos + np.array([dx, dy, 0]),
                    color=ACCENT_COLOR, stroke_width=2, buff=0,
                    max_tip_length_to_length_ratio=0.4
                )
                vectors.add(vec)
        
        field_label = MathTex(r"\vec{F}(x,y) = (-y, x)", font_size=26, color=ACCENT_COLOR)
        field_label.to_edge(RIGHT, buff=0.4).shift(UP * 2)
        
        self.play(
            LaggedStart(*[GrowArrow(v) for v in vectors], lag_ratio=0.02),
            FadeIn(field_label),
            run_time=2
        )
        self.wait(1)
        
        explanation = VGroup(
            Text("Integral de línea sobre C", font_size=24, color=CURVE_COLOR),
            MathTex("=", font_size=30, color=TEXT_COLOR),
            Text("Integral doble sobre D", font_size=24, color=REGION_COLOR)
        ).arrange(RIGHT, buff=0.3).to_edge(DOWN, buff=0.3)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class FormulaBreakdownScene(Scene):
    def construct(self):
        title = Text("Análisis de la Fórmula", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.2)
        
        formula = MathTex(
            r"\oint_C", r"(P \, dx + Q \, dy)", r"=",
            r"\iint_D", r"\left(", r"\frac{\partial Q}{\partial x}",
            r"-", r"\frac{\partial P}{\partial y}", r"\right)", r"dA",
            font_size=42
        ).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(formula), run_time=2)
        self.wait(0.5)
        
        left_brace = Brace(formula[:2], DOWN, color=CURVE_COLOR)
        left_label = Text("Integral de Línea", font_size=22, color=CURVE_COLOR)
        left_label.next_to(left_brace, DOWN, buff=0.1)
        
        left_details = VGroup(
            MathTex(r"\oint_C = \text{integral cerrada sobre } C", font_size=20, color=TEXT_COLOR),
            MathTex(r"P\,dx + Q\,dy = \vec{F} \cdot d\vec{r}", font_size=20, color=TEXT_COLOR),
            MathTex(r"\vec{F} = (P, Q) \text{ es el campo vectorial}", font_size=20, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        left_details.to_edge(LEFT, buff=0.5).shift(DOWN * 1.5)
        
        self.play(
            GrowFromCenter(left_brace),
            FadeIn(left_label),
            formula[:2].animate.set_color(CURVE_COLOR),
            run_time=1
        )
        self.play(Write(left_details), run_time=1.5)
        self.wait(1)
        
        right_brace = Brace(formula[3:], DOWN, color=REGION_COLOR)
        right_label = Text("Integral Doble", font_size=22, color=REGION_COLOR)
        right_label.next_to(right_brace, DOWN, buff=0.1)
        
        right_details = VGroup(
            MathTex(r"\iint_D = \text{integral sobre la región } D", font_size=20, color=TEXT_COLOR),
            MathTex(r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = \text{rot}_z \vec{F}", font_size=20, color=TEXT_COLOR),
            MathTex(r"dA = dx\,dy \text{ (elemento de área)}", font_size=20, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        right_details.to_edge(RIGHT, buff=0.5).shift(DOWN * 1.5)
        
        self.play(
            GrowFromCenter(right_brace),
            FadeIn(right_label),
            formula[3:].animate.set_color(REGION_COLOR),
            run_time=1
        )
        self.play(Write(right_details), run_time=1.5)
        self.wait(1.5)
        
        key_concept = VGroup(
            Text("Concepto clave:", font_size=24, color=HIGHLIGHT_COLOR),
            MathTex(r"\text{rot}_z \vec{F} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}", 
                   font_size=28, color=FORMULA_COLOR)
        ).arrange(RIGHT, buff=0.3).to_edge(DOWN, buff=0.3)
        
        box = SurroundingRectangle(key_concept, color=HIGHLIGHT_COLOR, buff=0.15)
        
        self.play(FadeIn(key_concept), Create(box), run_time=1)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class TheoremFormsScene(Scene):
    def construct(self):
        title = Text("Formas del Teorema de Green", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.2)
        
        form1_box = RoundedRectangle(
            width=6.5, height=3, corner_radius=0.15,
            color=CURVE_COLOR, stroke_width=2, fill_opacity=0.05
        )
        form1_title = Text("Forma de Circulación", font_size=26, color=CURVE_COLOR)
        form1_formula = MathTex(
            r"\oint_C \vec{F} \cdot d\vec{r} = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA",
            font_size=22
        )
        form1_meaning = Text("Mide la rotación del campo", font_size=18, color=TEXT_COLOR)
        form1_app = MathTex(r"\text{Trabajo} = \oint_C \vec{F} \cdot d\vec{r}", font_size=20, color=ACCENT_COLOR)
        
        form1_content = VGroup(form1_title, form1_formula, form1_meaning, form1_app).arrange(DOWN, buff=0.2)
        form1_content.move_to(form1_box.get_center())
        form1_group = VGroup(form1_box, form1_content)
        
        form2_box = RoundedRectangle(
            width=6.5, height=3, corner_radius=0.15,
            color=REGION_COLOR, stroke_width=2, fill_opacity=0.05
        )
        form2_title = Text("Forma de Flujo", font_size=26, color=REGION_COLOR)
        form2_formula = MathTex(
            r"\oint_C \vec{F} \cdot \vec{n}\,ds = \iint_D \left(\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}\right) dA",
            font_size=22
        )
        form2_meaning = Text("Mide la divergencia del campo", font_size=18, color=TEXT_COLOR)
        form2_app = MathTex(r"\text{div}\,\vec{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}", font_size=20, color=ACCENT_COLOR)
        
        form2_content = VGroup(form2_title, form2_formula, form2_meaning, form2_app).arrange(DOWN, buff=0.2)
        form2_content.move_to(form2_box.get_center())
        form2_group = VGroup(form2_box, form2_content)
        
        forms = VGroup(form1_group, form2_group).arrange(RIGHT, buff=0.5)
        forms.next_to(title, DOWN, buff=0.6)
        
        self.play(Create(form1_box), run_time=0.6)
        self.play(FadeIn(form1_content), run_time=1.5)
        self.wait(1)
        
        self.play(Create(form2_box), run_time=0.6)
        self.play(FadeIn(form2_content), run_time=1.5)
        self.wait(1)
        
        relation = VGroup(
            Text("Vector tangente:", font_size=20, color=CURVE_COLOR),
            MathTex(r"d\vec{r} = (dx, dy)", font_size=22),
            Text("  |  ", font_size=20, color=TEXT_COLOR),
            Text("Vector normal:", font_size=20, color=REGION_COLOR),
            MathTex(r"\vec{n}\,ds = (dy, -dx)", font_size=22)
        ).arrange(RIGHT, buff=0.2).to_edge(DOWN, buff=0.4)
        
        self.play(FadeIn(relation), run_time=1)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class Exercise1Scene(Scene):
    def construct(self):
        title = Text("Ejercicio 1: Integral Básica", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)
        
        problem = VGroup(
            Text("Calcular usando el Teorema de Green:", font_size=24, color=TEXT_COLOR),
            MathTex(r"\oint_C (2xy\,dx + 3x^2\,dy)", font_size=36, color=FORMULA_COLOR),
            Text("donde C es el cuadrado con vértices (0,0), (1,0), (1,1), (0,1)", font_size=20, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.3)
        problem.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(problem), run_time=1.5)
        self.wait(1)
        
        axes = Axes(
            x_range=[-0.5, 2, 0.5], y_range=[-0.5, 1.5, 0.5],
            x_length=3.5, y_length=2.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 1}
        ).to_edge(RIGHT, buff=0.3).shift(UP * 1.5)
        
        square = Polygon(
            axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(1, 1), axes.c2p(0, 1),
            color=CURVE_COLOR, stroke_width=3, fill_color=REGION_COLOR, fill_opacity=0.2
        )
        
        c_label = MathTex("C", font_size=24, color=CURVE_COLOR).next_to(square, UP, buff=0.1)
        d_label = MathTex("D", font_size=24, color=REGION_COLOR).move_to(square.get_center())
        
        self.play(Create(axes), run_time=0.8)
        self.play(Create(square), FadeIn(c_label), FadeIn(d_label), run_time=1)
        
        solution = VGroup(
            Text("Solución:", font_size=24, color=HIGHLIGHT_COLOR),
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)
        
        self.play(Write(solution), run_time=0.5)
        
        step1 = MathTex(r"P = 2xy, \quad Q = 3x^2", font_size=24).next_to(solution, DOWN, buff=0.3).align_to(solution, LEFT)
        self.play(Write(step1), run_time=1)
        self.wait(0.5)
        
        step2 = MathTex(r"\frac{\partial Q}{\partial x} = 6x, \quad \frac{\partial P}{\partial y} = 2x", font_size=24)
        step2.next_to(step1, DOWN, buff=0.25).align_to(step1, LEFT)
        self.play(Write(step2), run_time=1)
        self.wait(0.5)
        
        step3 = MathTex(r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 6x - 2x = 4x", font_size=24, color=ACCENT_COLOR)
        step3.next_to(step2, DOWN, buff=0.25).align_to(step2, LEFT)
        self.play(Write(step3), run_time=1)
        self.wait(0.5)
        
        step4 = MathTex(r"\iint_D 4x\,dA = \int_0^1 \int_0^1 4x\,dx\,dy", font_size=24)
        step4.next_to(step3, DOWN, buff=0.25).align_to(step3, LEFT)
        self.play(Write(step4), run_time=1)
        self.wait(0.5)
        
        step5 = MathTex(r"= \int_0^1 \left[2x^2\right]_0^1 dy = \int_0^1 2\,dy = 2", font_size=24)
        step5.next_to(step4, DOWN, buff=0.25).align_to(step4, LEFT)
        self.play(Write(step5), run_time=1.2)
        
        result = MathTex(r"\boxed{\oint_C (2xy\,dx + 3x^2\,dy) = 2}", font_size=30, color=ACCENT_COLOR)
        result.to_edge(DOWN, buff=0.4)
        
        self.play(Write(result), run_time=1)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class Exercise2Scene(Scene):
    def construct(self):
        title = Text("Ejercicio 2: Cálculo de Área", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)
        
        area_formula = VGroup(
            Text("Fórmula de área con Green:", font_size=24, color=HIGHLIGHT_COLOR),
            MathTex(r"A = \frac{1}{2}\oint_C (x\,dy - y\,dx)", font_size=32, color=FORMULA_COLOR)
        ).arrange(DOWN, buff=0.2)
        area_formula.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(area_formula), run_time=1.2)
        self.wait(0.8)
        
        problem = VGroup(
            Text("Calcular el área de la elipse:", font_size=24, color=TEXT_COLOR),
            MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1", font_size=32, color=CURVE_COLOR)
        ).arrange(DOWN, buff=0.2)
        problem.next_to(area_formula, DOWN, buff=0.6)
        
        self.play(FadeIn(problem), run_time=1)
        
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 2, 1],
            x_length=5, y_length=3.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 1}
        ).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.5)
        
        ellipse = Ellipse(width=4, height=2.5, color=CURVE_COLOR, stroke_width=3, fill_color=REGION_COLOR, fill_opacity=0.2)
        ellipse.move_to(axes.c2p(0, 0))
        
        a_label = MathTex("a", font_size=22, color=HIGHLIGHT_COLOR).next_to(ellipse, RIGHT, buff=0.1)
        b_label = MathTex("b", font_size=22, color=HIGHLIGHT_COLOR).next_to(ellipse, UP, buff=0.1)
        
        self.play(Create(axes), Create(ellipse), FadeIn(a_label), FadeIn(b_label), run_time=1.5)
        
        solution = VGroup(
            Text("Solución:", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"x = a\cos t, \quad y = b\sin t, \quad t \in [0, 2\pi]", font_size=20),
            MathTex(r"dx = -a\sin t\,dt, \quad dy = b\cos t\,dt", font_size=20),
            MathTex(r"A = \frac{1}{2}\int_0^{2\pi} (ab\cos^2 t + ab\sin^2 t)\,dt", font_size=20, color=ACCENT_COLOR),
            MathTex(r"= \frac{ab}{2}\int_0^{2\pi} dt = \frac{ab}{2} \cdot 2\pi", font_size=20),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        solution.to_edge(LEFT, buff=0.5).shift(DOWN * 1)
        
        for s in solution:
            self.play(Write(s), run_time=0.9)
            self.wait(0.3)
        
        result = MathTex(r"\boxed{A = \pi a b}", font_size=40, color=ACCENT_COLOR)
        result.to_edge(DOWN, buff=0.4)
        
        self.play(Write(result), run_time=1)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class Exercise3Scene(Scene):
    def construct(self):
        title = Text("Ejercicio 3: Campo Complejo", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)
        
        problem = VGroup(
            Text("Evaluar:", font_size=24, color=TEXT_COLOR),
            MathTex(r"\oint_C (e^x + y^2)\,dx + (e^y + x^2)\,dy", font_size=32, color=FORMULA_COLOR),
            Text("C: triángulo con vértices (0,0), (2,0), (0,2)", font_size=20, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25)
        problem.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(problem), run_time=1.2)
        self.wait(0.8)
        
        axes = Axes(
            x_range=[-0.5, 3, 1], y_range=[-0.5, 2.5, 1],
            x_length=3.5, y_length=2.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 1}
        ).to_edge(RIGHT, buff=0.3).shift(UP * 1.5)
        
        triangle = Polygon(
            axes.c2p(0, 0), axes.c2p(2, 0), axes.c2p(0, 2),
            color=CURVE_COLOR, stroke_width=3, fill_color=REGION_COLOR, fill_opacity=0.2
        )
        
        vertices = VGroup(
            Dot(axes.c2p(0, 0), color=HIGHLIGHT_COLOR),
            Dot(axes.c2p(2, 0), color=HIGHLIGHT_COLOR),
            Dot(axes.c2p(0, 2), color=HIGHLIGHT_COLOR)
        )
        
        self.play(Create(axes), Create(triangle), FadeIn(vertices), run_time=1.2)
        
        steps = VGroup(
            Text("Solución:", font_size=22, color=HIGHLIGHT_COLOR),
            MathTex(r"P = e^x + y^2, \quad Q = e^y + x^2", font_size=22),
            MathTex(r"\frac{\partial Q}{\partial x} = 2x, \quad \frac{\partial P}{\partial y} = 2y", font_size=22),
            MathTex(r"\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 2x - 2y = 2(x-y)", font_size=22, color=ACCENT_COLOR),
            MathTex(r"\iint_D 2(x-y)\,dA = \int_0^2\int_0^{2-x} 2(x-y)\,dy\,dx", font_size=20),
            MathTex(r"= \int_0^2 \left[2xy - y^2\right]_0^{2-x} dx", font_size=20),
            MathTex(r"= \int_0^2 (2x(2-x) - (2-x)^2)\,dx", font_size=20),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        steps.to_edge(LEFT, buff=0.4).shift(DOWN * 0.8)
        
        for s in steps:
            self.play(Write(s), run_time=0.8)
            self.wait(0.2)
        
        result = MathTex(r"\boxed{= -\frac{4}{3}}", font_size=36, color=ACCENT_COLOR)
        result.to_edge(DOWN, buff=0.3)
        
        self.play(Write(result), run_time=1)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)


class ApplicationsScene(Scene):
    def construct(self):
        title = Text("Aplicaciones del Teorema de Green", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.2)
        
        apps = VGroup(
            self.create_app("📐", "Cálculo de Áreas", 
                r"A = \frac{1}{2}\oint_C (x\,dy - y\,dx) = \oint_C x\,dy = -\oint_C y\,dx",
                HIGHLIGHT_COLOR),
            self.create_app("⚡", "Trabajo Mecánico",
                r"W = \oint_C \vec{F}\cdot d\vec{r} = \iint_D (\nabla \times \vec{F})_z\,dA",
                CURVE_COLOR),
            self.create_app("💧", "Dinámica de Fluidos",
                r"\text{Flujo} = \oint_C \vec{v}\cdot\vec{n}\,ds = \iint_D \nabla\cdot\vec{v}\,dA",
                REGION_COLOR),
            self.create_app("🔬", "Electromagnetismo",
                r"\oint_C \vec{E}\cdot d\vec{l} = -\frac{d\Phi_B}{dt} \quad \text{(Ley de Faraday)}",
                SECONDARY_COLOR),
            self.create_app("🌡️", "Transferencia de Calor",
                r"\oint_C (-k\nabla T)\cdot\vec{n}\,ds = \iint_D Q\,dA",
                FORMULA_COLOR)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        apps.next_to(title, DOWN, buff=0.5)
        
        for app in apps:
            self.play(FadeIn(app, shift=RIGHT * 0.2), run_time=0.9)
            self.wait(0.5)
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)
    
    def create_app(self, icon, title_text, formula_str, color):
        icon_mob = Text(icon, font_size=28)
        title = Text(title_text, font_size=22, color=color)
        formula = MathTex(formula_str, font_size=20, color=TEXT_COLOR)
        header = VGroup(icon_mob, title).arrange(RIGHT, buff=0.2)
        return VGroup(header, formula).arrange(DOWN, buff=0.1, aligned_edge=LEFT)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen del Teorema de Green", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.2)
        
        points = VGroup(
            self.create_point("✓", "Conecta integrales de línea ↔ integrales dobles", CURVE_COLOR),
            self.create_point("✓", "Requiere: curva cerrada, simple, orientada +", TEXT_COLOR),
            self.create_point("✓", "Dos formas: Circulación (rot) y Flujo (div)", SECONDARY_COLOR),
            self.create_point("✓", "Generalización: Teoremas de Stokes y Gauss", ACCENT_COLOR),
            self.create_point("✓", "Aplicaciones: física, ingeniería, matemáticas", HIGHLIGHT_COLOR)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        points.next_to(title, DOWN, buff=0.6)
        
        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.7)
            self.wait(0.3)
        
        self.wait(1)
        
        final_box = RoundedRectangle(
            width=10, height=1.5, corner_radius=0.15,
            color=FORMULA_COLOR, stroke_width=2, fill_opacity=0.1
        )
        final_formula = MathTex(
            r"\oint_C (P\,dx + Q\,dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA",
            font_size=34, color=FORMULA_COLOR
        )
        final_group = VGroup(final_box, final_formula)
        final_formula.move_to(final_box.get_center())
        final_group.next_to(points, DOWN, buff=0.6)
        
        self.play(Create(final_box), Write(final_formula), run_time=1.5)
        self.wait(1.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        
        thanks = Text(
            "¡Gracias por ver!",
            font_size=64, color=PRIMARY_COLOR
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR)
        
        self.play(Write(thanks), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(thanks), run_time=1.2)
    
    def create_point(self, icon, text, color):
        icon_mob = Text(icon, font_size=26, color=color)
        text_mob = Text(text, font_size=22, color=TEXT_COLOR)
        return VGroup(icon_mob, text_mob).arrange(RIGHT, buff=0.2)


class GreensTheoremFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        DefinitionScene.construct(self)
        GeometricIntuitionScene.construct(self)
        FormulaBreakdownScene.construct(self)
        TheoremFormsScene.construct(self)
        Exercise1Scene.construct(self)
        Exercise2Scene.construct(self)
        Exercise3Scene.construct(self)
        self.play_applications()
        self.play_conclusion()
    
    def play_applications(self):
        title = Text("Aplicaciones del Teorema de Green", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1.2)
        
        apps = VGroup(
            self.create_app("📐", "Cálculo de Áreas", 
                r"A = \frac{1}{2}\oint_C (x\,dy - y\,dx) = \oint_C x\,dy = -\oint_C y\,dx",
                HIGHLIGHT_COLOR),
            self.create_app("⚡", "Trabajo Mecánico",
                r"W = \oint_C \vec{F}\cdot d\vec{r} = \iint_D (\nabla \times \vec{F})_z\,dA",
                CURVE_COLOR),
            self.create_app("💧", "Dinámica de Fluidos",
                r"\text{Flujo} = \oint_C \vec{v}\cdot\vec{n}\,ds = \iint_D \nabla\cdot\vec{v}\,dA",
                REGION_COLOR),
            self.create_app("🔬", "Electromagnetismo",
                r"\oint_C \vec{E}\cdot d\vec{l} = -\frac{d\Phi_B}{dt} \quad \text{(Ley de Faraday)}",
                SECONDARY_COLOR),
            self.create_app("🌡️", "Transferencia de Calor",
                r"\oint_C (-k\nabla T)\cdot\vec{n}\,ds = \iint_D Q\,dA",
                FORMULA_COLOR)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        apps.next_to(title, DOWN, buff=0.5)
        
        for app in apps:
            self.play(FadeIn(app, shift=RIGHT * 0.2), run_time=0.9)
            self.wait(0.5)
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        self.wait(0.3)
    
    def play_conclusion(self):
        title = Text("Resumen del Teorema de Green", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.2)
        
        points = VGroup(
            self.create_point("✓", "Conecta integrales de línea ↔ integrales dobles", CURVE_COLOR),
            self.create_point("✓", "Requiere: curva cerrada, simple, orientada +", TEXT_COLOR),
            self.create_point("✓", "Dos formas: Circulación (rot) y Flujo (div)", SECONDARY_COLOR),
            self.create_point("✓", "Generalización: Teoremas de Stokes y Gauss", ACCENT_COLOR),
            self.create_point("✓", "Aplicaciones: física, ingeniería, matemáticas", HIGHLIGHT_COLOR)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        points.next_to(title, DOWN, buff=0.6)
        
        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.7)
            self.wait(0.3)
        
        self.wait(1)
        
        final_box = RoundedRectangle(
            width=10, height=1.5, corner_radius=0.15,
            color=FORMULA_COLOR, stroke_width=2, fill_opacity=0.1
        )
        final_formula = MathTex(
            r"\oint_C (P\,dx + Q\,dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA",
            font_size=34, color=FORMULA_COLOR
        )
        final_formula.move_to(final_box.get_center())
        final_group = VGroup(final_box, final_formula)
        final_group.next_to(points, DOWN, buff=0.6)
        
        self.play(Create(final_box), Write(final_formula), run_time=1.5)
        self.wait(1.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        
        thanks = Text(
            "¡Gracias por ver!",
            font_size=64, color=PRIMARY_COLOR
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR)
        
        self.play(Write(thanks), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(thanks), run_time=1.2)
    
    def create_app(self, icon, title_text, formula_str, color):
        icon_mob = Text(icon, font_size=28)
        title = Text(title_text, font_size=22, color=color)
        formula = MathTex(formula_str, font_size=20, color=TEXT_COLOR)
        header = VGroup(icon_mob, title).arrange(RIGHT, buff=0.2)
        return VGroup(header, formula).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
    
    def create_point(self, icon, text, color):
        icon_mob = Text(icon, font_size=26, color=color)
        text_mob = Text(text, font_size=22, color=TEXT_COLOR)
        return VGroup(icon_mob, text_mob).arrange(RIGHT, buff=0.2)

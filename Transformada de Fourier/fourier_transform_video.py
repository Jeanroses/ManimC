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
            "Transformada de Fourier",
            font_size=52,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)

        subtitle = Text(
            "Descomponer senales en frecuencias",
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


class WhyFourierScene(Scene):
    def construct(self):
        title = Text("Por que Fourier?", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        idea = Text("Toda senal periodica puede representarse como suma de senos y cosenos", font_size=26, color=TEXT_COLOR, line_spacing=1.3)
        idea.next_to(title, DOWN, buff=0.7)

        components = VGroup(
            MathTex(r"f(t) = a_0 + \sum_{n=1}^\infty a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)", font_size=28, color=HIGHLIGHT_COLOR),
        ).arrange(DOWN, buff=0.4)
        components.next_to(idea, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(idea, shift=UP * 0.2), run_time=1)
        self.play(Write(components[0]), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ContinuousFTScene(Scene):
    def construct(self):
        title = Text("Transformada de Fourier continua", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        forward = VGroup(
            Text("Transformada directa:", font_size=24, color=SECONDARY_COLOR),
            MathTex(r"F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} \, dt", font_size=32, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.15)
        forward.next_to(title, DOWN, buff=0.6)

        inverse = VGroup(
            Text("Transformada inversa:", font_size=24, color=SECONDARY_COLOR),
            MathTex(r"f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega) e^{i\omega t} \, d\omega", font_size=32, color=HIGHLIGHT_COLOR),
        ).arrange(DOWN, buff=0.15)
        inverse.next_to(forward, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(forward, shift=UP * 0.2), run_time=1)
        self.play(FadeIn(inverse, shift=UP * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FrequencyDomainScene(Scene):
    def construct(self):
        title = Text("Dominio del tiempo vs frecuencia", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        time_label = Text("Dominio del tiempo", font_size=24, color=CURVE_COLOR).to_edge(LEFT, buff=0.5).shift(UP * 1.5)
        freq_label = Text("Dominio de la frecuencia", font_size=24, color=ACCENT_COLOR).to_edge(RIGHT, buff=0.5).shift(UP * 1.5)

        time_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3.5,
            y_length=2.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)

        freq_axes = Axes(
            x_range=[0, 8, 2],
            y_range=[0, 1.5, 0.5],
            x_length=3.5,
            y_length=2.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        signal = time_axes.plot(lambda t: np.sin(2 * np.pi * 2 * t) + 0.5 * np.sin(2 * np.pi * 5 * t), x_range=[0, 4], color=CURVE_COLOR, stroke_width=2)

        spectrum = VGroup(
            Line(freq_axes.c2p(4, 0), freq_axes.c2p(4, 1.2), color=ACCENT_COLOR, stroke_width=4),
            Line(freq_axes.c2p(10, 0), freq_axes.c2p(10, 0.6), color=ACCENT_COLOR, stroke_width=4),
        )

        arrow = DoubleArrow(
            time_axes.get_right() + RIGHT * 0.3,
            freq_axes.get_left() + LEFT * 0.3,
            color=WARNING_COLOR,
            buff=0.1,
        )
        transform_label = Text("F", font_size=28, color=WARNING_COLOR).next_to(arrow, UP, buff=0.1)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(time_label), FadeIn(freq_label), run_time=0.6)
        self.play(Create(time_axes), Create(freq_axes), run_time=0.8)
        self.play(Create(signal), run_time=1)
        self.play(Create(spectrum), run_time=0.8)
        self.play(GrowArrow(arrow), FadeIn(transform_label), run_time=0.6)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FourierSeriesScene(Scene):
    def construct(self):
        title = Text("Serie de Fourier", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        formula = MathTex(
            r"f(t) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[ a_n \cos\left(\frac{2\pi n t}{T}\right) + b_n \sin\left(\frac{2\pi n t}{T}\right) \right]",
            font_size=24,
            color=HIGHLIGHT_COLOR,
        )
        formula.next_to(title, DOWN, buff=0.7)

        coeffs_title = Text("Coeficientes:", font_size=26, color=SECONDARY_COLOR)
        coeffs_title.next_to(formula, DOWN, buff=0.5)

        a0 = MathTex(r"a_n = \frac{2}{T}\int_0^T f(t)\cos\left(\frac{2\pi n t}{T}\right) dt", font_size=22, color=TEXT_COLOR)
        an = MathTex(r"b_n = \frac{2}{T}\int_0^T f(t)\sin\left(\frac{2\pi n t}{T}\right) dt", font_size=22, color=TEXT_COLOR)
        coeffs = VGroup(a0, an).arrange(DOWN, buff=0.2)
        coeffs.next_to(coeffs_title, DOWN, buff=0.2)

        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.5)
        self.play(FadeIn(coeffs_title), run_time=0.8)
        self.play(FadeIn(coeffs, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SquareWaveScene(Scene):
    def construct(self):
        title = Text("Serie de Fourier: Onda cuadrada", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=6.5,
            y_length=3.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).shift(DOWN * 0.2)

        square_wave = VGroup(
            Line(axes.c2p(0, 1), axes.c2p(0.5, 1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(0.5, 1), axes.c2p(0.5, -1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(0.5, -1), axes.c2p(1.5, -1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(1.5, -1), axes.c2p(1.5, 1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(1.5, 1), axes.c2p(2.5, 1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(2.5, 1), axes.c2p(2.5, -1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(2.5, -1), axes.c2p(3.5, -1), color=WARNING_COLOR, stroke_width=3),
            Line(axes.c2p(3.5, -1), axes.c2p(3.5, 1), color=WARNING_COLOR, stroke_width=3),
        )

        formula = MathTex(
            r"f(t) = \frac{4}{\pi}\sum_{n=1,3,5...} \frac{\sin(n\omega t)}{n}",
            font_size=30,
            color=HIGHLIGHT_COLOR,
        ).to_edge(RIGHT, buff=0.5).shift(UP * 1.5)

        self.play(Write(title), run_time=1)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(square_wave), run_time=1)
        self.play(Write(formula), run_time=1.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class Gibb PhenomenonScene(Scene):
    def construct(self):
        title = Text("Fenomeno de Gibbs", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=5.0,
            y_length=3.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)

        original = axes.plot(lambda t: 1 if 0.4 < t < 2.4 else -1, x_range=[0, 4], color=WARNING_COLOR, stroke_width=3)

        approx_5 = axes.plot(lambda t: (4/np.pi) * (np.sin(2*np.pi*t) + np.sin(6*np.pi*t)/3 + np.sin(10*np.pi*t)/5), x_range=[0, 4], color=ACCENT_COLOR, stroke_width=2)

        self.play(Write(title), run_time=1)
        self.play(Create(axes), run_time=0.8)
        self.play(Create(original), run_time=0.8)
        self.play(Create(approx_5), run_time=0.8)

        note = Text(" overshoot ~9% en los saltos", font_size=22, color=SECONDARY_COLOR)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DFTScene(Scene):
    def construct(self):
        title = Text("Transformada Discreta de Fourier (DFT)", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        formula = MathTex(
            r"X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}",
            font_size=34,
            color=HIGHLIGHT_COLOR,
        )
        formula.next_to(title, DOWN, buff=0.7)

        explanation = Text("N muestras -> N frecuencias", font_size=24, color=TEXT_COLOR)
        explanation.next_to(formula, DOWN, buff=0.5)

        note = Text("FFT: algoritmo O(N log N)", font_size=24, color=ACCENT_COLOR)
        note.next_to(explanation, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.2)
        self.play(FadeIn(explanation), run_time=0.8)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FFTVisualizationScene(Scene):
    def construct(self):
        title = Text("FFT: Fast Fourier Transform", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        complexity = VGroup(
            Text("DFT: O(N^2)", font_size=28, color=WARNING_COLOR),
            Text("FFT: O(N log N)", font_size=28, color=SUCCESS_COLOR),
        ).arrange(DOWN, buff=0.3)
        complexity.next_to(title, DOWN, buff=0.7)

        diagram_title = Text("Algoritmo divide y venceras", font_size=24, color=SECONDARY_COLOR)
        diagram_title.next_to(complexity, DOWN, buff=0.5)

        butterfly = VGroup(
            Line(LEFT * 1.5, ORIGIN, color=CURVE_COLOR, stroke_width=2),
            Line(RIGHT * 1.5, ORIGIN, color=CURVE_COLOR, stroke_width=2),
            Line(ORIGIN + UP * 0.5, ORIGIN + UP * 1.5, color=ACCENT_COLOR, stroke_width=2),
            Line(ORIGIN + DOWN * 0.5, ORIGIN + DOWN * 1.5, color=ACCENT_COLOR, stroke_width=2),
        ).scale(1.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(complexity, shift=UP * 0.2), run_time=1)
        self.play(FadeIn(diagram_title), run_time=0.8)
        self.play(Create(butterfly), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TimeFrequencyTradeoffScene(Scene):
    def construct(self):
        title = Text("Compromiso Tiempo-Frecuencia", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        explanation = Text("No se puede conocer simultaneamente tiempo y frecuencia con precision maxima", font_size=24, color=TEXT_COLOR, line_spacing=1.4)
        explanation.next_to(title, DOWN, buff=0.7)

        principle = MathTex(
            r"\Delta t \cdot \Delta \omega \geq \frac{1}{2}",
            font_size=36,
            color=HIGHLIGHT_COLOR,
        )
        principle.next_to(explanation, DOWN, buff=0.6)

        scenarios = VGroup(
            Text("Senales de corta duracion -> ancho de banda grande", font_size=22, color=CURVE_COLOR),
            Text("Senales de larga duracion -> ancho de banda pequeno", font_size22, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.25)
        scenarios.next_to(principle, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=1)
        self.play(Write(principle), run_time=1)
        self.play(FadeIn(scenarios, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ApplicationAudioScene(Scene):
    def construct(self):
        title = Text("Aplicacion: Procesamiento de audio", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        applications = VGroup(
            Text("Ecualizacion: ajustar bandas de frecuencia", font_size=24, color=TEXT_COLOR),
            Text("Compresion: MP3 usa transformada", font_size=24, color=TEXT_COLOR),
            Text("Noise reduction: filtrar frecuencias especificas", font_size=24, color=TEXT_COLOR),
            Text("Analisis espectral: identificar notas musicales", font_size=24, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        applications.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        for app in applications:
            self.play(FadeIn(app, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ApplicationImageScene(Scene):
    def construct(self):
        title = Text("Aplicacion: Procesamiento de imagenes", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        jpeg_expl = Text("JPEG: divide imagen en bloques y aplica DCT", font_size=24, color=HIGHLIGHT_COLOR)
        jpeg_expl.next_to(title, DOWN, buff=0.6)

        dct = MathTex(
            r"X[u,v] = \sum_{x=0}^{N-1}\sum_{y=0}^{N-1} x[x,y] \cos\left(\frac{(2x+1)u\pi}{2N}\right) \cos\left(\frac{(2y+1)v\pi}{2N}\right)",
            font_size=18,
            color=TEXT_COLOR,
        )
        dct.next_to(jpeg_expl, DOWN, buff=0.4)

        other = VGroup(
            Text("Filtrado: eliminar frecuencias indeseadas", font_size=22, color=SECONDARY_COLOR),
            Text("Sharpen/Blur: modificar componentes de frecuencia", font_size=22, color=SECONDARY_COLOR),
            Text("Compresion:丢弃 componentes de alta frecuencia", font_size=22, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.2)
        other.next_to(dct, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(jpeg_expl), run_time=0.8)
        self.play(Write(dct), run_time=1)
        self.play(FadeIn(other, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ApplicationCommunicationsScene(Scene):
    def construct(self):
        title = Text("Aplicacion: Comunicaciones", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        modulation = VGroup(
            Text("Modulacion AM/FM:", font_size=26, color=HIGHLIGHT_COLOR),
            Text("Mover senal a diferentes frecuencias para transmision", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        modulation.next_to(title, DOWN, buff=0.6)

        multiplexing = VGroup(
            Text("FDMA/TDMA/CDMA:", font_size=26, color=HIGHLIGHT_COLOR),
            Text("Multiplear senales en dominio de frecuencia", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        multiplexing.next_to(modulation, DOWN, buff=0.4)

        filters = Text("Filtros: permitir/rechazar bandas de frecuencia", font_size=24, color=ACCENT_COLOR)
        filters.next_to(multiplexing, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(modulation, shift=RIGHT * 0.2), run_time=1)
        self.play(FadeIn(multiplexing, shift=RIGHT * 0.2), run_time=1)
        self.play(FadeIn(filters), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PropertiesScene(Scene):
    def construct(self):
        title = Text("Propiedades de la transformada de Fourier", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        props = VGroup(
            VGroup(
                Text("1. Linealidad", font_size=24, color=CURVE_COLOR),
                MathTex(r"\mathcal{F}\{af + bg\} = aF + bG", font_size=26, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("2. Desplazamiento", font_size=24, color=SECONDARY_COLOR),
                MathTex(r"\mathcal{F}\{f(t-t_0)\} = F(\omega)e^{-i\omega t_0}", font_size=26, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("3. Escalado", font_size=24, color=ACCENT_COLOR),
                MathTex(r"\mathcal{F}\{f(at)\} = \frac{1}{|a|}F\left(\frac{\omega}{a}\right)", font_size=26, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("4. Convolucion", font_size=24, color=HIGHLIGHT_COLOR),
                MathTex(r"\mathcal{F}\{f * g\} = F(\omega) \cdot G(\omega)", font_size=26, color=TEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(DOWN, buff=0.3)
        props.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for p in props:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.7)
            self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ParsevalScene(Scene):
    def construct(self):
        title = Text("Teorema de Parseval", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        formula = MathTex(
            r"\int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^{\infty} |F(\omega)|^2 d\omega",
            font_size=28,
            color=HIGHLIGHT_COLOR,
        )
        formula.next_to(title, DOWN, buff=0.7)

        explanation = Text("La energia en el dominio del tiempo es igual a la energia en frecuencia", font_size=22, color=TEXT_COLOR, line_spacing=1.3)
        explanation.next_to(formula, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=1.2)
        self.play(FadeIn(explanation), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WindowingScene(Scene):
    def construct(self):
        title = Text("Windowing: Ventanas en el tiempo", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        window_types = VGroup(
            Text("Hamming: reduce discontinuidades en bordes", font_size=22, color=WARNING_COLOR),
            Text("Hanning: similar a Hamming", font_size=22, color=TEXT_COLOR),
            Text("Blackman: menor leakage espectral", font_size=22, color=TEXT_COLOR),
            Text("Exponential: decaimiento suave", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        window_types.next_to(title, DOWN, buff=0.7)

        reason = Text("Previene leakage espectral por truncation", font_size=24, color=ACCENT_COLOR)
        reason.next_to(window_types, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for wt in window_types:
            self.play(FadeIn(wt, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        self.play(FadeIn(reason), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class STFTScene(Scene):
    def construct(self):
        title = Text("STFT: Short-Time Fourier Transform", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        concept = Text("Dividir la senal en ventanas y aplicar FFT a cada una", font_size=26, color=TEXT_COLOR)
        concept.next_to(title, DOWN, buff=0.6)

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 8, 2],
            x_length=7.0,
            y_length=4.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
            x_axis_config={"label": "Tiempo"},
            y_axis_config={"label": "Frecuencia"},
        ).shift(DOWN * 0.3)

        spectrogram = VGroup()
        for i in range(8):
            freq1 = np.random.uniform(1, 3)
            freq2 = np.random.uniform(4, 6)
            rect1 = Rectangle(
                width=1.0, height=freq1 * 0.5,
                color=random.choice([PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR]),
                fill_opacity=0.6,
            ).move_to(axes.c2p(i + 0.5, freq1 * 0.25))
            rect2 = Rectangle(
                width=1.0, height=freq2 * 0.4,
                color=random.choice([CURVE_COLOR, ITER_COLOR, HIGHLIGHT_COLOR]),
                fill_opacity=0.6,
            ).move_to(axes.c2p(i + 0.5, 4 + freq2 * 0.25))
            spectrogram.add(rect1, rect2)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(concept), run_time=0.8)
        self.play(Create(axes), run_time=0.8)
        self.play(FadeIn(spectrogram), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WaveletScene(Scene):
    def construct(self):
        title = Text("Wavelets: Alternativa a Fourier", font_size=40, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)

        advantage = Text("Resolucion adaptativa: mejor en tiempo para altas frecuencias", font_size=24, color=HIGHLIGHT_COLOR)
        advantage.next_to(title, DOWN, buff=0.6)

        transforms = VGroup(
            Text("Fourier: resolucion fija en tiempo-frecuencia", font_size=22, color=TEXT_COLOR),
            Text("Wavelet: resolucion variable (multi-resolucion)", font_size=22, color=TEXT_COLOR),
            Text("JPEG2000 usa wavelets en lugar de DCT", font_size=22, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.25)
        transforms.next_to(advantage, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(advantage), run_time=0.8)
        self.play(FadeIn(transforms, shift=RIGHT * 0.2), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Transformada de Fourier", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Descompone senales en componentes de frecuencia", font_size=26, color=TEXT_COLOR),
            Text("Serie de Fourier: senales periodicas", font_size=26, color=TEXT_COLOR),
            Text("Transformada continua: senales no periodicas", font_size=26, color=TEXT_COLOR),
            Text("DFT/FFT: calculo eficiente para senales discretas", font_size=26, color=TEXT_COLOR),
            Text("Aplicaciones: audio, imagen, comunicaciones", font_size=26, color=TEXT_COLOR),
            Text("STFT y wavelets: analisis tiempo-frecuencia", font_size=26, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Herramienta fundamental en senales y sistemas",
            font_size=28,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FourierTransformFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        WhyFourierScene.construct(self)
        ContinuousFTScene.construct(self)
        FrequencyDomainScene.construct(self)
        FourierSeriesScene.construct(self)
        SquareWaveScene.construct(self)
        GibbPhenomenonScene.construct(self)
        DFTScene.construct(self)
        FFTVisualizationScene.construct(self)
        TimeFrequencyTradeoffScene.construct(self)
        ApplicationAudioScene.construct(self)
        ApplicationImageScene.construct(self)
        ApplicationCommunicationsScene.construct(self)
        PropertiesScene.construct(self)
        ParsevalScene.construct(self)
        WindowingScene.construct(self)
        STFTScene.construct(self)
        WaveletScene.construct(self)
        ConclusionScene.construct(self)
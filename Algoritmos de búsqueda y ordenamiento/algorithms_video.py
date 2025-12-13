
from manim import *
import numpy as np

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
WARNING_COLOR = "#fab387"
TEXT_COLOR = "#cdd6f4"
COMPARING_COLOR = "#f38ba8"
FOUND_COLOR = "#a6e3a1"
PIVOT_COLOR = "#cba6f7"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Algoritmos de Búsqueda\ny Ordenamiento",
            font_size=56,
            color=PRIMARY_COLOR,
            line_spacing=1.2
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)
        
        subtitle = Text(
            "Una exploración visual",
            font_size=32,
            color=TEXT_COLOR
        ).next_to(title, DOWN, buff=0.8)
        
        circles = VGroup(*[
            Circle(radius=0.15, color=c, fill_opacity=0.8)
            for c in [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
        ]).arrange(RIGHT, buff=0.3).next_to(subtitle, DOWN, buff=0.6)
        
        self.play(Write(title, run_time=2.5))
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=1)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in circles], lag_ratio=0.2),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            *[c.animate.scale(1.3) for c in circles],
            rate_func=there_and_back,
            run_time=0.8
        )
        self.wait(0.5)
        
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP * 0.5),
            *[FadeOut(c, shift=DOWN) for c in circles],
            run_time=1.2
        )
        self.wait(0.3)


class WhatIsSearchScene(Scene):
    def construct(self):
        section_title = Text(
            "¿Qué son los Algoritmos de Búsqueda?",
            font_size=42,
            color=PRIMARY_COLOR
        ).to_edge(UP, buff=0.8)
        
        self.play(Write(section_title), run_time=1.5)
        
        definition = Text(
            "Un algoritmo de búsqueda es un conjunto de instrucciones\n"
            "para encontrar un elemento específico dentro de una estructura de datos.",
            font_size=26,
            color=TEXT_COLOR,
            line_spacing=1.3
        ).next_to(section_title, DOWN, buff=0.8)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.5)
        self.wait(1.5)
        
        array_label = Text("Ejemplo: Buscar el 7", font_size=28, color=HIGHLIGHT_COLOR)
        array_label.next_to(definition, DOWN, buff=0.8)
        
        values = [3, 1, 4, 1, 5, 9, 2, 6, 7, 8]
        array_group = self.create_array(values)
        array_group.next_to(array_label, DOWN, buff=0.6)
        
        self.play(FadeIn(array_label))
        self.play(
            LaggedStart(*[GrowFromCenter(cell) for cell in array_group], lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(1)
        
        target_idx = values.index(7)
        target_cell = array_group[target_idx]
        
        highlight_rect = SurroundingRectangle(
            target_cell, color=FOUND_COLOR, buff=0.1, stroke_width=3
        )
        
        self.play(Create(highlight_rect), run_time=0.8)
        self.play(
            target_cell[0].animate.set_fill(FOUND_COLOR, opacity=0.3),
            run_time=0.5
        )
        self.wait(1.5)
        
        question = Text(
            "¿Cómo lo encontramos eficientemente?",
            font_size=30,
            color=SECONDARY_COLOR
        ).next_to(array_group, DOWN, buff=0.8)
        
        self.play(Write(question), run_time=1.2)
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(0.3)
    
    def create_array(self, values, cell_size=0.7):
        cells = VGroup()
        for val in values:
            cell = VGroup(
                Square(side_length=cell_size, color=PRIMARY_COLOR, stroke_width=2),
                Text(str(val), font_size=24, color=TEXT_COLOR)
            )
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.05)
        return cells


class LinearSearchScene(Scene):
    def construct(self):
        title = Text("Búsqueda Lineal", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        subtitle = Text(
            "Recorre cada elemento uno por uno",
            font_size=24, color=TEXT_COLOR
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2))
        self.wait(0.8)
        
        values = [23, 45, 12, 67, 34, 89, 56, 78]
        target = 67
        
        array_group = self.create_array(values)
        array_group.move_to(ORIGIN + UP * 0.5)
        
        indices = VGroup(*[
            Text(str(i), font_size=18, color=HIGHLIGHT_COLOR)
            for i in range(len(values))
        ])
        for i, idx_text in enumerate(indices):
            idx_text.next_to(array_group[i], DOWN, buff=0.2)
        
        target_label = Text(
            f"Buscando: {target}",
            font_size=28, color=HIGHLIGHT_COLOR
        ).to_edge(LEFT, buff=1).shift(UP * 2)
        
        self.play(FadeIn(target_label))
        self.play(
            LaggedStart(*[FadeIn(cell, scale=0.8) for cell in array_group], lag_ratio=0.08),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[FadeIn(idx) for idx in indices], lag_ratio=0.05),
            run_time=0.8
        )
        self.wait(0.5)
        
        pointer = Arrow(
            start=UP * 0.8, end=DOWN * 0.1,
            color=COMPARING_COLOR, stroke_width=4
        )
        pointer.next_to(array_group[0], UP, buff=0.1)
        
        self.play(GrowArrow(pointer))
        
        for i, val in enumerate(values):
            if i > 0:
                self.play(
                    pointer.animate.next_to(array_group[i], UP, buff=0.1),
                    run_time=0.4
                )
            
            self.play(
                array_group[i][0].animate.set_stroke(COMPARING_COLOR, width=4),
                run_time=0.2
            )
            
            if val == target:
                found_text = Text("¡Encontrado!", font_size=32, color=FOUND_COLOR)
                found_text.next_to(array_group, DOWN, buff=0.8)
                
                self.play(
                    array_group[i][0].animate.set_fill(FOUND_COLOR, opacity=0.4),
                    array_group[i][0].animate.set_stroke(FOUND_COLOR, width=4),
                    FadeIn(found_text, scale=1.2),
                    run_time=0.6
                )
                self.wait(1)
                break
            else:
                self.play(
                    array_group[i][0].animate.set_stroke(PRIMARY_COLOR, width=2),
                    run_time=0.15
                )
        
        self.wait(0.5)
        
        self.play(
            FadeOut(pointer),
            array_group.animate.shift(UP * 1),
            indices.animate.shift(UP * 1),
            FadeOut(found_text) if 'found_text' in dir() else Wait(0),
            run_time=0.8
        )
        
        java_code = self.create_java_code()
        java_code.scale(0.7).to_edge(DOWN, buff=0.4)
        
        self.play(FadeIn(java_code, shift=UP * 0.3), run_time=1)
        self.wait(2.5)
        
        complexity = VGroup(
            Text("Complejidad:", font_size=26, color=TEXT_COLOR),
            MathTex(r"O(n)", font_size=40, color=WARNING_COLOR)
        ).arrange(RIGHT, buff=0.3).next_to(java_code, UP, buff=0.5).to_edge(RIGHT, buff=1)
        
        self.play(Write(complexity), run_time=1)
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
    
    def create_array(self, values, cell_size=0.8):
        cells = VGroup()
        for val in values:
            cell = VGroup(
                Square(side_length=cell_size, color=PRIMARY_COLOR, stroke_width=2),
                Text(str(val), font_size=22, color=TEXT_COLOR)
            )
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.08)
        return cells
    
    def create_java_code(self):
        code_str = '''int linearSearch(int[] arr, int x) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == x) return i;
    }
    return -1;
}'''
        code = Code(
            code_string=code_str,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            add_line_numbers=True
        )
        return code


class BinarySearchScene(Scene):
    def construct(self):
        title = Text("Búsqueda Binaria", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        subtitle = Text(
            "Divide y conquista en arrays ordenados",
            font_size=24, color=TEXT_COLOR
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2))
        self.wait(0.8)
        
        values = [11, 23, 34, 45, 56, 67, 78, 89]
        target = 56
        
        sorted_note = Text(
            "⚠ Requiere array ordenado",
            font_size=22, color=WARNING_COLOR
        ).to_edge(LEFT, buff=0.8).shift(UP * 1.5)
        
        target_label = Text(
            f"Buscando: {target}",
            font_size=28, color=HIGHLIGHT_COLOR
        ).next_to(sorted_note, DOWN, buff=0.3).align_to(sorted_note, LEFT)
        
        self.play(FadeIn(sorted_note), FadeIn(target_label))
        
        array_group = self.create_array(values)
        array_group.move_to(ORIGIN + UP * 0.3)
        
        indices = VGroup(*[
            Text(str(i), font_size=18, color=HIGHLIGHT_COLOR)
            for i in range(len(values))
        ])
        for i, idx_text in enumerate(indices):
            idx_text.next_to(array_group[i], DOWN, buff=0.2)
        
        self.play(
            LaggedStart(*[FadeIn(cell, scale=0.8) for cell in array_group], lag_ratio=0.06),
            run_time=1
        )
        self.play(FadeIn(indices), run_time=0.5)
        self.wait(0.5)
        
        low, high = 0, len(values) - 1
        
        low_ptr = self.create_pointer("low", ACCENT_COLOR)
        high_ptr = self.create_pointer("high", COMPARING_COLOR)
        mid_ptr = self.create_pointer("mid", PIVOT_COLOR)
        
        low_ptr.next_to(array_group[low], UP, buff=0.15)
        high_ptr.next_to(array_group[high], UP, buff=0.15)
        
        self.play(FadeIn(low_ptr), FadeIn(high_ptr))
        
        iteration = 0
        while low <= high:
            mid = (low + high) // 2
            
            mid_ptr.next_to(array_group[mid], UP, buff=0.15)
            if iteration == 0:
                self.play(FadeIn(mid_ptr), run_time=0.5)
            else:
                self.play(mid_ptr.animate.next_to(array_group[mid], UP, buff=0.15), run_time=0.5)
            
            self.play(
                array_group[mid][0].animate.set_stroke(PIVOT_COLOR, width=4),
                run_time=0.3
            )
            
            if values[mid] == target:
                found_text = Text("¡Encontrado!", font_size=32, color=FOUND_COLOR)
                found_text.next_to(indices, DOWN, buff=0.6)
                
                self.play(
                    array_group[mid][0].animate.set_fill(FOUND_COLOR, opacity=0.4),
                    FadeIn(found_text, scale=1.2),
                    run_time=0.6
                )
                self.wait(1)
                break
            elif values[mid] < target:
                for i in range(low, mid + 1):
                    self.play(
                        array_group[i][0].animate.set_opacity(0.3),
                        run_time=0.1
                    )
                low = mid + 1
                self.play(low_ptr.animate.next_to(array_group[low], UP, buff=0.15), run_time=0.4)
            else:
                for i in range(mid, high + 1):
                    self.play(
                        array_group[i][0].animate.set_opacity(0.3),
                        run_time=0.1
                    )
                high = mid - 1
                if high >= 0:
                    self.play(high_ptr.animate.next_to(array_group[high], UP, buff=0.15), run_time=0.4)
            
            iteration += 1
        
        self.wait(0.5)
        
        self.play(
            FadeOut(low_ptr), FadeOut(mid_ptr), FadeOut(high_ptr),
            FadeOut(found_text) if 'found_text' in dir() else Wait(0),
            array_group.animate.shift(UP * 0.8).scale(0.85),
            indices.animate.shift(UP * 0.8).scale(0.85),
            run_time=0.7
        )
        
        java_code = self.create_java_code()
        java_code.scale(0.6).to_edge(DOWN, buff=0.3)
        
        self.play(FadeIn(java_code, shift=UP * 0.3), run_time=1)
        self.wait(1.5)
        
        complexity = VGroup(
            Text("Complejidad:", font_size=24, color=TEXT_COLOR),
            MathTex(r"O(\log n)", font_size=36, color=FOUND_COLOR)
        ).arrange(RIGHT, buff=0.3).next_to(java_code, UP, buff=0.4).to_edge(RIGHT, buff=0.8)
        
        self.play(Write(complexity), run_time=1)
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
    
    def create_array(self, values, cell_size=0.8):
        cells = VGroup()
        for val in values:
            cell = VGroup(
                Square(side_length=cell_size, color=PRIMARY_COLOR, stroke_width=2),
                Text(str(val), font_size=22, color=TEXT_COLOR)
            )
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.08)
        return cells
    
    def create_pointer(self, label, color):
        arrow = Arrow(start=UP * 0.5, end=ORIGIN, color=color, stroke_width=3)
        text = Text(label, font_size=16, color=color).next_to(arrow, UP, buff=0.05)
        return VGroup(arrow, text)
    
    def create_java_code(self):
        code_str = '''int binarySearch(int[] arr, int x) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == x) return mid;
        if (arr[mid] < x) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}'''
        return Code(
            code_string=code_str, language="java",
            formatter_style="monokai", background="rectangle",
            add_line_numbers=True
        )


class SearchComparisonScene(Scene):
    def construct(self):
        title = Text("Comparación de Complejidad", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title))
        
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 100, 20],
            x_length=8,
            y_length=5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.5)
        
        x_label = Text("n (elementos)", font_size=20, color=TEXT_COLOR)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("operaciones", font_size=20, color=TEXT_COLOR)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)
        
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.5)
        
        linear_graph = axes.plot(lambda x: x, x_range=[0, 100], color=WARNING_COLOR, stroke_width=3)
        linear_label = MathTex(r"O(n)", color=WARNING_COLOR, font_size=32)
        linear_label.next_to(linear_graph.get_end(), RIGHT, buff=0.2)
        
        log_graph = axes.plot(
            lambda x: 15 * np.log2(x + 1), x_range=[0, 100],
            color=FOUND_COLOR, stroke_width=3
        )
        log_label = MathTex(r"O(\log n)", color=FOUND_COLOR, font_size=32)
        log_label.next_to(log_graph.point_from_proportion(0.9), UP, buff=0.2)
        
        self.play(Create(linear_graph), Write(linear_label), run_time=1.5)
        self.wait(0.5)
        self.play(Create(log_graph), Write(log_label), run_time=1.5)
        self.wait(1)
        
        legend = VGroup(
            VGroup(
                Line(ORIGIN, RIGHT * 0.5, color=WARNING_COLOR, stroke_width=4),
                Text("Búsqueda Lineal", font_size=20, color=WARNING_COLOR)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Line(ORIGIN, RIGHT * 0.5, color=FOUND_COLOR, stroke_width=4),
                Text("Búsqueda Binaria", font_size=20, color=FOUND_COLOR)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        
        self.play(FadeIn(legend), run_time=0.8)
        self.wait(2)
        
        key_msg = Text(
            "¡La búsqueda binaria es exponencialmente más rápida!",
            font_size=26, color=SECONDARY_COLOR
        ).next_to(axes, DOWN, buff=0.6)
        
        self.play(Write(key_msg), run_time=1.2)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


class WhatIsSortingScene(Scene):
    def construct(self):
        title = Text(
            "¿Qué son los Algoritmos de Ordenamiento?",
            font_size=40, color=PRIMARY_COLOR
        ).to_edge(UP, buff=0.7)
        
        self.play(Write(title), run_time=1.5)
        
        definition = Text(
            "Un algoritmo de ordenamiento organiza los elementos\n"
            "de una colección en un orden específico (ascendente o descendente).",
            font_size=24, color=TEXT_COLOR, line_spacing=1.3
        ).next_to(title, DOWN, buff=0.7)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.2)
        self.wait(1.5)
        
        before_label = Text("Antes:", font_size=24, color=WARNING_COLOR)
        after_label = Text("Después:", font_size=24, color=FOUND_COLOR)
        
        unsorted = [64, 25, 12, 22, 11]
        sorted_vals = sorted(unsorted)
        
        before_array = self.create_array(unsorted)
        after_array = self.create_array(sorted_vals)
        
        before_group = VGroup(before_label, before_array).arrange(RIGHT, buff=0.5)
        after_group = VGroup(after_label, after_array).arrange(RIGHT, buff=0.5)
        
        examples = VGroup(before_group, after_group).arrange(DOWN, buff=0.6)
        examples.next_to(definition, DOWN, buff=0.8)
        
        self.play(FadeIn(before_group), run_time=1)
        self.wait(0.8)
        
        arrow = Arrow(before_array.get_right(), after_array.get_left(), color=ACCENT_COLOR)
        arrow.shift(DOWN * 0.3)
        
        self.play(
            FadeIn(after_label),
            GrowArrow(arrow),
            run_time=0.8
        )
        
        self.play(
            LaggedStart(*[FadeIn(cell, scale=0.8) for cell in after_array], lag_ratio=0.1),
            run_time=1.2
        )
        self.wait(1.5)
        
        question = Text(
            "¿Cómo lo hacemos eficientemente?",
            font_size=28, color=SECONDARY_COLOR
        ).next_to(examples, DOWN, buff=0.6)
        
        self.play(Write(question), run_time=1)
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
    
    def create_array(self, values, cell_size=0.65):
        cells = VGroup()
        for val in values:
            cell = VGroup(
                Square(side_length=cell_size, color=PRIMARY_COLOR, stroke_width=2),
                Text(str(val), font_size=20, color=TEXT_COLOR)
            )
            cells.add(cell)
        cells.arrange(RIGHT, buff=0.05)
        return cells


class BubbleSortScene(Scene):
    def construct(self):
        title = Text("Bubble Sort", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        subtitle = Text(
            "Compara e intercambia elementos adyacentes",
            font_size=24, color=TEXT_COLOR
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2))
        self.wait(0.8)
        
        values = [64, 34, 25, 12, 22, 11, 90]
        n = len(values)
        
        bars = self.create_bars(values)
        bars.move_to(ORIGIN)
        
        self.play(
            LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(0.5)
        
        for i in range(min(3, n-1)):
            for j in range(n - i - 1):
                self.play(
                    bars[j].animate.set_color(COMPARING_COLOR),
                    bars[j+1].animate.set_color(COMPARING_COLOR),
                    run_time=0.2
                )
                
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]
                    
                    self.play(
                        bars[j].animate.move_to(bars[j+1].get_center()),
                        bars[j+1].animate.move_to(bars[j].get_center()),
                        run_time=0.3
                    )
                    bars[j], bars[j+1] = bars[j+1], bars[j]
                
                self.play(
                    bars[j].animate.set_color(PRIMARY_COLOR),
                    bars[j+1].animate.set_color(PRIMARY_COLOR),
                    run_time=0.15
                )
            
            self.play(
                bars[n-i-1].animate.set_color(FOUND_COLOR),
                run_time=0.3
            )
        
        for k in range(n - 3):
            self.play(bars[k].animate.set_color(FOUND_COLOR), run_time=0.15)
        
        self.wait(0.5)
        
        self.play(bars.animate.scale(0.7).shift(UP * 1.5), run_time=0.7)
        
        java_code = self.create_java_code()
        java_code.scale(0.6).to_edge(DOWN, buff=0.3)
        
        self.play(FadeIn(java_code, shift=UP * 0.3), run_time=1)
        self.wait(1.5)
        
        complexity_group = VGroup(
            Text("Complejidad:", font_size=22, color=TEXT_COLOR),
            MathTex(r"O(n^2)", font_size=32, color=WARNING_COLOR)
        ).arrange(RIGHT, buff=0.2).next_to(java_code, UP, buff=0.4).to_edge(RIGHT, buff=0.6)
        
        self.play(Write(complexity_group), run_time=0.8)
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
    
    def create_bars(self, values, max_height=3.5, bar_width=0.6):
        max_val = max(values)
        bars = VGroup()
        for val in values:
            height = (val / max_val) * max_height
            bar = Rectangle(
                width=bar_width, height=height,
                color=PRIMARY_COLOR, fill_opacity=0.7,
                stroke_width=2
            )
            label = Text(str(val), font_size=16, color=TEXT_COLOR)
            label.next_to(bar, UP, buff=0.1)
            bar_group = VGroup(bar, label)
            bars.add(bar_group)
        bars.arrange(RIGHT, buff=0.15, aligned_edge=DOWN)
        return bars
    
    def create_java_code(self):
        code_str = '''void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (arr[j] > arr[j+1])
                swap(arr, j, j+1);
}'''
        return Code(
            code_string=code_str, language="java",
            formatter_style="monokai", background="rectangle",
            add_line_numbers=True
        )


class QuickSortScene(Scene):
    def construct(self):
        title = Text("Quick Sort", font_size=44, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        subtitle = Text(
            "Divide y conquista con pivote",
            font_size=24, color=TEXT_COLOR
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2))
        self.wait(0.8)
        
        concept = VGroup(
            Text("1. Elegir un pivote", font_size=22, color=PIVOT_COLOR),
            Text("2. Particionar: menores a izquierda, mayores a derecha", font_size=22, color=TEXT_COLOR),
            Text("3. Repetir recursivamente", font_size=22, color=ACCENT_COLOR)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(subtitle, DOWN, buff=0.6)
        
        for step in concept:
            self.play(Write(step), run_time=0.8)
            self.wait(0.4)
        
        self.wait(1)
        
        self.play(FadeOut(concept), run_time=0.5)
        
        values = [38, 27, 43, 3, 9, 82, 10]
        bars = self.create_bars(values)
        bars.move_to(ORIGIN + UP * 0.3)
        
        self.play(
            LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.08),
            run_time=1.2
        )
        
        pivot_idx = len(values) - 1
        pivot_label = Text("Pivote", font_size=20, color=PIVOT_COLOR)
        pivot_label.next_to(bars[pivot_idx], UP, buff=0.3)
        
        self.play(
            bars[pivot_idx].animate.set_color(PIVOT_COLOR),
            FadeIn(pivot_label),
            run_time=0.6
        )
        self.wait(0.8)
        
        partition_text = Text(
            "Elementos < pivote van a la izquierda",
            font_size=22, color=SECONDARY_COLOR
        ).next_to(bars, DOWN, buff=0.8)
        
        self.play(Write(partition_text), run_time=1)
        self.wait(1)
        
        left_vals = [3, 9]
        right_vals = [38, 27, 43, 82]
        pivot_val = 10
        
        left_bars = self.create_small_bars(left_vals, ACCENT_COLOR)
        pivot_bar = self.create_small_bars([pivot_val], PIVOT_COLOR)
        right_bars = self.create_small_bars(right_vals, WARNING_COLOR)
        
        new_arrangement = VGroup(left_bars, pivot_bar, right_bars).arrange(RIGHT, buff=0.4)
        new_arrangement.move_to(ORIGIN + UP * 0.3)
        
        labels = VGroup(
            Text("< pivote", font_size=18, color=ACCENT_COLOR).next_to(left_bars, DOWN, buff=0.3),
            Text("pivote", font_size=18, color=PIVOT_COLOR).next_to(pivot_bar, DOWN, buff=0.3),
            Text("> pivote", font_size=18, color=WARNING_COLOR).next_to(right_bars, DOWN, buff=0.3)
        )
        
        self.play(
            FadeOut(bars), FadeOut(pivot_label), FadeOut(partition_text),
            run_time=0.5
        )
        self.play(
            FadeIn(new_arrangement),
            FadeIn(labels),
            run_time=1
        )
        self.wait(1.5)
        
        self.play(
            new_arrangement.animate.scale(0.7).shift(UP * 1.2),
            labels.animate.scale(0.7).shift(UP * 1.2),
            run_time=0.7
        )
        
        java_code = self.create_java_code()
        java_code.scale(0.55).to_edge(DOWN, buff=0.25)
        
        self.play(FadeIn(java_code, shift=UP * 0.3), run_time=1)
        self.wait(1.5)
        
        complexity = VGroup(
            Text("Promedio:", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(n \log n)", font_size=28, color=FOUND_COLOR)
        ).arrange(RIGHT, buff=0.2).next_to(java_code, UP, buff=0.3).to_edge(RIGHT, buff=0.5)
        
        self.play(Write(complexity), run_time=0.8)
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
    
    def create_bars(self, values, max_height=2.8, bar_width=0.55):
        max_val = max(values)
        bars = VGroup()
        for val in values:
            height = (val / max_val) * max_height
            bar = Rectangle(
                width=bar_width, height=height,
                color=PRIMARY_COLOR, fill_opacity=0.7, stroke_width=2
            )
            label = Text(str(val), font_size=14, color=TEXT_COLOR)
            label.next_to(bar, UP, buff=0.08)
            bars.add(VGroup(bar, label))
        bars.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
        return bars
    
    def create_small_bars(self, values, color, max_height=2.0, bar_width=0.45):
        if not values:
            return VGroup()
        max_val = max(values) if values else 1
        bars = VGroup()
        for val in values:
            height = (val / 82) * max_height
            bar = Rectangle(
                width=bar_width, height=max(height, 0.3),
                color=color, fill_opacity=0.7, stroke_width=2
            )
            label = Text(str(val), font_size=12, color=TEXT_COLOR)
            label.next_to(bar, UP, buff=0.05)
            bars.add(VGroup(bar, label))
        bars.arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        return bars
    
    def create_java_code(self):
        code_str = '''void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}'''
        return Code(
            code_string=code_str, language="java",
            formatter_style="monokai", background="rectangle",
            add_line_numbers=True
        )


class SortComparisonScene(Scene):
    def construct(self):
        title = Text("Comparación de Algoritmos", font_size=42, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title))
        
        axes = Axes(
            x_range=[0, 50, 10],
            y_range=[0, 2500, 500],
            x_length=7,
            y_length=4.5,
            axis_config={"color": TEXT_COLOR, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.3 + LEFT * 0.5)
        
        x_label = Text("n", font_size=22, color=TEXT_COLOR).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("ops", font_size=22, color=TEXT_COLOR).next_to(axes.y_axis, LEFT, buff=0.2)
        
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.2)
        
        quadratic = axes.plot(lambda x: x**2, x_range=[0, 50], color=WARNING_COLOR, stroke_width=3)
        quad_label = MathTex(r"O(n^2)", color=WARNING_COLOR, font_size=28)
        quad_label.next_to(quadratic.point_from_proportion(0.85), UP + RIGHT, buff=0.1)
        
        nlogn = axes.plot(
            lambda x: x * np.log2(x + 1) * 5, x_range=[0, 50],
            color=FOUND_COLOR, stroke_width=3
        )
        nlogn_label = MathTex(r"O(n \log n)", color=FOUND_COLOR, font_size=28)
        nlogn_label.next_to(nlogn.point_from_proportion(0.9), RIGHT, buff=0.15)
        
        self.play(Create(quadratic), Write(quad_label), run_time=1.5)
        self.wait(0.5)
        self.play(Create(nlogn), Write(nlogn_label), run_time=1.5)
        self.wait(1)
        
        table = VGroup(
            Text("Algoritmo", font_size=18, color=PRIMARY_COLOR),
            Text("Mejor", font_size=18, color=PRIMARY_COLOR),
            Text("Promedio", font_size=18, color=PRIMARY_COLOR),
            Text("Peor", font_size=18, color=PRIMARY_COLOR),
            
            Text("Bubble", font_size=16, color=WARNING_COLOR),
            MathTex(r"O(n)", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(n^2)", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(n^2)", font_size=20, color=TEXT_COLOR),
            
            Text("Quick", font_size=16, color=FOUND_COLOR),
            MathTex(r"O(n \log n)", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(n \log n)", font_size=20, color=TEXT_COLOR),
            MathTex(r"O(n^2)", font_size=20, color=TEXT_COLOR),
        )
        
        table.arrange_in_grid(rows=3, cols=4, buff=(0.4, 0.25))
        table.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.3)
        
        self.play(FadeIn(table), run_time=1)
        self.wait(2.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen", font_size=48, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=1)
        
        points = VGroup(
            self.create_point("🔍", "Búsqueda Lineal", "O(n)", "Simple pero lenta", WARNING_COLOR),
            self.create_point("⚡", "Búsqueda Binaria", "O(log n)", "Rápida en arrays ordenados", FOUND_COLOR),
            self.create_point("🔄", "Bubble Sort", "O(n²)", "Simple pero ineficiente", WARNING_COLOR),
            self.create_point("🚀", "Quick Sort", "O(n log n)", "Eficiente para grandes datos", FOUND_COLOR),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(title, DOWN, buff=0.7)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT * 0.3), run_time=0.8)
            self.wait(0.3)
        
        self.wait(1)
        
        final_msg = Text(
            "Elegir el algoritmo correcto puede marcar\nuna gran diferencia en el rendimiento.",
            font_size=26, color=SECONDARY_COLOR, line_spacing=1.3
        ).next_to(points, DOWN, buff=0.7)
        
        self.play(Write(final_msg), run_time=1.5)
        self.wait(2)
        
        thanks = Text(
            "¡Gracias por ver!",
            font_size=42, color=PRIMARY_COLOR
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR)
        
        self.play(
            *[FadeOut(mob) for mob in [title, points, final_msg]],
            run_time=0.8
        )
        self.play(Write(thanks), run_time=1.5)
        self.wait(2)
        
        self.play(FadeOut(thanks), run_time=1)
    
    def create_point(self, icon, name, complexity, desc, color):
        return VGroup(
            Text(icon, font_size=28),
            Text(name, font_size=24, color=color),
            MathTex(complexity, font_size=28, color=HIGHLIGHT_COLOR),
            Text(f"- {desc}", font_size=20, color=TEXT_COLOR)
        ).arrange(RIGHT, buff=0.3)


class AlgorithmsFullVideo(Scene):
    def construct(self):
        self.play_intro()
        
        self.play_what_is_search()
        
        self.play_linear_search()
        
        self.play_binary_search()
        
        self.play_search_comparison()
        
        self.play_what_is_sorting()
        
        self.play_bubble_sort()
        
        self.play_quick_sort()
        
        self.play_sort_comparison()
        
        self.play_conclusion()
    
    def play_intro(self):
        title = Text(
            "Algoritmos de Búsqueda\ny Ordenamiento",
            font_size=56, color=PRIMARY_COLOR, line_spacing=1.2
        ).set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR)
        
        subtitle = Text("Una exploración visual", font_size=32, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        circles = VGroup(*[
            Circle(radius=0.15, color=c, fill_opacity=0.8)
            for c in [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
        ]).arrange(RIGHT, buff=0.3).next_to(subtitle, DOWN, buff=0.6)
        
        self.play(Write(title, run_time=2.5))
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.play(LaggedStart(*[GrowFromCenter(c) for c in circles], lag_ratio=0.2), run_time=1.5)
        self.wait(1)
        self.play(*[c.animate.scale(1.3) for c in circles], rate_func=there_and_back, run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle), *[FadeOut(c) for c in circles])
        self.wait(0.3)
    
    def play_what_is_search(self):
        section_title = Text("¿Qué son los Algoritmos de Búsqueda?", font_size=42, color=PRIMARY_COLOR)
        section_title.to_edge(UP, buff=0.8)
        self.play(Write(section_title), run_time=1.5)
        
        definition = Text(
            "Un algoritmo de búsqueda es un conjunto de instrucciones\n"
            "para encontrar un elemento específico dentro de una estructura de datos.",
            font_size=26, color=TEXT_COLOR, line_spacing=1.3
        ).next_to(section_title, DOWN, buff=0.8)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.5)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def play_linear_search(self):
        title = Text("Búsqueda Lineal", font_size=44, color=PRIMARY_COLOR).to_edge(UP, buff=0.5)
        subtitle = Text("Recorre cada elemento uno por uno", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        
        complexity = MathTex(r"O(n)", font_size=48, color=WARNING_COLOR)
        self.play(Write(complexity))
        self.wait(1.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def play_binary_search(self):
        title = Text("Búsqueda Binaria", font_size=44, color=PRIMARY_COLOR).to_edge(UP, buff=0.5)
        subtitle = Text("Divide y conquista", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        
        complexity = MathTex(r"O(\log n)", font_size=48, color=FOUND_COLOR)
        self.play(Write(complexity))
        self.wait(1.5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def play_search_comparison(self):
        title = Text("Comparación", font_size=44, color=PRIMARY_COLOR)
        self.play(Write(title))
        self.wait(1.5)
        self.play(FadeOut(title))
    
    def play_what_is_sorting(self):
        title = Text("Algoritmos de Ordenamiento", font_size=44, color=PRIMARY_COLOR)
        self.play(Write(title))
        self.wait(1.5)
        self.play(FadeOut(title))
    
    def play_bubble_sort(self):
        title = Text("Bubble Sort", font_size=44, color=PRIMARY_COLOR).to_edge(UP, buff=0.5)
        complexity = MathTex(r"O(n^2)", font_size=48, color=WARNING_COLOR)
        
        self.play(Write(title))
        self.play(Write(complexity))
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def play_quick_sort(self):
        title = Text("Quick Sort", font_size=44, color=PRIMARY_COLOR).to_edge(UP, buff=0.5)
        complexity = MathTex(r"O(n \log n)", font_size=48, color=FOUND_COLOR)
        
        self.play(Write(title))
        self.play(Write(complexity))
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def play_sort_comparison(self):
        title = Text("Comparación Final", font_size=44, color=PRIMARY_COLOR)
        self.play(Write(title))
        self.wait(1.5)
        self.play(FadeOut(title))
    
    def play_conclusion(self):
        thanks = Text("¡Gracias por ver!", font_size=48, color=PRIMARY_COLOR)
        thanks.set_color_by_gradient(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR)
        self.play(Write(thanks))
        self.wait(2)
        self.play(FadeOut(thanks))

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
FLUTTER_COLOR = "#02569B"
DART_COLOR = "#0175C2"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Flutter",
            font_size=58,
            color=FLUTTER_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(FLUTTER_COLOR, PRIMARY_COLOR)

        subtitle = Text(
            "Framework cross-platform para desarrollo mobile, web y desktop",
            font_size=24,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [FLUTTER_COLOR, PRIMARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
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


class FlutterHistoryScene(Scene):
    def construct(self):
        title = Text("Historia de Flutter", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        timeline = VGroup(
            Text("2015: Flutter annunciado en Dart Developer Summit", font_size=20, color=TEXT_COLOR),
            Text("2017: Flutter Beta 1 - Primeros lanzamientos", font_size=20, color=TEXT_COLOR),
            Text("2018: Flutter 1.0 - Version establereleased", font_size=22, color=FLUTTER_COLOR),
            Text("2019: Flutter 1.12 - Web and desktop support", font_size=20, color=TEXT_COLOR),
            Text("2020: Flutter 1.20 - Null safety beta", font_size=20, color=TEXT_COLOR),
            Text("2021: Flutter 2.0 - Null safety stable, web stable", font_size=20, color=ACCENT_COLOR),
            Text("2022: Flutter 3.0 - Cross-platform unificado", font_size=20, color=HIGHLIGHT_COLOR),
            Text("2023: Flutter 3.16 - Impeller renderer", font_size=20, color=SUCCESS_COLOR),
            Text("2024: Flutter 3.24+ - Material 3, GPU improvements", font_size=20, color=FLUTTER_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        timeline.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        for t in timeline:
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WhyFlutterScene(Scene):
    def construct(self):
        title = Text("Por que Flutter?", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        reasons = VGroup(
            Text("Single Codebase - Una base de codigo para iOS, Android, Web, Desktop", font_size=20, color=HIGHLIGHT_COLOR),
            Text("Hot Reload - Cambios inmediatos en tiempo de ejecucion", font_size=20, color=ACCENT_COLOR),
            Text("Expressive UI - Widgets personalizables y animaciones suaves", font_size=20, color=SECONDARY_COLOR),
            Text("Native Performance - Compilacion nativa para cada plataforma", font_size=20, color=CURVE_COLOR),
            Text("Open Source - Comunidad activa y documentacion extensa", font_size=20, color=TEXT_COLOR),
            Text("Dart - Lenguaje modernejo con null safety", font_size=20, color=SUCCESS_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        reasons.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for r in reasons:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DartLanguageScene(Scene):
    def construct(self):
        title = Text("Lenguaje Dart", font_size=48, color=DART_COLOR)
        title.to_edge(UP, buff=0.5)

        basics = '''// Variables y tipos
String nombre = 'Juan';
int edad = 25;
double altura = 1.75;
bool activo = true;
List<String> colores = ['rojo', 'verde', 'azul'];
Map<String, dynamic> usuario = {'nombre': 'Juan', 'edad': 25};

// Null safety
String? nullable;  // Puede ser null
String noNull = nullable ?? 'valor por defecto';

// Final y Const
final fechaActual = DateTime.now();
const pi = 3.14159;'''

        dart_code = Code(
            code_string=basics,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        dart_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DartFunctionsScene(Scene):
    def construct(self):
        title = Text("Funciones en Dart", font_size=44, color=DART_COLOR)
        title.to_edge(UP, buff=0.5)

        functions = '''// Funcion basica
int sumar(int a, int b) {
  return a + b;
}

// Arrow function
int multiplicar(int a, int b) => a * b;

// Parametros opcionales
String saludar(String nombre, {String? saludo}) {
  return '${saludo ?? 'Hola'}, $nombre!';
}

// Funciones de orden superior
List<int> duplicar(List<int> numeros) {
  return numeros.map((n) => n * 2).toList();
}

// Funciones anonimas
final callback = (int x) => x * x;'''

        dart_code = Code(
            code_string=functions,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        dart_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DartOOPScene(Scene):
    def construct(self):
        title = Text("POO en Dart", font_size=44, color=DART_COLOR)
        title.to_edge(UP, buff=0.5)

        oop_code = '''// Clases
class Persona {
  final String nombre;
  final int edad;

  Persona(this.nombre, this.edad);

  void saludar() => print('Hola, soy $nombre');
}

// Herencia
class Estudiante extends Persona {
  final String curso;

  Estudiante(String nombre, int edad, this.curso)
      : super(nombre, edad);

  @override
  void saludar() => print('Soy $nombre del curso $curso');
}

// Mixins
mixin Logger {
  void log(String msg) => print('[LOG] $msg');
}

// Mixin en clase
class Servicio with Logger {
  void procesar() => log('Procesando...');
}'''

        dart_code = Code(
            code_string=oop_code,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        dart_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WidgetIntroScene(Scene):
    def construct(self):
        title = Text("Introduccion a Widgets", font_size=42, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        explanation = Text(
            "Todo en Flutter es un widget - botones, textos, layouts, etc.",
            font_size=24,
            color=TEXT_COLOR,
        )
        explanation.next_to(title, DOWN, buff=0.5)

        hierarchy = VGroup(
            Text("Widget Tree:", font_size=24, color=HIGHLIGHT_COLOR),
            Text("MaterialApp", font_size=20, color=ACCENT_COLOR),
            Text("  Scaffold", font_size=18, color=SECONDARY_COLOR),
            Text("    AppBar", font_size=16, color=TEXT_COLOR),
            Text("    Column", font_size=16, color=TEXT_COLOR),
            Text("      Text", font_size=14, color=CURVE_COLOR),
            Text("      ElevatedButton", font_size=14, color=CURVE_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        hierarchy.next_to(explanation, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(explanation), run_time=0.8)
        self.play(FadeIn(hierarchy), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class StatelessWidgetScene(Scene):
    def construct(self):
        title = Text("StatelessWidget", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        stateless = '''import 'package:flutter/material.dart';

class Saludo extends StatelessWidget {
  final String nombre;

  const Saludo({super.key, required this.nombre});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.blue.shade100,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Text(
        'Hola, $nombre!',
        style: const TextStyle(
          fontSize: 24,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}

// Uso
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Saludo(nombre: 'Juan'),
      ),
    );
  }
}'''

        dart_code = Code(
            code_string=stateless,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dart_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class StatefulWidgetScene(Scene):
    def construct(self):
        title = Text("StatefulWidget", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        stateful = '''class Contador extends StatefulWidget {
  const Contador({super.key});

  @override
  State<Contador> createState() => _ContadorState();
}

class _ContadorState extends State<Contador> {
  int _contador = 0;

  void _incrementar() {
    setState(() {
      _contador++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(
          '$_contador',
          style: const TextStyle(fontSize: 48),
        ),
        const SizedBox(height: 20),
        ElevatedButton(
          onPressed: _incrementar,
          child: const Text('Incrementar'),
        ),
      ],
    );
  }
}'''

        dart_code = Code(
            code_string=stateful,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        dart_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CommonWidgetsScene(Scene):
    def construct(self):
        title = Text("Widgets Comunes", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        text_widgets = '''// Textos
Text('Hola Mundo', style: TextStyle(fontSize: 24, color: Colors.blue))
Text.rich(TextSpan(text: 'Hola ', children: [
  TextSpan(text: 'negrita', style: TextStyle(fontWeight: FontWeight.bold)),
]))

// Iconos
Icon(Icons.add, size: 48, color: Colors.red)
IconButton(icon: const Icon(Icons.star), onPressed: () {})

// Imagenes
Image.network('https://ejemplo.com/imagen.png')
Image.asset('assets/imagen.png')
Image.memory(bytes)'''

        text_code = Code(
            code_string=text_widgets,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        text_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        layout_widgets = '''// Layout basico
Container(
  padding: EdgeInsets.all(16),
  margin: EdgeInsets.all(8),
  decoration: BoxDecoration(color: Colors.white),
  child: Child(),
)

// Column, Row, Stack
Column(children: [w1, w2, w3], mainAxisAlignment: MainAxisAlignment.center)
Row(children: [w1, w2], crossAxisAlignment: CrossAxisAlignment.center)
Stack(children: [w1, Positioned(right: 10, top: 10, child: w2)])

// ListView
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => ListTile(title: Text(items[index])),
)'''

        layout_code = Code(
            code_string=layout_widgets,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        layout_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(text_code), run_time=1)
        self.play(Create(layout_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LayoutsScene(Scene):
    def construct(self):
        title = Text("Layouts en Flutter", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        container = '''// Container
Container(
  width: 200,
  height: 100,
  padding: EdgeInsets.all(16),
  margin: EdgeInsets.all(8),
  decoration: BoxDecoration(
    color: Colors.blue,
    borderRadius: BorderRadius.circular(12),
    border: Border.all(color: Colors.black, width: 2),
    boxShadow: [
      BoxShadow(color: Colors.black26, blurRadius: 8, offset: Offset(0, 4))
    ],
  ),
  child: Center(child: Text('Contenido')),
)'''

        flex = '''// Flex - Row y Column
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  crossAxisAlignment: CrossAxisAlignment.center,
  children: [Icon1, Icon2, Icon3],
)

Column(
  mainAxisSize: MainAxisSize.min,
  children: [Text1, Text2, Text3],
)

// Expanded
Row(children: [
  Expanded(flex: 2, child: Container(color: Colors.red)),
  Expanded(flex: 1, child: Container(color: Colors.blue)),
])'''

        container_code = Code(
            code_string=container,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        container_code.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        flex_code = Code(
            code_string=flex,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        flex_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(container_code), run_time=1)
        self.play(Create(flex_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class MaterialDesignScene(Scene):
    def construct(self):
        title = Text("Material Design Widgets", font_size=42, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        buttons = '''// Botones
ElevatedButton(
  onPressed: () {},
  child: Text('Elevated'),
)

TextButton(
  onPressed: () {},
  child: Text('Text Button'),
)

OutlinedButton(
  onPressed: () {},
  child: Text('Outlined'),
)

FloatingActionButton(
  onPressed: () {},
  child: Icon(Icons.add),
)

// Icon Button
IconButton(
  icon: Icon(Icons.favorite),
  onPressed: () {},
)'''

        input = '''// Inputs
TextField(
  decoration: InputDecoration(
    labelText: 'Nombre',
    hintText: 'Ingrese su nombre',
    border: OutlineInputBorder(),
    prefixIcon: Icon(Icons.person),
    suffixIcon: IconButton(icon: Icon(Icons.clear), onPressed: () {}),
  ),
  onChanged: (value) => print(value),
  controller: TextEditingController(),
)

// Checkbox, Switch, Radio
Checkbox(value: true, onChanged: (v) {})
Switch(value: true, onChanged: (v) {})
Radio(value: 1, groupValue: 1, onChanged: (v) {})

// Dropdown
DropdownButton(
  value: selectedValue,
  items: items.map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
  onChanged: (v) {},
)'''

        buttons_code = Code(
            code_string=buttons,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        buttons_code.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        input_code = Code(
            code_string=input,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        input_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(buttons_code), run_time=1)
        self.play(Create(input_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class NavigationScene(Scene):
    def construct(self):
        title = Text("Navegacion en Flutter", font_size=42, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        basic_nav = '''// Navegacion basica
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => NuevaPantalla()),
);

Navigator.pop(context);

// Con datos
Navigator.push(
  context,
  MaterialPageRoute(
    builder: (context) => DetallePage(producto: producto),
  ),
);

// Obtener resultado
final result = await Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => SelectorPage()),
);'''

        routes = '''// Named Routes
MaterialApp(
  routes: {
    '/': (context) => HomePage(),
    '/detalle': (context) => DetallePage(),
    '/perfil': (context) => PerfilPage(),
  },
);

// Navigation
Navigator.pushNamed(context, '/detalle');
Navigator.pushNamed(context, '/perfil', arguments: data);

// Obtener argumentos
final args = ModalRoute.of(context).settings.arguments as Map;'''

        basic_code = Code(
            code_string=basic_nav,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        basic_code.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        routes_code = Code(
            code_string=routes,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        routes_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(basic_code), run_time=1)
        self.play(Create(routes_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class GoRouterScene(Scene):
    def construct(self):
        title = Text("GoRouter - Navegacion Declarativa", font_size=38, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        setup = '''// dependencia: flutter_bloc, go_router

final router = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => HomePage(),
    ),
    GoRoute(
      path: '/productos/:id',
      builder: (context, state) {
        final id = state.pathParameters['id']!;
        return DetallePage(productoId: id);
      },
    ),
    GoRoute(
      path: '/perfil',
      builder: (context, state) => PerfilPage(),
      redirect: (context, state) {
        // Redireccion condicional
        if (!isLoggedIn) return '/login';
        return null;
      },
    ),
  ],
);

// Uso en MaterialApp
MaterialApp.router(
  routerConfig: router,
  builder: (context, child) => AppShell(child: child),
);'''

        dart_code = Code(
            code_string=setup,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dart_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class StateManagementIntroScene(Scene):
    def construct(self):
        title = Text("State Management", font_size=48, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        options = VGroup(
            Text("Opciones de Estado:", font_size=26, color=HIGHLIGHT_COLOR),
            Text("1. setState - Estado local simple", font_size=22, color=TEXT_COLOR),
            Text("2. Provider - Inyeccion de dependencias ligera", font_size=22, color=TEXT_COLOR),
            Text("3. Riverpod - Provider mejorado con tipado", font_size=22, color=TEXT_COLOR),
            Text("4. BLoC - Streams y eventos", font_size=22, color=TEXT_COLOR),
            Text("5. GetX - Todo en uno", font_size=22, color=TEXT_COLOR),
            Text("6. Redux - Unidireccional", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        options.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for o in options:
            self.play(FadeIn(o, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ProviderScene(Scene):
    def construct(self):
        title = Text("Provider", font_size=48, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        model = '''// Modelo
class ContadorModel extends ChangeNotifier {
  int _contador = 0;

  int get contador => _contador;

  void incrementar() {
    _contador++;
    notifyListeners();
  }

  void decrementar() {
    _contador--;
    notifyListeners();
  }
}'''

        provider_code = Code(
            code_string=model,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        provider_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(UP * 0.8)

        consumer = '''// Proveedor en main
runApp(
  ChangeNotifierProvider(
    create: (_) => ContadorModel(),
    child: const MyApp(),
  ),
);

// Consumo en widgets
class Pantalla extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer<ContadorModel>(
      builder: (context, modelo, child) {
        return Column(
          children: [
            Text('${modelo.contador}'),
            ElevatedButton(
              onPressed: () => modelo.incrementar(),
              child: Text('+'),
            ),
          ],
        );
      },
    );
  }
}

// Sin rebuild
Builder(
  builder: (context) {
    final modelo = context.read<ContadorModel>();
    return Text('${modelo.contador}');
  },
)'''

        consumer_code = Code(
            code_string=consumer,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        consumer_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(provider_code), run_time=1)
        self.play(Create(consumer_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RiverpodScene(Scene):
    def construct(self):
        title = Text("Riverpod", font_size=48, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        providers = '''// Providers
final contadorProvider = StateProvider((ref) => 0);

final nombreProvider = Provider<String>((ref) {
  final contador = ref.watch(contadorProvider);
  return 'Contador: $contador';
});

final dataProvider = FutureProvider<List<Producto>>((ref) async {
  final api = ref.watch(apiServiceProvider);
  return api.getProductos();
});

final streamProvider = StreamProvider<int>((ref) {
  return Stream.periodic(Duration(seconds: 1), (x) => x);
});'''

        riverpod_code = Code(
            code_string=providers,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        riverpod_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(riverpod_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class BlocPatternScene(Scene):
    def construct(self):
        title = Text("BLoC Pattern", font_size=48, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        events = '''// Events
abstract class ContadorEvent {}

class IncrementarEvent extends ContadorEvent {}
class DecrementarEvent extends ContadorEvent {}
class ResetEvent extends ContadorEvent {}'''

        state = '''// State
class ContadorState {
  final int valor;
  final String mensaje;

  ContadorState({required this.valor, this.mensaje = ''});

  ContadorState copyWith({int? valor, String? mensaje}) {
    return ContadorState(
      valor: valor ?? this.valor,
      mensaje: mensaje ?? this.mensaje,
    );
  }
}'''

        bloc = '''// Bloc
class ContadorBloc extends Bloc<ContadorEvent, ContadorState> {
  ContadorBloc() : super(ContadorState(valor: 0)) {
    on<IncrementarEvent>((event, emit) {
      emit(state.copyWith(valor: state.valor + 1));
    });

    on<DecrementarEvent>((event, emit) {
      emit(state.copyWith(valor: state.valor - 1));
    });

    on<ResetEvent>((event, emit) {
      emit(ContadorState(valor: 0, mensaje: 'Reseteado'));
    });
  }
}

// Uso
BlocBuilder<ContadorBloc, ContadorState>(
  builder: (context, state) => Text('${state.valor}'),
)

BlocListener<ContadorBloc, ContadorState>(
  listener: (context, state) {
    if (state.mensaje.isNotEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(state.mensaje)),
      );
    }
  },
  child: Child(),
)'''

        events_code = Code(
            code_string=events,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        events_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        state_code = Code(
            code_string=state,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        state_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(UP * 0.5)

        bloc_code = Code(
            code_string=bloc,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        bloc_code.scale(0.9).to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(events_code), run_time=0.8)
        self.play(Create(state_code), run_time=0.8)
        self.play(Create(bloc_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class HTTPCallsScene(Scene):
    def construct(self):
        title = Text("Llamadas HTTP", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        http_example = '''// Usando http package
import 'package:http/http.dart' as http;
import 'dart:convert';

final url = Uri.parse('https://api.ejemplo.com/usuarios');

final response = await http.get(
  url,
  headers: {'Content-Type': 'application/json'},
);

if (response.statusCode == 200) {
  final List<dynamic> data = json.decode(response.body);
  // Procesar datos
} else {
  throw Exception('Error: ${response.statusCode}');
}

// POST
final postResponse = await http.post(
  url,
  headers: {'Content-Type': 'application/json'},
  body: json.encode({'nombre': 'Juan', 'edad': 25}),
);

// PUT
final putResponse = await http.put(
  Uri.parse('https://api.ejemplo.com/usuarios/1'),
  body: json.encode({'nombre': 'Juan Actualizado'}),
);

// DELETE
await http.delete(Uri.parse('https://api.ejemplo.com/usuarios/1'));'''

        dart_code = Code(
            code_string=http_example,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dart_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DioClientScene(Scene):
    def construct(self):
        title = Text("Dio - Cliente HTTP Avanzado", font_size=40, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        dio_setup = '''// Configuracion de Dio
class ApiClient {
  late final Dio _dio;

  ApiClient() {
    _dio = Dio(BaseOptions(
      baseUrl: 'https://api.ejemplo.com',
      connectTimeout: const Duration(seconds: 30),
      receiveTimeout: const Duration(seconds: 30),
      headers: {'Content-Type': 'application/json'},
    ));

    _dio.interceptors.add(LogInterceptor(
      requestBody: true,
      responseBody: true,
      logPrint: (obj) => print(obj),
    ));

    _dio.interceptors.add(InterceptorsWrapper(
      onRequest: (options, handler) {
        // Agregar token
        options.headers['Authorization'] = 'Bearer $token';
        return handler.next(options);
      },
      onError: (error, handler) {
        // Manejo de errores global
        if (error.response?.statusCode == 401) {
          // Redirigir a login
        }
        return handler.next(error);
      },
    ));
  }

  Future<List<Usuario>> getUsuarios() async {
    final response = await _dio.get('/usuarios');
    return (response.data as List).map((e) => Usuario.fromJson(e)).toList();
  }

  Future<Usuario> crearUsuario(Usuario usuario) async {
    final response = await _dio.post('/usuarios', data: usuario.toJson());
    return Usuario.fromJson(response.data);
  }
}'''

        dart_code = Code(
            code_string=dio_setup,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dart_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LocalStorageScene(Scene):
    def construct(self):
        title = Text("Almacenamiento Local", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        shared_prefs = '''// SharedPreferences
import 'package:shared_preferences/shared_preferences.dart';

// Guardar
final prefs = await SharedPreferences.getInstance();
await prefs.setString('nombre', 'Juan');
await prefs.setInt('edad', 25);
await prefs.setBool('activo', true);
await prefs.setDouble('altura', 1.75);
await prefs.setStringList('colores', ['rojo', 'azul']);

// Leer
final nombre = prefs.getString('nombre') ?? '';
final edad = prefs.getInt('edad') ?? 0;
final activo = prefs.getBool('activo') ?? false;

// Eliminar
await prefs.remove('nombre');
await prefs.clear();'''

        sqflite = '''// SQLite con sqflite
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

final db = await openDatabase(
  join(await getDatabasesPath(), 'miapp.db'),
  version: 1,
  onCreate: (db, version) async {
    await db.execute('''
      CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        edad INTEGER
      )
    ''');
  },
);

// CRUD
final id = await db.insert('usuarios', {'nombre': 'Juan', 'email': 'juan@test.com', 'edad': 25});

final usuarios = await db.query('usuarios', where: 'edad > ?', whereArgs: [18]);

await db.update('usuarios', {'nombre': 'Juan Actualizado'}, where: 'id = ?', whereArgs: [id]);

await db.delete('usuarios', where: 'id = ?', whereArgs: [id]);'''

        prefs_code = Code(
            code_string=shared_prefs,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        prefs_code.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        sqflite_code = Code(
            code_string=sqflite,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        sqflite_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(prefs_code), run_time=1)
        self.play(Create(sqflite_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FirebaseScene(Scene):
    def construct(self):
        title = Text("Firebase Integration", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        firebase_setup = '''// pubspec.yaml dependencies
firebase_core: ^3.0.0
firebase_auth: ^4.0.0
cloud_firestore: ^4.0.0
firebase_storage: ^12.0.0
firebase_messaging: ^14.0.0

// main.dart
import 'package:firebase_core/firebase_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: FirebaseOptions(
      apiKey: 'your-api-key',
      appId: 'your-app-id',
      messagingSenderId: 'your-sender-id',
      projectId: 'your-project-id',
    ),
  );
  runApp(const MyApp());
}'''

        auth = '''// Firebase Auth
import 'package:firebase_auth/firebase_auth.dart';

final auth = FirebaseAuth.instance;

// Registro
final credencial = await auth.createUserWithEmailAndPassword(
  email: 'juan@test.com',
  password: 'password123',
);

// Login
final credencial = await auth.signInWithEmailAndPassword(
  email: 'juan@test.com',
  password: 'password123',
);

final user = credencial.user;
print(user?.uid);

// Cerrar sesion
await auth.signOut();

// Estado actual
final currentUser = auth.currentUser;
if (currentUser != null) {
  print('Logged in as: ${currentUser.email}');
}

// Escuchar cambios
auth.authStateChanges().listen((user) {
  if (user == null) {
    print('Logged out');
  } else {
    print('Logged in: ${user.email}');
  }
});'''

        firestore = '''// Cloud Firestore
import 'package:cloud_firestore/cloud_firestore.dart';

final firestore = FirebaseFirestore.instance;

// Coleccion
final usuariosRef = firestore.collection('usuarios');

// Create
await usuariosRef.add({
  'nombre': 'Juan',
  'email': 'juan@test.com',
  'edad': 25,
});

// Read
final snapshot = await usuariosRef.get();
for (final doc in snapshot.docs) {
  print(doc.data());
}

// Query
final query = await usuariosRef.where('edad', isGreaterThan: 18).get();

// Update
await usuariosRef.doc('docId').update({
  'nombre': 'Juan Actualizado',
});

// Delete
await usuariosRef.doc('docId').delete();

// Realtime
usuariosRef.snapshots().listen((snapshot) {
  snapshot.docChanges.forEach((change) {
    print(change.type); // added, modified, removed
  });
});'''

        firebase_code = Code(
            code_string=firebase_setup,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        firebase_code.scale(0.7).to_edge(LEFT, buff=0.3).shift(UP * 0.8)

        auth_code = Code(
            code_string=auth,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        auth_code.scale(0.7).to_edge(RIGHT, buff=0.3).shift(UP * 0.8)

        firestore_code = Code(
            code_string=firestore,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        firestore_code.scale(0.7).next_to(firebase_code, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(firebase_code), run_time=1)
        self.play(Create(auth_code), run_time=1)
        self.play(Create(firestore_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AnimationsScene(Scene):
    def construct(self):
        title = Text("Animaciones en Flutter", font_size=42, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        explicit = '''// Animacion Explicita
class AnimationWidget extends StatefulWidget {
  @override
  State<AnimationWidget> createState() => _AnimationWidgetState();
}

class _AnimationWidgetState extends State<AnimationWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    );
    _animation = Tween<double>(begin: 0, end: 1).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    );
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        return Opacity(opacity: _animation.value, child: child);
      },
      child: const Text('Animado'),
    );
  }
}'''

        implicit = '''// Animacion Implicita
AnimatedContainer(
  duration: Duration(milliseconds: 300),
  width: _expanded ? 200 : 50,
  height: _expanded ? 200 : 50,
  color: _expanded ? Colors.blue : Colors.red,
  child: Text('Tap me'),
)

AnimatedOpacity(
  duration: Duration(milliseconds: 500),
  opacity: _visible ? 1.0 : 0.0,
  child: const Text('Fade'),
)

// AnimatedCrossFade
AnimatedCrossFade(
  firstChild: const FlutterLogo(size: 100),
  secondChild: const Icon(Icons.star, size: 100),
  crossFadeState: _showLogo
    ? CrossFadeState.showFirst
    : CrossFadeState.showSecond,
  duration: Duration(seconds: 1),
)'''

        explicit_code = Code(
            code_string=explicit,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        explicit_code.scale(0.7).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        implicit_code = Code(
            code_string=implicit,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=14,
        )
        implicit_code.scale(0.7).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(explicit_code), run_time=1)
        self.play(Create(implicit_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FormsAndValidationScene(Scene):
    def construct(self):
        title = Text("Formularios y Validacion", font_size=42, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        form = '''final _formKey = GlobalKey<FormState>();

Form(
  key: _formKey,
  child: Column(
    children: [
      TextFormField(
        decoration: InputDecoration(labelText: 'Nombre'),
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Por favor ingrese su nombre';
          }
          if (value.length < 3) {
            return 'El nombre debe tener al menos 3 caracteres';
          }
          return null;
        },
      ),
      TextFormField(
        decoration: InputDecoration(labelText: 'Email'),
        keyboardType: TextInputType.emailAddress,
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Por favor ingrese un email';
          }
          if (!value.contains('@')) {
            return 'Ingrese un email valido';
          }
          return null;
        },
      ),
      TextFormField(
        decoration: InputDecoration(labelText: 'Password'),
        obscureText: true,
        validator: (value) {
          if (value == null || value.length < 6) {
            return 'La contrasena debe tener al menos 6 caracteres';
          }
          return null;
        },
      ),
      ElevatedButton(
        onPressed: () {
          if (_formKey.currentState!.validate()) {
            // Enviar datos
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(content: Text('Procesando...')),
            );
          }
        },
        child: Text('Enviar'),
      ),
    ],
  ),
)'''

        dart_code = Code(
            code_string=form,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dart_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(dart_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TestingScene(Scene):
    def construct(self):
        title = Text("Testing en Flutter", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        test_types = VGroup(
            Text("Unit Tests - Test de logica de negocio", font_size=22, color=HIGHLIGHT_COLOR),
            Text("Widget Tests - Test de widgets individuales", font_size=22, color=ACCENT_COLOR),
            Text("Integration Tests - Test de flujos completos", font_size=22, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        test_types.next_to(title, DOWN, buff=0.6)

        unit_test = '''// Test unitario
import 'package:flutter_test/flutter_test';
import 'package:miapp/models/calculadora.dart';

void main() {
  group('Calculadora', () {
    test('suma de dos numeros', () {
      final calc = Calculadora();
      expect(calc.suma(2, 3), 5);
    });

    test('division por cero lanza excepcion', () {
      final calc = Calculadora();
      expect(
        () => calc.division(10, 0),
        throwsA(isA<DivideByZeroException>()),
      );
    });
  });
}'''

        widget_test = '''// Widget test
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:miapp/widgets/btn.dart';

void main() {
  testWidgets('Boton muestra texto correctamente', (WidgetTester tester) async {
    await tester.pumpWidget(
      const MaterialApp(
        home: Scaffold(
          body: MiBoton(texto: 'Click me'),
        ),
      ),
    );

    expect(find.text('Click me'), findsOneWidget);
    expect(find.byType(ElevatedButton), findsOneWidget);
  });

  testWidgets('Boton responde al tap', (WidgetTester tester) async {
    bool presionado = false;

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: MiBoton(
            texto: 'Click',
            onPressed: () => presionado = true,
          ),
        ),
      ),
    );

    await tester.tap(find.byType(ElevatedButton));
    await tester.pump();

    expect(presionado, true);
  });
}'''

        unit_code = Code(
            code_string=unit_test,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        unit_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(DOWN * 0.3)

        widget_code = Code(
            code_string=widget_test,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        widget_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.8)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(test_types), run_time=1)
        self.play(Create(unit_code), run_time=1)
        self.play(Create(widget_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class BuildReleaseScene(Scene):
    def construct(self):
        title = Text("Build y Release", font_size=48, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        build_commands = '''// Debug build
flutter build apk --debug
flutter build ios --debug

// Release build
flutter build apk --release
flutter build ios --release --no-codesign

// Web
flutter build web --release

// Build runner (generar archivos)
flutter pub run build_runner build

// Limpiar cache
flutter clean
flutter pub get

// Actualizar paquetes
flutter pub upgrade'''

        app_store = '''// iOS App Store
1. Crear certificados en Apple Developer Portal
2. Configurar App Store Connect
3. Build: flutter build ios --release --no-codesign
4. Subir con Transporter o xcodebuild

// Play Store (Android)
1. Crear keystore para signing
2. Configurar build.gradle
3. Build: flutter build apk --release
4. Firmar APK con jarsigner
5. Subir a Play Store Console

// App Bundle (recomendado)
flutter build appbundle --release'''

        build_code = Code(
            code_string=build_commands,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        build_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        store_code = Code(
            code_string=app_store,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        store_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(build_code), run_time=1)
        self.play(Create(store_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CI_CDScene(Scene):
    def construct(self):
        title = Text("CI/CD con Flutter", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        github_actions = '''# .github/workflows/flutter.yml
name: Flutter CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.24.0'
      - run: flutter pub get
      - run: flutter test
      - run: flutter build apk --debug
      - uses: actions/upload-artifact@v3
        with:
          name: apk
          path: build/app/outputs/flutter-apk/app-debug.apk'''

        codemagic = '''# codemagic.yaml
workflows:
  flutter-workflow:
    name: Flutter Workflow
    environment:
      flutter: stable
      xcode: latest
      cocoapods: default
    scripts:
      - name: Get dependencies
        script: |
          flutter pub get
      - name: Run tests
        script: |
          flutter test
      - name: Build iOS
        script: |
          flutter build ipa --release
      - name: Build Android
        script: |
          flutter build apk --release
    artifacts:
      - build/ios/ipa/*.ipa
      - build/app/outputs/flutter-apk/*.apk'''

        github_code = Code(
            code_string=github_actions,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        github_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.5)

        codemagic_code = Code(
            code_string=codemagic,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        codemagic_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(github_code), run_time=1)
        self.play(Create(codemagic_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PlatformChannelsScene(Scene):
    def construct(self):
        title = Text("Platform Channels", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        platform_channel = '''// Flutter - Comunicacion nativa
import 'package:flutter/services.dart';

class PlatformChannel {
  static const platform = MethodChannel('com.example/native');

  Future<String> getNativeData() async {
    try {
      final String result = await platform.invokeMethod('getData');
      return result;
    } on PlatformException catch (e) {
      return 'Error: ${e.message}';
    }
  }

  Future<int> calculateNative(int a, int b) async {
    final result = await platform.invokeMethod('calculate', {
      'a': a,
      'b': b,
    });
    return result as int;
  }
}'''

        android_impl = '''// Android - Kotlin (MainActivity.kt)
class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.example/native"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler { call, result ->
            when (call.method) {
                "getData" -> {
                    result.success("Data from Android")
                }
                "calculate" -> {
                    val a = call.argument<Int>("a") ?: 0
                    val b = call.argument<Int>("b") ?: 0
                    result.success(a + b)
                }
                else -> {
                    result.notImplemented()
                }
            }
        }
    }
}'''

        flutter_code = Code(
            code_string=platform_channel,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        flutter_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        android_code = Code(
            code_string=android_impl,
            language="kotlin",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        android_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(flutter_code), run_time=1)
        self.play(Create(android_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PerformanceScene(Scene):
    def construct(self):
        title = Text("Optimizacion de Rendimiento", font_size=40, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        tips = VGroup(
            Text("1. Evita rebuilds innecesarios - Usa const y Consumer", font_size=20, color=HIGHLIGHT_COLOR),
            Text("2. ListView.builder para listas grandes", font_size=20, color=TEXT_COLOR),
            Text("3. Cache imagenes con cached_network_image", font_size=20, color=TEXT_COLOR),
            Text("4. Usa RepaintBoundary para areas estaticas", font_size=20, color=TEXT_COLOR),
            Text("5. Evita operadores complejos en build()", font_size=20, color=TEXT_COLOR),
            Text("6. Usa keys apropiadamente para mantenimiento de estado", font_size=20, color=TEXT_COLOR),
            Text("7. Measure performance con DevTools", font_size=20, color=TEXT_COLOR),
            Text("8. Avoid loading large assets at startup", font_size=20, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        tips.next_to(title, DOWN, buff=0.6)

        const_example = '''// Bad - se reconstruye cada vez
Text('${widget.nombre} tiene ${contador} clicks');

// Good - solo rebuild cuando cambia
Text(
  '$nombre tiene $contador clicks',
  style: const TextStyle(fontSize: 16),  // const
);

// Good - Usa const constructor
const MiWidget()

// Bad - sin const
MiWidget(data: data)

// Good - con const
const MiWidget(data: data)'''

        const_code = Code(
            code_string=const_example,
            language="dart",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        const_code.scale(0.85).next_to(tips, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(tips), run_time=1)
        self.play(Create(const_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PubPackagesScene(Scene):
    def construct(self):
        title = Text("Paquetes Populares", font_size=44, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.5)

        packages = VGroup(
            Text("State Management:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("provider, flutter_bloc, riverpod, get, mobx", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("Networking:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("http, dio, chopper", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("Storage:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("shared_preferences, sqflite, hive, drift", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("UI/UX:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("flutter_svg, cached_network_image, shimmer, flutter_animate", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("Navigation:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("go_router, auto_route, beamer", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("Utilities:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("json_serializable, freezed, intl, uuid, timeago", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        packages.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(packages, shift=RIGHT * 0.2), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Flutter", font_size=42, color=FLUTTER_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Flutter: Framework cross-platform de Google", font_size=22, color=TEXT_COLOR),
            Text("Dart: Lenguaje moderno con null safety y tipado estatico", font_size=22, color=TEXT_COLOR),
            Text("Widgets: Todo es un widget - composicion reusable", font_size=22, color=TEXT_COLOR),
            Text("State: setState, Provider, Riverpod, BLoC", font_size=22, color=TEXT_COLOR),
            Text("HTTP: http package, Dio para clientes avanzados", font_size=22, color=TEXT_COLOR),
            Text("Storage: SharedPreferences, SQLite, Hive", font_size=22, color=TEXT_COLOR),
            Text("Firebase: Auth, Firestore, Storage, Cloud Functions", font_size=22, color=TEXT_COLOR),
            Text("Animations: Explicitas e implicitas con AnimatedBuilder", font_size=22, color=TEXT_COLOR),
            Text("Testing: Unit, Widget, Integration tests", font_size=22, color=TEXT_COLOR),
            Text("CI/CD: GitHub Actions, Codemagic, Fastlane", font_size=22, color=TEXT_COLOR),
            Text("Platform Channels: Comunicacion con codigo nativo", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Framework dominante para desarrollo cross-platform moderno",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FlutterFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        FlutterHistoryScene.construct(self)
        WhyFlutterScene.construct(self)
        DartLanguageScene.construct(self)
        DartFunctionsScene.construct(self)
        DartOOPScene.construct(self)
        WidgetIntroScene.construct(self)
        StatelessWidgetScene.construct(self)
        StatefulWidgetScene.construct(self)
        CommonWidgetsScene.construct(self)
        LayoutsScene.construct(self)
        MaterialDesignScene.construct(self)
        NavigationScene.construct(self)
        GoRouterScene.construct(self)
        StateManagementIntroScene.construct(self)
        ProviderScene.construct(self)
        RiverpodScene.construct(self)
        BlocPatternScene.construct(self)
        HTTPCallsScene.construct(self)
        DioClientScene.construct(self)
        LocalStorageScene.construct(self)
        FirebaseScene.construct(self)
        AnimationsScene.construct(self)
        FormsAndValidationScene.construct(self)
        TestingScene.construct(self)
        BuildReleaseScene.construct(self)
        CI_CDScene.construct(self)
        PlatformChannelsScene.construct(self)
        PerformanceScene.construct(self)
        PubPackagesScene.construct(self)
        ConclusionScene.construct(self)
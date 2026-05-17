from manim import *
import numpy as np

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
REACT_COLOR = "#61dafb"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("React", font_size=60, color=REACT_COLOR).set_color_by_gradient(REACT_COLOR, PRIMARY_COLOR)
        subtitle = Text("Libreria JavaScript para construir interfaces", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class ComponentsScene(Scene):
    def construct(self):
        title = Text("Componentes", font_size=48, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Componente funcional
function Saludo({ nombre }) {
  return <h1>Hola {nombre}!</h1>;
}

// Componente con estado
function Contador() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Contador: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Incrementar
      </button>
    </div>
  );
}

// JSX Rules
// - className en lugar de class
// - camelCase para atributos
// -.self-closing tags deben cerrarse
// - Un solo elemento raiz

// Renderizado condicional
{isLogged ? <Dashboard /> : <Login />}

// Renderizado de listas
{lista.map(item => (
  <Item key={item.id} datos={item} />
))}'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class HooksScene(Scene):
    def construct(self):
        title = Text("Hooks", font_size=48, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// useState
const [state, setState] = useState(initialValue);

// useEffect
useEffect(() => {
  // Se ejecuta despues del render
  fetchData();
  return () => cleanup(); // Cleanup
}, [dependency]); // Re-ejecutar si cambia

// useContext
const theme = useContext(ThemeContext);

// useReducer
const [state, dispatch] = useReducer(
  (state, action) => {
    switch (action.type) {
      case "INCREMENT":
        return { count: state.count + 1 };
      case "DECREMENT":
        return { count: state.count - 1 };
      default:
        return state;
    }
  },
  { count: 0 }
);

// useMemo - cachear calculos
const memoizedValue = useMemo(
  () => computeExpensiveValue(a, b),
  [a, b]
);

// useCallback - cachear funciones
const handleClick = useCallback(
  () => doSomething(a, b),
  [a, b]
);

// Custom Hook
function useWindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });
  // ... listeners
  return size;
}'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class RouterScene(Scene):
    def construct(self):
        title = Text("React Router", font_size=48, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// npm install react-router-dom

import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  useParams,
  useNavigate
} from "react-router-dom";

// Configuracion
function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Inicio</Link>
        <Link to="/productos">Productos</Link>
        <Link to="/contacto">Contacto</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/productos" element={<Productos />} />
        <Route path="/productos/:id" element={<DetalleProducto />} />
        <Route path="/contacto" element={<Contacto />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

// Navegacion programatica
function Producto() {
  const navigate = useNavigate();
  const { id } = useParams();

  const irAInicio = () => navigate("/");

  return (
    <div>
      <h1>Producto {id}</h1>
      <button onClick={irAInicio}>Volver</button>
    </div>
  );
}

// Rutas protegidas
function ProtectedRoute({ children }) {
  const autenticado = useAuth();
  return autenticado ? children : <Navigate to="/login" />;
}'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class StateManagementScene(Scene):
    def construct(self):
        title = Text("Estado Global - Redux/Zustand", font_size=40, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// ZUSTAND (mas simple)
import { create } from "zustand";

const useStore = create((set) => ({
  count: 0,
  user: null,
  increment: () => set((state) => ({
    count: state.count + 1
  })),
  setUser: (user) => set({ user }),
}));

// Uso
function Contador() {
  const { count, increment } = useStore();
  return <button onClick={increment}>{count}</button>;
}

// REDUX TOOLKIT (mas robusto)
import { configureStore, createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; },
    decrement: (state) => { state.value -= 1; },
  },
});

const store = configureStore({
  reducer: {
    counter: counterSlice.reducer,
  },
});

// Provider en App
import { Provider } from "react-redux";

<Provider store={store}>
  <App />
</Provider>

// useSelector y useDispatch
const count = useSelector(state => state.counter.value);
const dispatch = useDispatch();
dispatch(increment());'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class FormsScene(Scene):
    def construct(self):
        title = Text("Formularios y Validacion", font_size=42, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Formulario controlado
function Formulario() {
  const [form, setForm] = useState({
    nombre: "",
    email: "",
    password: ""
  });
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const validate = () => {
    const newErrors = {};
    if (!form.nombre) newErrors.nombre = "Requerido";
    if (!form.email.includes("@")) {
      newErrors.email = "Email invalido";
    }
    if (form.password.length < 6) {
      newErrors.password = "Minimo 6 caracteres";
    }
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const errs = validate();
    if (Object.keys(errs).length === 0) {
      // Enviar datos
    } else {
      setErrors(errs);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="nombre"
        value={form.nombre}
        onChange={handleChange}
      />
      {errors.nombre && <span>{errors.nombre}</span>}
      {/* ... */}
    </form>
  );
}

// React Hook Form
import { useForm } from "react-hook-form";

function FormConHook() {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data) => console.log(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("nombre", { required: true })} />
      {errors.nombre && <span>Requerido</span>}
      <input type="submit" />
    </form>
  );
}'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class EffectsScene(Scene):
    def construct(self):
        title = Text("useEffect y Ciclo de Vida", font_size=42, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// componentDidMount
useEffect(() => {
  console.log("Se ejecuta 1 vez al montar");
  fetchData();
}, []);

// componentDidUpdate
useEffect(() => {
  console.log("Se ejecuta cuando 'count' cambia");
}, [count]);

// Cleanup con return
useEffect(() => {
  const subscription = api.subscribe();

  return () => {
    // componentWillUnmount
    subscription.unsubscribe();
  };
}, []);

// Multiples useEffect
useEffect(() => {
  document.title = `Contador: ${count}`;
}, [count]);

useEffect(() => {
  console.log("Otro efecto");
}, [nombre, email]);

// Fetch con useEffect
useEffect(() => {
  let cancel = false;

  async function fetchData() {
    try {
      const res = await fetch(`/api/users/${userId}`);
      const data = await res.json();
      if (!cancel) setUsers(data);
    } catch (error) {
      if (!cancel) setError(error);
    }
  }

  fetchData();
  return () => { cancel = true; };
}, [userId]);

// useLayoutEffect (antes del paint)
useLayoutEffect(() => {
  // Mediciones del DOM sincrono
}, []);'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class APIScene(Scene):
    def construct(self):
        title = Text("Consumo de APIs", font_size=48, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// Fetch basico
async function fetchUsers() {
  const res = await fetch("https://api.example.com/users");
  const data = await res.json();
  return data;
}

// with async/await en componente
function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        const res = await fetch("/api/users");
        if (!res.ok) throw new Error("Error");
        const data = await res.json();
        setUsers(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <Spinner />;
  if (error) return <Error message={error} />;
  return <UserList users={users} />;
}

// Axios
import axios from "axios";

const api = axios.create({
  baseURL: "https://api.example.com",
  timeout: 5000,
  headers: { "Content-Type": "application/json" },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login
    }
    return Promise.reject(error);
  }
);

// POST request
const crearUsuario = async (userData) => {
  const res = await api.post("/users", userData);
  return res.data;
};'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class StylingScene(Scene):
    def construct(self):
        title = Text("Estilos en React", font_size=48, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// CSS Modules
/* Button.module.css */
.button {
  background: blue;
  color: white;
}
.buttonPrimary {
  composes: button;
  background: green;
}

/* Button.jsx */
import styles from "./Button.module.css";
<button className={styles.button}>Click</button>

// Styled Components
import styled from "styled-components";

const Boton = styled.button`
  background: ${props => props.primary ? "blue" : "gray"};
  color: white;
  padding: 10px 20px;
  border-radius: 5px;

  &:hover {
    opacity: 0.9;
  }
`;

// Tailwind CSS
// npm install -D tailwindcss postcss autoprefixer
// npx tailwindcss init -p

<div className="flex items-center justify-between p-4 bg-white shadow-md">
  <h1 className="text-2xl font-bold text-gray-800">Titulo</h1>
  <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
    Accion
  </button>
</div>

// CSS-in-JS con objetos
const estilo = {
  backgroundColor: "blue",
  color: "white",
  padding: "10px 20px",
};
<div style={estilo}>Contenido</div>

// Variables CSS
:root {
  --primary: #3498db;
  --secondary: #2ecc71;
}
<div style={{ "--primary": "red" }}>Dynamic</div>'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class PerformanceScene(Scene):
    def construct(self):
        title = Text("Optimizacion de Performance", font_size=38, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// React.memo
const ComponentePesado = memo(({ data }) => {
  // Solo re-renderiza si 'data' cambia
  return <div>{/* renderizado costoso */}</div>;
});

// useMemo para calculos costosos
function Lista({ items, filtro }) {
  const filtrados = useMemo(() => {
    return items.filter(item =>
      item.nombre.includes(filtro)
    );
  }, [items, filtro]);

  return filtrados.map(item => (
    <Item key={item.id} item={item} />
  ));
}

// useCallback para callbacks
const handleClick = useCallback((id) => {
  console.log("Click", id);
}, []); // Dependencias

// Lazy loading de componentes
const LazyComponent = lazy(() => import("./ heavy"));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <LazyComponent />
    </Suspense>
  );
}

// Fragment para evitar divs innecesarios
<>
  <Componente1 />
  <Componente2 />
</>

// Virtualizacion para listas grandes
import { FixedSizeList } from "react-window";

function ListaVirtual({ items }) {
  return (
    <FixedSizeList
      height={400}
      itemCount={items.length}
      itemSize={50}
      width={300}
    >
      {({ index, style }) => (
        <div style={style}>{items[index].nombre}</div>
      )}
    </FixedSizeList>
  );
}

// useTransition para actualizaciones no urgentes
const [isPending, startTransition] = useTransition();

startTransition(() => {
  setInput(input);
});'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class TestingScene(Scene):
    def construct(self):
        title = Text("Testing con React Testing Library", font_size=38, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// npm install --save-dev @testing-library/react

import { render, screen, fireEvent } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

// Test basico
test("renderiza titulo", () => {
  render(<App />);
  expect(screen.getByText("Hola")).toBeInTheDocument();
});

// Query methods
screen.getByText("texto");        // throws si no existe
screen.queryByText("texto");      // null si no existe
screen.findByText("texto");       // promise cuando existe
screen.getAllByRole("button");    // array de resultados

// fireEvent vs userEvent
fireEvent.click(button);
userEvent.click(button);          // mas realista

// Testing formularios
test("submit del formulario", async () => {
  render(<Formulario />);

  await userEvent.type(
    screen.getByLabelText("Nombre"),
    "Juan"
  );
  await userEvent.click(
    screen.getByRole("button", { name: "Enviar" })
  );

  expect(screen.getByText("Registro exitoso")).toBeInTheDocument();
});

// Mock de fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ id: 1, nombre: "Test" }),
  })
) as jest.Mock;

// Testing asincrono
await waitFor(() => {
  expect(screen.getByText("Cargado")).toBeInTheDocument();
});

// Coverage
// npx react-scripts test --coverage'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class TypeScriptReactScene(Scene):
    def construct(self):
        title = Text("React con TypeScript", font_size=44, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// npx create-react-app app --template typescript

// Props tipadas
interface Props {
  nombre: string;
  edad: number;
  onClick?: () => void;
  children: React.ReactNode;
}

function Componente({ nombre, edad, onClick, children }: Props) {
  return (
    <div onClick={onClick}>
      <h1>{nombre}, {edad}</h1>
      {children}
    </div>
  );
}

// Event handlers tipados
<button
  onClick={(e) => handleClick(e)}
  onChange={(e) => setValue(e.target.value)}
>
  Click
</button>;

// useState tipado
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<User | null>(null);
const [items, setItems] = useState<Item[]>([]);

// Tipos para API responses
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

interface User {
  id: number;
  nombre: string;
  email: string;
}

// Generic components
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map(renderItem)}</ul>;
}

// Refs tipadas
const inputRef = useRef<HTMLInputElement>(null);
inputRef.current?.focus();'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class NextJSScene(Scene):
    def construct(self):
        title = Text("Next.js y SSR", font_size=48, color=REACT_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''// npx create-next-app@latest

// Estructura App Router (Next.js 13+)
app/
  layout.tsx      # Layout raiz
  page.tsx        # Home (/)
  about/
    page.tsx      # (/about)
  api/
    users/
      route.ts    # (/api/users)

// Server Components (default)
async function UsersPage() {
  const res = await fetch("https://api.example.com/users");
  const users = await res.json();

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.nombre}</li>
      ))}
    </ul>
  );
}

// Client Components
"use client";
import { useState } from "react";

export function Contador() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

// Dynamic Routes
app/productos/[id]/page.tsx
export default function ProductoPage({
  params,
}: {
  params: { id: string };
}) {
  return <h1>Producto {params.id}</h1>;
}

// Metadata
export const metadata = {
  title: "Mi App",
  description: "Descripcion de la app",
};

// API Routes
export async function GET() {
  return Response.json({ mensaje: "GET" });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ data: body });
}

// fetch con revalidation
const res = await fetch(url, {
  next: { revalidate: 3600 } // Revalidar cada hora
});'''

        code_str = Code(code=code, language="tsx", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: React", font_size=38, color=REACT_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Componentes funcionales y JSX", font_size=22, color=TEXT_COLOR),
            Text("Hooks: useState, useEffect, useCallback", font_size=22, color=TEXT_COLOR),
            Text("React Router para navegacion", font_size=22, color=TEXT_COLOR),
            Text("Estado global: Redux Toolkit, Zustand", font_size=22, color=TEXT_COLOR),
            Text("Formularios y validacion", font_size=22, color=TEXT_COLOR),
            Text("Consumo de APIs con fetch y Axios", font_size=22, color=TEXT_COLOR),
            Text("Estilos: CSS Modules, Tailwind, Styled", font_size=22, color=TEXT_COLOR),
            Text("Performance: memo, useMemo, lazy", font_size=22, color=TEXT_COLOR),
            Text("Testing con React Testing Library", font_size=22, color=TEXT_COLOR),
            Text("TypeScript para tipado robusto", font_size=22, color=TEXT_COLOR),
            Text("Next.js para SSR y static generation", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Libreria #1 para interfaces web modernas", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class ReactFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        ComponentsScene.construct(self)
        HooksScene.construct(self)
        RouterScene.construct(self)
        StateManagementScene.construct(self)
        FormsScene.construct(self)
        EffectsScene.construct(self)
        APIScene.construct(self)
        StylingScene.construct(self)
        PerformanceScene.construct(self)
        TestingScene.construct(self)
        TypeScriptReactScene.construct(self)
        NextJSScene.construct(self)
        ConclusionScene.construct(self)
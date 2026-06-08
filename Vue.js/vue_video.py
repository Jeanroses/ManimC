from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
VUE_COLOR = "#42b883"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Vue.js", font_size=60, color=VUE_COLOR).set_color_by_gradient(VUE_COLOR, ACCENT_COLOR)
        subtitle = Text("Framework progresivo para interfaces de usuario", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class ComponentesScene(Scene):
    def construct(self):
        title = Text("Componentes y Template Syntax", font_size=42, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Componente basico
<script setup>
import { ref, computed } from "vue"

const nombre = ref("Juan")
const edad = ref(25)

// Computed property
const mensaje = computed(() => {
  return `Hola ${nombre.value}, tienes ${edad.value} anos`
})

// Methods
function incrementar() {
  edad.value++
}

// Watcher
watch(edad, (nuevo, viejo) => {
  console.log(`Edad cambio: ${viejo} -> ${nuevo}`)
})
</script>

<template>
  <div class="container">
    <h1>{{ mensaje }}</h1>
    <input v-model="nombre" placeholder="Nombre" />
    <p>Edad: {{ edad }}</p>
    <button @click="incrementar">+1</button>

    <!-- Renderizado condicional -->
    <p v-if="edad >= 18">Mayor de edad</p>
    <p v-else>Menor de edad</p>

    <!-- Renderizado de listas -->
    <ul>
      <li v-for="(item, i) in items" :key="i">
        {{ i + 1 }}. {{ item }}
      </li>
    </ul>

    <!-- Class & Style bindings -->
    <div :class="{ activo: isActive, error: hasError }">
    <div :style="{ color: colorPrimario, fontSize: tamano + 'px' }">
  </div>
</template>

<style scoped>
.container { padding: 20px; }
h1 { color: #42b883; }
</style>'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class CompositionScene(Scene):
    def construct(self):
        title = Text("Composition API", font_size=42, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Composition API (recomendada)
<script setup>
import { ref, reactive, onMounted, onUnmounted, provide, inject } from "vue"

// Reactividad
const contador = ref(0)
const estado = reactive({
  usuario: null,
  items: [],
  loading: false
})

// Props (componente hijo)
const props = defineProps({
  titulo: { type: String, required: true },
  items: { type: Array, default: () => [] },
  editable: { type: Boolean, default: false }
})

// Emits
const emit = defineEmits(["update", "delete"])
const actualizar = (data) => emit("update", data)

// Lifecycle hooks
onMounted(async () => {
  estado.loading = true
  try {
    const res = await fetch("/api/data")
    estado.items = await res.json()
  } finally {
    estado.loading = false
  }
})

onUnmounted(() => {
  console.log("Componente destruido")
})

// Provide / Inject (abuelo -> nieto)
provide("tema", { primario: "#42b883", secundario: "#35495e" })

// Composables (logica reutilizable)
// useCounter.js
export function useCounter() {
  const count = ref(0)
  const increment = () => count.value++
  const decrement = () => count.value--
  return { count, increment, decrement }
}
</script>'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class RouterScene(Scene):
    def construct(self):
        title = Text("Vue Router", font_size=48, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// npm install vue-router@4

// router/index.js
import { createRouter, createWebHistory } from "vue-router"
import Home from "../views/Home.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/productos",
    name: "Productos",
    component: () => import("../views/Productos.vue")
  },
  {
    path: "/productos/:id",
    name: "DetalleProducto",
    component: () => import("../views/DetalleProducto.vue"),
    props: true
  },
  {
    path: "/contacto",
    name: "Contacto",
    component: () => import("../views/Contacto.vue"),
    meta: { requiereAuth: false }
  },
  {
    path: "/admin",
    name: "Admin",
    component: () => import("../views/Admin.vue"),
    meta: { requiereAuth: true, role: "admin" }
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("../views/NotFound.vue")
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { top: 0 }
  }
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const autenticado = localStorage.getItem("token")
  if (to.meta.requiereAuth && !autenticado) {
    next({ name: "Login", query: { redirect: to.fullPath } })
  } else {
    next()
  }
})

export default router

// App.vue
<template>
  <nav>
    <router-link to="/">Inicio</router-link>
    <router-link to="/productos">Productos</router-link>
    <router-link to="/contacto">Contacto</router-link>
  </nav>
  <router-view v-slot="{ Component, route }">
    <transition name="fade" mode="out-in">
      <component :is="Component" :key="route.path" />
    </transition>
  </router-view>
</template>'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class EstadoScene(Scene):
    def construct(self):
        title = Text("Estado Global - Pinia", font_size=42, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Pinia - Estado global (reemplazo de Vuex)
// npm install pinia

// stores/auth.js
import { defineStore } from "pinia"

export const useAuthStore = defineStore("auth", {
  // State
  state: () => ({
    usuario: null,
    token: localStorage.getItem("token"),
    loading: false
  }),

  // Getters (computados)
  getters: {
    isAutenticado: (state) => !!state.token,
    isAdmin: (state) => state.usuario?.role === "admin",
    nombreUsuario: (state) => state.usuario?.nombre ?? "Invitado"
  },

  // Actions (metodos)
  actions: {
    async login(email, password) {
      this.loading = true
      try {
        const res = await api.post("/auth/login", { email, password })
        this.token = res.data.token
        this.usuario = res.data.usuario
        localStorage.setItem("token", this.token)
      } finally {
        this.loading = false
      }
    },

    logout() {
      this.token = null
      this.usuario = null
      localStorage.removeItem("token")
      router.push("/login")
    }
  }
})

// stores/cart.js (setup syntax)
export const useCartStore = defineStore("cart", () => {
  const items = ref([])
  const total = computed(() =>
    items.value.reduce((sum, item) => sum + item.precio * item.cantidad, 0)
  )
  const count = computed(() => items.value.length)

  function agregar(producto) {
    const existente = items.value.find(i => i.id === producto.id)
    if (existente) {
      existente.cantidad++
    } else {
      items.value.push({ ...producto, cantidad: 1 })
    }
  }

  function eliminar(id) {
    items.value = items.value.filter(i => i.id !== id)
  }

  return { items, total, count, agregar, eliminar }
})

// Componente usando Pinia
<script setup>
import { useAuthStore } from "@/stores/auth"
import { useCartStore } from "@/stores/cart"

const auth = useAuthStore()
const cart = useCartStore()

console.log(auth.nombreUsuario)
console.log(cart.total)
</script>'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class FormulariosScene(Scene):
    def construct(self):
        title = Text("Formularios y Validacion", font_size=42, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Formularios reactivos con VeeValidate + Zod
// npm install vee-validate zod @vee-validate/zod

<script setup>
import { useForm, useField } from "vee-validate"
import { toFormValidator } from "@vee-validate/zod"
import { z } from "zod"

const schema = toFormValidator(
  z.object({
    nombre: z.string().min(3, "Minimo 3 caracteres"),
    email: z.string().email("Email invalido"),
    password: z.string()
      .min(8, "Minimo 8 caracteres")
      .regex(/[A-Z]/, "Debe contener mayuscula")
      .regex(/[0-9]/, "Debe contener numero"),
    edad: z.number({ invalid_type_error: "Debe ser numero" })
      .min(18, "Minimo 18 anos")
      .max(120, "Maximo 120 anos"),
    pais: z.string().min(1, "Seleccione un pais"),
    terminos: z.boolean().refine(v => v === true, "Debe aceptar terminos")
  })
)

const { handleSubmit, errors, isSubmitting } = useForm({
  validationSchema: schema,
  initialValues: {
    nombre: "",
    email: "",
    password: "",
    edad: null,
    pais: "",
    terminos: false
  }
})

const { value: nombre } = useField("nombre")
const { value: email } = useField("email")
const { value: password } = useField("password")

const onSubmit = handleSubmit(async (values) => {
  // Enviar al servidor
  const res = await api.post("/usuarios", values)
  // Redirigir
  router.push("/exito")
})
</script>

<template>
  <form @submit="onSubmit">
    <div>
      <label>Nombre</label>
      <input v-model="nombre" />
      <span class="error">{{ errors.nombre }}</span>
    </div>

    <div>
      <label>Email</label>
      <input v-model="email" type="email" />
      <span class="error">{{ errors.email }}</span>
    </div>

    <div>
      <label>Password</label>
      <input v-model="password" type="password" />
      <span class="error">{{ errors.password }}</span>
    </div>

    <button :disabled="isSubmitting" type="submit">
      {{ isSubmitting ? "Enviando..." : "Registrarse" }}
    </button>
  </form>
</template>'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class APIYTestingScene(Scene):
    def construct(self):
        title = Text("APIs y Testing", font_size=48, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Consumo de APIs con Fetch/Axios
<script setup>
import { ref, onMounted, watch } from "vue"

const usuarios = ref([])
const error = ref(null)
const loading = ref(false)
const search = ref("")

// Fetch con watch
watch(search, async (nuevoValor) => {
  if (nuevoValor.length < 3) return
  loading.value = true
  try {
    const res = await fetch(`/api/users?q=${nuevoValor}`)
    if (!res.ok) throw new Error("Error en la peticion")
    usuarios.value = await res.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}, { debounce: 300 })

// Axios con interceptors
import axios from "axios"

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 5000
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token")
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

api.interceptors.response.use(
  (res) => res,
  (error) => {
    if (error.response?.status === 401) {
      authStore.logout()
      router.push("/login")
    }
    return Promise.reject(error)
  }
)
</script>

// Vitest - Testing unitario
// npm install vitest @vue/test-utils
import { mount } from "@vue/test-utils"
import { describe, it, expect } from "vitest"
import Contador from "../Contador.vue"

describe("Contador.vue", () => {
  it("renderiza el valor inicial", () => {
    const wrapper = mount(Contador)
    expect(wrapper.text()).toContain("0")
  })

  it("incrementa al hacer click", async () => {
    const wrapper = mount(Contador)
    await wrapper.find("button").trigger("click")
    expect(wrapper.text()).toContain("1")
  })
})'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class RendimientoScene(Scene):
    def construct(self):
        title = Text("Rendimiento y SSR", font_size=42, color=VUE_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''// Optimizacion de rendimiento

// 1. Suspense para carga asincrona
// Padre:
<template>
  <Suspense>
    <template #default>
      <UserProfile :id="userId" />
    </template>
    <template #fallback>
      <SkeletonLoader />
    </template>
  </Suspense>
</template>

// Hija async:
<script setup>
const props = defineProps(["id"])
const user = await fetch(`/api/users/${props.id}`).then(r => r.json())
</script>

// 2. Lazy loading de componentes
import { defineAsyncComponent } from "vue"
const HeavyComponent = defineAsyncComponent(() =>
  import("./HeavyComponent.vue")
)

// 3. v-memo (evitar re-renders)
<div v-for="item in list" :key="item.id" v-memo="[item.id, item.updated]">
  {{ item.name }}
</div>

// 4. shallowRef (reactividad superficial)
import { shallowRef } from "vue"
const largeArray = shallowRef([])
// Solo .value dispara reactividad, no cambios internos

// 5. Teleport (renderizar fuera del arbol)
<Teleport to="body">
  <Modal v-if="showModal" />
</Teleport>

// 6. KeepAlive (cachear componentes)
<KeepAlive include="TabA,TabB">
  <component :is="currentTab" />
</KeepAlive>

// 7. Nuxt.js - SSR y SSG
// npx nuxi init my-app
// app.vue
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

// useFetch (auto-optimizado)
const { data, pending, error } = await useFetch("/api/users")

// 8. v-for con trackBy
<li v-for="item in items" :key="item.id">
// Siempre usar :key con identificador unico'''

        code = Code(code=code_str, language="html", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Vue.js", font_size=38, color=VUE_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Componentes reactivos con Composition API", font_size=22, color=TEXT_COLOR),
            Text("Template syntax: v-if, v-for, v-model, @click", font_size=22, color=TEXT_COLOR),
            Text("Vue Router con lazy loading y guards", font_size=22, color=TEXT_COLOR),
            Text("Pinia para estado global tipado", font_size=22, color=TEXT_COLOR),
            Text("Formularios con VeeValidate y Zod", font_size=22, color=TEXT_COLOR),
            Text("Consumo de APIs con Fetch/Axios", font_size=22, color=TEXT_COLOR),
            Text("Testing con Vitest y Vue Test Utils", font_size=22, color=TEXT_COLOR),
            Text("SSR con Nuxt.js y optimizacion", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Framework progresivo, de simple a complejo", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class VueJSFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        ComponentesScene.construct(self)
        CompositionScene.construct(self)
        RouterScene.construct(self)
        EstadoScene.construct(self)
        FormulariosScene.construct(self)
        APIYTestingScene.construct(self)
        RendimientoScene.construct(self)
        ConclusionScene.construct(self)


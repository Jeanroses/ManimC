from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
GRAPHQL_COLOR = "#e535ab"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("GraphQL", font_size=60, color=GRAPHQL_COLOR).set_color_by_gradient(GRAPHQL_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class SchemaScene(Scene):
    def construct(self):
        title = Text("Schemas y Types", font_size=48, color=GRAPHQL_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Schema GraphQL

type Query {
  usuarios: [Usuario!]!
  usuario(id: ID!): Usuario
  posts(limite: Int, offset: Int): [Post!]!
  buscar(termino: String!): [ResultadoBusqueda!]!
}

type Mutation {
  crearUsuario(input: InputUsuario!): Usuario!
  actualizarUsuario(id: ID!, input: InputUsuario!): Usuario!
  eliminarUsuario(id: ID!): Boolean!
  crearPost(input: InputPost!): Post!
}

type Subscription {
  usuarioCreado: Usuario!
  postActualizado: Post!
}

type Usuario {
  id: ID!
  nombre: String!
  email: String!
  edad: Int
  posts: [Post!]!
  createdAt: DateTime!
}

type Post {
  id: ID!
  titulo: String!
  contenido: String!
  autor: Usuario!
  comentarios: [Comentario!]!
  createdAt: DateTime!
}

type Comentario {
  id: ID!
  texto: String!
  autor: Usuario!
}

input InputUsuario {
  nombre: String!
  email: String!
  password: String!
}

input InputPost {
  titulo: String!
  contenido: String!
  autorId: ID!
}

# Query de ejemplo
query ObtenerUsuarios {
  usuarios {
    id
    nombre
    email
    posts {
      titulo
      comentarios {
        texto
        autor { nombre }
      }
    }
  }
}

query ObtenerUsuario($id: ID!) {
  usuario(id: $id) {
    nombre
    email
    posts { titulo contenido }
  }
}'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ResolversScene(Scene):
    def construct(self):
        title = Text("Resolvers y DataLoaders", font_size=48, color=GRAPHQL_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''// Resolvers en Apollo Server
const resolvers = {
  Query: {
    usuarios: async (_, __, { fuentes }) => {
      return fuentes.apiUsuarios.obtenerTodos();
    },
    usuario: async (_, { id }, { fuentes }) => {
      return fuentes.apiUsuarios.obtenerPorId(id);
    },
    posts: async (_, { limite = 10, offset = 0 }, { fuentes }) => {
      return fuentes.apiPosts.obtenerPosts(limite, offset);
    }
  },

  Mutation: {
    crearUsuario: async (_, { input }, { fuentes }) => {
      return fuentes.apiUsuarios.crear(input);
    },
    crearPost: async (_, { input }, { fuentes }) => {
      return fuentes.apiPosts.crear(input);
    }
  },

  Usuario: {
    posts: async (padre, _, { cargadores }) => {
      // Usa DataLoader para evitar N+1
      return cargadores.cargadorPosts.load(padre.id);
    }
  },

  Post: {
    autor: async (padre, _, { fuentes }) => {
      return fuentes.apiUsuarios.obtenerPorId(padre.autorId);
    },
    comentarios: async (padre, _, { cargadores }) => {
      return cargadores.cargadorComentarios.load(padre.id);
    }
  }
};

// DataLoader - Batching y Caching
const DataLoader = require("dataloader");

const crearCargadorPosts = new DataLoader(async (idsUsuarios) => {
  const posts = await db("posts").whereIn("autor_id", idsUsuarios);
  return idsUsuarios.map(id =>
    posts.filter(post => post.autor_id === id)
  );
});

const crearCargadorComentarios = new DataLoader(async (idsPosts) => {
  const comentarios = await db("comentarios").whereIn("post_id", idsPosts);
  return idsPosts.map(id =>
    comentarios.filter(com => com.post_id === id)
  );
});

// Sin DataLoader: N+1 queries (1 + N)
// Con DataLoader: 2 queries (1 users + 1 posts batch)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ApolloScene(Scene):
    def construct(self):
        title = Text("Apollo Client", font_size=48, color=GRAPHQL_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''// Apollo Client en React
import { ApolloClient, InMemoryCache, gql, useQuery, useMutation } from "@apollo/client";

const cliente = new ApolloClient({
  uri: "https://api.example.com/graphql",
  cache: new InMemoryCache({
    typePolicies: {
      Query: {
        fields: {
          usuarios: {
            merge(existing, incoming) {
              return incoming;
            }
          }
        }
      }
    }
  }),
  defaultOptions: {
    watchQuery: {
      fetchPolicy: "cache-and-network",
    },
  },
});

// Query
const USUARIOS = gql`
  query GetUsuarios {
    usuarios {
      id
      nombre
      email
      posts { titulo }
    }
  }
`;

function ListaUsuarios() {
  const { loading, error, data } = useQuery(USUARIOS);

  if (loading) return <Cargando />;
  if (error) return <Error mensaje={error.message} />;

  return data.usuarios.map(u => (
    <div key={u.id}>{u.nombre} - {u.email}</div>
  ));
}

// Mutation con actualizacion de cache
const CREAR_USUARIO = gql`
  mutation CrearUsuario($input: InputUsuario!) {
    crearUsuario(input: $input) { id nombre email }
  }
`;

function FormularioUsuario() {
  const [crearUsuario] = useMutation(CREAR_USUARIO, {
    update: (cache, { data: { crearUsuario } }) => {
      const existente = cache.readQuery({ query: USUARIOS });
      cache.writeQuery({
        query: USUARIOS,
        data: { usuarios: [...existente.usuarios, crearUsuario] },
      });
    },
    onCompleted: () => { toast.success("Usuario creado"); }
  });

  const submit = (formData) => {
    crearUsuario({ variables: { input: formData } });
  };

  return <Formulario onSubmit={submit} />;
}

// Subscription
const SUSCRIPCION = gql`
  subscription OnUsuarioCreado {
    usuarioCreado { id nombre email }
  }
`;

function Notificacion() {
  const { data } = useSubscription(SUSCRIPCION);
  useEffect(() => {
    if (data?.usuarioCreado) {
      toast(`Nuevo usuario: ${data.usuarioCreado.nombre}`);
    }
  }, [data]);
  return null;
}'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class FederationScene(Scene):
    def construct(self):
        title = Text("Federacion y Gateway", font_size=48, color=GRAPHQL_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Apollo Federation - Microservicios GraphQL

# Servicio 1 - Usuarios (schema)
type User @key(fields: "id") {
  id: ID!
  nombre: String!
  email: String!
}

extend type Query {
  usuarios: [User!]!
  usuario(id: ID!): User
}

# Servicio 2 - Posts (schema)
type Post @key(fields: "id") {
  id: ID!
  titulo: String!
  contenido: String!
  autor: User!
}

extend type User @key(fields: "id") {
  id: ID! @external
  posts: [Post!]!
}

extend type Query {
  posts: [Post!]!
}

# Gateway - Punto de entrada unificado
import { ApolloGateway } from "@apollo/gateway";
import { ApolloServer } from "@apollo/server";

const gateway = new ApolloGateway({
  serviceList: [
    { name: "usuarios", url: "http://usuarios:4001/graphql" },
    { name: "posts", url: "http://posts:4002/graphql" },
    { name: "comentarios", url: "http://comentarios:4003/graphql" },
  ],
});

const server = new ApolloServer({ gateway });

// Query federada
query ObtenerFeed {
  usuarios {
    nombre
    email
    posts {
      titulo
      contenido
      comentarios {
        texto
        autor { nombre }
      }
    }
  }
}

# Beneficios de Federacion
# - Cada equipo maneja su propio schema
# - Escalabilidad independiente
# - Types compartidos via @key
# - Gateway unifica todo'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class SecurityScene(Scene):
    def construct(self):
        title = Text("GraphQL Security", font_size=48, color=GRAPHQL_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Seguridad en GraphQL

# 1. Query Depth Limiting
# Limitar profundidad maxima de queries
app.use("/graphql", graphqlHTTP({
  schema,
  validationRules: [
    depthLimit(10),
  ],
}));

# Query peligrosa (demasiado profunda):
query Deep {
  user { posts { comments { author { posts { comments { author { ... } } } } } } }
}

# 2. Query Cost Analysis
const { costAnalysis } = require("graphql-cost-analysis");

const reglas = [
  costAnalysis({
    maxCost: 1000,
    objectCost: 1,
    scalarCost: 0,
    multipliers: ["limite", "offset"],
  }),
];

# 3. Rate Limiting
const rateLimit = require("express-rate-limit");
const limitador = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  message: { error: "Demasiadas peticiones" },
});
app.use("/graphql", limitador);

# 4. Persisted Queries
# Solo permitir queries pre-aprobadas
const queriesPersistidas = {
  "sha256hash1": "query GetUsers { usuarios { id nombre } }",
  "sha256hash2": "query GetUser($id: ID!) { usuario(id: $id) { nombre email } }",
};

# 5. Autenticacion y Autorizacion
const contexto = async ({ req }) => {
  const token = req.headers.authorization?.split(" ")[1];
  const usuario = await verificarToken(token);
  return { usuario };
};

# 6. Field-level authorization
# type Usuario {
#   id: ID!
#   nombre: String!
#   email: String! @requiresAuth
#   password: String! @requiresRole(admin: true)
# }'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: GraphQL", font_size=38, color=GRAPHQL_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Schemas, Queries y Mutations", font_size=22, color=TEXT_COLOR),
            Text("Resolvers y DataLoaders", font_size=22, color=TEXT_COLOR),
            Text("Apollo Client en React", font_size=22, color=TEXT_COLOR),
            Text("Subscriptions en tiempo real", font_size=22, color=TEXT_COLOR),
            Text("Federacion de microservicios", font_size=22, color=TEXT_COLOR),
            Text("Seguridad y rate limiting", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("La evolucion de las APIs", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class GraphQLFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        SchemaScene.construct(self)
        ResolversScene.construct(self)
        ApolloScene.construct(self)
        FederationScene.construct(self)
        SecurityScene.construct(self)
        ConclusionScene.construct(self)

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
SPRING_COLOR = "#6db33f"
JAVA_COLOR = "#007396"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Spring Boot",
            font_size=58,
            color=SPRING_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(SPRING_COLOR, PRIMARY_COLOR)

        subtitle = Text(
            "El framework de referencia para desarrollo enterprise en Java",
            font_size=26,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [SPRING_COLOR, PRIMARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
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


class SpringHistoryScene(Scene):
    def construct(self):
        title = Text("Historia de Spring Framework", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        timeline = VGroup(
            Text("2004: Spring Framework 1.0 - IOC Container", font_size=20, color=TEXT_COLOR),
            Text("2006: Spring 2.0 - Annotations support", font_size=20, color=TEXT_COLOR),
            Text("2009: Spring 3.0 - RestTemplate, JavaConfig", font_size=20, color=TEXT_COLOR),
            Text("2013: Spring 4.0 - Java 8, WebSocket", font_size=20, color=TEXT_COLOR),
            Text("2014: Spring Boot 1.0 - Opinionated defaults", font_size=22, color=SPRING_COLOR),
            Text("2017: Spring 5.0 - Reactive Programming", font_size=20, color=ACCENT_COLOR),
            Text("2020: Spring Boot 2.4+ - Modern configuration", font_size=20, color=HIGHLIGHT_COLOR),
            Text("2023: Spring Boot 3.x - Jakarta EE, GraalVM", font_size=20, color=SUCCESS_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        timeline.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        for t in timeline:
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SpringBootPhilosophyScene(Scene):
    def construct(self):
        title = Text("Filosofia de Spring Boot", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        pillars = VGroup(
            Text("Convention over Configuration", font_size=26, color=ACCENT_COLOR),
            Text("Opinionated defaults para comenzar rapidamente", font_size=22, color=TEXT_COLOR),
            Text("", font_size=20),
            Text("Standalone", font_size=26, color=SPRING_COLOR),
            Text("Aplicaciones autocontenidas, sin servidores externos", font_size=22, color=TEXT_COLOR),
            Text("", font_size=20),
            Text("Production-ready", font_size=26, color=HIGHLIGHT_COLOR),
            Text("Metrics, health checks, externalized configuration", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        pillars.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for p in pillars:
            if p.text.strip():
                self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=0.5)
                self.wait(0.3)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SpringInitializrScene(Scene):
    def construct(self):
        title = Text("Spring Initializr", font_size=48, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        description = Text(
            "Generador de proyectos Spring Boot online",
            font_size=24,
            color=TEXT_COLOR,
        )
        description.next_to(title, DOWN, buff=0.5)

        url = Text("https://start.spring.io", font_size=28, color=HIGHLIGHT_COLOR)
        url.next_to(description, DOWN, buff=0.5)

        options = VGroup(
            Text("Project: Maven/Gradle", font_size=20, color=CURVE_COLOR),
            Text("Language: Java/Kotlin/Groovy", font_size=20, color=CURVE_COLOR),
            Text("Spring Boot Version", font_size=20, color=CURVE_COLOR),
            Text("Project Metadata (Group, Artifact)", font_size=20, color=CURVE_COLOR),
            Text("Dependencies: Web, Data, Security, etc.", font_size=20, color=CURVE_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        options.next_to(url, DOWN, buff=0.6)

        maven = '''<!-- pom.xml -->
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.0</version>
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>'''

        gradle = '''// build.gradle
plugins {
    id 'java'
    id 'org.springframework.boot' version '3.2.0'
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
}'''

        maven_code = Code(
            code_string=maven,
            language="xml",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        maven_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(DOWN * 0.5)

        gradle_code = Code(
            code_string=gradle,
            language="groovy",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        gradle_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(description), FadeIn(url), run_time=0.8)
        self.play(FadeIn(options), run_time=1)
        self.play(Create(maven_code), run_time=1)
        self.play(Create(gradle_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SpringApplicationScene(Scene):
    def construct(self):
        title = Text("SpringApplication", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        main_class = '''package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}'''

        java_code = Code(
            code_string=main_class,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=22,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        annotations = VGroup(
            Text("@SpringBootApplication incluye:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("@Configuration - Define beans", font_size=18, color=TEXT_COLOR),
            Text("@EnableAutoConfiguration - Auto-configuracion", font_size=18, color=TEXT_COLOR),
            Text("@ComponentScan - Escaneo de componentes", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15)
        annotations.next_to(java_code, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.2)
        self.play(FadeIn(annotations), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ComponentScene(Scene):
    def construct(self):
        title = Text("Component Scanning", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        stereotype = '''// Stereotypes de Spring
@Component       // Componente genérico
@Service         // Servicio de negocio
@Repository      // Acceso a datos
@Controller      // Controlador web
@RestController // API REST
@Configuration  // Configuración'''

        code = Code(
            code_string=stereotype,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.85).to_edge(LEFT, buff=0.5).shift(UP * 0.3)

        example = '''@Service
public class UsuarioService {
    @Autowired
    private UsuarioRepository usuarioRepo;

    public Usuario buscarPorId(Long id) {
        return usuarioRepo.findById(id).orElse(null);
    }
}'''

        example_code = Code(
            code_string=example,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        example_code.scale(0.8).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1)
        self.play(Create(example_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DependencyInjectionScene(Scene):
    def construct(self):
        title = Text("Inyeccion de Dependencias", font_size=42, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        constructor = '''// Constructor Injection (RECOMENDADO)
@Service
public class OrderService {
    private final PaymentGateway paymentGateway;
    private final InventoryService inventoryService;

    public OrderService(PaymentGateway paymentGateway,
                       InventoryService inventoryService) {
        this.paymentGateway = paymentGateway;
        this.inventoryService = inventoryService;
    }
}'''

        field = '''// Field Injection (NO RECOMENDADO)
@Service
public class OrderService {
    @Autowired
    private PaymentGateway paymentGateway;
}'''

        setter = '''// Setter Injection
@Service
public class OrderService {
    private PaymentGateway paymentGateway;

    @Autowired
    public void setPaymentGateway(PaymentGateway pg) {
        this.paymentGateway = pg;
    }
}'''

        constructor_code = Code(
            code_string=constructor,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        constructor_code.scale(0.8).to_edge(LEFT, buff=0.3).shift(UP * 0.8)

        field_code = Code(
            code_string=field,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        field_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(UP * 0.8)

        setter_code = Code(
            code_string=setter,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        setter_code.scale(0.75).to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(constructor_code), run_time=1)
        self.play(Create(field_code), run_time=1)
        self.play(Create(setter_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class BeanConfigurationScene(Scene):
    def construct(self):
        title = Text("Configuracion de Beans", font_size=42, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        java_config = '''// Configuracion con @Configuration
@Configuration
public class AppConfig {

    @Bean
    public DataSource dataSource() {
        return DataSourceBuilder.create()
            .url("jdbc:postgresql://localhost:5432/mydb")
            .username("admin")
            .password("password")
            .build();
    }

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplateBuilder()
            .setConnectTimeout(Duration.ofSeconds(5))
            .build();
    }
}'''

        java_code = Code(
            code_string=java_config,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        explanation = Text(
            "@Bean declara metodos que producen objetos gestionados por Spring",
            font_size=22,
            color=HIGHLIGHT_COLOR,
        )
        explanation.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.play(FadeIn(explanation), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ApplicationPropertiesScene(Scene):
    def construct(self):
        title = Text("application.properties / application.yml", font_size=38, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        properties = '''# application.properties
server.port=8080
server.servlet.context-path=/api
spring.application.name=mi-servicio

# Database
spring.datasource.url=jdbc:postgresql://localhost:5432/mydb
spring.datasource.username=admin
spring.datasource.password=secret
spring.datasource.driver-class-name=org.postgresql.Driver

# JPA/Hibernate
spring.jpa.show-sql=true
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.format_sql=true

# Logging
logging.level.root=INFO
logging.level.com.example=DEBUG

# Actuator
management.endpoints.web.exposure.include=health,info,metrics
management.endpoint.health.show-details=always'''

        properties_code = Code(
            code_string=properties,
            language="properties",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        properties_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(properties_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class YamlConfigurationScene(Scene):
    def construct(self):
        title = Text("application.yml (YAML)", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        yaml = '''server:
  port: 8080
  servlet:
    context-path: /api

spring:
  application:
    name: mi-servicio
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: admin
    password: secret
    driver-class-name: org.postgresql.Driver
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true

logging:
  level:
    root: INFO
    com.example: DEBUG
    org.springframework.web: DEBUG

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
  endpoint:
    health:
      show-details: always'''

        yaml_code = Code(
            code_string=yaml,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        yaml_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(yaml_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RESTControllerScene(Scene):
    def construct(self):
        title = Text("REST Controller", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        controller = '''@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {

    @Autowired
    private UsuarioService usuarioService;

    @GetMapping
    public List<Usuario> listarTodos() {
        return usuarioService.buscarTodos();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Usuario> buscarPorId(@PathVariable Long id) {
        return usuarioService.buscarPorId(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Usuario> crear(@RequestBody Usuario usuario) {
        Usuario guardado = usuarioService.guardar(usuario);
        return ResponseEntity.created(URI.create("/api/usuarios/" + guardado.getId()))
            .body(guardado);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Usuario> actualizar(@PathVariable Long id,
                                              @RequestBody Usuario usuario) {
        return usuarioService.actualizar(id, usuario)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminar(@PathVariable Long id) {
        if (usuarioService.eliminar(id)) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}'''

        java_code = Code(
            code_string=controller,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RequestMappingScene(Scene):
    def construct(self):
        title = Text("Anotaciones HTTP", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        annotations = VGroup(
            Text("@GetMapping - Consultar recursos", font_size=22, color=SUCCESS_COLOR),
            Text("@PostMapping - Crear recursos", font_size=22, color=HIGHLIGHT_COLOR),
            Text("@PutMapping - Actualizar recurso completo", font_size=22, color=WARNING_COLOR),
            Text("@PatchMapping - Actualizar parcialmente", font_size=22, color=CURVE_COLOR),
            Text("@DeleteMapping - Eliminar recursos", font_size=22, color=ITER_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        annotations.next_to(title, DOWN, buff=0.6)

        examples = '''// Variantes
@GetMapping("/usuarios")
@GetMapping(value = "/usuarios", produces = "application/json")
@PostMapping(value = "/usuarios", consumes = "application/json")

// Parametros de path
@GetMapping("/usuarios/{id}")
@GetMapping("/usuarios/{id}/pedidos/{pedidoId}")

// Query parameters
@GetMapping("/buscar")
public List<Usuario> buscar(
    @RequestParam String nombre,
    @RequestParam(required = false) Integer edad,
    @RequestParam(defaultValue = "0") int pagina)'''

        examples_code = Code(
            code_string=examples,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        examples_code.scale(0.85).next_to(annotations, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(annotations, shift=RIGHT * 0.2), run_time=1)
        self.play(Create(examples_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RequestBodyScene(Scene):
    def construct(self):
        title = Text("Request Body y Response", font_size=42, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        dto = '''// DTO - Data Transfer Object
public class UsuarioRequest {
    @NotBlank(message = "El nombre es obligatorio")
    @Size(min = 2, max = 50)
    private String nombre;

    @Email
    private String email;

    @NotNull
    @Min(18) @Max(100)
    private Integer edad;

    @NotNull
    private Rol rol;

    // Getters y Setters
}

public enum Rol {
    ADMIN, USER, GUEST
}'''

        response = '''// Response Entity
@PostMapping("/usuarios")
public ResponseEntity<UsuarioResponse> crear(
        @Valid @RequestBody UsuarioRequest request,
        BindingResult result) {

    if (result.hasErrors()) {
        return ResponseEntity.badRequest()
            .body(new ErrorResponse("Validacion fallida"));
    }

    Usuario guardado = usuarioService.guardar(request);
    return ResponseEntity
        .created(URI.create("/api/usuarios/" + guardado.getId()))
        .body(mapper.toResponse(guardado));
}'''

        dto_code = Code(
            code_string=dto,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dto_code.scale(0.8).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        response_code = Code(
            code_string=response,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        response_code.scale(0.8).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(dto_code), run_time=1)
        self.play(Create(response_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SpringDataJPAIntroScene(Scene):
    def construct(self):
        title = Text("Spring Data JPA", font_size=48, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Capa de abstraccion para acceso a datos con JPA/Hibernate",
            font_size=24,
            color=TEXT_COLOR,
        )
        definition.next_to(title, DOWN, buff=0.5)

        starter = '''<!-- Dependencia -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<!-- Base de datos H2 para desarrollo -->
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>'''

        starter_code = Code(
            code_string=starter,
            language="xml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        starter_code.scale(0.8).next_to(definition, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(starter_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class EntityScene(Scene):
    def construct(self):
        title = Text("Entidades JPA", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        entity = '''@Entity
@Table(name = "usuarios")
public class Usuario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String nombre;

    @Column(unique = true)
    private String email;

    @Column(name = "fecha_registro")
    private LocalDateTime fechaRegistro;

    @Enumerated(EnumType.STRING)
    @Column(length = 20)
    private Rol rol;

    @Column(nullable = false)
    private Boolean activo = true;

    // Constructores, Getters, Setters
}

public enum Rol {
    ADMIN, USER, GUEST
}'''

        java_code = Code(
            code_string=entity,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class JpaRepositoryScene(Scene):
    def construct(self):
        title = Text("JpaRepository", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        repository = '''public interface UsuarioRepository extends JpaRepository<Usuario, Long> {

    // Metodos derivados del nombre del metodo
    List<Usuario> findByNombre(String nombre);
    List<Usuario> findByEmailContaining(String email);
    List<Usuario> findByActivoTrue();
    List<Usuario> findByRolAndActivo(Rol rol, Boolean activo);
    Optional<Usuario> findByEmail(String email);
    boolean existsByEmail(String email);
    long countByActivo(Boolean activo);

    // JPQL Queries
    @Query("SELECT u FROM Usuario u WHERE u.rol = :rol")
    List<Usuario> buscarPorRol(@Param("rol") Rol rol);

    // SQL Nativo
    @Query(value = "SELECT * FROM usuarios WHERE nombre LIKE %:nombre%",
           nativeQuery = true)
    List<Usuario> buscarPorNombreLike(@Param("nombre") String nombre);

    // Actualizacion
    @Modifying
    @Query("UPDATE Usuario u SET u.activo = false WHERE u.id = :id")
    void desactivar(@Param("id") Long id);
}'''

        java_code = Code(
            code_string=repository,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RelationshipsScene(Scene):
    def construct(self):
        title = Text("Relaciones JPA", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        one_to_many = '''// One-to-Many (Un Cliente -> Muchos Pedidos)
@Entity
public class Cliente {
    @Id @GeneratedValue
    private Long id;

    @OneToMany(mappedBy = "cliente", cascade = CascadeType.ALL,
                fetch = FetchType.LAZY)
    private List<Pedido> pedidos;
}

@Entity
public class Pedido {
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "cliente_id")
    private Cliente cliente;
}'''

        many_to_many = '''// Many-to-Many (Estudiantes <-> Cursos)
@Entity
public class Estudiante {
    @ManyToMany
    @JoinTable(
        name = "estudiante_curso",
        joinColumns = @JoinColumn(name = "estudiante_id"),
        inverseJoinColumns = @JoinColumn(name = "curso_id")
    )
    private Set<Curso> cursos;
}'''

        otm_code = Code(
            code_string=one_to_many,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        otm_code.scale(0.8).to_edge(LEFT, buff=0.3).shift(UP * 0.5)

        mtm_code = Code(
            code_string=many_to_many,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        mtm_code.scale(0.8).to_edge(RIGHT, buff=0.3).shift(UP * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(otm_code), run_time=1)
        self.play(Create(mtm_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ServiceLayerScene(Scene):
    def construct(self):
        title = Text("Capa de Servicio", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        service = '''@Service
@Transactional
public class UsuarioService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private EmailService emailService;

    public List<Usuario> buscarTodos() {
        return usuarioRepository.findAll();
    }

    public Optional<Usuario> buscarPorId(Long id) {
        return usuarioRepository.findById(id);
    }

    public Usuario guardar(Usuario usuario) {
        if (usuarioRepository.existsByEmail(usuario.getEmail())) {
            throw new EmailExistenteException("Email ya registrado");
        }
        Usuario guardado = usuarioRepository.save(usuario);
        emailService.enviarBienvenida(guardado.getEmail());
        return guardado;
    }

    public void eliminar(Long id) {
        usuarioRepository.deleteById(id);
    }

    public List<Usuario> buscarPorRol(Rol rol) {
        return usuarioRepository.findByRol(rol);
    }
}'''

        java_code = Code(
            code_string=service,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SpringSecurityIntroScene(Scene):
    def construct(self):
        title = Text("Spring Security", font_size=48, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        starter = '''<!-- Dependencia -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<dependency>
    <groupId>org.thymeleaf.extras</groupId>
    <artifactId>thymeleaf-extras-springsecurity6</artifactId>
</dependency>'''

        starter_code = Code(
            code_string=starter,
            language="xml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        starter_code.scale(0.8).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(starter_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SecurityConfigScene(Scene):
    def construct(self):
        title = Text("Security Config", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        config = '''@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/publico/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/usuarios/**").authenticated()
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")
                .defaultSuccessUrl("/dashboard", true)
                .permitAll()
            )
            .logout(logout -> logout
                .logoutSuccessUrl("/login?logout")
                .permitAll()
            )
            .httpBasic(Customizer.withDefaults());

        return http.build();
    }

    @Bean
    public UserDetailsService userDetailsService() {
        UserDetails user = User.builder()
            .username("user")
            .password("{noop}password")
            .roles("USER")
            .build();

        UserDetails admin = User.builder()
            .username("admin")
            .password("{noop}admin123")
            .roles("USER", "ADMIN")
            .build();

        return new InMemoryUserDetailsManager(user, admin);
    }
}'''

        java_code = Code(
            code_string=config,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class JWTIntroductionScene(Scene):
    def construct(self):
        title = Text("JWT - JSON Web Tokens", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        explanation = Text(
            "Autenticacion stateless para APIs REST",
            font_size=24,
            color=TEXT_COLOR,
        )
        explanation.next_to(title, DOWN, buff=0.5)

        structure = MathTex(
            r"\text{JWT} = \text{Header.Payload.Signature}",
            font_size=32,
            color=HIGHLIGHT_COLOR,
        )
        structure.next_to(explanation, DOWN, buff=0.5)

        header = '''{
  "alg": "HS256",
  "typ": "JWT"
}'''

        payload = '''{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true,
  "exp": 1699999999
}'''

        header_code = Code(
            code_string=header,
            language="json",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        header_code.scale(0.7).to_edge(LEFT, buff=0.4).shift(DOWN * 0.3)

        payload_code = Code(
            code_string=payload,
            language="json",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        payload_code.scale(0.7).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.3)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(explanation), run_time=0.8)
        self.play(Write(structure), run_time=1)
        self.play(Create(header_code), run_time=0.8)
        self.play(Create(payload_code), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class JWTFilterScene(Scene):
    def construct(self):
        title = Text("JWT Filter Implementation", font_size=40, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        filter_code = '''@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    @Autowired
    private JwtService jwtService;

    @Autowired
    private UserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain)
        throws ServletException, IOException {

        String authHeader = request.getHeader("Authorization");

        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            filterChain.doFilter(request, response);
            return;
        }

        String token = authHeader.substring(7);
        String username = jwtService.extractUsername(token);

        if (username != null &&
            SecurityContextHolder.getContext().getAuthentication() == null) {

            UserDetails userDetails =
                userDetailsService.loadUserByUsername(username);

            if (jwtService.isTokenValid(token, userDetails)) {
                UsernamePasswordAuthenticationToken authToken =
                    new UsernamePasswordAuthenticationToken(
                        userDetails, null, userDetails.getAuthorities());
                authToken.setDetails(
                    new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }

        filterChain.doFilter(request, response);
    }
}'''

        java_code = Code(
            code_string=filter_code,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ValidationScene(Scene):
    def construct(self):
        title = Text("Validacion de Datos", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        annotations = '''// Anotaciones de validacion
@NotNull          - No puede ser null
@NotEmpty         - No puede estar vacio
@NotBlank         - No puede estar en blanco (Strings)
@Size(min, max)   - Tamano minimo y maximo
@Min(value)       - Valor minimo
@Max(value)       - Valor maximo
@Email            - Formato de email valido
@Pattern(regex)   - Expresion regular
@Past             - Fecha en el pasado
@Future           - Fecha en el futuro
@Valid            - Validar objeto anidado'''

        entity = '''public class UsuarioRequest {
    @NotBlank(message = "Nombre obligatorio")
    @Size(min = 2, max = 100)
    private String nombre;

    @NotBlank @Email
    private String email;

    @NotNull @Min(18) @Max(100)
    private Integer edad;

    @NotNull
    private Set<@NotBlank String> telefonos;

    @Valid
    private DireccionRequest direccion;
}'''

        annotations_code = Code(
            code_string=annotations,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        annotations_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        entity_code = Code(
            code_string=entity,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        entity_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(annotations_code), run_time=1)
        self.play(Create(entity_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ExceptionHandlingScene(Scene):
    def construct(self):
        title = Text("Manejo de Excepciones", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        global_handler = '''@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(RecursoNoEncontradoException.class)
    public ResponseEntity<ErrorResponse> manejarNoEncontrado(
            RecursoNoEncontradoException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            LocalDateTime.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> manejarValidacion(
            MethodArgumentNotValidException ex) {
        Map<String, String> errores = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error ->
            errores.put(error.getField(), error.getDefaultMessage()));

        return ResponseEntity.badRequest()
            .body(new ErrorResponse(400, "Validation failed", errores));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> manejarGeneral(Exception ex) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(new ErrorResponse(500, "Error interno del servidor"));
    }
}'''

        java_code = Code(
            code_string=global_handler,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        java_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ActuatorScene(Scene):
    def construct(self):
        title = Text("Spring Boot Actuator", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        starter = '''<!-- Dependencia -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>'''

        starter_code = Code(
            code_string=starter,
            language="xml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        starter_code.scale(0.7).to_edge(LEFT, buff=0.8).shift(UP * 1.5)

        config = '''# application.yml
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,env,beans,loggers
  endpoint:
    health:
      show-details: always
  health:
    livenessState:
      enabled: true
    readinessState:
      enabled: true'''

        config_code = Code(
            code_string=config,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        config_code.scale(0.75).to_edge(RIGHT, buff=0.6).shift(UP * 1.2)

        endpoints = VGroup(
            Text("Endpoints disponibles:", font_size=22, color=HIGHLIGHT_COLOR),
            Text("/actuator/health - Estado de la aplicacion", font_size=18, color=TEXT_COLOR),
            Text("/actuator/metrics - Metricas de rendimiento", font_size=18, color=TEXT_COLOR),
            Text("/actuator/info - Informacion de la aplicacion", font_size=18, color=TEXT_COLOR),
            Text("/actuator/env - Variables de entorno", font_size=18, color=TEXT_COLOR),
            Text("/actuator/beans - Beans registrados", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        endpoints.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(starter_code), run_time=0.8)
        self.play(Create(config_code), run_time=0.8)
        self.play(FadeIn(endpoints), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TestingScene(Scene):
    def construct(self):
        title = Text("Testing en Spring Boot", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        test_types = VGroup(
            Text("Unit Tests - @SpringBootTest, @DataJpaTest", font_size=22, color=HIGHLIGHT_COLOR),
            Text("Integration Tests - @WebMvcTest, @RestClientTest", font_size=22, color=SECONDARY_COLOR),
            Text("Mock Tests - @MockBean, Mockito", font_size=22, color=ACCENT_COLOR),
            Text("Slice Tests - Testing por capa", font_size=22, color=CURVE_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        test_types.next_to(title, DOWN, buff=0.6)

        unit_test = '''@SpringBootTest
class UsuarioServiceTest {

    @Autowired
    private UsuarioService usuarioService;

    @Test
    void testBuscarPorId() {
        Optional<Usuario> usuario = usuarioService.buscarPorId(1L);
        assertTrue(usuario.isPresent());
        assertEquals("Juan", usuario.get().getNombre());
    }
}'''

        unit_code = Code(
            code_string=unit_test,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        unit_code.scale(0.8).next_to(test_types, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(test_types), run_time=1)
        self.play(Create(unit_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ProfileScene(Scene):
    def construct(self):
        title = Text("Spring Profiles", font_size=48, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        profile_files = '''application.yml              # Configuracion base
application-dev.yml        # Desarrollo
application-prod.yml       # Produccion
application-test.yml       # Testing'''

        profile_code = Code(
            code_string=profile_files,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        profile_code.scale(0.8).next_to(title, DOWN, buff=0.5)

        activation = '''# Activar profile
# Via application.yml
spring:
  profiles:
    active: dev

# Via variable de entorno
export SPRING_PROFILES_ACTIVE=prod

# Via linea de comandos
java -jar app.jar --spring.profiles.active=prod

# En tests
@ActiveProfiles("test")'''

        activation_code = Code(
            code_string=activation,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        activation_code.scale(0.8).next_to(profile_code, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(Create(profile_code), run_time=1)
        self.play(Create(activation_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LoggingScene(Scene):
    def construct(self):
        title = Text("Logging en Spring Boot", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        usage = '''@Slf4j  // Lombok - crea: private Logger log = LoggerFactory.getLogger(...)
public class UsuarioService {

    public void procesar() {
        log.info("Iniciando procesamiento de usuario");
        log.debug("Datos del usuario: {}", usuario);
        log.warn("El usuario tiene permisos limitados");
        log.error("Error al procesar: ", excepcion);
    }
}

// Sin Lombok
public class UsuarioService {
    private static final Logger log =
        LoggerFactory.getLogger(UsuarioService.class);
}'''

        java_code = Code(
            code_string=usage,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CachingScene(Scene):
    def construct(self):
        title = Text("Spring Cache", font_size=48, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        enable_cache = '''// Configuracion
@EnableCaching
@Configuration
public class CacheConfig {

    @Bean
    public CacheManager cacheManager() {
        return new ConcurrentMapCacheManager("usuarios", "productos");
    }
}'''

        usage = '''@Service
@Slf4j
public class UsuarioService {

    @Cacheable(value = "usuarios", key = "#id")
    public Usuario buscarPorId(Long id) {
        log.info("Buscando usuario en BD: {}", id);
        return usuarioRepository.findById(id).orElse(null);
    }

    @CachePut(value = "usuarios", key = "#usuario.id")
    public Usuario guardar(Usuario usuario) {
        return usuarioRepository.save(usuario);
    }

    @CacheEvict(value = "usuarios", key = "#id")
    public void eliminar(Long id) {
        usuarioRepository.deleteById(id);
    }

    @CacheEvict(value = "usuarios", allEntries = true)
    public void limpiarCache() { }
}'''

        enable_code = Code(
            code_string=enable_cache,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        enable_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.5)

        usage_code = Code(
            code_string=usage,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        usage_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(enable_code), run_time=1)
        self.play(Create(usage_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AsyncScene(Scene):
    def construct(self):
        title = Text("Programacion Asincrona", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        async_config = '''@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("async-");
        executor.initialize();
        return executor;
    }
}'''

        async_usage = '''@Service
public class EmailService {

    @Async
    public CompletableFuture<Void> enviarEmailAsync(String destinatario,
                                                     String asunto,
                                                     String cuerpo) {
        // Simulacion de envio
        try {
            Thread.sleep(2000);
            log.info("Email enviado a: {}", destinatario);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return CompletableFuture.completedFuture(null);
    }

    // Llamada desde controller
    @GetMapping("/procesar")
    public String procesar() {
        emailService.enviarEmailAsync("user@test.com", "Test", "Cuerpo");
        return "Procesamiento iniciado";
    }
}'''

        config_code = Code(
            code_string=async_config,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        config_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(UP * 0.5)

        usage_code = Code(
            code_string=async_usage,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        usage_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(config_code), run_time=1)
        self.play(Create(usage_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SchedulingScene(Scene):
    def construct(self):
        title = Text("Programacion de Tareas (Scheduler)", font_size=38, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        enable_scheduling = '''@Configuration
@EnableScheduling
public class SchedulingConfig { }'''

        scheduled_task = '''@Service
@Slf4j
public class ReporteService {

    // Cada hora
    @Scheduled(cron = "0 0 * * * *")
    public void generarReporteDiario() {
        log.info("Generando reporte...");
    }

    // Cada 30 minutos
    @Scheduled(fixedRate = 1800000)
    public void limpiarDatos() {
        log.info("Limpiando datos antiguos...");
    }

    // Con inicializacion diferida
    @Scheduled(fixedDelay = 60000, initialDelay = 10000)
    public void sincronizarDatos() {
        log.info("Sincronizando datos...");
    }
}'''

        enable_code = Code(
            code_string=enable_scheduling,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        enable_code.scale(0.8).to_edge(LEFT, buff=0.5).shift(UP * 1.5)

        scheduled_code = Code(
            code_string=scheduled_task,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        scheduled_code.scale(0.85).next_to(enable_code, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(enable_code), run_time=0.8)
        self.play(Create(scheduled_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WebClientScene(Scene):
    def construct(self):
        title = Text("WebClient - Cliente HTTP", font_size=42, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        webclient_config = '''@Configuration
public class WebClientConfig {

    @Bean
    public WebClient webClient() {
        return WebClient.builder()
            .baseUrl("https://api.ejemplo.com")
            .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
            .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer token")
            .filter(logRequest())
            .filter(logResponse())
            .build();
    }

    private ExchangeFilterFunction logRequest() {
        return ExchangeFilterFunction.ofRequestProcessor(clientRequest -> {
            log.info("Request: {} {}", clientRequest.method(),
                     clientRequest.url());
            return Mono.just(clientRequest);
        });
    }
}'''

        usage = '''@Service
public class ExternalApiService {

    @Autowired
    private WebClient webClient;

    public Mono<Usuario> buscarUsuario(Long id) {
        return webClient.get()
            .uri("/usuarios/{id}", id)
            .retrieve()
            .bodyToMono(Usuario.class);
    }

    public Flux<Producto> listarProductos() {
        return webClient.get()
            .uri("/productos")
            .retrieve()
            .bodyToFlux(Producto.class);
    }
}'''

        config_code = Code(
            code_string=webclient_config,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        config_code.scale(0.8).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        usage_code = Code(
            code_string=usage,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        usage_code.scale(0.8).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(config_code), run_time=1)
        self.play(Create(usage_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FileUploadScene(Scene):
    def construct(self):
        title = Text("Subida de Archivos", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        controller = '''@RestController
@RequestMapping("/api/archivos")
public class ArchivoController {

    @PostMapping("/upload")
    public ResponseEntity<?> uploadFile(@RequestParam("file") MultipartFile file) {
        if (file.isEmpty()) {
            return ResponseEntity.badRequest().body("Archivo vacio");
        }

        try {
            String uploadDir = "uploads/";
            Path path = Paths.get(uploadDir + file.getOriginalFilename());
            Files.write(path, file.getBytes());

            return ResponseEntity.ok(Map.of(
                "filename", file.getOriginalFilename(),
                "size", file.getSize()
            ));
        } catch (IOException e) {
            return ResponseEntity.status(500).body("Error al guardar");
        }
    }
}'''

        java_code = Code(
            code_string=controller,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        java_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        config = '''# application.yml - Configuracion de archivos
spring.servlet.multipart.enabled=true
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=50MB
spring.servlet.multipart.file-size-threshold=2KB'''

        config_code = Code(
            code_string=config,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        config_code.scale(0.8).next_to(java_code, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(java_code), run_time=1)
        self.play(Create(config_code), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WebSocketScene(Scene):
    def construct(self):
        title = Text("WebSockets", font_size=48, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        config = '''@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    @Override
    public void configureMessageBroker(MessageBrokerRegistry registry) {
        registry.enableSimpleBroker("/topic");
        registry.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
            .setAllowedOrigins("*")
            .withSockJS();
    }
}'''

        handler = '''@MessageMapping("/chat")
@SendTo("/topic/messages")
public MessageDTO chat(@Payload MessageDTO message) {
    message.setTimestamp(LocalDateTime.now());
    return message;
}

// Frontend con STOMP
const socket = new SockJS('/ws');
const stompClient = Stomp.over(socket);
stompClient.connect({}, () => {
    stompClient.subscribe('/topic/messages', (message) => {
        console.log(JSON.parse(message.body));
    });
    stompClient.send('/app/chat', {}, JSON.stringify({text: 'Hola!'}));
});'''

        config_code = Code(
            code_string=config,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        config_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.5)

        handler_code = Code(
            code_string=handler,
            language="java",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        handler_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(config_code), run_time=1)
        self.play(Create(handler_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FlywayScene(Scene):
    def construct(self):
        title = Text("Flyway - Migraciones de DB", font_size=42, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        dependency = '''<!-- Dependencia -->
<dependency>
    <groupId>org.flywaydb</groupId>
    <artifactId>flyway-core</artifactId>
</dependency>
<dependency>
    <groupId>org.flywaydb</groupId>
    <artifactId>flyway-database-postgresql</artifactId>
</dependency>'''

        migration = '''-- V1__Create_usuarios.sql
CREATE TABLE usuarios (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- V2__Add_rol_column.sql
ALTER TABLE usuarios ADD COLUMN rol VARCHAR(20) DEFAULT 'USER';

-- V3__Create_productos.sql
CREATE TABLE productos (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    usuario_id BIGINT REFERENCES usuarios(id)
);'''

        dep_code = Code(
            code_string=dependency,
            language="xml",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        dep_code.scale(0.85).to_edge(LEFT, buff=0.5).shift(UP * 1.2)

        migration_code = Code(
            code_string=migration,
            language="sql",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        migration_code.scale(0.85).next_to(dep_code, DOWN, buff=0.4)

        self.play(Write(title), run_time=1)
        self.play(Create(dep_code), run_time=1)
        self.play(Create(migration_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerScene(Scene):
    def construct(self):
        title = Text("Docker con Spring Boot", font_size=44, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.5)

        dockerfile = '''# Dockerfile
FROM eclipse-temurin:21-jdk-alpine AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN ./mvnw package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]'''

        dockerfile_code = Code(
            code_string=dockerfile,
            language="dockerfile",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        dockerfile_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        docker_compose = '''# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=mydb
      - POSTGRE_USER=admin
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:'''

        compose_code = Code(
            code_string=docker_compose,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        compose_code.scale(0.85).next_to(dockerfile_code, DOWN, buff=0.3)

        self.play(Write(title), run_time=1)
        self.play(Create(dockerfile_code), run_time=1)
        self.play(Create(compose_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Spring Boot", font_size=42, color=SPRING_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Spring Boot: Opinionated framework para desarrollo rapido", font_size=22, color=TEXT_COLOR),
            Text("Inyeccion de dependencias con @Autowired", font_size=22, color=TEXT_COLOR),
            Text("Spring Data JPA: Abstraccion para acceso a datos", font_size=22, color=TEXT_COLOR),
            Text("Spring Security: Autenticacion y autorizacion", font_size=22, color=TEXT_COLOR),
            Text("JWT: Autenticacion stateless para APIs REST", font_size=22, color=TEXT_COLOR),
            Text("Validacion: Bean Validation con @Valid", font_size=22, color=TEXT_COLOR),
            Text("Excepciones: @ControllerAdvice para manejo centralizado", font_size=22, color=TEXT_COLOR),
            Text("Actuator: Observabilidad y health checks", font_size=22, color=TEXT_COLOR),
            Text("Testing: @SpringBootTest, MockMvc, @DataJpaTest", font_size=22, color=TEXT_COLOR),
            Text("Caching, Async, Scheduling: Funcionalidades avanzadas", font_size=22, color=TEXT_COLOR),
            Text("Docker: Contenedorizacion de aplicaciones", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Framework fundamental para desarrollo enterprise en Java",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SpringBootFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        SpringHistoryScene.construct(self)
        SpringBootPhilosophyScene.construct(self)
        SpringInitializrScene.construct(self)
        SpringApplicationScene.construct(self)
        ComponentScene.construct(self)
        DependencyInjectionScene.construct(self)
        BeanConfigurationScene.construct(self)
        ApplicationPropertiesScene.construct(self)
        YamlConfigurationScene.construct(self)
        RESTControllerScene.construct(self)
        RequestMappingScene.construct(self)
        RequestBodyScene.construct(self)
        SpringDataJPAIntroScene.construct(self)
        EntityScene.construct(self)
        JpaRepositoryScene.construct(self)
        RelationshipsScene.construct(self)
        ServiceLayerScene.construct(self)
        SpringSecurityIntroScene.construct(self)
        SecurityConfigScene.construct(self)
        JWTIntroductionScene.construct(self)
        JWTFilterScene.construct(self)
        ValidationScene.construct(self)
        ExceptionHandlingScene.construct(self)
        ActuatorScene.construct(self)
        TestingScene.construct(self)
        ProfileScene.construct(self)
        LoggingScene.construct(self)
        CachingScene.construct(self)
        AsyncScene.construct(self)
        SchedulingScene.construct(self)
        WebClientScene.construct(self)
        FileUploadScene.construct(self)
        WebSocketScene.construct(self)
        FlywayScene.construct(self)
        DockerScene.construct(self)
        ConclusionScene.construct(self)
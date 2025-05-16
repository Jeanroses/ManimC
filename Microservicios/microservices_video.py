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
MICRO_COLOR = "#94e2d5"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Arquitectura de Microservicios",
            font_size=52,
            color=MICRO_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(MICRO_COLOR, PRIMARY_COLOR)

        subtitle = Text(
            "Diseño, implementación y despliegue",
            font_size=26,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [MICRO_COLOR, PRIMARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
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


class MonolithicVsMicroservicesScene(Scene):
    def construct(self):
        title = Text("Monolito vs Microservicios", font_size=44, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        comparison = '''// ARQUITECTURA MONOLITICA
+ Todo en un solo deployment
+ Desarrollo simple inicial
+ Testing facil
+ Despliegue sencillo
- Dificil escalar
- Acoplamiento fuerte
- Tecnologia unica
- Fallo en todo el sistema
- CI/CD lento

// ARQUITECTURA DE MICROSERVICIOS
+ Escalabilidad independiente
+ Despliegue independientes
+ Tecnologia heterogenea
+ Equipos autonomos
+ Fallos aislados
+ Innovacion rapida
- Complejidad operativa
- Gestion de datos distribuidos
- Testing distribuido
- Latencia de red'''

        code = Code(
            code_string=comparison,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ServiceCharacteristicsScene(Scene):
    def construct(self):
        title = Text("Caracteristicas de Microservicios", font_size=40, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        characteristics = '''// PRINCIPIOS FUNDAMENTALES

1. Alta Cohesion
   - Cada servicio hace una cosa bien
   - Responsabilidad unica
   - Bound context definido

2. Bajo Acoplamiento
   - Interfaces bien definidas
   - Comunicacion via API
   - Independientes entre si

3. Deployment Independiente
   - Cada equipo despliega a su ritmo
   - Blue-green deployments
   - Canary releases

4. Base de datos propia
   - Cada servicio su propio schema
   - No comparten tablas
   - Transacciones distribuidas

5. Equipo de producto
 - Equipo completo (DevOps)
 - Ownership end-to-end
 - autonomia'''

        code = Code(
            code_string=characteristics,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ServiceCommunicationScene(Scene):
    def construct(self):
        title = Text("Comunicacion entre Servicios", font_size=40, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        communication = '''// COMUNICACION SINCRONA (REST/gRPC)

Sincrona: Cliente espera respuesta

// REST API
GET /api/orders/123
POST /api/users
PUT /api/products/456

// gRPC
- Protocol Buffers
- Mas rapido que REST
- Tipos fuertemente tipados
- Streaming bidireccional

// PROBLEMAS
- Acoplamiento temporal
- Latencia
- Cascading failures

// COMUNICACION ASINCRONA (Eventos)

Asincrona: Publicar/Suscribir

// Message Brokers
- RabbitMQ
- Apache Kafka
- AWS SQS/SNS
- Redis Streams

// Patrones
- Pub/Sub
- Event Sourcing
- CQRS'''

        code = Code(
            code_string=communication,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class APIGatewayScene(Scene):
    def construct(self):
        title = Text("API Gateway", font_size=48, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        api_gateway = '''// API GATEWAY

Punto de entrada unificado

// Responsabilidades
- Enrutamiento
- Autenticacion/Autorizacion
- Rate limiting
- Logging
- Transformacion de protocolos
- Circuit breaker

// Herramientas
- Kong
- AWS API Gateway
- Azure API Management
- NGINX
- Apigee

// Ejemplo: NGINX config
server {
    location /api/users {
        proxy_pass http://user-service:8080;
        auth_request /auth;
        limit_req zone=api_limit;
    }
    location /api/orders {
        proxy_pass http://order-service:8080;
    }
}'''

        code = Code(
            code_string=api_gateway,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ServiceDiscoveryScene(Scene):
    def construct(self):
        title = Text("Service Discovery", font_size=44, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        discovery = '''// SERVICE DISCOVERY

Como los servicios se encuentran

// Server-side Discovery
- Consul
- Eureka (Netflix)
- etcd
- Zookeeper

// Client-side Discovery
- Fabric/Feign (Spring)
- Ribbon (Netflix)

// Registro de servicios
POST /register
{
  "serviceId": "user-service",
  "hostname": "10.0.0.5",
  "port": 8080,
  "healthCheck": "/health"
}

// Health checks
- Heartbeat cada 30s
- Eliminacion si no responde
- DNS/HTTP discovery'''

        code = Code(
            code_string=discovery,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CircuitBreakerScene(Scene):
    def construct(self):
        title = Text("Circuit Breaker", font_size=48, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        circuit_breaker = '''// CIRCUIT BREAKER

Prevenir fallos en cascada

// Estados
1. CLOSED (Normal)
   - Peticions fluyen normal
   - Si fallos > umbral -> OPEN

2. OPEN (Fallo)
   - Rechazar peticiones
   - Timeout para verificar

3. HALF-OPEN (Recuperacion)
   - Prueba limitada
   - Si exitosa -> CLOSED

// Implementaciones
- Resilience4j (Java)
- Hystrix (Netflix)
- Polly (.NET)
- Sentinel (Alibaba)

// Configuracion
@CircuitBreaker(
  fallbackMethod = "fallback",
  failureThreshold = 50,
  waitDuration = 10s,
  successThreshold = 3
)
public Order getOrder(id) { }'''

        code = Code(
            code_string=circuit_breaker,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DataManagementScene(Scene):
    def construct(self):
        title = Text("Gestion de Datos", font_size=44, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        data = '''// DATOS EN MICROSERVICIOS

// Base de datos por servicio
- Cada servicio su propia DB
- Schema independiente
- No comparten tablas

// PROBLEMAS

1. Transacciones distribuidas
   - No ACID entre servicios
   - Solucion: Saga Pattern

2. Consultas entre servicios
   - No puedo hacer JOIN
   - Solucion: API composition

// SAGA PATTERN

Orquestacion:
Order -> Payment -> Inventory -> Shipping

// Compensating transactions
- Si falla Payment
- Rollback Inventory
- Cancel Order

// Patrones
- Choreography (eventos)
- Orchestration (orquestador)

// API Composition
- GraphQL federation
- BFF (Backend for Frontend)'''

        code = Code(
            code_string=data,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ContainerizationScene(Scene):
    def construct(self):
        title = Text("Contenedores y Docker", font_size=44, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        docker = '''// DOCKERFILE para microservicio

FROM openjdk:17-alpine
WORKDIR /app
COPY target/app.jar app.jar
EXPOSE 8080
ENV JAVA_OPTS="-Xmx512m"
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]

// docker-compose.yml

services:
  user-service:
    build: ./user-service
    ports:
      - "8081:8080"
    environment:
      - DB_HOST=postgres
    depends_on:
      - postgres

  order-service:
    build: ./order-service
    ports:
      - "8082:8080"
    environment:
      - KAFKA_BROKER=kafka
    depends_on:
      - kafka

  postgres:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data

  kafka:
    image: confluentinc/cp-kafka
    ports:
      - "9092:9092"'''

        code = Code(
            code_string=docker,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class KubernetesScene(Scene):
    def construct(self):
        title = Text("Kubernetes para Microservicios", font_size=38, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        k8s = '''// deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: myapp/user-service:v1
        ports:
        - containerPort: 8080
        resources:
          limits:
            memory: "512Mi"
            cpu: "500m"

// service.yaml

apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP

// Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
spec:
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /users
        backend:
          service:
            name: user-service
            port:
              number: 80'''

        code = Code(
            code_string=k8s,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ObservabilityScene(Scene):
    def construct(self):
        title = Text("Observabilidad", font_size=48, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        observability = '''// PILARES DE OBSERVABILIDAD

1. LOGS
   - Estructurados (JSON)
   - Niveles: ERROR, WARN, INFO, DEBUG
   - Correlation IDs para tracing

2. METRICAS
   - PromQL/Grafana
   - Latencia, throughput, errores
   - Utilization de recursos

3. TRACING
   - Distributed tracing
   - Jaeger, Zipkin
   - Trace ID propagate

// EFK Stack
- Elasticsearch
- Fluentd
- Kibana

// Prometheus + Grafana
- Scrape metrics
- Alerting
- Dashboards

// OpenTelemetry
- Estandar de instrumentation
- Vendor-agnostic'''

        code = Code(
            code_string=observability,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class CI_CDScene(Scene):
    def construct(self):
        title = Text("CI/CD para Microservicios", font_size=42, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        cicd = '''// GITHUB ACTIONS

name: CI Pipeline

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: ./mvnw test
      - name: Build
        run: ./mvnw package -DskipTests
      - name: Build Docker
        run: docker build -t app:${{ github.sha }} .

// GITHUB ACTIONS - Deploy

deploy:
  needs: test
  runs-on: ubuntu-latest
  if: github.ref == refs/heads/main
  steps:
    - name: Deploy to K8s
      run: |
        kubectl set image deployment/user-service \
        user-service=app:${{ github.sha }}

strategies:
  - canary
  - blue-green
  - rolling update'''

        code = Code(
            code_string=cicd,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class MicroservicesPatternsScene(Scene):
    def construct(self):
        title = Text("Patrones de Diseno", font_size=44, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        patterns = '''// PATRONES ESENCIALES

1. API Gateway
   - Punto de entrada unificado

2. Service Discovery
   - Localizacion dinamica

3. Circuit Breaker
   - Tolerancia a fallos

4. CQRS
   - Separacion lectura/escritura

5. Event Sourcing
   - Estado via eventos

6. Strangler Fig
   - Migracion gradual

7. Sidecar
   - Log sidecar (Fluentd)

8. Ambassador
   - Cliente sidecar

9. Adapter
   - Formato de datos

10. Database per Service
    - Datos distribuidos

11. Saga
    - Transacciones distribuidas

12. BFF
    - Backend for Frontend

13. Service Mesh
    - Istio, Linkerd, Consul Connect'''

        code = Code(
            code_string=patterns,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ServiceMeshScene(Scene):
    def construct(self):
        title = Text("Service Mesh", font_size=48, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        service_mesh = '''// SERVICE MESH

Infraestructura para comunicación

// QUE PROVEE?
- mTLS automatico
- Tracing distribuido
- Balanceo de carga
- Retry/Timeout
- Traffic splitting

// ISTIO
- Control plane: istiod
- Data plane: Envoy proxies
- Virtual services
- Destination rules

// Ejemplo Istio
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews
spec:
  http:
  - route:
    - destination:
        host: reviews
        subset: v2
      weight: 50
    - destination:
        host: reviews
        subset: v3
      weight: 50

// LINKERD
- Ligero
- Rust-based
- Simpler que Istio

// CONSUL CONNECT
- HashiCorp ecosystem'''

        code = Code(
            code_string=service_mesh,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SecurityScene(Scene):
    def construct(self):
        title = Text("Seguridad en Microservicios", font_size=40, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.5)

        security = '''// SEGURIDAD

1. AUTENTICACION
   - OAuth 2.0 / OpenID Connect
   - JWT tokens
   - Keycloak, Auth0

2. AUTORIZACION
   - RBAC (Role-based)
   - ABAC (Attribute-based)
   - Policies

3. mTLS (Mutual TLS)
   - Service mesh
   - Certs automaticos
   - Spiffe standard

4. SECRETOS
   - Vault (HashiCorp)
   - Kubernetes secrets
   - AWS Secrets Manager

5. API SECURITY
   - Rate limiting
   - Input validation
   - API keys

// JWT Token
{
  "alg": "RS256",
  "typ": "JWT"
}
{
  "sub": "user123",
  "role": "admin",
  "exp": 1715623400
}'''

        code = Code(
            code_string=security,
            language="json",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Microservicios", font_size=38, color=MICRO_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Monolito vs Microservicios: trade-offs", font_size=22, color=TEXT_COLOR),
            Text("Alta cohesion y bajo acoplamiento", font_size=22, color=TEXT_COLOR),
            Text("Comunicacion sincrona y asincrona", font_size=22, color=TEXT_COLOR),
            Text("API Gateway y Service Discovery", font_size=22, color=TEXT_COLOR),
            Text("Circuit Breaker para tolerancia a fallos", font_size=22, color=TEXT_COLOR),
            Text("Gestion de datos: Saga y CQRS", font_size=22, color=TEXT_COLOR),
            Text("Docker y Kubernetes para despliegue", font_size=22, color=TEXT_COLOR),
            Text("Observabilidad: Logs, Metricas, Tracing", font_size=22, color=TEXT_COLOR),
            Text("CI/CD con estrategias de despliegue", font_size=22, color=TEXT_COLOR),
            Text("Service Mesh: Istio, Linkerd", font_size=22, color=TEXT_COLOR),
            Text("Seguridad: OAuth, JWT, mTLS", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Arquitectura moderna para aplicaciones escalables",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class MicroservicesFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        MonolithicVsMicroservicesScene.construct(self)
        ServiceCharacteristicsScene.construct(self)
        ServiceCommunicationScene.construct(self)
        APIGatewayScene.construct(self)
        ServiceDiscoveryScene.construct(self)
        CircuitBreakerScene.construct(self)
        DataManagementScene.construct(self)
        ContainerizationScene.construct(self)
        KubernetesScene.construct(self)
        ObservabilityScene.construct(self)
        CI_CDScene.construct(self)
        MicroservicesPatternsScene.construct(self)
        ServiceMeshScene.construct(self)
        SecurityScene.construct(self)
        ConclusionScene.construct(self)
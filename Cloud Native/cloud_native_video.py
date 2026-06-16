from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
CLOUD_COLOR = "#4285f4"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Cloud Native", font_size=60, color=CLOUD_COLOR).set_color_by_gradient(CLOUD_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class ServerlessScene(Scene):
    def construct(self):
        title = Text("Serverless Computing", font_size=48, color=CLOUD_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# AWS Lambda - Serverless
import json
import boto3

def lambda_handler(event, context):
    # Procesar evento
    body = json.loads(event.get("body", "{}"))
    nombre = body.get("nombre", "Mundo")

    # Interactuar con otros servicios
    dynamodb = boto3.resource("dynamodb")
    tabla = dynamodb.Table("Usuarios")
    tabla.put_item(Item={
        "id": context.aws_request_id,
        "nombre": nombre,
        "timestamp": context.log_stream_name
    })

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "mensaje": f"Hola {nombre}!",
            "requestId": context.aws_request_id
        })
    }

# SAM Template (Serverless Application Model)
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  MiFuncion:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./src
      Handler: index.handler
      Runtime: nodejs20.x
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /hello
            Method: GET

# Azure Functions
module.exports = async function (context, req) {
    context.log("Funcion ejecutada");
    context.res = { body: "Hola desde Azure!" };
};'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class TwelveFactorScene(Scene):
    def construct(self):
        title = Text("12-Factor App", font_size=48, color=CLOUD_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# 12-Factor App - Metodologia para apps nativas cloud

# 1. Codebase - Un codigo, multiples despliegues
git remote add production https://git.heroku.com/myapp-prod.git
git remote add staging https://git.heroku.com/myapp-staging.git

# 2. Dependencies - Declaradas explicitamente
# package.json / requirements.txt / go.mod
npm install express

# 3. Config - En variables de entorno
export DB_URL="postgres://user:pass@host:5432/db"
export REDIS_URL="redis://localhost:6379"

# 4. Backing Services - Recursos como adjuntos
# DB, cache, colas son recursos intercambiables
DATABASE_URL=postgres://...
REDIS_URL=redis://...

# 5. Build, Release, Run - Etapas separadas
# build -> release -> run
docker build -t myapp:${BUILD_TAG} .
heroku container:release web

# 6. Processes - Sin estado (stateless)
# No guardar datos localmente
# Usar Redis o DB externa para sesiones

# 7. Port Binding - Servicio autonomo
# La app es su propio servidor
app.listen(process.env.PORT || 3000)

# 8. Concurrency - Escalar con procesos
# Horizontal scaling via procesos
kubectl scale deployment myapp --replicas=5

# 9. Disposability - Inicio rapido, cierre graceful
process.on("SIGTERM", () => {
  server.close(() => process.exit(0));
});

# 10. Dev/Prod Parity - Similaridad entornos
docker-compose up  # igual en dev y prod

# 11. Logs - Como flujo de eventos
# stdout/stderr, no archivos
logger.info("Request processed");

# 12. Admin Processes - Tareas puntuales
heroku run rails db:migrate
kubectl exec pod -- python manage.py migrate'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ContainersCloudScene(Scene):
    def construct(self):
        title = Text("Contenedores Cloud", font_size=48, color=CLOUD_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Cloud Native Containers

# Kubernetes Pod
apiVersion: v1
kind: Pod
metadata:
  name: web-app
  labels:
    app: web
    version: v1
spec:
  containers:
  - name: app
    image: myapp:latest
    ports:
    - containerPort: 3000
    env:
    - name: DB_URL
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: url
    resources:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 500m
        memory: 256Mi
    livenessProbe:
      httpGet:
        path: /healthz
        port: 3000
      initialDelaySeconds: 3
      periodSeconds: 10

# Horizontal Pod Autoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70

# Service Mesh (Istio)
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: web-vs
spec:
  hosts:
  - web-app
  http:
  - match:
    - headers:
        version:
          exact: v2
    route:
    - destination:
        host: web-app
        subset: v2
  - route:
    - destination:
        host: web-app
        subset: v1
      weight: 90
    - destination:
        host: web-app
        subset: v2
      weight: 10'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ObservabilidadScene(Scene):
    def construct(self):
        title = Text("Observabilidad", font_size=48, color=CLOUD_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Three Pillars of Observability

# 1. LOGS - Eventos discretos
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Usuario creado", extra={
    "user_id": usuario.id,
    "action": "create",
    "duration_ms": 45
})

# Structured logging (JSON)
{"level": "info", "message": "Request processed",
 "method": "GET", "path": "/api/users",
 "status": 200, "duration_ms": 120}

# 2. METRICS - Datos agregados
from prometheus_client import Counter, Histogram, Gauge

requests_total = Counter("http_requests_total", "Total requests", ["method", "path"])
request_duration = Histogram("http_request_duration_seconds", "Request duration", ["method"])
users_active = Gauge("users_active", "Active users")

@ app.route("/api/users")
def get_users():
    with request_duration.labels(method="GET").time():
        users_active.inc()
        result = get_all_users()
        requests_total.labels(method="GET", path="/api/users").inc()
        users_active.dec()
        return jsonify(result)

# 3. TRACES - Flujo de requests
from opentelemetry import trace
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("procesar_pedido") as span:
    span.set_attribute("pedido.id", pedido_id)

    with tracer.start_as_current_span("validar_pago") as child:
        child.add_event("Inicio validacion")
        resultado = validar_pago()
        child.set_attribute("pago.exitoso", resultado)

    with tracer.start_as_current_span("actualizar_inventario"):
        actualizar_stock()

# Distribued tracing con Jaeger
# Trace: arbol completo de spans
# Span: unidad de trabajo individual'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class CICDCloudScene(Scene):
    def construct(self):
        title = Text("CI/CD Cloud Native", font_size=48, color=CLOUD_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# GitLab CI para Cloud Native
image: docker:latest

services:
  - docker:dind

variables:
  DOCKER_HOST: tcp://docker:2375
  DOCKER_TLS_CERTDIR: ""

stages:
  - build
  - test
  - package
  - deploy

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

test:
  stage: test
  script:
    - npm run test:coverage
    - npm run lint
  coverage: /All files[^|]*\|[^|]*\s+([\d.]+)/

package:
  stage: package
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy_staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/app app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - kubectl rollout status deployment/app
  environment: staging
  only:
    - develop

deploy_production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl set image deployment/app app=$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - kubectl rollout status deployment/app
  environment: production
  when: manual
  only:
    - main

# GitOps con ArgoCD
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
spec:
  destination:
    namespace: default
    server: https://kubernetes.default.svc
  source:
    repoURL: https://gitlab.com/myteam/myapp.git
    path: k8s
    targetRevision: main
  syncPolicy:
    automated:
      prune: true
      selfHeal: true'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Cloud Native", font_size=38, color=CLOUD_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Serverless con AWS Lambda y SAM", font_size=22, color=TEXT_COLOR),
            Text("12-Factor App methodology", font_size=22, color=TEXT_COLOR),
            Text("Kubernetes y HPA", font_size=22, color=TEXT_COLOR),
            Text("Service Mesh con Istio", font_size=22, color=TEXT_COLOR),
            Text("Observabilidad: logs, metrics, traces", font_size=22, color=TEXT_COLOR),
            Text("GitOps con ArgoCD", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Arquitectura para la nube moderna", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class CloudNativeFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        ServerlessScene.construct(self)
        TwelveFactorScene.construct(self)
        ContainersCloudScene.construct(self)
        ObservabilidadScene.construct(self)
        CICDCloudScene.construct(self)
        ConclusionScene.construct(self)

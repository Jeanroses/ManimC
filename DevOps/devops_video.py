from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
DEVOPS_COLOR = "#f05030"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("DevOps", font_size=60, color=DEVOPS_COLOR).set_color_by_gradient(DEVOPS_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class CICDScene(Scene):
    def construct(self):
        title = Text("CI/CD Pipelines", font_size=48, color=DEVOPS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# GitLab CI/CD Pipeline
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: registry.gitlab.com/$CI_PROJECT_PATH

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE:$CI_COMMIT_SHA .
    - docker push $DOCKER_IMAGE:$CI_COMMIT_SHA
  only:
    - main

test:
  stage: test
  script:
    - npm ci
    - npm run lint
    - npm run test:coverage
    - npm run build
  artifacts:
    paths:
      - coverage/
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

deploy_staging:
  stage: deploy
  script:
    - kubectl set image deployment/app app=$DOCKER_IMAGE:$CI_COMMIT_SHA
  environment:
    name: staging
  only:
    - develop

deploy_production:
  stage: deploy
  script:
    - kubectl set image deployment/app app=$DOCKER_IMAGE:$CI_COMMIT_SHA
  environment:
    name: production
  when: manual
  only:
    - main

# GitHub Actions
name: CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test
      - run: npm run build'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class IaCScene(Scene):
    def construct(self):
        title = Text("Infraestructura como Codigo", font_size=48, color=DEVOPS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Terraform - AWS
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "main-vpc" }
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.${count.index}.0/24"
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

resource "aws_ecs_cluster" "main" {
  name = "main-cluster"
}

resource "aws_ecs_service" "app" {
  name = "app-service"
  cluster = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  launch_type = "FARGATE"
  desired_count = 3
  network_configuration {
    subnets = aws_subnet.public[*].id
    security_groups = [aws_security_group.app.id]
  }
}

# Ansible Playbook
---
- name: Configurar servidores web
  hosts: webservers
  become: yes
  tasks:
    - name: Instalar nginx
      apt:
        name: nginx
        state: latest
    - name: Iniciar servicio
      service:
        name: nginx
        state: started
        enabled: yes
    - name: Copiar configuracion
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: reiniciar nginx
  handlers:
    - name: reiniciar nginx
      service:
        name: nginx
        state: restarted'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ContenedoresScene(Scene):
    def construct(self):
        title = Text("Contenedores y K8s", font_size=48, color=DEVOPS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Multi-stage Dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Docker Compose
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      DB_HOST: postgres
      REDIS_HOST: redis
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
  postgres:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: myapp
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
  redis:
    image: redis:7-alpine

# Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: app
  template:
    metadata:
      labels:
        app: app
    spec:
      containers:
      - name: app
        image: myapp:latest
        ports:
        - containerPort: 3000
        resources:
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class MonitoreoScene(Scene):
    def construct(self):
        title = Text("Monitoreo y Observabilidad", font_size=48, color=DEVOPS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Prometheus - Metricas
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: kubernetes
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        action: keep
        regex: myapp

  - job_name: node
    static_configs:
      - targets:
        - localhost:9100

# Grafana Dashboard - JSON
{
  "title": "App Dashboard",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [{
        "expr": "rate(http_requests_total[5m])",
        "legendFormat": "{{method}}"
      }]
    },
    {
      "title": "Error Rate",
      "type": "graph",
      "targets": [{
        "expr": "rate(http_errors_total[5m])",
        "legendFormat": "{{status}}"
      }]
    },
    {
      "title": "P99 Latency",
      "type": "graph",
      "targets": [{
        "expr": "histogram_quantile(0.99, rate(http_duration_seconds_bucket[5m]))",
        "legendFormat": "p99"
      }]
    }
  ]
}

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.exporter.otlp import OTLPSpanExporter

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("procesar-solicitud") as span:
    span.set_attribute("usuario.id", user_id)
    span.add_event("inicio procesamiento")
    resultado = procesar()
    span.set_attribute("resultado.tamano", len(resultado))'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class LoggingScene(Scene):
    def construct(self):
        title = Text("Logging y Alertas", font_size=48, color=DEVOPS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# ELK Stack (Elasticsearch, Logstash, Kibana)

# Filebeat - Recoleccion de logs
filebeat.inputs:
- type: container
  paths:
    - /var/lib/docker/containers/*/*.log
  processors:
    - add_kubernetes_metadata:
        host: ${NODE_NAME}

output.elasticsearch:
  hosts: ["${ELASTICSEARCH_HOST}:9200"]
  username: ${ELASTICSEARCH_USER}
  password: ${ELASTICSEARCH_PASS}

# Logstash Pipeline
input {
  beats { port => 5044 }
}
filter {
  grok {
    match => { "message" => "%{COMBINEDAPACHELOG}" }
  }
  date {
    match => ["timestamp", "dd/MMM/yyyy:HH:mm:ss Z"]
  }
}
output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "logs-app-%{+YYYY.MM.dd}"
  }
}

# Kibana Query
# Visualizaciones: barras, lineas, mapas
# Dashboards personalizados
# Alertas basadas en umbrales

# Alertmanager (Prometheus)
groups:
- name: critical
  rules:
  - alert: HighErrorRate
    expr: rate(http_errors_total[5m]) > 0.05
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Tasa de error alta: {{ $value }}"

# PagerDuty integration
# On-call rotation
# Escalamiento automatico'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: DevOps", font_size=38, color=DEVOPS_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("CI/CD con GitLab y GitHub Actions", font_size=22, color=TEXT_COLOR),
            Text("IaC con Terraform y Ansible", font_size=22, color=TEXT_COLOR),
            Text("Docker y contenedores", font_size=22, color=TEXT_COLOR),
            Text("Kubernetes y orquestacion", font_size=22, color=TEXT_COLOR),
            Text("Prometheus y Grafana", font_size=22, color=TEXT_COLOR),
            Text("ELK Stack y logging centralizado", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Cultura, automatizacion y medicion", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class DevOpsFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        CICDScene.construct(self)
        IaCScene.construct(self)
        ContenedoresScene.construct(self)
        MonitoreoScene.construct(self)
        LoggingScene.construct(self)
        ConclusionScene.construct(self)

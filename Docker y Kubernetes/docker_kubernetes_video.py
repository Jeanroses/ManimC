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
DOCKER_COLOR = "#2496ED"
KUBERNETES_COLOR = "#326CE5"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Docker y Kubernetes",
            font_size=52,
            color=PRIMARY_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(DOCKER_COLOR, KUBERNETES_COLOR)

        subtitle = Text(
            "Contenedores y orquestacion a escala",
            font_size=28,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [DOCKER_COLOR, KUBERNETES_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
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


class WhatIsDockerScene(Scene):
    def construct(self):
        title = Text("Que es Docker?", font_size=48, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores",
            font_size=24,
            color=TEXT_COLOR,
            line_spacing=1.3,
        )
        definition.next_to(title, DOWN, buff=0.6)

        containers = VGroup(
            Text("Contenedor:", font_size=26, color=HIGHLIGHT_COLOR),
            Text("Paquete ligero y autocontenido que incluye todo lo necesario", font_size=20, color=TEXT_COLOR),
            Text("- Codigo fuente", font_size=18, color=ACCENT_COLOR),
            Text("- Runtime (Python, Node, etc.)", font_size=18, color=ACCENT_COLOR),
            Text("- Librerias y dependencias", font_size=18, color=ACCENT_COLOR),
            Text("- Configuracion del sistema", font_size=18, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        containers.next_to(definition, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(FadeIn(containers), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerVsVMScene(Scene):
    def construct(self):
        title = Text("Docker vs Virtual Machines", font_size=42, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        vm_diagram = VGroup(
            Text("Virtual Machine", font_size=22, color=WARNING_COLOR),
            RoundedRectangle(width=3, height=4, corner_radius=0.1, color=WARNING_COLOR, stroke_width=2),
            Text("Hypervisor", font_size=18, color=TEXT_COLOR).move_to(ORIGIN + UP * 1.5),
        ).arrange(DOWN, buff=0.1)

        container_diagram = VGroup(
            Text("Docker Container", font_size=22, color=SUCCESS_COLOR),
            RoundedRectangle(width=3, height=2.5, corner_radius=0.1, color=SUCCESS_COLOR, stroke_width=2),
            Text("Docker Engine", font_size=18, color=TEXT_COLOR).move_to(ORIGIN + UP * 0.8),
        ).arrange(DOWN, buff=0.1)

        vm_diagram.to_edge(LEFT, buff=0.8).shift(UP * 0.3)
        container_diagram.to_edge(RIGHT, buff=0.8).shift(UP * 0.3)

        comparison = VGroup(
            Text("VM: Hipervisor, OS completo, GBs", font_size=18, color=TEXT_COLOR),
            Text("Container: Docker Engine, kernel compartido, MBs", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.2)
        comparison.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(vm_diagram[1]), FadeIn(vm_diagram[0]), run_time=1)
        self.play(Create(container_diagram[1]), FadeIn(container_diagram[0]), run_time=1)
        self.play(FadeIn(comparison), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerImagesScene(Scene):
    def construct(self):
        title = Text("Docker Images", font_size=48, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        image_concept = '''// Concepto de imagen
- Plantilla inmutable
- Capas superpuestas (union filesystem)
- Tag: version o variante (latest, alpine, 3.9-slim)
- Registry: repositorio (Docker Hub, GCR, ECR, Harbor)

// Comandos basicos
docker pull nginx:latest
docker images
docker image ls
docker rmi nginx
docker image prune

// Buscar imagenes
docker search nginx
docker search alpine --limit 10'''

        code = Code(
            code_string=image_concept,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerfileScene(Scene):
    def construct(self):
        title = Text("Dockerfile", font_size=48, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        dockerfile = '''# Imagen base
FROM node:20-alpine AS builder

# Metadatos
LABEL maintainer="dev@example.com"
LABEL version="1.0"

# Variables de entorno
ENV NODE_ENV=production
ENV PORT=3000

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY package*.json ./
RUN npm ci --only=production
COPY . .

# Exponer puerto
EXPOSE 3000

# Comando por defecto
CMD ["node", "server.js"]

# Multi-stage build
FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]'''

        code = Code(
            code_string=dockerfile,
            language="dockerfile",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerCommandsScene(Scene):
    def construct(self):
        title = Text("Comandos Docker Esenciales", font_size=40, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        commands = '''// Gestion de contenedores
docker run -d -p 8080:3000 --name mi-app mi-imagen
docker run -d --restart=always --env FILE=.env mi-imagen
docker run -d -v /path/local:/path/container mi-imagen
docker run -d --network mi-red mi-imagen

docker ps
docker ps -a
docker logs -f mi-app
docker exec -it mi-app bash
docker stop mi-app
docker rm mi-app
docker rm -f mi-app

// Gestion de imagenes
docker build -t mi-imagen:latest .
docker tag mi-imagen:latest registry.com/mi-imagen:v1
docker push registry.com/mi-imagen:v1
docker pull registry.com/mi-imagen:v1

// Inspeccion
docker inspect mi-app
docker stats
docker network ls
docker volume ls'''

        code = Code(
            code_string=commands,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerComposeScene(Scene):
    def construct(self):
        title = Text("Docker Compose", font_size=48, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        compose = '''version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DB_HOST=db
    depends_on:
      - db
    networks:
      - frontend
      - backend
    volumes:
      - ./src:/app/src

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass mypass

networks:
  frontend:
  backend:

volumes:
  db-data:'''

        code = Code(
            code_string=compose,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerNetworkingScene(Scene):
    def construct(self):
        title = Text("Docker Networking", font_size=44, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        networks = '''// Tipos de redes
bridge      - Red por defecto, contenedores aislados
host        - Contenedor comparte red con host
overlay     - Multi-host,Swarm mode
macvlan     - MAC address por contenedor
none        - Sin red

// Crear red personalizada
docker network create mi-red
docker network rm mi-red

// DNS automatico
docker run -d --name service1 myimage
docker run -d --name service2 myimage
# service2 puede reaching service1 por nombre

// Puertos
-p 8080:3000  # host:container
-P           # Puerto aleatorio

// Variables de entorno
--env VAR1=value1
--env-file .env'''

        code = Code(
            code_string=networks,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerVolumesScene(Scene):
    def construct(self):
        title = Text("Docker Volumes", font_size=48, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        volumes = '''// Tipos de volumenes
// Named volumes
docker volume create mi-volumen
docker run -v mi-volumen:/path/container myimage

// Bind mounts (archivos del host)
docker run -v /path/local:/path/container myimage

// tmpfs (en memoria)
docker run --tmpfs /path/container myimage

// Volume drivers
docker volume create --driver nas myvolume

// Comandos
docker volume ls
docker volume inspect mi-volumen
docker volume rm mi-volumen
docker volume prune

// Backup
docker run --rm -v mi-volumen:/data -v $(pwd):/backup alpine tar cvf /backup/backup.tar /data

// Restore
docker run --rm -v mi-volumen:/data -v $(pwd):/backup alpine tar xvf /backup/backup.tar -C /data'''

        code = Code(
            code_string=volumes,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerSecurityScene(Scene):
    def construct(self):
        title = Text("Docker Security", font_size=48, color=DOCKER_COLOR)
        title.to_edge(UP, buff=0.5)

        security = '''// Usuario no root
RUN addgroup -g 1000 appgroup && \\
    adduser -u 1000 -G appgroup -D appuser
USER appuser

// Limitar recursos
docker run --memory=512m --cpus=0.5 myimage
docker run --memory-reservation=256m myimage

// Read-only filesystem
docker run --read-only --tmpfs /tmp myimage

// Capabilities
docker run --cap-add=SYS_ADMIN myimage
docker run --cap-drop=ALL myimage

// Seccomp
docker run --security-opt seccomp=default myimage

// SELinux/AppArmor
docker run --security-opt label=type:container_runtime_t myimage

// Scan de vulnerabilidades
docker scout cves myimage
trivy image myimage
dockle myimage

// Best practices
- Usar imagenes oficiales
- No exponer secretos
- Usar saludos (HEALTHCHECK)
- Minimizar layers'''

        code = Code(
            code_string=security,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class WhatIsK8sScene(Scene):
    def construct(self):
        title = Text("Que es Kubernetes?", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        definition = Text(
            "Sistema de orquestacion de contenedores para automatizar despliegue, escalado y gestion",
            font_size=24,
            color=TEXT_COLOR,
            line_spacing=1.3,
        )
        definition.next_to(title, DOWN, buff=0.6)

        features = VGroup(
            Text("Caracteristicas principales:", font_size=26, color=HIGHLIGHT_COLOR),
            Text("Automated scheduling", font_size=22, color=TEXT_COLOR),
            Text("Self-healing (restart failed containers)", font_size=22, color=TEXT_COLOR),
            Text("Horizontal scaling", font_size=22, color=TEXT_COLOR),
            Text("Service discovery y load balancing", font_size=22, color=TEXT_COLOR),
            Text("Automated rollbacks y rollouts", font_size=22, color=TEXT_COLOR),
            Text("Secret y configuration management", font_size=22, color=TEXT_COLOR),
            Text("Storage orchestration", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        features.next_to(definition, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(definition), run_time=1)
        self.play(FadeIn(features), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class K8sArchitectureScene(Scene):
    def construct(self):
        title = Text("Arquitectura de Kubernetes", font_size=40, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        architecture = '''// Control Plane (Master)
- kube-api-server: API REST
- etcd: Base de datos distribuida
- kube-scheduler: Asigna pods a nodos
- kube-controller-manager: Controladores
- cloud-controller-manager: Integracion cloud

// Node (Worker)
- kubelet: Agent que comunica con master
- kube-proxy: Networking
- container runtime: Docker, containerd, CRI-O

// Componentes del Pod
- container: Imagen ejecutable
- pause: Infra container
- init container: Pre-startup scripts
- sidecar: Helper containers'''

        code = Code(
            code_string=architecture,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=20,
        )
        code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class K8sPodsScene(Scene):
    def construct(self):
        title = Text("Pods", font_size=48, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        pod_yaml = '''apiVersion: v1
kind: Pod
metadata:
  name: my-app
  labels:
    app: my-app
    tier: frontend
spec:
  containers:
  - name: app
    image: myapp:1.0
    ports:
    - containerPort: 8080
    env:
    - name: ENV_VAR
      value: "production"
    resources:
      requests:
        memory: "128Mi"
        cpu: "250m"
      limits:
        memory: "256Mi"
        cpu: "500m"
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 30
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
    volumeMounts:
    - name: data
      mountPath: /data

  initContainers:
  - name: init-db
    image: busybox:1.36
    command: ['sh', '-c', 'echo Initializing...']

  volumes:
  - name: data
    emptyDir: {}'''

        code = Code(
            code_string=pod_yaml,
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


class K8sDeploymentsScene(Scene):
    def construct(self):
        title = Text("Deployments", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        deployment = '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: myapp:1.0
        ports:
        - containerPort: 8080
---
# Comandos
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl describe deployment my-app
kubectl rollout status deployment my-app
kubectl rollout history deployment my-app
kubectl rollout undo deployment my-app
kubectl rollout undo deployment my-app --to-revision=2
kubectl scale deployment my-app --replicas=5'''

        code = Code(
            code_string=deployment,
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


class K8sServicesScene(Scene):
    def construct(self):
        title = Text("Services", font_size=48, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        services_yaml = '''# ClusterIP (default - interno)
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080

# NodePort (exponer en cada nodo)
kind: Service
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080

# LoadBalancer (cloud provider)
kind: Service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8080

# Headless (sin ClusterIP)
kind: Service
spec:
  clusterIP: None
  selector:
    app: my-app'''

        code = Code(
            code_string=services_yaml,
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


class K8sIngressScene(Scene):
    def construct(self):
        title = Text("Ingress", font_size=48, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        ingress = '''apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /web
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
  - host: admin.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-service
            port:
              number: 80
---
# TLS
spec:
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        backend:
          service:
            name: my-service
            port:
              number: 80'''

        code = Code(
            code_string=ingress,
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


class K8sConfigMapsSecretsScene(Scene):
    def construct(self):
        title = Text("ConfigMaps y Secrets", font_size=42, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        configmap = '''# ConfigMap - Configuracion
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  database_url: "postgres://db:5432/mydb"
  app_config.json: |
    {"debug": false, "maxUsers": 100}
---
# Secret - Datos sensibles
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  # echo -n "admin" | base64
  username: YWRtaW4=
  # echo -n "secretpass" | base64
  password: c2VjcmV0cGFzcw==
---
# Uso en Pod
env:
- name: DB_URL
  valueFrom:
    configMapKeyRef:
      name: my-config
      key: database_url
- name: DB_PASSWORD
  valueFrom:
    secretKeyRef:
      name: my-secret
      key: password
envFrom:
- configMapRef:
    name: my-config
- secretRef:
    name: my-secret'''

        code = Code(
            code_string=configmap,
            language="yaml",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class K8sPVCPVCScene(Scene):
    def construct(self):
        title = Text("PersistentVolumes y Claims", font_size=40, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        storage = '''# PersistentVolume
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: standard
  hostPath:
    path: /mnt/data

# PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
---
# Usage in Pod
spec:
  containers:
  - name: app
    image: myapp:1.0
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: my-pvc'''

        code = Code(
            code_string=storage,
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


class K8sStatefulSetsScene(Scene):
    def construct(self):
        title = Text("StatefulSets", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        stateful = '''apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: mysql
        image: mysql:8
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
---
# Caracteristicas
- Nombres estables (mysql-0, mysql-1, mysql-2)
- Identidad de red estable
- Ordering y graceful deployment
- Persistent storage con PVCs'''

        code = Code(
            code_string=stateful,
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


class K8sRBACScene(Scene):
    def construct(self):
        title = Text("RBAC - Control de Acceso", font_size=42, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        rbac = '''# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-app-sa

# Role (namespace scope)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]

# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
subjects:
- kind: ServiceAccount
  name: my-app-sa
  namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io

# ClusterRole (cluster scope)
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]

# ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: secret-reader-binding
subjects:
- kind: User
  name: developer
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io'''

        code = Code(
            code_string=rbac,
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


class K8sNamespaceScene(Scene):
    def construct(self):
        title = Text("Namespaces", font_size=48, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        namespace = '''apiVersion: v1
kind: Namespace
metadata:
  name: production
---
# ResourceQuota
apiVersion: v1
kind: ResourceQuota
metadata:
  name: prod-quota
  namespace: production
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    pods: "20"
    persistentvolumeclaims: "10"
---
# LimitRange
apiVersion: v1
kind: LimitRange
metadata:
  name: prod-limits
  namespace: production
spec:
  limits:
  - max:
      cpu: "2"
      memory: "2Gi"
    min:
      cpu: "100m"
      memory: "128Mi"
    default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "200m"
      memory: "256Mi"
    type: Container
---
# Comandos
kubectl get namespaces
kubectl create namespace dev
kubectl config set-context --current --namespace=dev'''

        code = Code(
            code_string=namespace,
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


class K8sHelmScene(Scene):
    def construct(self):
        title = Text("Helm - Package Manager", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        helm = '''# Estructura de Chart
mychart/
  Chart.yaml          # Metadata
  values.yaml         # Configuracion por defecto
  values-prod.yaml    # Override para prod
  templates/          # Plantillas K8s
    deployment.yaml
    service.yaml
    _helpers.tpl       # Funciones reutilizables
  charts/             # Dependencias
  crds/               # Custom Resources

# Comandos
helm create mychart
helm install myrelease mychart
helm upgrade myrelease mychart
helm rollback myrelease 1
helm uninstall myrelease
helm list
helm history myrelease

# Repos
helm repo add bitnami https://charts.bitnami.com/bitnami
helm search repo nginx
helm pull bitnami/nginx --version 15.0.0
helm template mychart -f values-prod.yaml

# Show template
helm template mychart
helm template mychart --debug'''

        code = Code(
            code_string=helm,
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


class K8sMonitoringScene(Scene):
    def construct(self):
        title = Text("Monitoring y Logging", font_size=42, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        monitoring = '''# Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl top node
kubectl top pod

# Prometheus + Grafana
# Helm install
helm install prometheus prometheus-community/kube-prometheus-stack

# Dashboard
# Grafana: visualizar metricas
# Prometheus: queries PromQL

# Logs
kubectl logs my-pod
kubectl logs -f my-pod
kubectl logs --previous my-pod
kubectl logs my-pod -c app
kubectl logs -l app=my-app --all-containers=true

# Centralized logging (ELK/EFK)
# Fluentd -> Elasticsearch -> Kibana

# Alerts
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: my-app-monitor
spec:
  selector:
    matchLabels:
      app: my-app
  podMetricsEndpoints:
  - port: metrics'''

        code = Code(
            code_string=monitoring,
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


class K8sNetworkingScene(Scene):
    def construct(self):
        title = Text("Networking en K8s", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        networking = '''# NetworkPolicy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
spec:
  podSelector:
    matchLabels:
      app: my-app
  policyTypes:
  - Ingress

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-db
spec:
  podSelector:
    matchLabels:
      app: database
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: backend
    ports:
    - port: 5432
      protocol: TCP

# DNS
# Service: my-service.namespace.svc.cluster.local
# Pod: pod-ip.namespace.pod.cluster.local
# External: service.example.com

# Ingress Controller
# nginx, traefik, ambassador, istio'''

        code = Code(
            code_string=networking,
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


class K8sAutoscalingScene(Scene):
    def construct(self):
        title = Text("Autoscaling", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        autoscaling = '''# HPA - Horizontal Pod Autoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15

# VPA - Vertical Pod Autoscaler
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Auto"

# Cluster Autoscaler (Cloud)
#scale-down-enabled: true
#scale-down-delay-after-add: 10m'''

        code = Code(
            code_string=autoscaling,
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


class K8sTroubleshootingScene(Scene):
    def construct(self):
        title = Text("Troubleshooting", font_size=44, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        troubleshooting = '''# Debug Pods
kubectl describe pod my-pod
kubectl logs my-pod
kubectl logs -f my-pod -c container-name
kubectl exec -it my-pod -- /bin/bash

# Debug Deployments
kubectl rollout status deployment my-app
kubectl rollout history deployment my-app

# Events
kubectl get events
kubectl get events --sort-by='.lastTimestamp'
kubectl get events --field-selector involvedObject.name=my-pod

# Node issues
kubectl describe node worker-node-1
kubectl top node worker-node-1

# API server issues
kubectl auth can-i create pods --as=developer@default

# DNS issues
kubectl exec -it my-pod -- nslookup service-name
kubectl exec -it my-pod -- cat /etc/resolv.conf

# Resource issues
kubectl top pod
kubectl describe node | grep -A 5 "Allocated resources"

# Common commands
kubectl get all
kubectl get pods -o wide
kubectl get pods --show-labels
kubectl get pods -l app=my-app
kubectl get pods -o jsonpath='{.items[*].status.podIP}'

# Port forwarding
kubectl port-forward pod/my-pod 8080:80

# Copy files
kubectl cp my-pod:/path/in/pod /local/path
kubectl cp /local/path my-pod:/path/in/pod'''

        code = Code(
            code_string=troubleshooting,
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


class K8sCI_CDScene(Scene):
    def construct(self):
        title = Text("CI/CD con Kubernetes", font_size=42, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        cicd = '''# GitOps con ArgoCD
# Install
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# ArgoCD Application
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/my-app
    targetRevision: HEAD
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true

# FluxCD (another GitOps)
# Helm + Kustomize for configuration management

# Pipeline tipico
# 1. Build: docker build -t myapp:$COMMIT .
# 2. Test: pytest, integration tests
# 3. Scan: trivy image --security-checks vuln myapp
# 4. Push: docker push registry/myapp:$COMMIT
# 5. Deploy: kubectl set image deployment/my-app app=registry/myapp:$COMMIT
# 6. Verify: kubectl rollout status
# 7. Notify: slack webhook notification'''

        code = Code(
            code_string=cicd,
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


class K8sBestPracticesScene(Scene):
    def construct(self):
        title = Text("Best Practices", font_size=48, color=KUBERNETES_COLOR)
        title.to_edge(UP, buff=0.5)

        best_practices = VGroup(
            Text("1. Usar deployments en lugar de pods desnudos", font_size=20, color=TEXT_COLOR),
            Text("2. Requests y limits en todos los contenedores", font_size=20, color=TEXT_COLOR),
            Text("3. Readiness y Liveness probes", font_size=20, color=TEXT_COLOR),
            Text("4. Labels para organizacion", font_size=20, color=TEXT_COLOR),
            Text("5. Resources quotas por namespace", font_size=20, color=TEXT_COLOR),
            Text("6. RBAC - principio de menor privilegio", font_size=20, color=TEXT_COLOR),
            Text("7. No usar latest en imagenes", font_size=20, color=TEXT_COLOR),
            Text("8. Secrets vs ConfigMaps", font_size=20, color=TEXT_COLOR),
            Text("9. Network policies para segmentation", font_size=20, color=TEXT_COLOR),
            Text("10. Pod disruption budgets para actualizaciones", font_size20, color=TEXT_COLOR),
            Text("11. Logs centralizados", font_size=20, color=TEXT_COLOR),
            Text("12. Health checks en la aplicacion", font_size20, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        best_practices.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for bp in best_practices:
            self.play(FadeIn(bp, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Docker y Kubernetes", font_size=38, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Docker: Contenedores ligeros y portables", font_size=22, color=TEXT_COLOR),
            Text("Dockerfile: Receta para crear imagenes", font_size22, color=TEXT_COLOR),
            Text("Docker Compose: Multi-contenedor local", font_size22, color=TEXT_COLOR),
            Text("Kubernetes: Orquestacion a escala production", font_size22, color=TEXT_COLOR),
            Text("Pods: Unidad minima de scheduling", font_size22, color=TEXT_COLOR),
            Text("Deployments: Declarative updates y rollbacks", font_size22, color=TEXT_COLOR),
            Text("Services: Exposición y descubrimiento interno", font_size22, color=TEXT_COLOR),
            Text("Ingress: HTTP routing externo", font_size22, color=TEXT_COLOR),
            Text("Helm: Package manager para K8s", font_size22, color=TEXT_COLOR),
            Text("Monitoring: Prometheus + Grafana", font_size22, color=TEXT_COLOR),
            Text("Autoscaling: HPA, VPA, Cluster Autoscaler", font_size22, color=TEXT_COLOR),
            Text("CI/CD: GitOps con ArgoCD/Flux", font_size22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Infraestructura moderna para aplicaciones cloud-native",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DockerKubernetesFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        WhatIsDockerScene.construct(self)
        DockerVsVMScene.construct(self)
        DockerImagesScene.construct(self)
        DockerfileScene.construct(self)
        DockerCommandsScene.construct(self)
        DockerComposeScene.construct(self)
        DockerNetworkingScene.construct(self)
        DockerVolumesScene.construct(self)
        DockerSecurityScene.construct(self)
        WhatIsK8sScene.construct(self)
        K8sArchitectureScene.construct(self)
        K8sPodsScene.construct(self)
        K8sDeploymentsScene.construct(self)
        K8sServicesScene.construct(self)
        K8sIngressScene.construct(self)
        K8sConfigMapsSecretsScene.construct(self)
        K8sPVCPVCScene.construct(self)
        K8sStatefulSetsScene.construct(self)
        K8sRBACScene.construct(self)
        K8sNamespaceScene.construct(self)
        K8sHelmScene.construct(self)
        K8sMonitoringScene.construct(self)
        K8sNetworkingScene.construct(self)
        K8sAutoscalingScene.construct(self)
        K8sTroubleshootingScene.construct(self)
        K8sCI_CDScene.construct(self)
        K8sBestPracticesScene.construct(self)
        ConclusionScene.construct(self)
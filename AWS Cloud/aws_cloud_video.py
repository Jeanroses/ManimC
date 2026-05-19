from manim import *
import numpy as np

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
AWS_COLOR = "#ff9900"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("AWS Cloud", font_size=60, color=AWS_COLOR).set_color_by_gradient(AWS_COLOR, ACCENT_COLOR)
        subtitle = Text("Amazon Web Services - Servicios en la nube", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class EC2Scene(Scene):
    def construct(self):
        title = Text("EC2 - Elastic Compute Cloud", font_size=44, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# Instancias EC2 - VMs en la nube

# Tipos de instancia
# General: t3, t2 (burstable)
# Compute: c5, c6 (high CPU)
# Memory: r5, r6 (RAM grande)
# Storage: i3, d2 (SSD/NVMe)

# Lanzar instancia via AWS CLI
aws ec2 run-instances \\
  --image-id ami-0c55b159cbfafe1f0 \\
  --count 1 \\
  --instance-type t3.micro \\
  --key-name mi-keypair \\
  --security-group-ids sg-xxxx \\
  --subnet-id subnet-xxxx

# User Data (script al iniciar)
--user-data file://init.sh

# SSH a la instancia
ssh -i "mi-keypair.pem" ec2-user@ip-publica

# Instalar nginx
sudo yum install -y nginx
sudo systemctl start nginx

# Security Groups (firewall)
aws ec2 authorize-security-group-ingress \\
  --group-id sg-xxxx \\
  --protocol tcp \\
  --port 22 \\
  --cidr 0.0.0.0/0

# Elastic IP (IP fija)
aws ec2 allocate-address
aws ec2 associate-address \\
  --instance-id i-xxxx \\
  --allocation-id eipalloc-xxxx

# snapshots
aws ec2 create-snapshot \\
  --volume-id vol-xxxx

# ASG - Auto Scaling Group
aws autoscaling create-auto-scaling-group \\
  --auto-scaling-group-name mi-asg \\
  --min-size 2 \\
  --max-size 10 \\
  --desired-capacity 4'''

        code_str = Code(code=code, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class S3Scene(Scene):
    def construct(self):
        title = Text("S3 - Simple Storage Service", font_size=44, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# S3 - Almacenamiento de objetos

# Buckets
aws s3 mb s3://mi-bucket-2024

# Subir archivos
aws s3 cp archivo.txt s3://mi-bucket/
aws s3 sync ./carpeta s3://mi-bucket/carpeta/

# Descargar
aws s3 cp s3://mi-bucket/archivo.txt ./

# Generar URL pre-firmada (1 hora)
aws s3 presign s3://mi-bucket/archivo.txt \\
  --expires-in 3600

# Politicas de bucket
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": "*",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::mi-bucket/*"
  }]
}

# Versioning
aws s3api put-bucket-versioning \\
  --bucket mi-bucket \\
  --versioning-configuration Status=Enabled

# Lifecycle rules
aws s3api put-bucket-lifecycle-configuration \\
  --bucket mi-bucket \\
  --lifecycle-configuration file://lifecycle.json

# Clase de almacenamiento
# Standard (frecuente)
# IA - Infrequent Access
# Glacier (archivo, minutos a horas)
# Intelligent Tiering (automatico)

# Replication
aws s3api put-bucket-replication \\
  --bucket bucket-destino \\
  --replication-configuration file://replication.json

# CloudFront (CDN)'''

        code_str = Code(code=code, language="json", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class IAMScene(Scene):
    def construct(self):
        title = Text("IAM - Identity Access Management", font_size=42, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# IAM - Usuarios, roles, politicas

# Crear usuario
aws iam create-user --user-name mi-usuario

# Crear access key
aws iam create-access-key --user-name mi-usuario

# Adjuntar politica gestionada
aws iam attach-user-policy \\
  --user-name mi-usuario \\
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# Crear rol para EC2
aws iam create-role \\
  --role-name mi-rol \\
  --assume-role-policy-document file://trust.json

# Politica inline
aws iam put-role-policy \\
  --role-name mi-rol \\
  --policy-name mi-politica \\
  --policy-document file://politica.json

# Grupo
aws iam create-group --group-name desarrolladores
aws iam add-user-to-group \\
  --user-name mi-usuario \\
  --group-name desarrolladores

# Policy example
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:PutObject"
    ],
    "Resource": "arn:aws:s3:::mi-bucket/*"
  }]
}

# Password policy
aws iam update-account-password-policy \\
  --minimum-password-length 12 \\
  --require-symbols \\
  --require-numbers \\
  --require-uppercase-characters

# MFA
aws iam create-virtual-mfa-device \\
  --virtual-mfa-device-name mi-mfa'''

        code_str = Code(code=code, language="json", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class RDSScene(Scene):
    def construct(self):
        title = Text("RDS - Relational Database Service", font_size=42, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# RDS - MySQL, PostgreSQL, Oracle, SQL Server

# Crear instancia
aws rds create-db-instance \\
  --db-instance-identifier mi-db \\
  --db-instance-class db.t3.micro \\
  --engine mysql \\
  --allocated-storage 20 \\
  --master-username admin \\
  --master-user-password miPassword123

# engine: mysql, postgres, mariadb, oracle-ee, sqlserver-ex

# Multi-AZ (alta disponibilidad)
aws rds modify-db-instance \\
  --db-instance-identifier mi-db \\
  --multi-az \\
  --apply-immediately

# Read replica
aws rds create-db-instance-read-replica \\
  --db-instance-identifier mi-db-read \\
  --source-db-instance-identifier mi-db

# snapshots
aws rds create-db-snapshot \\
  --db-instance-identifier mi-db \\
  --db-snapshot-identifier mi-snapshot

# Restaurar desde snapshot
aws rds restore-db-instance-from-db-snapshot \\
  --db-instance-identifier mi-db-nueva \\
  --db-snapshot-identifier mi-snapshot

# Connection
mysql -h mi-db.xxxx.us-east-1.rds.amazonaws.com \\
  -u admin -p

# Parameter groups
aws rds create-db-parameter-group \\
  --db-parameter-group-name mi-params \\
  --db-parameter-group-family mysql8.0 \\
  --description "Mis parametros"'''

        code_str = Code(code=code, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class LambdaScene(Scene):
    def construct(self):
        title = Text("Lambda - Computo sin servidores", font_size=42, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# Lambda - Funciones serverless

# python-lambda
def handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hola Lambda"
    }

# Crear funcion
aws lambda create-function \\
  --function-name mi-funcion \\
  --runtime python3.11 \\
  --role arn:aws:iam::123456:role/lambda-role \\
  --handler lambda_function.handler \\
  --zip-file fileb://function.zip

# Invocar
aws lambda invoke \\
  --function-name mi-funcion \\
  --payload '{"nombre": "Juan"}' \\
  response.json

# Environment variables
aws lambda update-function-configuration \\
  --function-name mi-funcion \\
  --environment Variables={DB_HOST=localhost}

# Layers (dependencias)
aws lambda publish-layer-version \\
  --layer-name mis-dependencias \\
  --zip-file file://layer.zip \\
  --compatible-runtimes python3.11

# Event Source Mapping (S3 trigger)
aws lambda create-event-source-mapping \\
  --function-name mi-funcion \\
  --event-source-arn arn:aws:s3:::mi-bucket

# CloudWatch Events (trigger programado)
aws events put-rule \\
  --name mi-cron \\
  --schedule-expression "rate(5 minutes)"

aws lambda add-permission \\
  --function-name mi-funcion \\
  --statement-id cron-invoke \\
  --action lambda:InvokeFunction \\
  --principal events.amazonaws.com'''

        code_str = Code(code=code, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class VPCScene(Scene):
    def construct(self):
        title = Text("VPC - Virtual Private Cloud", font_size=44, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# VPC - Red virtual privada

# Crear VPC
aws ec2 create-vpc \\
  --cidr-block 10.0.0.0/16
# Output: vpc-xxxx

# Subnets (al menos 2 AZs)
aws ec2 create-subnet \\
  --vpc-id vpc-xxxx \\
  --cidr-block 10.0.1.0/24 \\
  --availability-zone us-east-1a

aws ec2 create-subnet \\
  --vpc-id vpc-xxxx \\
  --cidr-block 10.0.2.0/24 \\
  --availability-zone us-east-1b

# Internet Gateway
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway \\
  --vpc-id vpc-xxxx \\
  --internet-gateway-id igw-xxxx

# Route Table
aws ec2 create-route-table --vpc-id vpc-xxxx
aws ec2 create-route \\
  --route-table-id rtb-xxxx \\
  --destination-cidr-block 0.0.0.0/0 \\
  --gateway-id igw-xxxx

# Security Groups
aws ec2 create-security-group \\
  --group-name mi-sg \\
  --description "Security group" \\
  --vpc-id vpc-xxxx

aws ec2 authorize-security-group-ingress \\
  --group-id sg-xxxx \\
  --protocol tcp \\
  --port 80 \\
  --cidr 0.0.0.0/0

# NAT Gateway (para instancias privadas)
aws ec2 create-nat-gateway \\
  --subnet-id subnet-publica \\
  --allocation-id eip-xxxx

# VPC Peering
aws ec2 create-vpc-peering-connection \\
  --vpc-id vpc-xxxx \\
  --peer-vpc-id vpc-yyyy'''

        code_str = Code(code=code, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class CloudWatchScene(Scene):
    def construct(self):
        title = Text("CloudWatch - Monitoreo", font_size=44, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# CloudWatch - Metricas y logs

# Dashboard
aws cloudwatch put-dashboard \\
  --dashboard-name mi-dashboard \\
  --dashboard-body file://dashboard.json

# Alarmas
aws cloudwatch put-metric-alarm \\
  --alarm-name alta-cpu \\
  --metric-name CPUUtilization \\
  --namespace AWS/EC2 \\
  --statistic Average \\
  --period 300 \\
  --threshold 80 \\
  --comparison-operator GreaterThanThreshold \\
  --evaluation-periods 2 \\
  --alarm-actions arn:aws:sns:us-east-1:123456:mi-tema

# Logs
aws logs create-log-group \\
  --log-group-name /aws/lambda/mi-funcion

aws logs put-log-events \\
  --log-group-name /aws/lambda/mi-funcion \\
  --log-stream-name stream-1 \\
  --log-events \\
    timestamp=1234567890000,\\
    message="Log message"

# Insights (query logs)
fields @timestamp, @message \\
| filter @message like /error/ \\
| sort @timestamp desc \\
| limit 20

# Metric Filter
aws logs put-metric-filter \\
  --log-group-name /aws/ec2/mi-instance \\
  --filter-name errores \\
  --metric-transformations \\
    metricName=ErrorCount,\\
    metricNamespace=MiApp,\\
    metricValue=1 \\
  --filter-pattern "error"

# Events
aws events put-rule \\
  --name "cpu-high" \\
  --event-pattern file://pattern.json

# SNS Topic (notificaciones)
aws sns create-topic --name mi-tema
aws sns subscribe \\
  --topic-arn arn:aws:sns:... \\
  --protocol email \\
  --notification-endpoint correo@mail.com'''

        code_str = Code(code=code, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class EKSScene(Scene):
    def construct(self):
        title = Text("EKS - Elastic Kubernetes Service", font_size=42, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# EKS - Kubernetes manejado

# Crear cluster
aws eks create-cluster \\
  --name mi-cluster \\
  --role-arn arn:aws:iam::123456:role/eks-role \\
  --resources-vpc-config subnetIds=subnet-xxx,subnet-yyy

# Configurar kubectl
aws eks update-kubeconfig --name mi-cluster

# kubectl commands
kubectl get nodes
kubectl get pods -A
kubectl get services

# Deploy aplicacion
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mi-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mi-app
  template:
    metadata:
      labels:
        app: mi-app
    spec:
      containers:
      - name: mi-app
        image: mi-repo/mi-app:latest
        ports:
        - containerPort: 8080

# Ingress con ALB
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mi-ingress
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
spec:
  rules:
  - http:
      paths:
      - path: /
        backend:
          service:
            name: mi-servicio
            port:
              number: 80

# HPA (Auto Scaling)
kubectl autoscale deployment mi-app \\
  --cpu-percent=70 \\
  --min=2 --max=10'''

        code_str = Code(code=code, language="yaml", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class Route53Scene(Scene):
    def construct(self):
        title = Text("Route 53 - DNS", font_size=48, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# Route 53 - Servicio DNS

# Crear hosted zone
aws route53 create-hosted-zone \\
  --name midominio.com \\
  --caller-reference $(date +%s)

# Crear record sets
aws route53 change-resource-record-sets \\
  --hosted-zone-id ZXXXXX \\
  --change-batch file://records.json

# records.json
{
  "Changes": [{
    "Action": "CREATE",
    "ResourceRecordSet": {
      "Name": "www.midominio.com",
      "Type": "A",
      "TTL": 300,
      "ResourceRecords": [
        {"Value": "52.45.67.89"}
      ]
    }
  }]
}

# Alias para CloudFront/S3
{
  "Name": "midominio.com",
  "Type": "A",
  "AliasTarget": {
    "DNSName": "d123.cloudfront.net",
    "HostedZoneId": "Z2FDTNDATAQYW2"
  }
}

# Routing policies
# Simple - una respuesta
# Weighted - porcentaje
# Latency - menor latencia
# Failover - primario/secundario
# Geolocation - por ubicacion

# Health checks
aws route53 create-health-check \\
  --caller-reference $(date +%s) \\
  --health-check-config \\
    FullyQualifiedDomainName=api.midominio.com,\\
    Port=443,\\
    Type=HTTPS,\\
    ResourcePath="/health",\\
    RequestInterval=10,\\
    FailureThreshold=3'''

        code_str = Code(code=code, language="json", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class CICDScene(Scene):
    def construct(self):
        title = Text("CI/CD con CodePipeline", font_size=44, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# CodePipeline - CI/CD automatizado

# Crear pipeline
aws codepipeline create-pipeline \\
  --pipeline file://pipeline.json

# pipeline.json
{
  "pipeline": {
    "name": "mi-pipeline",
    "roleArn": "arn:aws:iam::123456:role/CodePipelineRole",
    "artifactStore": {
      "type": "S3",
      "location": "mi-codepipeline-artifacts"
    },
    "stages": [
      {
        "name": "Source",
        "actions": [{
          "name": "SourceAction",
          "actionTypeId": {
            "category": "Source",
            "owner": "ThirdParty",
            "provider": "GitHub",
            "version": "1"
          },
          "configuration": {
            "Owner": "mi-user",
            "Repo": "mi-repo",
            "Branch": "main",
            "OAuthToken": "xxx"
          },
          "outputArtifacts": ["SourceOutput"]
        }]
      },
      {
        "name": "Build",
        "actions": [{
          "name": "BuildAction",
          "actionTypeId": {
            "category": "Build",
            "owner": "AWS",
            "provider": "CodeBuild",
            "version": "1"
          },
          "configuration": {
            "ProjectName": "mi-codebuild-project"
          },
          "inputArtifacts": ["SourceOutput"],
          "outputArtifacts": ["BuildOutput"]
        }]
      },
      {
        "name": "Deploy",
        "actions": [{
          "name": "DeployAction",
          "actionTypeId": {
            "category": "Deploy",
            "owner": "AWS",
            "provider": "ECS",
            "version": "1"
          },
          "configuration": {
            "ClusterName": "mi-cluster",
            "ServiceName": "mi-servicio"
          },
          "inputArtifacts": ["BuildOutput"]
        }]
      }
    ]
  }
}

# CodeBuild buildspec.yml
version: 0.2
phases:
  install:
    commands:
      - npm install
  build:
    commands:
      - npm run build
      - npm test
artifacts:
  files:
    - "**/*"'''

        code_str = Code(code=code, language="json", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class SecurityScene(Scene):
    def construct(self):
        title = Text("Seguridad en AWS", font_size=48, color=AWS_COLOR)
        title.to_edge(UP, buff=0.5)

        code = '''# Security Hub, GuardDuty, WAF

# Security Hub
aws securityhub enable-security-hub \\
  --region us-east-1

# GuardDuty (deteccion amenazas)
aws guardduty create-detector \\
  --enable

# WAF (Web Application Firewall)
aws wafv2 create-web-acl \\
  --name mi-waf \\
  --scope CLOUDFRONT \\
  --default-action Block={}

# Web ACL con reglas
aws wafv2 create-rule-group \\
  --name mi-reglas \\
  --capacity 100 \\
  --rules file://rules.json

# Shield (proteccion DDoS)
aws shield create-protection \\
  --resource-arn arn:aws:cloudfront::123456:distribution/xxx

# KMS (Key Management Service)
aws kms create-key \\
  --description "Mi clave" \\
  --key-usage ENCRYPT_DECRYPT

aws kms encrypt \\
  --key-id alias/mi-clave \\
  --plaintext fileb://archivo.txt \\
  --output text --query CiphertextBlob

# Secrets Manager
aws secretsmanager create-secret \\
  --name mi-db-password \\
  --secret-string "password123"

# Macie (datos sensibles en S3)
aws macie2 enable-macie

# Config (compliance)
aws configservice start-config-rule-evaluation \\
  --config-rule-name required-tags'''

        code_str = Code(code=code, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code_str.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code_str), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code_str), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: AWS Cloud", font_size=38, color=AWS_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("EC2: Maquinas virtuales escalables", font_size=22, color=TEXT_COLOR),
            Text("S3: Almacenamiento de objetos", font_size=22, color=TEXT_COLOR),
            Text("IAM: Usuarios, roles, politicas", font_size=22, color=TEXT_COLOR),
            Text("RDS: Bases de datos relacionales", font_size=22, color=TEXT_COLOR),
            Text("Lambda: Computo serverless", font_size=22, color=TEXT_COLOR),
            Text("VPC: Redes virtuales privadas", font_size=22, color=TEXT_COLOR),
            Text("CloudWatch: Monitoreo y logs", font_size=22, color=TEXT_COLOR),
            Text("EKS: Kubernetes manejado", font_size=22, color=TEXT_COLOR),
            Text("Route 53: DNS y routing", font_size=22, color=TEXT_COLOR),
            Text("CodePipeline: CI/CD automatizado", font_size=22, color=TEXT_COLOR),
            Text("Seguridad: WAF, Shield, KMS", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Infraestructura cloud a escala global", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class AWSFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        EC2Scene.construct(self)
        S3Scene.construct(self)
        IAMScene.construct(self)
        RDSScene.construct(self)
        LambdaScene.construct(self)
        VPCScene.construct(self)
        CloudWatchScene.construct(self)
        EKSScene.construct(self)
        Route53Scene.construct(self)
        CICDScene.construct(self)
        SecurityScene.construct(self)
        ConclusionScene.construct(self)
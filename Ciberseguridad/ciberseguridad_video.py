from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
SECURITY_COLOR = "#e64553"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Ciberseguridad", font_size=60, color=SECURITY_COLOR).set_color_by_gradient(SECURITY_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class CifradoScene(Scene):
    def construct(self):
        title = Text("Cifrado y Hashing", font_size=48, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Cifrado simetrico (AES)
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
datos = b"Mensaje secreto"
token = cipher.encrypt(datos)
descifrado = cipher.decrypt(token)

# Cifrado asimetrico (RSA)
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

cifrado = public_key.encrypt(
    mensaje,
    padding.OAEP(padding.MGF1(hashes.SHA256()), hashes.SHA256(), None)
)

# Hashing con SHA-256
import hashlib
hash_obj = hashlib.sha256(b"datos").hexdigest()

# Hashing seguro para passwords
import bcrypt
password = b"mi_password_seguro"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
# Verificacion
bcrypt.checkpw(password, hashed)  # True

# Firmas digitales
signature = private_key.sign(
    mensaje,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)
try:
    public_key.verify(signature, mensaje, ...)
    print("Firma valida")
except:
    print("Firma invalida")'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class AutenticacionScene(Scene):
    def construct(self):
        title = Text("Autenticacion y Autorizacion", font_size=48, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# JWT (JSON Web Tokens)
import jwt
from datetime import datetime, timedelta

payload = {
    "user_id": 123,
    "role": "admin",
    "exp": datetime.utcnow() + timedelta(hours=1)
}
token = jwt.encode(payload, "secret_key", algorithm="HS256")
decoded = jwt.decode(token, "secret_key", algorithms=["HS256"])

# OAuth 2.0 Authorization Code Flow
# 1. Authorization Request
# GET /authorize?response_type=code&client_id=app&redirect_uri=callback
# 2. Authorization Code Grant
# POST /token
# grant_type=authorization_code&code=AUTH_CODE
# 3. Access Token Response
# { "access_token": "eyJhbGci...", "token_type": "Bearer", "expires_in": 3600 }

# TOTP (Time-based One-Time Password)
import pyotp
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)
codigo_actual = totp.now()
# Verificar codigo
totp.verify(codigo_actual)  # True

# RBAC (Role-Based Access Control)
ROLES = {
    "admin": ["read", "write", "delete", "admin"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}

def check_permission(user, action):
    permissions = ROLES.get(user.role, [])
    return action in permissions

# MFA (Multi-Factor Authentication)
# Algo que sabes (password) + algo que tienes (TOTP) + algo que eres (biometria)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class RedesScene(Scene):
    def construct(self):
        title = Text("Seguridad en Redes", font_size=48, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Firewall con iptables
# Permitir SSH solo desde red interna
iptables -A INPUT -p tcp --dport 22 -s 10.0.0.0/8 -j ACCEPT
# Permitir HTTP/HTTPS publico
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
# Denegar todo lo demas
iptables -A INPUT -j DROP

# IDS con Snort
# Regla para detectar SQL injection
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (
    msg: "SQL Injection attempt";
    content: "' OR 1=1";
    sid: 1000001; )

# VPN con WireGuard
[Interface]
PrivateKey = [CLAVE_PRIVADA]
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = [CLAVE_PUBLICA_PAR]
AllowedIPs = 10.0.0.2/32

# TLS 1.3 Handshake (simplificado)
# 1. ClientHello (soporta TLS 1.3, ciphers)
# 2. ServerHello + Certificado + KeyShare
# 3. Client Finished (cifrado)
# 4. Server Finished (cifrado)
# 5. Secure channel established

# Zero Trust Architecture
# - Nunca confiar, siempre verificar
# - Microsegmentacion de red
# - Acceso con privilegios minimos
# - Autenticacion continua'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class OWASPScene(Scene):
    def construct(self):
        title = Text("OWASP Top 10", font_size=48, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# OWASP Top 10 - Principales vulnerabilidades

# 1. XSS (Cross-Site Scripting)
# MALO:
<div th:text="${userInput}"></div>
# BUENO (escapado):
<div th:utext="${#strings.escapeXml(userInput)}"></div>

# 2. SQL Injection
# MALO:
query = "SELECT * FROM users WHERE id = " + user_id
# BUENO (parametrizado):
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))

# 3. CSRF (Cross-Site Request Forgery)
# MALO: Cookie se envia automaticamente
<img src="/api/transfer?amount=1000&to=atacante" />
# BUENO: Token CSRF
<form>
  <input type="hidden" name="_csrf" value="{{token}}" />
</form>

# 4. SSRF (Server-Side Request Forgery)
# MALO:
import requests
requests.get(request.GET["url"])
# BUENO:
ALLOWED = ["api.example.com"]
from urllib.parse import urlparse
if urlparse(url).hostname in ALLOWED:
    requests.get(url)

# 5. Security Headers
Content-Security-Policy: default-src 'self'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000
Referrer-Policy: strict-origin-when-cross-origin'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class CloudScene(Scene):
    def construct(self):
        title = Text("Seguridad en Cloud", font_size=48, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# AWS IAM Policy - Principio de minimo privilegio
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::mi-bucket/*",
        "Condition": {
            "IpAddress": {
                "aws:SourceIp": "10.0.0.0/8"
            }
        }
    }]
}

# AWS KMS - Encriptacion de datos
import boto3
kms = boto3.client("kms")
response = kms.encrypt(
    KeyId="alias/mi-llave",
    Plaintext=b"datos-sensibles"
)
cifrado = response["CiphertextBlob"]

# AWS WAF - Web Application Firewall
{
    "Name": "BloquearSQLi",
    "Priority": 1,
    "Statement": {
        "SqlInjectionMatchStatement": {
            "FieldToMatch": {"Type": "URI"}
        }
    },
    "Action": {"Block": {}}
}

# AWS Secrets Manager
import boto3
sm = boto3.client("secretsmanager")
secret = sm.get_secret_value(SecretId="prod/db/password")
password = secret["SecretString"]

# Security Groups
aws ec2 authorize-security-group-ingress \
    --group-id sg-123456 \
    --protocol tcp --port 443 \
    --cidr 10.0.0.0/16

# Bienes practices cloud
# - Encriptar en reposo y en transito
# - Rotacion de llaves y secretos
# - Auditoria con AWS CloudTrail
# - Parches de seguridad automaticos'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class PentestScene(Scene):
    def construct(self):
        title = Text("Ethical Hacking", font_size=48, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Nmap - Escaneo de puertos y servicios
nmap -sV -sC -O target.com
nmap -p 1-65535 -A 10.0.0.1

# Gobuster - Enumeracion de directorios
gobuster dir -u https://target.com -w /usr/share/wordlists/common.txt

# SQLMap - Deteccion de SQL injection
sqlmap -u "http://target.com/page?id=1" --batch --dbs
sqlmap -u "http://target.com/page?id=1" -D db_name --tables

# Metasploit Framework
msfconsole
use exploit/multi/handler
set PAYLOAD linux/x64/meterpreter/reverse_tcp
set LHOST 10.0.0.5
set LPORT 4444
run

# Burp Suite - Proxy de interceptacion
# 1. Proxy: Interceptar y modificar requests
# 2. Repeater: Reenviar requests modificados
# 3. Intruder: Ataques de fuerza bruta
# 4. Scanner: Vulnerabilidades automaticas

# John the Ripper - Crackeo de passwords
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Principios de Ethical Hacking
# - Autorizacion explicita por escrito
# - Alcance definido
# - Confidencialidad de datos
# - Reportar vulnerabilidades encontradas'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Ciberseguridad", font_size=38, color=SECURITY_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Cifrado simetrico y asimetrico", font_size=22, color=TEXT_COLOR),
            Text("Hashing y firmas digitales", font_size=22, color=TEXT_COLOR),
            Text("Autenticacion: JWT, OAuth, MFA", font_size=22, color=TEXT_COLOR),
            Text("Seguridad en redes: firewalls, VPN", font_size=22, color=TEXT_COLOR),
            Text("OWASP Top 10: XSS, SQLi, CSRF", font_size=22, color=TEXT_COLOR),
            Text("Seguridad en cloud: IAM, KMS, WAF", font_size=22, color=TEXT_COLOR),
            Text("Ethical hacking y pentesting", font_size=22, color=TEXT_COLOR),
            Text("Zero Trust Architecture", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Fundamento esencial en todo sistema moderno", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class CiberseguridadFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        CifradoScene.construct(self)
        AutenticacionScene.construct(self)
        RedesScene.construct(self)
        OWASPScene.construct(self)
        CloudScene.construct(self)
        PentestScene.construct(self)
        ConclusionScene.construct(self)

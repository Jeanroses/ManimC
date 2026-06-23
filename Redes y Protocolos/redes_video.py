from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
REDES_COLOR = "#0d47a1"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Redes y Protocolos", font_size=60, color=REDES_COLOR).set_color_by_gradient(REDES_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class TCPScene(Scene):
    def construct(self):
        title = Text("TCP/IP y Protocolos", font_size=48, color=REDES_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Modelo TCP/IP (4 capas)

# 1. Aplicacion: HTTP, DNS, SMTP, FTP, SSH
# 2. Transporte: TCP, UDP
# 3. Internet: IP, ICMP, ARP
# 4. Acceso Red: Ethernet, WiFi, PPP

# TCP - Transmission Control Protocol
# Orientado a conexion, confiable, ordenado
# Three-way handshake:
# 1. SYN (cliente -> servidor)
# 2. SYN-ACK (servidor -> cliente)
# 3. ACK (cliente -> servidor)

# TCP Segment Header
# Source Port (16) | Dest Port (16)
# Sequence Number (32)
# Acknowledgment Number (32)
# Data Offset (4) | Reserved (6) | Flags (6) | Window (16)
# Checksum (16) | Urgent Pointer (16)

# Flags TCP
# SYN: Iniciar conexion
# ACK: Confirmacion
# FIN: Cerrar conexion
# RST: Resetear conexion
# PSH: Push data
# URG: Urgente

# Flow Control - Ventana deslizante
# Congestion Control - Slow start, AIMD
# Ventana de congestion (cwnd)
# Umbral de slow start (ssthresh)

# UDP - User Datagram Protocol
# Sin conexion, no confiable, rapido
# Usado en: DNS, DHCP, VoIP, Streaming, Gaming

# Sockets en Python
import socket

# TCP Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(5)
while True:
    client, addr = server.accept()
    data = client.recv(1024)
    client.send(b"HTTP/1.1 200 OK\r\n\r\nHola!")
    client.close()'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class HTTPScene(Scene):
    def construct(self):
        title = Text("HTTP/1.1, HTTP/2 y HTTP/3", font_size=48, color=REDES_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# HTTP/1.1 (1997)
# - Conexiones persistentes (keep-alive)
# - Chunked transfer encoding
# - Cache control
# - Host header (virtual hosting)
# Problema: Head-of-line blocking

# HTTP/2 (2015)
# - Multiplexing (varios streams en una conexion)
# - Server push
# - Header compression (HPACK)
# - Binario (no texto)
# - Stream prioritization

# HTTP/3 (2022)
# - Usa QUIC (UDP-based)
# - 0-RTT handshake
# - Conexion migration
# - Sin Head-of-line blocking

# HTTP Methods
GET /api/users HTTP/1.1
Host: example.com
Accept: application/json
Authorization: Bearer token123

# Response
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 42
Cache-Control: max-age=3600

{"users": [{"id": 1, "name": "Juan"}]}

# Status Codes
# 1xx: Informational (101 Switching Protocols)
# 2xx: Success (200 OK, 201 Created, 204 No Content)
# 3xx: Redirection (301 Moved, 304 Not Modified)
# 4xx: Client Error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
# 5xx: Server Error (500 Internal, 502 Bad Gateway, 503 Service Unavailable)

# RESTful API Design
GET /api/users        # Listar usuarios
POST /api/users       # Crear usuario
GET /api/users/:id    # Obtener usuario
PUT /api/users/:id    # Actualizar usuario
DELETE /api/users/:id # Eliminar usuario'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class DNSScene(Scene):
    def construct(self):
        title = Text("DNS y CDN", font_size=48, color=REDES_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# DNS - Domain Name System

# Jerarquia DNS
# . (root) -> .com, .org, .net -> example.com -> www.example.com

# Tipos de registros DNS
# A: IPv4 address
# AAAA: IPv6 address
# CNAME: Canonical name (alias)
# MX: Mail exchange
# TXT: Text records (SPF, DKIM, DMARC)
# NS: Name server
# SOA: Start of Authority

# Resolucion DNS
# 1. Resolver consulta a root server
# 2. Root redirige a TLD server (.com)
# 3. TLD redirige a authoritative server (example.com)
# 4. Authoritative responde con IP

# DNS Query
nslookup example.com
dig example.com ANY
dig -x 8.8.8.8  # Reverse lookup

# CDN - Content Delivery Network
# Distribucion geografica de contenido
# Edge servers cercanos al usuario
# Beneficios: baja latencia, alta disponibilidad

# Anycast DNS
# Varios servidores comparten misma IP
# BGP enruta al mas cercano

# Cloudflare / AWS CloudFront / Akamai

# DDoS Protection
# Rate limiting
# WAF (Web Application Firewall)
# IP blacklisting
# Challenge (CAPTCHA, JS challenge)

# mDNS - Multicast DNS
# DNS sin servidor central
# .local domain
# Usado en IoT, Apple Bonjour'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class gRPCScene(Scene):
    def construct(self):
        title = Text("gRPC y WebSockets", font_size=48, color=REDES_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# gRPC - Remote Procedure Call moderno

# Protocol Buffers (protobuf)
syntax = "proto3";

service UsuarioService {
    rpc GetUser (GetUserRequest) returns (User);
    rpc ListUsers (ListUsersRequest) returns (ListUsersResponse);
    rpc CreateUser (CreateUserRequest) returns (User);
    rpc StreamUsers (Empty) returns (stream User);
}

message User {
    int32 id = 1;
    string name = 2;
    string email = 3;
}

message GetUserRequest {
    int32 id = 1;
}

# gRPC en Python
import grpc
import usuario_pb2
import usuario_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = usuario_pb2_grpc.UsuarioServiceStub(channel)
user = stub.GetUser(usuario_pb2.GetUserRequest(id=123))

# gRPC vs REST
# gRPC: HTTP/2, protobuf, streaming bidireccional
# REST: HTTP/1.1, JSON, mas simple

# WebSockets - Comunicacion bidireccional
import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Recibido: {message}")
        await websocket.send(f"Echo: {message}")

start_server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# WebSocket vs HTTP
# WebSocket: full-duplex, baja latencia, conexion persistente
# Usos: chat, juegos, trading, notificaciones real-time'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class SeguridadRedScene(Scene):
    def construct(self):
        title = Text("Seguridad en Redes", font_size=48, color=REDES_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Protocolos de Seguridad

# TLS 1.3 - Transport Layer Security
# 1. ClientHello: soporte TLS 1.3, key share, ciphers
# 2. ServerHello: seleccion de cipher, certificado
# 3. Client Finished: verificado
# 4. Server Finished: verificado
# 5. Datos cifrados con AES-GCM / ChaCha20-Poly1305

# IPsec - IP Security
# AH: Authentication Header (integridad)
# ESP: Encapsulating Security Payload (confidencialidad)
# Modos: Transport (host-host), Tunnel (gateway-gateway)

# VPN - Virtual Private Network
# OpenVPN, WireGuard, IPsec
# Tunneling y cifrado de todo el trafico

# SSH - Secure Shell
ssh-keygen -t ed25519 -C "user@example.com"
ssh -i ~/.ssh/id_ed25519 user@server.com

# Firewall
# iptables/nftables (Linux)
# pf (BSD)
# AWS Security Groups / Network ACLs

# IDS/IPS
# Snort, Suricata (deteccion de intrusiones)
# OSSEC (host-based IDS)

# Zero Trust Networking
# Nunca confiar, siempre verificar
# Microsegmentacion
# Acceso con privilegios minimos
# Autenticacion continua

# Wireshark - Analisis de paquetes
# tcpdump: captura en CLI
# tshark: version CLI de Wireshark
tcpdump -i eth0 port 80 -w captura.pcap'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Redes y Protocolos", font_size=38, color=REDES_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("TCP/IP: handshake, ventanas, control", font_size=22, color=TEXT_COLOR),
            Text("HTTP/1.1, HTTP/2, HTTP/3", font_size=22, color=TEXT_COLOR),
            Text("DNS jerarquico y resolucion", font_size=22, color=TEXT_COLOR),
            Text("gRPC y protobuf", font_size=22, color=TEXT_COLOR),
            Text("WebSockets tiempo real", font_size=22, color=TEXT_COLOR),
            Text("Seguridad: TLS, IPsec, VPN", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("La columna vertebral de internet", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class RedesyProtocolosFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        TCPScene.construct(self)
        HTTPScene.construct(self)
        DNSScene.construct(self)
        gRPCScene.construct(self)
        SeguridadRedScene.construct(self)
        ConclusionScene.construct(self)

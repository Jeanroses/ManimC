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
CISCO_COLOR = "#1BA0D7"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Fundamentos de Redes",
            font_size=52,
            color=CISCO_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(CISCO_COLOR, PRIMARY_COLOR)

        subtitle = Text(
            "Modelo OSI,TCP/IP y conceptos de networking",
            font_size=26,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [CISCO_COLOR, PRIMARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
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


class NetworkTypesScene(Scene):
    def construct(self):
        title = Text("Tipos de Redes", font_size=48, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        networks = VGroup(
            Text("LAN - Local Area Network", font_size=24, color=HIGHLIGHT_COLOR),
            Text("   Area geográfica limitada (casa, oficina, edificio)", font_size=20, color=TEXT_COLOR),
            Text("   Alta velocidad, bajo retardo", font_size=18, color=TEXT_COLOR),
            Text("   Ejemplos: Ethernet, WiFi", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("WAN - Wide Area Network", font_size=24, color=ACCENT_COLOR),
            Text("   Area geográfica extensa (ciudades, paises)", font_size=20, color=TEXT_COLOR),
            Text("   Menor velocidad, mayor retardo", font_size=18, color=TEXT_COLOR),
            Text("   Ejemplos: MPLS, Internet, VPN", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("MAN - Metropolitan Area Network", font_size=24, color=SUCCESS_COLOR),
            Text("   Area urbana (universidad, ciudad)", font_size=20, color=TEXT_COLOR),
            Text("   Velocidad media-alta", font_size=18, color=TEXT_COLOR),
            Text("", font_size=16),
            Text("PAN - Personal Area Network", font_size=24, color=CURVE_COLOR),
            Text("   Area personal (Bluetooth, USB)", font_size=20, color=TEXT_COLOR),
            Text("   Muy corto alcance", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        networks.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for n in networks:
            if n.text.strip():
                self.play(FadeIn(n, shift=RIGHT * 0.2), run_time=0.4)
                self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class OSIIntroScene(Scene):
    def construct(self):
        title = Text("Modelo OSI - 7 Capas", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        layers = VGroup(
            Text("7. Aplicacion (Application)", font_size=20, color=HIGHLIGHT_COLOR),
            Text("6. Presentacion (Presentation)", font_size=20, color=HIGHLIGHT_COLOR),
            Text("5. Sesion (Session)", font_size=20, color=HIGHLIGHT_COLOR),
            Text("4. Transporte (Transport)", font_size=20, color=ACCENT_COLOR),
            Text("3. Red (Network)", font_size=20, color=ACCENT_COLOR),
            Text("2. Enlace de Datos (Data Link)", font_size=20, color=SUCCESS_COLOR),
            Text("1. Fisica (Physical)", font_size=20, color=SUCCESS_COLOR),
        ).arrange(DOWN, buff=0.15)
        layers.next_to(title, DOWN, buff=0.6)

        mnemonic = Text(
            "Aquel Personas Siempre Tienen Redes De Fibra",
            font_size=22,
            color=CURVE_COLOR,
        )
        mnemonic.to_edge(DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for l in layers:
            self.play(FadeIn(l), run_time=0.4)
            self.wait(0.2)
        self.play(FadeIn(mnemonic), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class LayerDetailsScene(Scene):
    def construct(self):
        title = Text("Detalle de Capas OSI", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        layer1 = VGroup(
            Text("Capa 1 - Física", font_size=22, color=SUCCESS_COLOR),
            Text("Bits (0/1), cables, conectores, hubs", font_size=18, color=TEXT_COLOR),
            Text("NIC, RJ45, fibra optica, cobre", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1)

        layer2 = VGroup(
            Text("Capa 2 - Enlace de Datos", font_size=22, color=SUCCESS_COLOR),
            Text("Frames, MAC addresses, switches", font_size=18, color=TEXT_COLOR),
            Text("ARP, VLAN, STP, Ethernet", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1)

        layer3 = VGroup(
            Text("Capa 3 - Red", font_size=22, color=ACCENT_COLOR),
            Text("Paquetes, IP addresses, routers", font_size=18, color=TEXT_COLOR),
            Text("IP, ICMP, OSPF, BGP, NAT", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1)

        layer4 = VGroup(
            Text("Capa 4 - Transporte", font_size=22, color=ACCENT_COLOR),
            Text("Segmentos, puertos,TCP/UDP", font_size=18, color=TEXT_COLOR),
            Text("TCP, UDP, port forwarding", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1)

        layer1.to_edge(LEFT, buff=0.5).shift(UP * 1.5)
        layer2.to_edge(LEFT, buff=0.5).shift(DOWN * 0.2)
        layer3.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)
        layer4.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.2)

        self.play(Write(title), run_time=1)
        self.play(FadeIn(layer1), FadeIn(layer3), run_time=1)
        self.play(FadeIn(layer2), FadeIn(layer4), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TCPIPModelScene(Scene):
    def construct(self):
        title = Text("Modelo TCP/IP vs OSI", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        tcp_ip = '''// Modelo TCP/IP (4 capas)
4. Aplicacion     -> HTTP, FTP, SMTP, DNS, SSH
3. Transporte    -> TCP, UDP
2. Internet      -> IP, ICMP, ARP
1. Acceso Red    -> Ethernet, WiFi, PPP

// Correspondencia con OSI
TCP/IP    | OSI
----------|--------
Aplicacion| 7, 6, 5
Transporte| 4
Internet  | 3
Acceso Red| 2, 1'''

        code = Code(
            code_string=tcp_ip,
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


class IPAddressingScene(Scene):
    def construct(self):
        title = Text("Direccionamiento IP", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        ip_types = '''// IPv4 - 32 bits (4 bytes)
192.168.1.100
11000000.10101000.00000001.01100100

// Clases de IP (obsoletas pero conceptuales)
A: 1.0.0.0    - 126.255.255.255   (0xxxxxxx)
B: 128.0.0.0  - 191.255.255.255   (10xxxxxx)
C: 192.0.0.0  - 223.255.255.255   (110xxxxx)
D: 224.0.0.0  - 239.255.255.255   (multicast)
E: 240.0.0.0  - 255.255.255.255   (experimental)

// IPv6 - 128 bits
2001:0db8:85a3:0000:0000:8a2e:0370:7334

// Tipos de direcciones
- Publica: Internet (ruteable)
- Privada: Redes locales (RFC 1918)
  10.0.0.0/8
  172.16.0.0/12
  192.168.0.0/16
- Loopback: 127.0.0.1 (localhost)'''

        code = Code(
            code_string=ip_types,
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


class SubnettingScene(Scene):
    def construct(self):
        title = Text("Subnetting", font_size=48, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        subnet = '''// Subnetting - Dividir red en subredes mas pequenas

// Notacion CIDR
192.168.1.0/24  -> 256 direcciones (254 usable)
192.168.1.0/25  -> 128 direcciones (126 usable)
192.168.1.0/26  -> 64 direcciones (62 usable)
192.168.1.0/27  -> 32 direcciones (30 usable)
192.168.1.0/28  -> 16 direcciones (14 usable)

// Formula
Numero de hosts = 2^(32 - prefix) - 2

// Ejemplo: /24
- Network: 192.168.1.0
- Broadcast: 192.168.1.255
- Hosts: 192.168.1.1 - 192.168.1.254

// Subredes de /26
192.168.1.0/26   - 192.168.1.63
192.168.1.64/26  - 192.168.1.127
192.168.1.128/26 - 192.168.1.191
192.168.1.192/26 - 192.168.1.255

// Mascara de subred
/24 = 255.255.255.0
/25 = 255.255.255.128
/26 = 255.255.255.192
/27 = 255.255.255.224'''

        code = Code(
            code_string=subnet,
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


class SwitchingScene(Scene):
    def construct(self):
        title = Text(" switching", font_size=48, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        switch = '''// Switch - Capa 2
- MAC Address Table (CAM Table)
- Aprendizaje de direcciones
- Forwarding basado en MAC

// Proceso de switching
1. Receiving frame
2. Learn: guardar MAC origen
3. Lookup: buscar MAC destino
4. Forward: enviar al puerto correcto

// Frame forwarding
- Unicast (a destino especifico)
- Broadcast (FF:FF:FF:FF:FF:FF) -> todos los puertos
- Multicast (direccion multicast) -> grupo de puertos

// Metodos de switching
- Store and Forward (recibe todo el frame, verifica, reenvia)
- Cut-through (comienza a reenviar cuando tiene destino)
- Fragment-free (verifica primeros 64 bytes)'''

        code = Code(
            code_string=switch,
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


class VLANScene(Scene):
    def construct(self):
        title = Text("VLAN - Virtual LAN", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        vlan = '''// VLAN - Red LAN virtual
- Segmentacion logica
- Seguridad
- Broadcast control

// Tipos de VLAN
- Data VLAN: datos de usuario
- Voice VLAN: VoIP
- Management VLAN: administracion
- Native VLAN: VLAN sin tag (default VLAN 1)

// Configuracion Cisco
switch# configure terminal
switch(config)# vlan 10
switch(config-vlan)# name DATA
switch(config)# interface fastEthernet 0/1
switch(config-if)# switchport mode access
switch(config-if)# switchport access vlan 10

// Trunk - Multiple VLANs
switch(config-if)# switchport mode trunk
switch(config-if)# switchport trunk allowed vlan 10,20,30

// Inter-VLAN Routing
- Router on a stick
- Layer 3 Switch'''

        code = Code(
            code_string=vlan,
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


class RoutingScene(Scene):
    def construct(self):
        title = Text("Routing", font_size=48, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        routing = '''// Router - Capa 3
- Conectar redes diferentes
- Tabla de enrutamiento
- Decision de mejor camino

// Tipos de routing
1. Static Routes
   ip route 192.168.2.0 255.255.255.0 192.168.1.1

2. Dynamic Routes
   - RIP (Distance Vector, max 15 hops)
   - OSPF (Link State, areas)
   - EIGRP (Hybrid, Cisco proprietary)
   - BGP (Path Vector, Internet)

// Tabla de enrutamiento
- Connected (C)
- Static (S)
- OSPF (O)
- EIGRP (D)
- BGP (B)

// Administrative Distance
Connected: 0
Static: 1
EIGRP: 90
OSPF: 110
RIP: 120
BGP: 20/200'''

        code = Code(
            code_string=routing,
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


class TCPUDPScene(Scene):
    def construct(self):
        title = Text("TCP vs UDP", font_size=48, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        protocols = '''// TCP - Transmission Control Protocol
- Orientado a conexion (3-way handshake)
- Confiable (acknowledgments)
- Control de flujo y congestion
- Ordenamiento de paquetes
- Uso: HTTP, HTTPS, FTP, SSH, Email

// 3-Way Handshake
SYN -> SYN-ACK -> ACK

// Flags TCP
SYN - Iniciar conexion
ACK - Confirmar
FIN - Finalizar
RST - Reset
PSH - Push datos
URG - Urgente

// UDP - User Datagram Protocol
- Sin conexion
- No confiable
- Sin control de flujo
- Mejor esfuerzo
- Uso: VoIP, Video, DNS, DHCP, SNMP

// Puertos comunes
HTTP: 80      HTTPS: 443
FTP: 20/21     SSH: 22
Telnet: 23     SMTP: 25
DNS: 53        DHCP: 67/68
MySQL: 3306    PostgreSQL: 5432'''

        code = Code(
            code_string=protocols,
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


class DNSScene(Scene):
    def construct(self):
        title = Text("DNS - Domain Name System", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        dns = '''// DNS - Traducir nombres a IPs

// Tipos de registros
A     - Address (nombre -> IPv4)
AAAA  - Address (nombre -> IPv6)
CNAME - Canonical Name (alias)
MX    - Mail Exchange
NS    - Name Server
TXT   - Text
PTR   - Pointer (IP -> nombre)

// Proceso de resolucion
1. Cliente pregunta al resolver local
2. Resolver pregunta a root server
3. Root -> TLD server (.com)
4. TLD -> Authoritative server
5. Authoritative -> IP
6. Resolver -> Cliente

// Comandos
nslookup google.com
dig google.com
ping google.com

// Servidores DNS
- 8.8.8.8 (Google)
- 1.1.1.1 (Cloudflare)
- 208.67.222.222 (OpenDNS)'''

        code = Code(
            code_string=dns,
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


class DHCPScene(Scene):
    def construct(self):
        title = Text("DHCP - Dynamic Host Configuration Protocol", font_size=38, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        dhcp = '''// DHCP - Asignacion automatica de IPs

// Proceso DORA
1. Discover (cliente busca servidor)
2. Offer (servidor ofrece IP)
3. Request (cliente solicita IP)
4. Acknowledge (servidor confirma)

// Configuracion Cisco
router# configure terminal
router(config)# ip dhcp pool LAN_POOL
router(dhcp-config)# network 192.168.1.0 255.255.255.0
router(dhcp-config)# default-router 192.168.1.1
router(dhcp-config)# dns-server 8.8.8.8
router(dhcp-config)# lease 7
router(dhcp-config)# exit

// Excluir direcciones
router(config)# ip dhcp excluded-address 192.168.1.1 192.168.1.10

// Verificar
show ip dhcp binding
show ip dhcp pool'''

        code = Code(
            code_string=dhcp,
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


class NATScene(Scene):
    def construct(self):
        title = Text("NAT - Network Address Translation", font_size=42, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        nat = '''// NAT - Traduccion de direcciones

// Tipos de NAT
1. Static NAT (uno a uno)
   ip nat inside source static 192.168.1.10 203.0.113.5

2. Dynamic NAT (pool de direcciones)
   ip nat pool POOL1 203.0.113.10 203.0.113.20 netmask 255.255.255.0
   ip nat inside source list 1 pool POOL1

3. PAT - Port Address Translation (Many to One)
   - Sobrecarga de IP interna
   - Diferentes puertos para cada sesion

// Configuracion
router(config)# interface fastethernet 0/0
router(config-if)# ip nat inside
router(config)# interface fastethernet 0/1
router(config-if)# ip nat outside

// NAT overload (PAT)
router(config)# ip nat inside source list 1 interface fastethernet 0/1 overload

// Verificar
show ip nat translations
show ip nat statistics'''

        code = Code(
            code_string=nat,
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


class ACLScene(Scene):
    def construct(self):
        title = Text("ACL - Access Control Lists", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        acl = '''// ACL - Control de trafico

// Tipos
- Standard (1-99, 1300-1999): Solo origen
- Extended (100-199, 2000-2699): Origen, destino, puerto, protocolo

// Configuracion Standard
router(config)# access-list 10 permit 192.168.1.0 0.0.0.255
router(config)# access-list 10 deny any
router(config)# interface fastethernet 0/0
router(config-if)# ip access-group 10 in

// Configuracion Extended
router(config)# access-list 100 permit tcp any host 10.0.0.1 eq 80
router(config)# access-list 100 permit tcp any host 10.0.0.1 eq 443
router(config)# access-list 100 deny ip any any

// Numeros de puerto comunes
80  - HTTP
443 - HTTPS
22  - SSH
23  - Telnet
21  - FTP
25  - SMTP
53  - DNS
67  - DHCP

// Wildcard mask
0.0.0.0 = host (exacta)
0.0.0.255 = subnet'''

        code = Code(
            code_string=acl,
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


class SpanningTreeScene(Scene):
    def construct(self):
        title = Text("STP - Spanning Tree Protocol", font_size=42, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        stp = '''// STP - Evitar loops en switches

// Problema: Loops de broadcast
- Switches conectados en redundancia
- Broadcast storm
- MAC address instability

// Solucion: STP
- Identificar y bloquear puertos redundantes
- Un unico camino activo
- Recalcular si falla enlace

// Conceptos STP
- Root Bridge (puente raiz)
- Root Ports (hacia root)
- Designated Ports (hacia red)
- Blocked Ports (backup)

// Variantes
- STP (802.1D) - Original
- RSTP (802.1w) - Rapid STP
- MSTP (802.1s) - Multiple STP

// Comandos Cisco
switch# show spanning-tree
switch(config)# spanning-tree mode rapid-pvst
switch(config)# spanning-tree vlan 10 priority 4096'''

        code = Code(
            code_string=stp,
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


class WirelessScene(Scene):
    def construct(self):
        title = Text("Redes Inalambricas", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        wireless = '''// Estandares WiFi
802.11a  - 5GHz, 54Mbps
802.11b  - 2.4GHz, 11Mbps
802.11g  - 2.4GHz, 54Mbps
802.11n  - 2.4/5GHz, 600Mbps (WiFi 4)
802.11ac - 5GHz, 3.4Gbps (WiFi 5)
802.11ax - 2.4/5GHz, 9.6Gbps (WiFi 6)

// Canales no重叠antes
2.4GHz: 1, 6, 11
5GHz: 36, 40, 44, 48, 149, 153, 157, 161

// Modos de AP
- Autonomous
- Lightweight (CAPWAP)

// Seguridad
WPA2 - AES (recomendado)
WPA3 - Mas seguro
WEP - Obsoleto

// Modos de cliente
- Infrastructure (AP)
- Ad-hoc (mesh)
- Monitor (sniffing)'''

        code = Code(
            code_string=wireless,
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


class TroubleshootingScene(Scene):
    def construct(self):
        title = Text("Comandos de Troubleshooting", font_size=40, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        troubleshooting = '''// Comandos basicos
ping <ip>                    - Probar conectividad
traceroute <ip>              - Seguimiento de ruta
ipconfig /all               - Configuracion IP (Windows)
ip addr show                 - Configuracion IP (Linux)
arp -a                      - Tabla ARP

// Cisco
show ip interface brief     - Estado de interfaces
show interfaces            - Detalles de interfaces
show ip route               - Tabla de enrutamiento
show running-config         - Config actual
show version                - Info del dispositivo

// Layer specific
show spanning-tree         - Estado STP
show vlan                   - VLANs
show access-lists           - ACLs
show ip nat translations    - NAT
show dhcp binding           - DHCP

// Performance
show processes cpu          - Uso de CPU
show memory                 - Uso de memoria
show interface stats        - Estadisticas de trafico

// Logging
show logging
debug ip packet'''

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


class SecurityScene(Scene):
    def construct(self):
        title = Text("Seguridad de Red", font_size=44, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.5)

        security = '''// Amenazas comunes
- Malware (virus, ransomware, troyanos)
- Phishing
- DDoS
- Man-in-the-Middle
- SQL Injection
- XSS

// Mitigacion
- Firewalls
- IDS/IPS
- VPN
- Segmentation
- ACLs
- Port Security

// Port Security Cisco
switch(config)# interface fastEthernet 0/1
switch(config-if)# switchport port-security
switch(config-if)# switchport port-security maximum 5
switch(config-if)# switchport port-security violation restrict
switch(config-if)# switchport port-security aging time 2

// SSH en lugar de Telnet
switch(config)# line vty 0 4
switch(config-line)# transport input ssh

// VLANs para segmentacion
- VLAN de gestion
- VLAN de datos
- VLAN de voz
- VLAN de invitados'''

        code = Code(
            code_string=security,
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


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Fundamentos de Redes", font_size=38, color=CISCO_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Modelo OSI: 7 capas para entender networking", font_size=22, color=TEXT_COLOR),
            Text("TCP/IP: Suite de protocolos de Internet", font_size=22, color=TEXT_COLOR),
            Text("Direccionamiento IP: IPv4 e IPv6", font_size=22, color=TEXT_COLOR),
            Text("Subnetting: Dividir redes eficientemente", font_size=22, color=TEXT_COLOR),
            Text("Switching Capa 2: MAC addresses y VLANs", font_size=22, color=TEXT_COLOR),
            Text("Routing: OSPF, EIGRP, BGP", font_size=22, color=TEXT_COLOR),
            Text("TCP vs UDP: Confiable vs rapido", font_size=22, color=TEXT_COLOR),
            Text("DNS/DHCP: Servicios esenciales de red", font_size=22, color=TEXT_COLOR),
            Text("NAT/ACL: Traduccion y filtrado", font_size=22, color=TEXT_COLOR),
            Text("STP: Prevenir loops en switches", font_size=22, color=TEXT_COLOR),
            Text("WiFi: Estandares y seguridad", font_size=22, color=TEXT_COLOR),
            Text("Troubleshooting: Comandos diagnostico", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Fundamentos esenciales para profesionales de networking",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class NetworkingFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        NetworkTypesScene.construct(self)
        OSIIntroScene.construct(self)
        LayerDetailsScene.construct(self)
        TCPIPModelScene.construct(self)
        IPAddressingScene.construct(self)
        SubnettingScene.construct(self)
        SwitchingScene.construct(self)
        VLANScene.construct(self)
        RoutingScene.construct(self)
        TCPUDPScene.construct(self)
        DNSScene.construct(self)
        DHCPScene.construct(self)
        NATScene.construct(self)
        ACLScene.construct(self)
        SpanningTreeScene.construct(self)
        WirelessScene.construct(self)
        TroubleshootingScene.construct(self)
        SecurityScene.construct(self)
        ConclusionScene.construct(self)
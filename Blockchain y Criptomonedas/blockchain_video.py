from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
BLOCKCHAIN_COLOR = "#f7931a"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Blockchain y Criptomonedas", font_size=60, color=BLOCKCHAIN_COLOR).set_color_by_gradient(BLOCKCHAIN_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class FundamentosScene(Scene):
    def construct(self):
        title = Text("Fundamentos Blockchain", font_size=48, color=BLOCKCHAIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Estructura de un Bloque
import hashlib
import json
from datetime import datetime

class Bloque:
    def __init__(self, indice, transacciones, hash_anterior):
        self.indice = indice
        self.timestamp = datetime.now().isoformat()
        self.transacciones = transacciones
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        contenido = json.dumps({
            "indice": self.indice,
            "timestamp": self.timestamp,
            "transacciones": self.transacciones,
            "hash_anterior": self.hash_anterior,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(contenido).hexdigest()

    def minar(self, dificultad):
        while self.hash[:dificultad] != "0" * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()
        print(f"Bloque minado: {self.hash}")

# Merkle Tree
def calcular_raiz_merkle(transacciones):
    if len(transacciones) == 1:
        return transacciones[0]
    nivel = []
    for i in range(0, len(transacciones), 2):
        if i + 1 < len(transacciones):
            combinado = transacciones[i] + transacciones[i + 1]
        else:
            combinado = transacciones[i] + transacciones[i]
        nivel.append(hashlib.sha256(combinado.encode()).hexdigest())
    return calcular_raiz_merkle(nivel)'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class ConsensoScene(Scene):
    def construct(self):
        title = Text("Mecanismos de Consenso", font_size=48, color=BLOCKCHAIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Proof of Work (PoW) - Bitcoin
# Mineros compiten resolviendo un problema computacional
# Dificultad se ajusta cada 2016 bloques (~2 semanas)
dificultad_objetivo = 0x0000FFFF00000000000000000000000000000000000000000000000000000000

# Hash rate: cantidad de hashes por segundo
# Bitcoin: ~400 EH/s (exahashes por segundo)

# Proof of Stake (PoS) - Ethereum 2.0
# Validadores "apuestan" criptomonedas como garantia
# Seleccion pseudo-aleatoria basada en:
#   - Cantidad apostada
#   - Tiempo desde ultima seleccion
#   - Aleatoriedad (RandDAO)
VALIDACION_MINIMA = 32  # ETH

# PBFT (Practical Byzantine Fault Tolerance)
# Tolerancia: 3f + 1 nodos para f nodos maliciosos
# Fases: Pre-prepare -> Prepare -> Commit
# Cada nodo envia mensajes a todos los demas

# Delegated Proof of Stake (DPoS) - EOS, TRON
# Titulares de tokens votan por productores de bloques
# EOS tiene 21 productores activos
# Rotacion continua de productores

# Byzantine Fault Tolerance
# Problema de los generales bizantinos
# Nodos pueden ser: honestos, maliciosos o fallidos
# Consenso requiere > 2/3 de nodos honestos'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class SmartContractsScene(Scene):
    def construct(self):
        title = Text("Smart Contracts y Solidity", font_size=48, color=BLOCKCHAIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Token ERC-20
contract MiToken {
    string public name = "Mi Token";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * 10 ** decimals;
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 value) external returns (bool) {
        require(balanceOf[msg.sender] >= value, "Saldo insuficiente");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(balanceOf[from] >= value, "Saldo insuficiente");
        require(allowance[from][msg.sender] >= value, "Allowance insuficiente");
        allowance[from][msg.sender] -= value;
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
        return true;
    }
}

// Crowdfunding
contract Crowdfunding {
    address payable public owner;
    uint256 public meta;
    uint256 public recaudado;
    mapping(address => uint256) public donaciones;

    constructor(uint256 _meta) {
        owner = payable(msg.sender);
        meta = _meta;
    }

    function donar() external payable {
        donaciones[msg.sender] += msg.value;
        recaudado += msg.value;
    }

    function retirar() external {
        require(msg.sender == owner, "Solo owner");
        require(recaudado >= meta, "Meta no alcanzada");
        owner.transfer(address(this).balance);
    }
}'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class Web3Scene(Scene):
    def construct(self):
        title = Text("Web3 y DApps", font_size=48, color=BLOCKCHAIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''// ethers.js - Conexion a Ethereum
import { ethers } from "ethers";

// Conectar wallet (MetaMask)
const provider = new ethers.BrowserProvider(window.ethereum);
const signer = await provider.getSigner();
const direccion = await signer.getAddress();

// Leer datos del contrato
const contrato = new ethers.Contract(
    "0x...",  // direccion del contrato
    abi,        // interface ABI
    provider
);

const balance = await contrato.balanceOf(direccion);
console.log(`Balance: ${ethers.formatEther(balance)} MTK`);

// Enviar transaccion
const tx = await contrato.transfer(
    "0xdestino...",
    ethers.parseEther("10.0")
);
const recibo = await tx.wait();
console.log(`Tx confirmada: ${recibo.hash}`);

// Escuchar eventos
contrato.on("Transfer", (from, to, value, event) => {
    console.log(`${from} -> ${to}: ${ethers.formatEther(value)} ETH`);
});

// IPFS - Almacenamiento descentralizado
// npm install ipfs-http-client
import { create } from "ipfs-http-client";
const ipfs = create({ url: "https://ipfs.infura.io:5001" });
const { cid } = await ipfs.add(JSON.stringify({
    name: "Mi NFT", description: "Arte digital", image: "ipfs://..."
}));
console.log(`CID: ${cid}`);

// The Graph - Indexado de datos blockchain
// GraphQL query para datos historicos
{
    transfers(first: 10, orderBy: timestamp, orderDirection: desc) {
        from { id }
        to { id }
        value
        transaction { hash }
    }
}'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class DefiScene(Scene):
    def construct(self):
        title = Text("DeFi, NFTs y DAOs", font_size=48, color=BLOCKCHAIN_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''// NFT - ERC-721
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract MiNFT is ERC721URIStorage {
    uint256 public nextTokenId;
    uint256 public precioMint = 0.01 ether;

    constructor() ERC721("MiNFT", "MNFT") {}

    function mint(string memory uri) external payable {
        require(msg.value >= precioMint, "Pago insuficiente");
        _safeMint(msg.sender, nextTokenId);
        _setTokenURI(nextTokenId, uri);
        nextTokenId++;
    }
}

// DeFi - AMM (Automated Market Maker)
// Uniswap: x * y = k (producto constante)
// Precio = reserves0 / reserves1
// swap: dx -> dy = y - (k / (x + dx))

// DAO - Organizacion Autonoma Descentralizada
contract DAO {
    struct Propuesta {
        address objetivo;
        uint256 valor;
        bytes datos;
        uint256 votosAFavor;
        uint256 votosEnContra;
        bool ejecutada;
    }

    mapping(address => uint256) public acciones;
    Propuesta[] public propuestas;

    function crearPropuesta(address objetivo, uint256 valor, bytes memory datos) external {
        propuestas.push(Propuesta(objetivo, valor, datos, 0, 0, false));
    }

    function votar(uint256 id, bool aFavor) external {
        require(acciones[msg.sender] > 0, "Sin acciones");
        if (aFavor) propuestas[id].votosAFavor += acciones[msg.sender];
        else propuestas[id].votosEnContra += acciones[msg.sender];
    }
}'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Blockchain y Criptomonedas", font_size=38, color=BLOCKCHAIN_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("Bloques, hash y mineria", font_size=22, color=TEXT_COLOR),
            Text("Consenso: PoW, PoS, PBFT", font_size=22, color=TEXT_COLOR),
            Text("Smart Contracts en Solidity", font_size=22, color=TEXT_COLOR),
            Text("Web3 con ethers.js", font_size=22, color=TEXT_COLOR),
            Text("IPFS y almacenamiento descentralizado", font_size=22, color=TEXT_COLOR),
            Text("DeFi, NFTs y DAOs", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Reinventando la confianza en la era digital", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class BlockchainyCriptomonedasFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        FundamentosScene.construct(self)
        ConsensoScene.construct(self)
        SmartContractsScene.construct(self)
        Web3Scene.construct(self)
        DefiScene.construct(self)
        ConclusionScene.construct(self)

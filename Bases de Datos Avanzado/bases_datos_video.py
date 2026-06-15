from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
DB_COLOR = "#336791"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Bases de Datos Avanzado", font_size=60, color=DB_COLOR).set_color_by_gradient(DB_COLOR, ACCENT_COLOR)
        subtitle = Text("Tema de ingenieria en computacion e informatica", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)

class SQLScene(Scene):
    def construct(self):
        title = Text("SQL Avanzado", font_size=48, color=DB_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# SQL Avanzado - Ventanas y CTEs

# Window Functions
SELECT
    nombre,
    departamento,
    salario,
    RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) as ranking,
    AVG(salario) OVER (PARTITION BY departamento) as salario_promedio,
    salario - AVG(salario) OVER (PARTITION BY departamento) as diferencia
FROM empleados;

# CTE (Common Table Expression)
WITH ventas_por_mes AS (
    SELECT
        DATE_TRUNC('month', fecha_venta) as mes,
        SUM(monto) as total_ventas,
        COUNT(*) as num_ventas
    FROM ventas
    WHERE fecha_venta >= '2024-01-01'
    GROUP BY DATE_TRUNC('month', fecha_venta)
),
crecimiento AS (
    SELECT
        mes,
        total_ventas,
        LAG(total_ventas) OVER (ORDER BY mes) as mes_anterior,
        (total_ventas - LAG(total_ventas) OVER (ORDER BY mes))
        / LAG(total_ventas) OVER (ORDER BY mes) * 100 as crecimiento_pct
    FROM ventas_por_mes
)
SELECT * FROM crecimiento;

# Indices compuestos
CREATE INDEX idx_empleados_dept_salario
ON empleados(departamento, salario DESC);

# Partial Index
CREATE INDEX idx_empleados_activos
ON empleados(departamento)
WHERE activo = true;

# EXPLAIN ANALYZE
EXPLAIN ANALYZE
SELECT * FROM empleados WHERE departamento = 'IT';'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class NoSQLScene(Scene):
    def construct(self):
        title = Text("NoSQL - MongoDB", font_size=48, color=DB_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''// MongoDB - Agregaciones

// Pipeline de agregacion
db.ordenes.aggregate([
    { $match: { fecha: { $gte: ISODate("2024-01-01") } } },
    { $unwind: "$items" },
    { $group: {
        _id: "$cliente_id",
        total_gastado: { $sum: { $multiply: ["$items.precio", "$items.cantidad"] } },
        num_ordenes: { $sum: 1 },
        productos: { $addToSet: "$items.producto" }
    }},
    { $sort: { total_gastado: -1 } },
    { $limit: 10 },
    { $lookup: {
        from: "clientes",
        localField: "_id",
        foreignField: "_id",
        as: "cliente"
    }},
    { $unwind: "$cliente" },
    { $project: {
        _id: 0,
        cliente_nombre: "$cliente.nombre",
        total_gastado: 1,
        num_ordenes: 1,
        productos: 1
    }}
]);

// Indices
db.ordenes.createIndex(
    { fecha: -1, cliente_id: 1 },
    { name: "idx_fecha_cliente" }
);
db.ordenes.createIndex(
    { "items.producto": 1 },
    { name: "idx_productos" }
);

// Text Search
db.articulos.createIndex(
    { titulo: "text", contenido: "text" },
    { weights: { titulo: 10, contenido: 5 } }
);
db.articulos.find({
    $text: { $search: "base de datos avanzado" }
}, {
    score: { $meta: "textScore" }
}).sort({ score: { $meta: "textScore" } });

// Replica Set
// rs.initiate()
// rs.add("mongodb2:27017")
// rs.add("mongodb3:27017", { arbiterOnly: true })'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class TransaccionesScene(Scene):
    def construct(self):
        title = Text("Transacciones y ACID", font_size=48, color=DB_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# ACID Properties
# Atomicity: Todo o nada
# Consistency: Estado valido siempre
# Isolation: Transacciones independientes
# Durability: Cambios persistentes

# PostgreSQL Transaction
BEGIN;
UPDATE cuentas SET saldo = saldo - 100 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
-- ROLLBACK si hay error

# Isolation Levels (PostgreSQL)
-- READ COMMITTED (default)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- SERIALIZABLE (mas estricto)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

# MongoDB Transactions
const session = client.startSession();
try {
    session.startTransaction();
    await coleccion1.updateOne(
        { _id: id1 },
        { $inc: { saldo: -100 } },
        { session }
    );
    await coleccion2.updateOne(
        { _id: id2 },
        { $inc: { saldo: 100 } },
        { session }
    );
    await session.commitTransaction();
} catch (error) {
    await session.abortTransaction();
} finally {
    session.endSession();
}

# Deadlock Prevention
-- Siempre acceder a recursos en el mismo orden
-- Timeouts para transacciones largas
SET lock_timeout = '5s';'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class CAPScene(Scene):
    def construct(self):
        title = Text("Teorema CAP", font_size=48, color=DB_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Teorema CAP - Consistency, Availability, Partition Tolerance
# Solo puedes tener 2 de 3

# CA - Consistency + Availability
# Sistemas tradicionales (PostgreSQL single node)
# No toleran particiones de red

# CP - Consistency + Partition Tolerance
# MongoDB (default), HBase
# Ante particion, sacrifican disponibilidad

# AP - Availability + Partition Tolerance
# Cassandra, CouchDB, DynamoDB
# Ante particion, sacrifican consistencia

# Eventual Consistency
# Los datos se propagan eventualmente
# Usado en DNS, CDN, redes sociales

# PACELC Extension
# Si particion (P): trade-off entre C y A
# Si no particion: trade-off entre Latencia (L) y Consistencia (C)

# BASE vs ACID
# BASE: Basically Available, Soft state, Eventual consistency
# ACID: Atomicity, Consistency, Isolation, Durability

# Ejemplo practico
# - Sistema bancario: CP (consistencia primero)
# - Red social: AP (disponibilidad primero)
# - Catalogo productos: CA (cuando no hay particion)

# Sharding - Distribucion horizontal
# Hash-based: clave % N particiones
# Range-based: por rango de valores
# Geographic: por region'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)

class OptimizacionScene(Scene):
    def construct(self):
        title = Text("Optimizacion de Queries", font_size=48, color=DB_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = r'''# Plan de ejecucion
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT e.nombre, d.nombre_dept
FROM empleados e
JOIN departamentos d ON e.depto_id = d.id
WHERE e.salario > 50000
ORDER BY e.nombre;

# Indices para optimizar
-- Indice cubriente (incluye columnas)
CREATE INDEX idx_cubriente
ON empleados(depto_id, salario)
INCLUDE (nombre);

-- Indice parcial
CREATE INDEX idx_altos_salarios
ON empleados(salario)
WHERE salario > 100000;

-- Indice funcional
CREATE INDEX idx_email_dominio
ON empleados((split_part(email, '@', 2)));

# Vacuum y Estadisticas
VACUUM ANALYZE empleados;
-- Actualiza estadisticas para el optimizador

# Particionamiento
CREATE TABLE ventas (
    id SERIAL,
    fecha DATE NOT NULL,
    monto DECIMAL
) PARTITION BY RANGE (fecha);

CREATE TABLE ventas_2024_q1
    PARTITION OF ventas
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE ventas_2024_q2
    PARTITION OF ventas
    FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

# Connection Pooling
# PgBouncer / Pgpool
# pool_size = 20
# max_client_conn = 200'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Bases de Datos Avanzado", font_size=38, color=DB_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(            Text("SQL avanzado con window functions y CTEs", font_size=22, color=TEXT_COLOR),
            Text("MongoDB aggregation pipeline", font_size=22, color=TEXT_COLOR),
            Text("Transacciones ACID y niveles de aislamiento", font_size=22, color=TEXT_COLOR),
            Text("Teorema CAP y bases distribuidas", font_size=22, color=TEXT_COLOR),
            Text("Optimizacion de queries y EXPLAIN", font_size=22, color=TEXT_COLOR),
            Text("Particionamiento e indices avanzados", font_size=22, color=TEXT_COLOR)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("El corazon de cualquier aplicacion", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class BasesdeDatosAvanzadoFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        SQLScene.construct(self)
        NoSQLScene.construct(self)
        TransaccionesScene.construct(self)
        CAPScene.construct(self)
        OptimizacionScene.construct(self)
        ConclusionScene.construct(self)

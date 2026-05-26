from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
PG_COLOR = "#336791"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("PostgreSQL", font_size=60, color=PG_COLOR).set_color_by_gradient(PG_COLOR, ACCENT_COLOR)
        subtitle = Text("Base de datos relacional avanzada", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Fundamentos", font_size=48, color=PG_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''-- DDL
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    edad INT CHECK (edad > 0),
    activo BOOLEAN DEFAULT true,
    creado_en TIMESTAMP DEFAULT NOW()
);

-- DML
INSERT INTO usuarios (nombre, email, edad)
VALUES ('Ana', 'ana@mail.com', 28);

-- Consultas
SELECT * FROM usuarios WHERE edad > 25;
SELECT nombre, email FROM usuarios ORDER BY nombre;

-- UPDATE / DELETE
UPDATE usuarios SET edad = 29 WHERE nombre = 'Ana';
DELETE FROM usuarios WHERE edad < 18;

-- JOIN
SELECT u.nombre, p.titulo
FROM usuarios u
JOIN publicaciones p ON p.usuario_id = u.id;

-- GROUP BY
SELECT edad, COUNT(*) FROM usuarios
GROUP BY edad
HAVING COUNT(*) > 1;

-- Subquery
SELECT * FROM usuarios
WHERE id IN (
    SELECT usuario_id FROM pedidos
);'''

        code = Code(code=code_str, language="sql", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AdvancedScene(Scene):
    def construct(self):
        title = Text("Caracteristicas Avanzadas", font_size=42, color=PG_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''-- Vistas
CREATE VIEW usuarios_activos AS
SELECT * FROM usuarios WHERE activo = true;

-- Indices
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_edad ON usuarios(edad DESC);

-- Indice parcial
CREATE INDEX idx_activos ON usuarios(id)
WHERE activo = true;

-- CTE (WITH)
WITH ventas_2024 AS (
    SELECT * FROM ventas WHERE anio = 2024
)
SELECT cliente_id, SUM(total) FROM ventas_2024
GROUP BY cliente_id;

-- Window functions
SELECT nombre, salario,
    RANK() OVER (ORDER BY salario DESC) as ranking
FROM empleados;

-- JSON
CREATE TABLE eventos (data JSONB);
INSERT INTO eventos VALUES ('{"tipo": "click", "pagina": "/home"}');
SELECT data->>'pagina' FROM eventos;
CREATE INDEX ON eventos USING gin(data);

-- Full-text search
SELECT * FROM documentos
WHERE to_tsvector('spanish', contenido) @@ to_tsquery('gato & perro');'''

        code = Code(code=code_str, language="sql", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class PerformanceScene(Scene):
    def construct(self):
        title = Text("Performance y Optimizacion", font_size=42, color=PG_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''-- EXPLAIN ANALYZE
EXPLAIN ANALYZE
SELECT * FROM usuarios WHERE email = 'test@mail.com';

-- Particionamiento
CREATE TABLE pedidos (
    id SERIAL,
    fecha DATE,
    total DECIMAL
) PARTITION BY RANGE (fecha);

CREATE TABLE pedidos_2024_q1
    PARTITION OF pedidos
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

-- VACUUM
VACUUM ANALYZE usuarios;
VACUUM FULL;

-- Configuracion
SHOW shared_buffers;
SHOW work_mem;
SHOW effective_cache_size;

-- Connection pooling
-- PgBouncer / Pgpool-II

-- Autovacuum
-- Monitorear dead tuples

-- Slow queries
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;

-- Bloqueos
SELECT * FROM pg_locks
WHERE NOT granted;'''

        code = Code(code=code_str, language="sql", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ExtensionsScene(Scene):
    def construct(self):
        title = Text("Extensiones", font_size=48, color=PG_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''-- Extensiones esenciales

-- PostGIS (geoespacial)
CREATE EXTENSION postgis;
SELECT ST_Distance(
    ST_MakePoint(-77.04, -12.04),
    ST_MakePoint(-76.99, -12.11)
);

-- pgvector (busqueda vectorial)
CREATE EXTENSION vector;
CREATE TABLE items (
    id SERIAL,
    embedding vector(1536)
);
SELECT * FROM items
ORDER BY embedding <=> '[0.1,0.2,...]'
LIMIT 10;

-- uuid-ossp
CREATE EXTENSION "uuid-ossp";
SELECT uuid_generate_v4();

-- pgcrypto
CREATE EXTENSION pgcrypto;
SELECT crypt('password', gen_salt('bf'));

-- hstore (key-value)
CREATE EXTENSION hstore;
SELECT * FROM productos
WHERE datos -> 'color' = 'rojo';

-- pg_stat_statements
CREATE EXTENSION pg_stat_statements;

-- timescaledb (time-series)
CREATE EXTENSION timescaledb;
SELECT create_hypertable('metricas', 'tiempo');'''

        code = Code(code=code_str, language="sql", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ReplicationScene(Scene):
    def construct(self):
        title = Text("Replicacion y Alta Disponibilidad", font_size=38, color=PG_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''-- Streaming Replication
-- Primario: postgresql.conf
wal_level = replica
max_wal_senders = 3

-- Replica: recovery.conf
primary_conninfo = 'host=192.168.1.10 port=5432 user=replicador'

-- Logical Replication
-- Publicacion (primario)
CREATE PUBLICATION mi_pub FOR TABLE usuarios;

-- Suscripcion (replica)
CREATE SUBSCRIPTION mi_sub
CONNECTION 'host=primario dbname=db user=replicador'
PUBLICATION mi_pub;

-- Failover con Patroni
-- + etcd/consul
-- + HAProxy / pgpool

-- Backup
pg_dump -U postgres -d mibase > backup.sql
pg_restore -U postgres -d mibase backup.sql

-- pg_basebackup
pg_basebackup -D /backup -h primario -U replicador

-- Point-in-Time Recovery (PITR)
recovery_target_time = '2024-01-15 12:00:00''''

        code = Code(code=code_str, language="sql", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: PostgreSQL", font_size=38, color=PG_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("SQL robusto y ACID completo", font_size=22, color=TEXT_COLOR),
            Text("JSONB, indices parciales, window functions", font_size=22, color=TEXT_COLOR),
            Text("Extensiones: PostGIS, pgvector", font_size=22, color=TEXT_COLOR),
            Text("Particionamiento y VACUUM", font_size=22, color=TEXT_COLOR),
            Text("Replicacion stream y logica", font_size=22, color=TEXT_COLOR),
            Text("Backup y PITR", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("La base de datos relacional mas avanzada", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class PostgreSQLFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        AdvancedScene.construct(self)
        PerformanceScene.construct(self)
        ExtensionsScene.construct(self)
        ReplicationScene.construct(self)
        ConclusionScene.construct(self)
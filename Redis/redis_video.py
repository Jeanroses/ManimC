from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
REDIS_COLOR = "#dc382d"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Redis", font_size=60, color=REDIS_COLOR).set_color_by_gradient(REDIS_COLOR, ACCENT_COLOR)
        subtitle = Text("Base de datos en memoria, cache y mensajeria", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Fundamentos", font_size=48, color=REDIS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Strings
SET nombre "Ana"
GET nombre
SETEX sesion 3600 "token123"
INCR contador
INCRBY contador 5

# Lists
LPUSH cola "tarea1"
RPUSH cola "tarea2"
LPOP cola
LRANGE cola 0 -1
LLEN cola

# Sets
SADD tags "python" "redis"
SMEMBERS tags
SISMEMBER tags "python"
SINTER set1 set2

# Sorted Sets
ZADD ranking 100 "jugador1"
ZADD ranking 200 "jugador2"
ZRANGE ranking 0 -1 WITHSCORES
ZREVRANK ranking "jugador1"

# Hashes
HSET usuario:1 nome "Ana" idade 28
HGET usuario:1 nome
HGETALL usuario:1
HINCRBY usuario:1 idade 1

# Keys
KEYS usuario:*
EXISTS usuario:1
TTL sesion
TYPE usuario:1'''

        code = Code(code=code_str, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AdvancedScene(Scene):
    def construct(self):
        title = Text("Caracteristicas Avanzadas", font_size=42, color=REDIS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# TTL / Expire
SET cache "data" EX 3600
EXPIRE cache 3600
TTL cache

# Transactions
MULTI
SET a 1
SET b 2
EXEC

# Pipeline
redis-cli --pipe < commands.txt

# Pub/Sub
SUBSCRIBE canal:noticias
PUBLISH canal:noticias "hola"

# Streams
XADD pedidos * usuario 1 producto "laptop"
XREAD COUNT 10 STREAMS pedidos 0
XGROUP CREATE pedidos grupo1 $
XREADGROUP GROUP grupo1 consumer1
  COUNT 1 STREAMS pedidos >

# Lua Scripting
EVAL "return redis.call('GET', KEYS[1])" 1 nombre

# Geospatial
GEOADD lugares -77.04 -12.04 "Lima"
GEODIST lugares Lima Cusco km

# HyperLogLog
PFADD visitas "user1" "user2"
PFCOUNT visitas'''

        code = Code(code=code_str, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class PatternsScene(Scene):
    def construct(self):
        title = Text("Patrones de uso", font_size=44, color=REDIS_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Cache
def get_user(id):
    cache_key = f"user:{id}"
    user = redis.get(cache_key)
    if user:
        return json.loads(user)
    user = db.query(User).get(id)
    redis.setex(cache_key, 3600, json.dumps(user))
    return user

# Session Store
SET session:abc123 user_id 1 EX 7200

# Rate Limiting
INCR rate:api:user:1
EXPIRE rate:api:user:1 60
# Si > 100, rechazar

# Message Queue
LPUSH tasks "process_order"
BRPOP tasks 0  # blocking pop

# Distributed Lock
SET lock:resource UUID NX EX 10
DEL lock:resource

# Leaderboard
ZADD leaderboard score user
ZREVRANGE leaderboard 0 9 WITHSCORES

# Autocomplete
ZADD autocomplete 0 "ana"
ZADD autocomplete 0 "anita"
ZRANK autocomplete "ana"
ZRANGEBYLEX autocomplete "[ana" "[anb"'''

        code = Code(code=code_str, language="python", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Redis", font_size=38, color=REDIS_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Estructuras: strings, lists, sets, hashes", font_size=22, color=TEXT_COLOR),
            Text("TTL y expiracion automatica", font_size=22, color=TEXT_COLOR),
            Text("Pub/Sub y Streams para mensajeria", font_size=22, color=TEXT_COLOR),
            Text("Cache, sesiones, rate limiting", font_size=22, color=TEXT_COLOR),
            Text("Locks distribuidos y liderboards", font_size=22, color=TEXT_COLOR),
            Text("Persistencia RDB/AOF", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Rapidez y versatilidad en memoria", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class RedisFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        AdvancedScene.construct(self)
        PatternsScene.construct(self)
        ConclusionScene.construct(self)
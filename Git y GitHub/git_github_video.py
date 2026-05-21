from manim import *

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
GIT_COLOR = "#f34f29"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text("Git y GitHub", font_size=60, color=GIT_COLOR).set_color_by_gradient(GIT_COLOR, ACCENT_COLOR)
        subtitle = Text("Control de versiones y colaboracion", font_size=26, color=TEXT_COLOR).next_to(title, DOWN, buff=0.7)
        self.play(Write(title, run_time=2), FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.8)


class BasicsScene(Scene):
    def construct(self):
        title = Text("Conceptos Basicos", font_size=48, color=GIT_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Estados de Git
- Working Directory
- Staging Area
- Repository

# Flujo basico
git init
git status
git add archivo.txt
git commit -m "mensaje"
git log --oneline

# Configuracion
git config --global user.name "Tu Nombre"
git config --global user.email "correo@mail.com"

# Ignorar archivos
echo "node_modules/" >> .gitignore

# Ver diferencias
git diff
git diff --staged

# Deshacer cambios
git restore archivo.txt
git restore --staged archivo.txt

# Checkout de commits
git checkout <hash>
git checkout -b nueva-rama'''

        code = Code(code=code_str, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class BranchingScene(Scene):
    def construct(self):
        title = Text("Branches y Merge", font_size=48, color=GIT_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Branches
git branch
git branch feature/login
git switch feature/login

# Merge
git switch main
git merge feature/login

# Merge con conflicto
git merge feature/pagos
# Resolver conflictos manualmente
git add archivo.txt
git commit

# Rebase
git switch feature/checkout
git rebase main

# Rebase interactivo
git rebase -i HEAD~3

# Fast-forward vs no-ff
git merge --no-ff feature

# Eliminar rama
git branch -d feature/login
git branch -D feature/login'''

        code = Code(code=code_str, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class RemoteScene(Scene):
    def construct(self):
        title = Text("GitHub y Remotos", font_size=46, color=GIT_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Remotos
git remote -v
git remote add origin https://github.com/user/repo.git

# Push / Pull
git push -u origin main
git pull origin main

# Fork y PRs
- Fork repo
- Crear rama
- Push a tu fork
- Crear Pull Request

# Clonar repositorio
git clone https://github.com/user/repo.git

# Tags (versiones)
git tag v1.0.0
git push origin v1.0.0

# GitHub Flow
- Crear rama por feature
- Abrir PR
- Revisar
- Merge a main

# Protected branches
- Requerir PRs
- Requerir tests
- Restringir force push'''

        code = Code(code=code_str, language="bash", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class AdvancedScene(Scene):
    def construct(self):
        title = Text("Workflows Avanzados", font_size=44, color=GIT_COLOR)
        title.to_edge(UP, buff=0.5)

        code_str = '''# Cherry-pick
git cherry-pick <hash>

# Stash
git stash
git stash list
git stash apply

# Reset (cuidado)
git reset --soft HEAD~1
git reset --mixed HEAD~1

# Reflog
git reflog
git reset --hard <hash>

# Bisect
git bisect start
git bisect bad
git bisect good <hash>

# GitHub Actions
name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test

# Conventional Commits
feat: nueva feature
fix: corregir bug
docs: actualizar docs'''

        code = Code(code=code_str, language="yaml", formatter_style="monokai", background="rectangle", font_size=18)
        code.scale(0.85).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), Create(code), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(code), run_time=0.8)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Git y GitHub", font_size=38, color=GIT_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Estados: working, staging, repo", font_size=22, color=TEXT_COLOR),
            Text("Branches y merge/rebase", font_size=22, color=TEXT_COLOR),
            Text("Remotos: push/pull", font_size=22, color=TEXT_COLOR),
            Text("PRs y flujo GitHub", font_size=22, color=TEXT_COLOR),
            Text("Cherry-pick, stash, bisect", font_size=22, color=TEXT_COLOR),
            Text("Automatizacion con Actions", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(1)

        final_msg = Text("Versionado profesional y colaborativo", font_size=26, color=ACCENT_COLOR).next_to(items, DOWN, buff=0.5)
        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(*items), FadeOut(final_msg), run_time=0.8)


class GitGitHubFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        BasicsScene.construct(self)
        BranchingScene.construct(self)
        RemoteScene.construct(self)
        AdvancedScene.construct(self)
        ConclusionScene.construct(self)

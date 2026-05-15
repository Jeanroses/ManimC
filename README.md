<p align="center">
  <img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png" alt="Manim Logo" width="250"/>
</p>

<h1 align="center">ManimC - Mathematical & Technical Animation Engine</h1>

<p align="center">
  <strong>Production-grade educational content with automated video generation for engineering and computer science</strong>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#technology-stack">Tech Stack</a> •
  <a href="#projects">Projects</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#development">Development</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Manim-Community-58B5F0?style=for-the-badge" alt="Manim CE"/>
  <img src="https://img.shields.io/badge/LaTeX-Supported-008080?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
  <img src="https://img.shields.io/badge/.NET-8.0-68217a?style=for-the-badge&logo=.net&logoColor=white" alt=".NET"/>
  <img src="https://img.shields.io/badge/Java-17+-007396?style=for-the-badge&logo=java&logoColor=white" alt="Java"/>
  <img src="https://img.shields.io/badge/status-active-success?style=for-the-badge" alt="Status"/>
</p>

---

## 📊 Overview

**ManimC** is a comprehensive repository containing production-ready Manim animations for technical and educational content. The project covers multiple domains including mathematics, computer science, software engineering, and system architecture visualization.

### Key Capabilities

- **High-precision mathematical rendering** with LaTeX integration
- **Professional-grade animations** at up to 4K 60fps
- **Modular scene architecture** for reusable components
- **Cross-platform rendering pipeline** using FFmpeg
- **Enterprise-level code quality** with proper documentation

---

## 🛠 Technology Stack

### Core Technologies

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Animation Engine** | Manim Community | 0.18+ | Mathematical animation rendering |
| **Programming Language** | Python | 3.10+ | Core animation logic |
| **Mathematical Typesetting** | LaTeX | TeX Live 2024+ | Formula rendering |
| **Video Encoding** | FFmpeg | 6.0+ | Video compilation and encoding |
| **IDE/Development** | VS Code | Latest | Development environment |

### Additional Technologies

| Domain | Technology | Purpose |
|--------|------------|---------|
| **Object-Oriented** | Java 17+ | POO concepts visualization |
| **Web Framework** | .NET 8 / ASP.NET Core | Web API and Entity Framework |
| **Database** | Entity Framework Core 8 | ORM patterns demonstration |
| **Version Control** | Git 2.40+ | Source control |

---

## 📁 Projects

### Current Portfolio

| # | Project Name | Domain | Status | Lines of Code |
|---|--------------|--------|--------|---------------|
| 01 | Algoritmos de búsqueda y ordenamiento | Computer Science | ✅ Active | ~1,073 |
| 02 | Integral de Green | Mathematics | ✅ Active | ~763 |
| 03 | Derivadas parciales y gradiente | Mathematics | ✅ Active | ~374 |
| 04 | Métodos numéricos | Numerical Analysis | ✅ Active | ~606 |
| 05 | Transformada de Laplace | Mathematics | ✅ Active | ~564 |
| 06 | Transformada de Fourier | Signal Processing | ✅ Active | ~620 |
| 07 | POO en Java | Software Engineering | ✅ Active | ~1,207 |
| 08 | .NET y Entity Framework | Enterprise Development | ✅ Active | ~1,275 |

---

## 🚀 Getting Started

### Prerequisites

```bash
# System Dependencies
- Python 3.10 or higher
- FFmpeg 6.0 or higher
- LaTeX distribution (MiKTeX/TeX Live)
- Git 2.40+
```

### Installation

```bash
# Clone repository
git clone https://github.com/Jeanroses/ManimC.git
cd ManimC

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
manim --version
```

### Quick Start

```bash
# Navigate to project directory
cd "Algoritmos de búsqueda y ordenamiento"

# Render preview (low quality)
manim -pql algorithms_video.py AlgorithmsFullVideo

# Render production (high quality)
manim -pqh algorithms_video.py AlgorithmsFullVideo

# Render 4K
manim -pqk algorithms_video.py AlgorithmsFullVideo
```

---

## 📂 Project Structure

```
ManimC/
├── README.md                           # This file
├── Algoritmos de búsqueda y ordenamiento/
│   ├── algorithms_video.py            # Main animation file
│   └── media/                         # Rendered output
├── Integral de Green/
│   ├── greens_theorem_video.py
│   └── media/
├── Derivadas parciales y gradiente/
│   ├── partial_derivatives_gradient_video.py
│   └── media/
├── Métodos numéricos/
│   ├── numerical_methods_video.py
│   └── media/
├── Transformada de Laplace/
│   ├── laplace_transform_video.py
│   └── media/
├── Transformada de Fourier/
│   ├── fourier_transform_video.py
│   └── media/
├── POO en Java/
│   ├── java_oop_video.py
│   └── media/
└── .NET y Entity Framework/
    ├── dotnet_entityframework_video.py
    └── media/
```

---

## ⚙️ Rendering Configuration

### Quality Presets

| Quality | Resolution | FPS | Use Case |
|---------|------------|-----|----------|
| `ql` (Low) | 854x480 | 15 | Development/Debugging |
| `qm` (Medium) | 1280x720 | 30 | Testing/Preview |
| `qh` (High) | 1920x1080 | 60 | Production |
| `qk` (4K) | 3840x2160 | 60 | Ultra HD Distribution |

### Output Format Options

```bash
# Video formats
manim -pqh video.py Scene                    # MP4 (default)
manim -pqh --format=gif video.py Scene       # Animated GIF
manim -pqh --format=mp4 video.py Scene       # Explicit MP4
manim -pqh --format=webm video.py Scene      # WebM

# Image capture
manim -pqh -s video.py Scene                 # Save final frame as PNG
```

---

## 🎨 Code Architecture

### Standard Scene Template

```python
from manim import *
import numpy as np

# Color palette
BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"

config.background_color = BACKGROUND_COLOR


class SceneName(Scene):
    def construct(self):
        # Scene implementation
        title = Text("Title", font_size=48, color=PRIMARY_COLOR)
        self.play(Write(title))
        self.wait(2)


class FullVideo(Scene):
    def construct(self):
        # Orchestrate multiple scenes
        SceneName.construct(self)
```

### Key Components

| Component | Description |
|-----------|-------------|
| **Scene** | Base class for all animations |
| **Mobjects** | Mathematical objects (Circle, Square, Axes, etc.) |
| **Animations** | Transitions (Create, FadeIn, Transform, etc.) |
| **MathTex** | LaTeX formula rendering |
| **Code** | Syntax-highlighted code blocks |

---

## 🔧 Development

### Running Tests

```bash
# Render all scenes in a project
manim -pql project.py -a

# Render specific scene
manim -pql project.py SceneName
```

### Debug Mode

```bash
# Enable preview window
manim -pqh -p project.py Scene

# Save last frame
manim -pqh -s project.py Scene
```

### Configuration File (manim.cfg)

```ini
[CLI]
quality = low_quality
preview = True
media_dir = ./media

[renderer]
background_color = #000000
frame_rate = 60

[output]
format = mp4
pixel_height = 1080
pixel_width = 1920
```

---

## 📚 Documentation References

### Official Documentation

| Resource | URL |
|----------|-----|
| Manim CE Docs | https://docs.manim.community/ |
| Manim API Reference | https://docs.manim.community/en/stable/reference.html |
| LaTeX Symbols | https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols |

### Learning Resources

| Channel | Content | URL |
|---------|---------|-----|
| 3Blue1Brown | Original Manim creator | https://www.youtube.com/c/3blue1brown |
| Theorem of Beethoven | Manim tutorials | https://www.youtube.com/c/TheoremofBeethoven |
| Reducible | CS concepts | https://www.youtube.com/c/Reducible |

### Community

| Platform | Link |
|----------|------|
| Discord | https://discord.gg/mMRrZQW |
| Reddit | https://www.reddit.com/r/manim/ |
| GitHub | https://github.com/ManimCommunity/manim |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Follow existing code style and conventions
- Include proper documentation for new scenes
- Test animations at multiple quality levels
- Ensure LaTeX formulas are properly escaped

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📈 Roadmap

### Planned Projects

- [ ] Series de Fourier
- [ ] Ecuaciones diferenciales básicas
- [ ] Álgebra lineal visual
- [ ] Probabilidad y estadística
- [ ] Señales y sistemas
- [ ] Optimización (gradiente descendente)
- [ ] Mecánica clásica
- [ ] Circuitos eléctricos
- [ ] Control automático

---

## 👤 Author

**Jeanroses** - Initial work and ongoing development

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Manim-58B5F0?style=for-the-badge" alt="Made with Manim"/>
  <img src="https://img.shields.io/badge/Powered%20by-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Powered by Python"/>
  <img src="https://img.shields.io/github/last-commit/Jeanroses/ManimC?style=for-the-badge" alt="Last Commit"/>
  <img src="https://img.shields.io/github/contributors/Jeanroses/ManimC?style=for-the-badge" alt="Contributors"/>
</p>
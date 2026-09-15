import os
import glob

def generate_readme():
    html_files = [f for f in glob.glob("*.html") if os.path.isfile(f)]
    html_files.sort()

    links_md = ""
    list_md = ""

    for f in html_files:
        name = f.replace(".html", "").replace("_", " ").title()
        links_md += f"[🎮 **{name}**](https://pogtvt.github.io/Vyom_sutra/{f}) • "
        list_md += f"* 🚀 **[{name}](https://pogtvt.github.io/Vyom_sutra/{f})**\n  *Real-time interactive simulation module powered by Master VyomEngine.*\n"

    links_md = links_md.rstrip(" • ")

    readme_content = f"""<div align="center">

# 🚀 Vyom Sutra (व्योम सूत्र)
### *Ultra-Fast Wave-Based Decision & Signal Processing Engine*

[![PyPI version](https://img.shields.io/pypi/v/vyom-sutra.svg?color=blue&style=for-the-badge)](https://pypi.org/project/vyom-sutra/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)](https://www.python.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22247703-blueviolet.svg?style=for-the-badge)](https://doi.org/10.5281/zenodo.22247703)
[![Speed](https://img.shields.io/badge/Speed-%3E20M%20Ops%2Fsec-red.svg?style=for-the-badge)](#-performance-benchmarks)

<br />

{links_md}

</div>

---

## ⚡ Overview

**Vyom Sutra** is a high-performance, wave-based similarity and signal processing engine designed with **Sine-Wave Universality** and **Null-Infinite Duality ($0 = \infty$)**. 

Engineered with a native **C core**, **Lookup Table (LUT) acceleration**, and **Master JavaScript Binding**, it achieves processing throughput exceeding **20 million operations per second**.

---

## 🕹️ Interactive Demos & Simulation Hub

Explore all interactive tools automatically tracked and integrated into the repository:

{list_md}

---

## 🔥 Key Core Principles

- **🌊 Sine-Wave = Everything:** Universal mathematical representation across all domains.
- **🌀 0 = Infinity (Null-Infinite Duality):** Handling absolute singularities and infinite expansions seamlessly.
- **⚡ Blazing Fast Engine:** Zero-latency local execution backed by Master `VyomEngine`.

---

## 📦 Quick Start & Installation

Install the package directly via PyPI:
```bash
pip install vyom-sutra

q






cat << 'EOF' > update_readme.py
import os
import glob

def generate_readme():
    html_files = [f for f in glob.glob("*.html") if os.path.isfile(f)]
    html_files.sort()

    links_md = ""
    list_md = ""

    for f in html_files:
        name = f.replace(".html", "").replace("_", " ").title()
        links_md += f"[🎮 **{name}**](https://pogtvt.github.io/Vyom_sutra/{f}) • "
        list_md += f"* 🚀 **[{name}](https://pogtvt.github.io/Vyom_sutra/{f})**\n  *Real-time interactive simulation module powered by Master VyomEngine.*\n"

    links_md = links_md.rstrip(" • ")

    readme_content = f"""<div align="center">

# 🚀 Vyom Sutra (व्योम सूत्र)
### *Ultra-Fast Wave-Based Decision & Signal Processing Engine*

[![PyPI version](https://img.shields.io/pypi/v/vyom-sutra.svg?color=blue&style=for-the-badge)](https://pypi.org/project/vyom-sutra/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)](https://www.python.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22247703-blueviolet.svg?style=for-the-badge)](https://doi.org/10.5281/zenodo.22247703)
[![Speed](https://img.shields.io/badge/Speed-%3E20M%20Ops%2Fsec-red.svg?style=for-the-badge)](#-performance-benchmarks)

<br />

{links_md}

</div>

---

## ⚡ Overview

**Vyom Sutra** is a high-performance, wave-based similarity and signal processing engine designed with **Sine-Wave Universality** and **Null-Infinite Duality ($0 = \infty$)**. 

Engineered with a native **C core**, **Lookup Table (LUT) acceleration**, and **Master JavaScript Binding**, it achieves processing throughput exceeding **20 million operations per second**.

---

## 🕹️ Interactive Demos & Simulation Hub

Explore all interactive tools automatically tracked and integrated into the repository:

{list_md}

---

## 🔥 Key Core Principles

- **🌊 Sine-Wave = Everything:** Universal mathematical representation across all domains.
- **🌀 0 = Infinity (Null-Infinite Duality):** Handling absolute singularities and infinite expansions seamlessly.
- **⚡ Blazing Fast Engine:** Zero-latency local execution backed by Master `VyomEngine`.

---

## 📦 Quick Start & Installation

Install the package directly via PyPI:
```bash
pip install vyom-sutra

q








q
[200~# १. Auto-README Generator Script सिर्जना गर्ने
cat << 'EOF' > update_readme.py
import os
import glob

def generate_readme():
    html_files = [f for f in glob.glob("*.html") if os.path.isfile(f)]
    html_files.sort()

    links_md = ""
    list_md = ""

    for f in html_files:
        name = f.replace(".html", "").replace("_", " ").title()
        links_md += f"[🎮 **{name}**](https://pogtvt.github.io/Vyom_sutra/{f}) • "
        list_md += f"* 🚀 **[{name}](https://pogtvt.github.io/Vyom_sutra/{f})**\n  *Real-time interactive simulation module powered by Master VyomEngine.*\n"

    links_md = links_md.rstrip(" • ")

    readme_content = f"""<div align="center">

# 🚀 Vyom Sutra (व्योम सूत्र)
### *Ultra-Fast Wave-Based Decision & Signal Processing Engine*

[![PyPI version](https://img.shields.io/pypi/v/vyom-sutra.svg?color=blue&style=for-the-badge)](https://pypi.org/project/vyom-sutra/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)](https://www.python.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22247703-blueviolet.svg?style=for-the-badge)](https://doi.org/10.5281/zenodo.22247703)
[![Speed](https://img.shields.io/badge/Speed-%3E20M%20Ops%2Fsec-red.svg?style=for-the-badge)](#-performance-benchmarks)

<br />

{links_md}

</div>

---

## ⚡ Overview

**Vyom Sutra** is a high-performance, wave-based similarity and signal processing engine designed with **Sine-Wave Universality** and **Null-Infinite Duality ($0 = \infty$)**. 

Engineered with a native **C core**, **Lookup Table (LUT) acceleration**, and **Master JavaScript Binding**, it achieves processing throughput exceeding **20 million operations per second**.

---

## 🕹️ Interactive Demos & Simulation Hub

Explore all interactive tools automatically tracked and integrated into the repository:

{list_md}

---

## 🔥 Key Core Principles

- **🌊 Sine-Wave = Everything:** Universal mathematical representation across all domains.
- **🌀 0 = Infinity (Null-Infinite Duality):** Handling absolute singularities and infinite expansions seamlessly.
- **⚡ Blazing Fast Engine:** Zero-latency local execution backed by Master `VyomEngine`.

---

## 📦 Quick Start & Installation

Install the package directly via PyPI:
```bash
pip install vyom-sutra
~




cat << 'EOF' > update_readme.py
import os
import glob

def generate_readme():
    html_files = [f for f in glob.glob("*.html") if os.path.isfile(f)]
    html_files.sort()

    links_md = ""
    list_md = ""

    for f in html_files:
        name = f.replace(".html", "").replace("_", " ").title()
        links_md += f"[🎮 **{name}**](https://pogtvt.github.io/Vyom_sutra/{f}) • "
        list_md += f"* 🚀 **[{name}](https://pogtvt.github.io/Vyom_sutra/{f})**\n  *Real-time interactive simulation module powered by Master VyomEngine.*\n"

    links_md = links_md.rstrip(" • ")

    readme_content = f"""<div align="center">

# 🚀 Vyom Sutra (व्योम सूत्र)
### *Ultra-Fast Wave-Based Decision & Signal Processing Engine*

[![PyPI version](https://img.shields.io/pypi/v/vyom-sutra.svg?color=blue&style=for-the-badge)](https://pypi.org/project/vyom-sutra/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)](https://www.python.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22247703-blueviolet.svg?style=for-the-badge)](https://doi.org/10.5281/zenodo.22247703)
[![Speed](https://img.shields.io/badge/Speed-%3E20M%20Ops%2Fsec-red.svg?style=for-the-badge)](#-performance-benchmarks)

<br />

{links_md}

</div>

---

## ⚡ Overview

**Vyom Sutra** is a high-performance, wave-based similarity and signal processing engine designed with **Sine-Wave Universality** and **Null-Infinite Duality ($0 = \infty$)**. 

---

## 🕹️ Interactive Demos & Simulation Hub

{list_md}

---

## 📦 Quick Start & Installation

```bash
pip install vyom-sutra



with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)
print("README.md successfully generated!")
​if name == "main":
generate_readme()

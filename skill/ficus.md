---
name: ficus
category: utility
description: "provides a context manager for matplotlib figures."
tags: [ficus, utility, visualization, matplotlib, python]
author: oxo-call-community
source_url: "https://github.com/camillescott/ficus"
---

## Concepts

- **Tool Overview**: ficus provides a context manager for matplotlib figures, simplifying figure creation and management in Python.
- **Core Function**: Provides easy-to-use context managers for matplotlib figure creation.
- **Input/Output**: Input: Plot parameters. Output: Matplotlib figures.
- **Algorithm**: Implements Python context manager pattern for figure handling.
- **Key Features**: Context manager, simplified API, automatic cleanup, multiple backends, easy customization.
- **Installation**: `conda install -c bioconda ficus`

## Pitfalls

- **Matplotlib Dependency**: Requires matplotlib installation.
- **Backend Compatibility**: May have backend-specific behavior.
- **Figure Size**: Large figures may require significant memory.
- **Python Version**: Some features may require specific Python versions.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic figure creation
**Args:** `python -c "from ficus import Figure; Figure(10, 10).plot([1,2,3], [1,4,9])"`
**Explanation:** Creates a simple figure.

### Multiple subplots
**Args:** `python -c "from ficus import Figure; fig = Figure(figsize=(15, 10)); fig.subplot(2, 2, 1); fig.plot([1,2,3], [1,4,9])"`
**Explanation:** Creates multi-panel figure.

### Auto-save
**Args:** `python -c "from ficus import Figure; with Figure('output.png', figsize=(10, 10)) as fig: fig.plot([1,2,3], [1,4,9])"`
**Explanation:** Creates and saves figure automatically.

### Different backends
**Args:** `python -c "from ficus import Figure; Figure(10, 10, backend='pdf').plot([1,2,3], [1,4,9])"`
**Explanation:** Uses specific matplotlib backend.

### Style customization
**Args:** `python -c "from ficus import Figure; Figure(10, 10, style='seaborn').plot([1,2,3], [1,4,9])"`
**Explanation:** Applies custom style to figure.
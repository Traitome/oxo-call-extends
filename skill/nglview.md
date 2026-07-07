---
name: nglview
category: visualization
description: NGLView is an IPython widget for interactive molecular structure visualization.
tags: [nglview, visualization, molecular-structure, ipython, jupyter]
author: oxo-call-community
source_url: "https://github.com/arose/nglview"
---

## Concepts

- **Tool Overview**: NGLView provides interactive 3D visualization of molecular structures in Jupyter notebooks.
- **Core Function**: Renders PDB structures, trajectories, and surfaces using WebGL.
- **Algorithm**: Uses NGL Viewer library for GPU-accelerated 3D rendering.
- **Input Format**: Accepts PDB, mmCIF, MMTF, and trajectory files.
- **Output**: Interactive 3D visualization in Jupyter notebooks.
- **Use Case**: Protein structure analysis, molecular dynamics visualization, and education.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Jupyter Environment**: Requires Jupyter notebook/lab installation.
- **Browser Support**: Requires modern browser with WebGL support.
- **Memory Usage**: Large structures require memory.
- **Performance**: Complex structures may affect rendering speed.
- **Dependency Conflicts**: May conflict with other visualization libraries.

## Examples

### Display help
**Args:** `python -c "import nglview; help(nglview)"`
**Explanation:** Shows available methods and usage instructions.

### View PDB structure
**Args:** `view = nglview.show_pdbid('1AKE'); view.display()`
**Explanation:** Displays structure from PDB database.

### View local file
**Args:** `view = nglview.show_file('structure.pdb'); view.display()`
**Explanation:** Displays local PDB file.

### Add representation
**Args:** `view.add_representation('cartoon', color='spectrum'); view.display()`
**Explanation:** Adds cartoon representation colored by spectrum.

### View trajectory
**Args:** `view = nglview.show_mdtraj(trajectory); view.display()`
**Explanation:** Displays molecular dynamics trajectory.

### Set background color
**Args:** `view.background = 'white'; view.display()`
**Explanation:** Sets white background for visualization.

### Save image
**Args:** `view.download_image(filename='structure.png')`
**Explanation:** Saves current view as PNG image.
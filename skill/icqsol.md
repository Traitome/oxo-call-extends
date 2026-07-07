---
name: icqsol
category: visualization
description: A collection of utilities for constructing complex geometries from primitive shapes.
tags: [icqsol, visualization, geometry, 3D, mesh-generation]
author: oxo-call-community
source_url: "https://github.com/pletzer/icqsol"
---

## Concepts

- **Tool Overview**: icqsol (v0.3.26) is a Python library for constructing and manipulating complex geometric shapes from primitive components.
- **Primitive Shapes**: Supports spheres, cylinders, cones, boxes, and other basic geometric primitives.
- **Boolean Operations**: Enables union, intersection, and difference operations on shapes.
- **Mesh Generation**: Generates high-quality triangular meshes for visualization and simulation.
- **CAD Integration**: Can export to various CAD and visualization formats.
- **Installation**: `conda install -c bioconda icqsol` or `pip install icqsol`

## Pitfalls

- **Mesh Complexity**: Complex geometries can result in very large mesh files.
- **Boolean Operation Artifacts**: Complex boolean operations may produce unexpected artifacts.
- **Performance**: Generating high-resolution meshes can be computationally intensive.
- **Memory Requirements**: Large models require significant memory resources.
- **Export Format Limitations**: Some export formats may not preserve all geometric details.
- **Coordinate System**: Requires careful attention to coordinate system conventions.

## Examples

### Create a simple sphere
**Args:** `icqsol sphere --radius 1.0 --output sphere.obj`
**Explanation:** Generates a sphere mesh with radius 1.0.

### Combine shapes with union
**Args:** `icqsol union sphere.obj cylinder.obj --output combined.obj`
**Explanation:** Creates a union of a sphere and cylinder.

### Create a complex shape
**Args:** `icqsol subtract box.obj sphere.obj --output hollow_box.obj`
**Explanation:** Subtracts a sphere from a box to create a hollow volume.

### Generate high-resolution mesh
**Args:** `icqsol cylinder --radius 0.5 --height 2.0 --resolution 100 --output cylinder.obj`
**Explanation:** Creates a cylinder with high-resolution mesh (100 segments).

### Export to STL format
**Args:** `icqsol convert input.obj output.stl --format stl`
**Explanation:** Converts a mesh file to STL format for 3D printing.
---
name: taxonomy
category: programming
description: Python and Rust library for loading, saving, and manipulating taxonomic trees with high performance.
tags: [taxonomy, programming, rust, python, phylogenetic, tree]
author: oxo-call-community
source_url: "https://docs.rs/crate/taxonomy/latest"
---

## Concepts

- **Tool Overview**: taxonomy (v0.10.5) - A library written in Rust with Python bindings for loading, saving, and manipulating taxonomic trees. Designed for high-performance phylogenetic tree operations in bioinformatics applications.
- **Core Functions**: Provides data structures for taxonomic tree representation, I/O operations for common tree formats (Newick, Nexus), and algorithms for tree manipulation including pruning, rerooting, and traversal.
- **Language Support**: Core library in Rust for performance-critical operations, with Python bindings via PyO3 for integration into Python bioinformatics workflows.
- **Installation**: For Rust projects, add to Cargo.toml; for Python, install via `pip install taxonomy` (if published) or build from source with `maturin develop`.
- **Input/Output Formats**: Supports Newick (.nw, .tree), Nexus (.nex, .nxs), and custom taxonomy-specific JSON formats.
- **Key Features**: Memory-efficient tree representation, parallel processing support for large trees, and consistent API across Rust and Python.

## Pitfalls

- **Building from Source**: Python bindings require Rust toolchain (rustc, cargo) and maturin for building. Simple `pip install` may fail without proper build environment.
- **Version Compatibility**: Python bindings version must match the Rust library version - check compatibility before updating either component.
- **Memory Management**: Large trees (millions of nodes) require significant memory - consider streaming approaches for very large datasets.
- **Format Specifics**: Newick format has limited support for metadata - complex annotations may need Nexus or JSON format instead.
- **Tree Structure Validation**: Not all Newick files represent valid phylogenetic trees - library may error on malformed input.
- **Parallelism Configuration**: Threading options may need tuning based on tree size and system resources - test different configurations.

## Examples

### Python: Load a Newick tree
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw")`
**Explanation:** Basic tree loading from Newick format file. The Tree object provides methods for traversal and manipulation.

### Python: Get tree statistics
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw"); print(t.node_count(), t.tip_count())`
**Explanation:** Query basic statistics about the loaded tree including total node count and number of tips/leaves.

### Python: Prune to subset of taxa
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw"); t.prune(tips=["9606", "10090", "10116"])`
**Explanation:** Keep only specified taxa (human, mouse, rat) and remove all other branches.

### Python: Export to Newick
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw"); t.to_newick("output.nw")`
**Explanation:** Save manipulated tree back to Newick format for use with other tools.

### Python: Iterate over tips
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw"); [print(node.name) for node in t.tips()]`
**Explanation:** Traverse and print all tip/leaf node names in the tree.

### Rust: Create tree programmatically
**Args:** `let mut tree = TaxonomyTree::new(); tree.add_child("root", "taxonomy"); tree.add_child("taxonomy", "species");`
**Explanation:** Rust API for building trees programmatically by adding child nodes to parent nodes.

### Python: Calculate LCA
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw"); lca = t.lca(tip1, tip2)`
**Explanation:** Find the lowest common ancestor of two tips, returning the internal node representing their common ancestor.

### Python: Reroot tree
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw"); t.reroot(at_tip="outgroup")`
**Explanation:** Reroot the tree at a specified tip or internal node, changing the tree's root placement.

### Python: Load from Newick with metadata
**Args:** `from taxonomy import Tree; t = Tree.from_newick("tree.nw", annotate=True)`
**Explanation:** Load Newick with additional annotations (branch lengths, node labels) preserved as metadata.

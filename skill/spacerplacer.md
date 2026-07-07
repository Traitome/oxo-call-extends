---
name: spacerplacer
category: microbiology
description: SpacerPlacer - Reconstruct ancestral CRISPR spacer arrays
tags: [spacerplacer, microbiology, crispr, spacer, ancestral-reconstruction]
author: oxo-call-community
source_url: "https://github.com/fbaumdicker/SpacerPlacer"
---

## Concepts

- **Tool Overview**: spacerplacer (v1.0.1) - A CRISPR spacer array reconstruction tool
- **Core Function**: Reconstructs ancestral CRISPR spacer arrays
- **Input/Output**: Accepts CRISPR spacer data; outputs ancestral arrays
- **Algorithm**: Phylogenetic reconstruction of spacer arrays
- **Installation**: `conda install -c bioconda spacerplacer`
- **Key Features**: Ancestral reconstruction, CRISPR analysis, spacer arrays

## Pitfalls

- **Input Requirements**: Requires properly formatted CRISPR spacer data
- **Phylogenetic Tree**: Requires phylogenetic tree for reconstruction
- **Spacer Quality**: Quality of spacers affects reconstruction accuracy
- **Memory Usage**: Large spacer sets require significant memory
- **Output Format**: Output format depends on configuration
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `spacerplacer --help`
**Explanation:** Shows available options and usage information.

### Basic reconstruction
**Args:** `spacerplacer -i spacers.fasta -t tree.nwk -o ancestral_arrays.fasta`
**Explanation:** Reconstruct ancestral CRISPR spacer arrays.

### With multiple species
**Args:** `spacerplacer -i spacers1.fasta spacers2.fasta -t tree.nwk -o ancestral_arrays.fasta`
**Explanation:** Reconstruct from multiple species.

### With evolutionary model
**Args:** `spacerplacer -i spacers.fasta -t tree.nwk -o ancestral_arrays.fasta --model Jukes-Cantor`
**Explanation:** Use specific evolutionary model.

### With bootstrap
**Args:** `spacerplacer -i spacers.fasta -t tree.nwk -o ancestral_arrays.fasta --bootstrap 100`
**Explanation:** Perform bootstrap analysis.

### Output detailed results
**Args:** `spacerplacer -i spacers.fasta -t tree.nwk -o ancestral_arrays.fasta --detailed`
**Explanation:** Output detailed reconstruction results.

### Output statistics
**Args:** `spacerplacer -i spacers.fasta -t tree.nwk -o ancestral_arrays.fasta --stats`
**Explanation:** Output reconstruction statistics.

### Generate report
**Args:** `spacerplacer -i spacers.fasta -t tree.nwk -o ancestral_arrays.fasta --report`
**Explanation:** Generate reconstruction report.
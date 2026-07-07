---
name: maskrc-svg
category: alignment
description: Masks recombinant regions in sequence alignments based on ClonalFrameML or Gubbins output.
tags: [maskrc-svg, recombination, masking, alignment]
author: oxo-call-community
source_url: "https://github.com/kwongj/maskrc-svg"
---

## Concepts

- **Tool Overview**: maskrc-svg masks recombinant regions in sequence alignments.
- **Core Function**: Identifies and masks recombination events detected by ClonalFrameML or Gubbins.
- **Input Sources**: Accepts output from ClonalFrameML or Gubbins recombination detectors.
- **Visualization**: Generates SVG visualization of recombinant regions.
- **Masking Strategy**: Replaces recombinant sites with ambiguity characters (N).
- **Installation**: `conda install -c bioconda maskrc-svg`

## Pitfalls

- **Dependence on Input Tools**: Requires prior analysis with ClonalFrameML or Gubbins.
- **Input Format**: Strict requirements for input file formats; may need conversion.
- **Ambiguity Handling**: Masked regions may affect downstream phylogenetic analysis.
- **Visualization Quality**: SVG output may need post-processing for publication.
- **Boundary Detection**: May miss short recombination events or incorrectly mask regions.
- **Performance**: Large alignments may require significant computation time.

## Examples

### Mask with ClonalFrameML output
**Args:** `maskrc-svg -a alignment.fasta -c recombinant_regions.txt -o masked.fasta`
**Explanation:** Masks recombination regions from ClonalFrameML output.

### Mask with Gubbins output
**Args:** `maskrc-svg -a alignment.fasta -g gubbins_output.tab -o masked.fasta`
**Explanation:** Uses Gubbins recombination predictions for masking.

### Generate SVG visualization
**Args:** `maskrc-svg -a alignment.fasta -c regions.txt -s -o recombinant.svg`
**Explanation:** Creates SVG visualization of recombination regions.

### Custom masking character
**Args:** `maskrc-svg -a alignment.fasta -c regions.txt -m X -o masked.fasta`
**Explanation:** Uses 'X' instead of 'N' for masking.

### Keep gaps
**Args:** `maskrc-svg -a alignment.fasta -c regions.txt -k -o masked.fasta`
**Explanation:** Preserves gap positions during masking.

### Multiple input files
**Args:** `maskrc-svg -a alignment.fasta -c region1.txt region2.txt -o masked.fasta`
**Explanation:** Combines multiple region files for masking.

---
name: floco
category: alignment
description: "Floco performs copy number variation calling using sequence-to-graph alignment with network flow optimization."
tags: [floco, alignment, copy-number, cnv, bioinformatics, genomics, network-flow]
author: oxo-call-community
source_url: "https://github.com/hugocarmaga/floco"
---

## Concepts
- **Tool Overview**: Floco is a copy number variation caller that uses sequence-to-graph alignment with network flow optimization for accurate CNV detection.
- **Core Function**: Detects copy number variations by aligning sequencing reads to a variation graph and solving a network flow problem.
- **Input/Output**: Input: BAM/CRAM alignment files, reference genome, variation graph. Output: CNV calls in VCF/BED format.
- **Graph Alignment**: Aligns reads to a variation graph containing known variants, enabling more accurate CNV detection.
- **Network Flow**: Formulates CNV calling as a minimum cost network flow problem for optimal copy number assignment.
- **Breakpoint Detection**: Identifies precise CNV breakpoints using split-read analysis and read depth information.
- **Installation**: `conda install -c bioconda floco` or clone from GitHub. Requires Python 3.x and networkx.

## Pitfalls
- **Graph Construction**: Requires pre-built variation graph. Missing variants in the graph affect CNV detection.
- **Read Depth**: CNV calling depends on read depth. Low coverage regions produce unreliable calls.
- **Complex Regions**: Repeat-rich regions and segmental duplications are challenging. Filter or mask these regions.
- **Memory Usage**: Network flow optimization requires significant memory for large genomes. Process chromosome-by-chromosome.
- **Variant Call Format**: Output may not be compatible with all downstream tools. Convert to standard formats if needed.
- **Reference Bias**: Reference genome choice affects CNV calling. Use appropriate reference for the sample.

## Examples
### Basic CNV calling
**Args:** `floco --bam sample.bam --graph variation_graph.gfa --output cnv.vcf`
**Explanation:** Calls CNVs from BAM file using variation graph and outputs to VCF.

### Include read depth
**Args:** `floco --bam sample.bam --graph variation_graph.gfa --depth depth.txt --output cnv.vcf`
**Explanation:** Uses precomputed read depth information for improved CNV calling.

### Custom ploidy
**Args:** `floco --bam sample.bam --graph variation_graph.gfa --ploidy 2 --output cnv.vcf`
**Explanation:** Sets custom ploidy level for CNV calling (default is diploid).

### Breakpoint refinement
**Args:** `floco --bam sample.bam --graph variation_graph.gfa --refine-breakpoints --output cnv.vcf`
**Explanation:** Enables breakpoint refinement for more precise CNV boundaries.

### Generate BED output
**Args:** `floco --bam sample.bam --graph variation_graph.gfa --output cnv.bed --format bed`
**Explanation:** Outputs CNV calls in BED format instead of VCF.

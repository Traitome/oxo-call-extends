---
name: mummer2circos
category: alignment
description: Circular bacterial genome plots based on BLAST or NUCMER/PROMER alignments
tags: [mummer2circos, alignment, visualization, circos, bacterial-genome, genome-comparison]
author: oxo-call-community
source_url: "https://github.com/metagenlab/mummer2circos"
---

## Concepts

- **Tool Overview**: mummer2circos v1.4.2 is a tool for generating circular bacterial genome plots (Circos-style visualizations) based on BLAST, NUCMER, or PROMER alignment results. It bridges genome alignment tools with the Circos visualization engine to create publication-quality figures.
- **Core Function**: Takes alignment output from nucmer/promer or BLAST and converts it into Circos configuration files and plots. Automatically generates GC content, GC skew, and heatmap tracks for genome comparisons.
- **Input Format**: Accepts multi-FASTA files for reference and query genomes. Alignment is performed internally using nucmer (default), promer (translated alignment), or megablast. Supports multiple query genomes in a single run.
- **Output**: Generates SVG and PNG circular plots, along with Circos configuration files (circos.config), contig definitions, GC content/skew tracks, and heatmap tracks for each query genome.
- **Dependencies**: Requires Circos (v0.69.8), MUMmer, BLAST, Biopython, pandas, and various Perl modules. Installation via conda/bioconda handles most dependencies.
- **Visualization Features**: Supports customizable tracks for GC content, GC skew, sequence similarity heatmaps, and syntenic blocks. Config file can be manually edited to adjust colors, track heights, and other visual parameters.

## Pitfalls

- **Complex Dependency Chain**: mummer2circos has many dependencies (Circos, BLAST, MUMmer, Perl modules). Installation issues are common. Docker/Singularity containers are recommended for reliable execution.
- **Reference Genome Format**: Reference genome FASTA headers should match GenBank locus tags for proper track annotation. Using arbitrary headers may cause track labeling issues.
- **Memory and Runtime**: Large genome comparisons with many query sequences can be memory-intensive. Process smaller batches for large datasets.
- **Circos Configuration**: The auto-generated circos.config may need manual editing for publication-quality figures. Understanding Circos configuration syntax is helpful.
- **NUCmer vs PROMER**: NUCmer is for nucleotide-level alignments (highly similar genomes). PROMER is for translated alignments (divergent genomes with conserved proteins). Choose the appropriate method with `-a` flag.
- **Missing Query Alignments**: If a query genome has no significant alignments to the reference, its heatmap track will be empty or missing from the plot.

## Examples

### Generate basic circular plot with nucmer
**Args:** `-l -r reference.fna -q query1.fna query2.fna`
**Explanation:** Creates a circular plot using nucmer alignment. The `-l` flag enables the layout mode. Reference is specified with `-r`, queries with `-q`. Multiple query genomes are allowed.

### Use promer for divergent genomes
**Args:** `-a promer -r ref.fna -q query.fna -l`
**Explanation:** Uses promer (translated alignment) instead of nucmer. Use this when comparing genomes that are too divergent for nucleotide alignment but share conserved protein-coding regions.

### Generate compact circular plot
**Args:** `-c -l -r ref.fna -q genomes/*.fna`
**Explanation:** The `-c` flag creates a more compact circular layout. Useful when comparing many genomes or when displaying at smaller scales. Wildcards can specify multiple query files.

### Custom output directory
**Args:** `-o my_output/ -l -r ref.fna -q query.fna`
**Explanation:** Specifies a custom output directory with `-o`. If the directory doesn't exist, it will be created. All output files (plots, config, tracks) go into this directory.

### Modify Circos configuration manually
**Args:** `circos -conf circos.config`
**Explanation:** After mummer2circos generates the initial plot, you can edit circos.config to adjust colors, track order, highlight regions, or change spacing. Re-run circos to regenerate with changes.

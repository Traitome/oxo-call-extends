---
name: mitoz
category: assembly
description: "MitoZ: A toolkit for assembly, annotation, and visualization of animal mitochondrial genomes"
tags: [mitoz, assembly, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/linzhi2013/MitoZ"
---
## Concepts

- **Tool Overview**: MitoZ v3.6 assembles, annotates, and visualizes animal mitochondrial genomes.
- **Core Function**: Comprehensive mitochondrial genome analysis toolkit.
- **Assembly Pipeline**: Integrates assembly, annotation, and visualization.
- **Animal Specific**: Designed for animal mitochondrial genomes.
- **Input/Output**: Accepts sequencing reads; outputs assembled and annotated mtDNA.
- **Visualization**: Includes graphical representation of mitochondrial genomes.

## Pitfalls

- **Animal Specific**: Designed for animal mitochondria.
- **Computational Resources**: Pipeline may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Results depend on input data quality.
- **Reference Dependence**: Requires appropriate reference sequences.

## Examples

### Run complete pipeline
**Args:** `mitoz all --genetic_code 5 --fq1 reads_1.fastq --fq2 reads_2.fastq --outprefix result`
**Explanation:** Runs complete assembly and annotation pipeline.

### Assembly only
**Args:** `mitoz assemble --fq1 reads_1.fastq --fq2 reads_2.fastq --outprefix assembly`
**Explanation:** Performs assembly only.

### Annotation only
**Args:** `mitoz annotate --genetic_code 5 --fasta genome.fasta --outprefix annotation`
**Explanation:** Performs annotation only.

### Visualization
**Args:** `mitoz visualize --annot annotation.gff --fasta genome.fasta --outfile plot.png`
**Explanation:** Generates genome visualization.

### Batch processing
**Args:** `mitoz all --genetic_code 5 --fq1 fastq/*_1.fastq --fq2 fastq/*_2.fastq --outprefix results/`
**Explanation:** Processes multiple samples.
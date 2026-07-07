---
name: metawrap-mg
category: metagenomics
description: MetaWRAP is a pipeline for genome-resolved metagenomic data analysis
tags: [metawrap-mg, metagenomics, pipeline]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP-MG v1.3.0 is a comprehensive pipeline specifically optimized for metagenomic data analysis, providing end-to-end analysis from raw reads to annotated genomes.
- **Core Function**: Provides optimized analysis pipeline for metagenomic data.
- **Multi-step Pipeline**: Covers quality control, assembly, binning, and annotation in a single workflow.
- **Modular Design**: Allows running individual modules or the complete pipeline.
- **Input/Output**: Accepts raw sequencing reads; outputs assembled contigs, genome bins, and annotations.
- **Quality Assessment**: Includes quality metrics for all steps of the analysis.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Complete pipeline execution can be time-consuming.
- **Dependency Management**: Requires proper installation of all dependencies.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Storage Requirements**: Intermediate files can require substantial storage space.

## Examples

### Run complete metagenomic analysis
**Args:** `metawrap-mg -i reads.fastq -o results/`
**Explanation:** Runs the complete MetaWRAP-MG metagenomic analysis pipeline.

### Quality control only
**Args:** `metawrap-mg read_qc -i reads.fastq -o qc/`
**Explanation:** Runs only the quality control step.

### Assembly only
**Args:** `metawrap-mg assembly -i reads.fastq -o assembly/`
**Explanation:** Runs only the assembly step.

### Binning only
**Args:** `metawrap-mg binning -i contigs.fasta -o bins/`
**Explanation:** Runs only the binning step.

### Annotation only
**Args:** `metawrap-mg annotate_bins -i bins/ -o annotations/`
**Explanation:** Runs only the annotation step.
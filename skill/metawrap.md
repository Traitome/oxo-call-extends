---
name: metawrap
category: metagenomics
description: MetaWRAP is a pipeline for genome-resolved metagenomic data analysis
tags: [metawrap, metagenomics, pipeline]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP v1.2 is a comprehensive pipeline for genome-resolved metagenomic data analysis, integrating multiple tools for assembly, binning, and annotation.
- **Core Function**: Provides end-to-end analysis of metagenomic data from raw reads to annotated genomes.
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

### Run complete pipeline
**Args:** `metawrap -i reads.fastq -o results/`
**Explanation:** Runs the complete MetaWRAP metagenomic analysis pipeline.

### Quality control only
**Args:** `metawrap read_qc -i reads.fastq -o qc/`
**Explanation:** Runs only the quality control step.

### Assembly only
**Args:** `metawrap assembly -i reads.fastq -o assembly/`
**Explanation:** Runs only the assembly step.

### Binning only
**Args:** `metawrap binning -i contigs.fasta -o bins/`
**Explanation:** Runs only the binning step.

### Annotation only
**Args:** `metawrap annotate_bins -i bins/ -o annotations/`
**Explanation:** Runs only the annotation step.
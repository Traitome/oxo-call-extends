---
name: graph2pro-var
category: bioinformatics
description: graph2pro-var performs meta-proteogenomic identification by integrating mass spectrometry data with metagenomic/transcriptomic data.
tags: [graph2pro-var, proteomics, metagenomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/COL-IU/graph2pro-var"
---

## Concepts

- **Meta-proteogenomics**: Integrates metagenomic/transcriptomic data with mass spectrometry for comprehensive protein identification.

- **Graph-based Search**: Uses graph-based approaches to identify proteins from complex microbial communities.

- **Variant Detection**: Identifies protein variants and post-translational modifications from mass spec data.

- **Multi-omics Integration**: Combines genomic, transcriptomic, and proteomic data for improved identification.

- **Database Construction**: Builds custom protein databases from metagenomic assemblies.

- **False Discovery Control**: Implements rigorous false discovery rate control for reliable protein identification.

## Pitfalls

- **Data Integration**: Requires coordinated multi-omics data from the same sample. Mismatched data will produce poor results.

- **Computational Resources**: Processing large multi-omics datasets may require significant memory and time.

- **Database Quality**: Results depend on the quality and completeness of the protein database.

- **Mass Spec Quality**: Low-quality mass spectrometry data can produce false identifications.

- **Annotation Quality**: Poorly annotated metagenomic assemblies will limit identification accuracy.

## Examples

### Basic meta-proteogenomic identification
**Args:** `graph2pro-var -m mass_spec.mzML -g genes.fasta -o results.txt`
**Explanation:** Performs protein identification using mass spec and gene sequences.

### Include transcriptomic data
**Args:** `graph2pro-var -m mass_spec.mzML -g genes.fasta -t transcripts.fasta -o results.txt`
**Explanation:** Integrates transcriptomic data for improved identification.

### Build custom database
**Args:** `graph2pro-var build -i contigs.fasta -o protein_db.fasta`
**Explanation:** Builds a protein database from metagenomic contigs.

### Specify false discovery rate
**Args:** `graph2pro-var -m mass_spec.mzML -g genes.fasta -f 0.01 -o results.txt`
**Explanation:** Sets false discovery rate threshold to 1%.

### Identify variants
**Args:** `graph2pro-var -m mass_spec.mzML -g genes.fasta --variants -o variants.txt`
**Explanation:** Identifies protein variants from mass spec data.

### Generate report
**Args:** `graph2pro-var -m mass_spec.mzML -g genes.fasta -r -o report.html`
**Explanation:** Generates a comprehensive HTML report with identification statistics.

### Batch processing
**Args:** `graph2pro-var batch -d samples/ -o results/`
**Explanation:** Processes multiple samples in a directory.
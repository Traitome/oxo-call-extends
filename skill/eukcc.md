---
name: eukcc
category: qc
description: "Check eukaryotic genomes or MAGs for completeness and contamination."
tags: [eukcc, qc, genome-quality, eukaryotes, MAGs]
author: oxo-call-community
source_url: "https://eukcc.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: EukCC is a tool for assessing the quality of eukaryotic genomes and metagenome-assembled genomes (MAGs) by evaluating completeness and contamination.
- **Core Function**: Uses a set of conserved single-copy orthologs (BUSCO-like approach) to estimate genome completeness and detect contamination from other organisms.
- **Input/Output**: Input: Genome assembly (FASTA). Output: Quality report with completeness/contamination scores, BUSCO results.
- **Algorithm**: Identifies conserved eukaryotic marker genes and uses their presence/absence to estimate genome quality metrics.
- **Key Features**: Eukaryotic-specific markers, contamination detection, completeness estimation, MAG quality assessment, detailed reporting.
- **Installation**: `conda install -c bioconda eukcc`

## Pitfalls

- **Reference Database**: Quality assessment depends on marker gene database.
- **Genome Complexity**: Highly fragmented genomes may produce unreliable results.
- **Contamination Level**: High contamination can skew completeness estimates.
- **Taxonomic Bias**: Marker sets may be biased towards well-studied taxa.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic genome quality check
**Args:** `eukcc -i genome.fasta -o quality_report/`
**Explanation:** Assesses eukaryotic genome completeness and contamination.

### With custom marker database
**Args:** `eukcc -i genome.fasta -d custom_markers/ -o quality_report/`
**Explanation:** Uses custom marker database for quality assessment.

### Batch processing
**Args:** `eukcc -i genomes/ -o results/ --batch`
**Explanation:** Processes multiple genome assemblies in batch mode.

### Detailed output
**Args:** `eukcc -i genome.fasta -o quality_report/ --verbose`
**Explanation:** Outputs detailed quality assessment report.

### MAG quality assessment
**Args:** `eukcc -i mags/ -o mag_quality/ --mags`
**Explanation:** Assesses quality of metagenome-assembled genomes.
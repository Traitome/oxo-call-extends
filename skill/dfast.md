---
name: dfast
category: annotation
description: DFAST - DDBJ Fast Annotation and Submission Tool for prokaryotic genomes.
tags: [dfast, annotation, prokaryote, genome, pipeline]
author: oxo-call-community
source_url: "https://dfast.nig.ac.jp"
---

## Concepts

- **Tool Overview**: dfast (v1.3.9+) is a prokaryotic genome annotation pipeline from DDBJ. It provides automated annotation and generates submission-ready files for database deposition.
- **Core Function**: Annotates prokaryotic genomes with gene predictions, functional assignments, tRNA/rRNA identification, and prepares files for GenBank/DDBJ submission.
- **Input/Output**: Input: Genome assembly (FASTA), optional annotation hints. Output: Annotated genome (GFF/GBK), submission files, statistics report.
- **Algorithm**: Combines multiple tools for gene prediction (Prodigal), functional annotation (BLAST, InterProScan), and non-coding RNA prediction.
- **Key Features**: Automated annotation, submission-ready output, supports complete and draft genomes, quality control, comparative analysis.
- **Installation**: `conda install -c bioconda dfast`

## Pitfalls

- **Input Requirements**: Requires complete or draft genome assembly in FASTA format.
- **Database Updates**: Requires regular database updates for functional annotation.
- **Computational Resources**: May require significant resources for large genomes.
- **Annotation Quality**: Depends on database completeness and sequence quality.
- **Submission Rules**: Must follow DDBJ submission guidelines for valid output.

## Examples

### Annotate prokaryotic genome
**Args:** `dfast --genome assembly.fa --output annotation/`
**Explanation:** Annotates prokaryotic genome and generates submission-ready files.

### With custom gene predictions
**Args:** `dfast --genome assembly.fa --output annotation/ --genes custom_genes.gff`
**Explanation:** Incorporate custom gene predictions into annotation.

### For draft genome
**Args:** `dfast --genome assembly.fa --output annotation/ --draft`
**Explanation:** Optimize annotation for draft genome assembly.

### Run quality check
**Args:** `dfast --genome assembly.fa --output annotation/ --quality-check`
**Explanation:** Perform quality control on annotation results.

### Generate submission files
**Args:** `dfast --genome assembly.fa --output annotation/ --submission`
**Explanation:** Generate files ready for DDBJ submission.
---
name: mantis_pfa
category: variant-calling
description: Consensus-driven protein function annotation tool
tags: [mantis_pfa, variant-calling, protein-annotation]
author: oxo-call-community
source_url: "https://github.com/PedroMTQ/Mantis"
---

## Concepts

- **Tool Overview**: mantis_pfa v1.5.5 - Mantis is a fully customizable protein function annotation tool that dynamically integrates multiple reference databases.
- **Core Function**: Provides consensus-driven protein function annotations by integrating multiple reference databases.
- **Input/Output**: Input: Protein sequences (FASTA); Output: Annotation reports, GO terms, functional predictions.
- **Installation**: `conda install -c bioconda mantis_pfa`
- **Database Integration**: Dynamically integrates multiple reference databases for comprehensive annotations.
- **Consensus-driven**: Generates consensus annotations from multiple prediction methods.

## Pitfalls

- **Database Updates**: Outdated databases affect annotation accuracy.
- **Sequence Quality**: Poor quality sequences produce unreliable annotations.
- **Database Availability**: Requires access to reference databases.
- **Computational Resources**: Large datasets require significant memory.
- **Annotation Conflicts**: Different databases may provide conflicting annotations.
- **Parameter Tuning**: Incorrect parameters affect annotation quality.

## Examples

### Annotate proteins
**Args:** `mantis_pfa -i proteins.fasta -o annotations.txt`
**Explanation:** Annotates protein sequences using default databases.

### With custom databases
**Args:** `mantis_pfa -i proteins.fasta -d databases/ -o annotations.txt`
**Explanation:** Uses custom databases for annotation.

### GO term enrichment
**Args:** `mantis_pfa -i proteins.fasta -o annotations.txt --go`
**Explanation:** Includes GO term annotations.

### Verbose mode
**Args:** `mantis_pfa -i proteins.fasta -o annotations.txt -v`
**Explanation:** Provides detailed logging during analysis.

### Batch processing
**Args:** `mantis_pfa -i fasta/ -o results/`
**Explanation:** Processes multiple FASTA files in batch.

### Generate report
**Args:** `mantis_pfa -i proteins.fasta -o annotations.txt --report`
**Explanation:** Generates comprehensive annotation report.
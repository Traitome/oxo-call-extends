---
name: gmgc-mapper
category: metagenomics
description: gmgc-mapper - Map genes and genomes to the Global Microbial Gene Catalog.
tags: [gmgc-mapper, metagenomics, gene-catalog, GMGC]
author: oxo-call-community
source_url: "https://github.com/BigDataBiology/GMGC-mapper"
---

## Concepts
- **Gene Mapping**: Maps genes to GMGC.
- **Genome Comparison**: Compares genomes to catalog.
- **Metagenomics**: Analyzes metagenomic data.
- **Functional Annotation**: Provides functional annotations.
- **Taxonomic Assignment**: Assigns taxonomy.

## Pitfalls
- **Database Coverage**: Limited to catalog coverage.
- **Sequence Quality**: Requires high-quality sequences.
- **E-value Selection**: Requires proper e-value.
- **Annotation Completeness**: May have incomplete annotations.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Map genes
**Args:** `gmgc-mapper map -i genes.fasta -o mapping.txt`
**Explanation:** Maps genes to GMGC.

### With taxonomy
**Args:** `gmgc-mapper map -i genes.fasta -t -o mapping.txt`
**Explanation:** Includes taxonomy assignment.

### Map genome
**Args:** `gmgc-mapper genome -i genome.fasta -o mapping.txt`
**Explanation:** Maps genome to GMGC.

### Generate report
**Args:** `gmgc-mapper map -i genes.fasta -r -o report.html`
**Explanation:** Generates mapping report.

### Batch processing
**Args:** `gmgc-mapper map -l genes.txt -o ./mapping/`
**Explanation:** Processes multiple samples.
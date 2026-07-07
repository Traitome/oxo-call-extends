---
name: gmsc-mapper
category: metagenomics
description: gmsc-mapper - Query the Global Microbial smORFs Catalog (GMSC).
tags: [gmsc-mapper, metagenomics, smORFs, GMSC]
author: oxo-call-community
source_url: "https://github.com/BigDataBiology/GMSC-mapper"
---

## Concepts
- **smORF Detection**: Detects small open reading frames.
- **Catalog Query**: Queries GMSC database.
- **Metagenomics**: Analyzes metagenomic data.
- **Functional Annotation**: Provides functional annotations.
- **Taxonomic Assignment**: Assigns taxonomy.

## Pitfalls
- **smORF Definition**: smORF length definition varies.
- **Database Coverage**: Limited to catalog coverage.
- **Sequence Quality**: Requires high-quality sequences.
- **E-value Selection**: Requires proper e-value.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Query smORFs
**Args:** `gmsc-mapper query -i smorfs.fasta -o results.txt`
**Explanation:** Queries GMSC for smORFs.

### With taxonomy
**Args:** `gmsc-mapper query -i smorfs.fasta -t -o results.txt`
**Explanation:** Includes taxonomy assignment.

### Batch query
**Args:** `gmsc-mapper query -l samples.txt -o ./results/`
**Explanation:** Queries multiple samples.

### Generate report
**Args:** `gmsc-mapper query -i smorfs.fasta -r -o report.html`
**Explanation:** Generates query report.

### Update database
**Args:** `gmsc-mapper update -o gmsc.db`
**Explanation:** Updates local database.
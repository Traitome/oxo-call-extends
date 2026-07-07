---
name: kegg-pathways-completeness
category: utility
description: Counts completeness of each KEGG pathway for protein sequences.
tags: [kegg-pathways-completeness, utility, KEGG, pathways, completeness]
author: oxo-call-community
source_url: "https://github.com/EBI-Metagenomics/kegg-pathways-completeness-tool/blob/1.4.3/README.md"
---

## Concepts

- **Tool Overview**: kegg-pathways-completeness (v1.4.3) - Evaluates KEGG pathway completeness from protein sequences.
- **Pathway Analysis**: Analyzes the completeness of KEGG pathways.
- **KEGG Integration**: Uses KEGG database for pathway definitions.
- **Protein Sequences**: Works with protein sequence inputs.
- **Completeness Score**: Calculates percentage of pathway present.
- **Functional Annotation**: Provides functional annotation insights.

## Pitfalls

- **KEGG Database**: Requires up-to-date KEGG database.
- **Protein Quality**: Poor quality proteins affect results.
- **Annotation Quality**: Depends on sequence annotation quality.
- **Database Access**: May require internet access.
- **Memory Usage**: Large datasets require memory.
- **Pathway Coverage**: Not all pathways may be available.

## Examples

### Calculate pathway completeness
**Args:** `kegg-pathways-completeness -i proteins.fasta -o results.txt`
**Explanation:** Calculates KEGG pathway completeness.

### Specify organism
**Args:** `kegg-pathways-completeness -i proteins.fasta -o results.txt -o hsa`
**Explanation:** Uses human KEGG pathways for analysis.

### Generate HTML report
**Args:** `kegg-pathways-completeness -i proteins.fasta -o report.html -f html`
**Explanation:** Generates HTML report with completeness scores.

### Filter by completeness
**Args:** `kegg-pathways-completeness -i proteins.fasta -o results.txt -c 50`
**Explanation:** Only shows pathways with >=50% completeness.

### Batch processing
**Args:** `kegg-pathways-completeness batch -i samples.txt -o output/`
**Explanation:** Processes multiple samples in batch.

### Update KEGG database
**Args:** `kegg-pathways-completeness update`
**Explanation:** Updates local KEGG database.
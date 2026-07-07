---
name: local-cd-search
category: annotation
description: local-cd-search - Protein annotation using local PSSM databases from CDD
tags: [local-cd-search, annotation, protein, PSSM, CDD, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/apcamargo/local-cd-search"
---

## Concepts

- **Protein Annotation**: Functional annotation of proteins
- **PSSM Database**: Position-specific scoring matrix database
- **CDD Database**: Conserved Domain Database
- **Local Search**: Local database search for annotation
- **Domain Identification**: Identification of conserved domains
- **Functional Prediction**: Prediction of protein function

## Pitfalls

- **Database Updates**: Database must be regularly updated
- **Sequence Quality**: Poor quality sequences affect annotation
- **Memory Usage**: Memory-intensive for large databases
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive annotations
- **Database Size**: Large databases require significant storage

## Examples

### Search for domains
**Args:** `local-cd-search -i proteins.fasta -o annotations.txt`
**Explanation:** Searches for conserved domains in proteins.

### Custom database
**Args:** `local-cd-search -i proteins.fasta -o annotations.txt -d custom_db`
**Explanation:** Uses custom PSSM database.

### E-value threshold
**Args:** `local-cd-search -i proteins.fasta -o annotations.txt -e 1e-5`
**Explanation:** Sets E-value threshold to 1e-5.

### Threads
**Args:** `local-cd-search -i proteins.fasta -o annotations.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `local-cd-search -i proteins.fasta -o annotations.gff -f gff`
**Explanation:** Outputs annotations in GFF format.

### Update database
**Args:** `local-cd-search --update-db`
**Explanation:** Updates CDD database.
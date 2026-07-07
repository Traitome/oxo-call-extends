---
name: dbcanlight
category: annotation
description: A lightweight CAZyme annotation tool using pyhmmer for efficient HMM searches.
tags: [dbcanlight, annotation, CAZyme, carbohydrate, enzyme]
author: oxo-call-community
source_url: "https://github.com/chtsai0105/dbcanlight/blob/v1.1.1/README.md"
---

## Concepts

- **Tool Overview**: dbcanlight (v1.1.1+) is a lightweight rewrite of run_dbcan for CAZyme annotation. It uses pyhmmer (Cython binding to HMMER3) instead of the HMMER3 CLI suite for faster and more efficient searches.
- **Core Function**: Identifies carbohydrate-active enzymes (CAZymes) in protein sequences using HMM profiles from the dbCAN database with optimized performance.
- **Input/Output**: Input: Protein FASTA sequences. Output: CAZyme annotations in tabular format with domain positions and e-values.
- **Algorithm**: Uses pyhmmer for HMM searches against dbCAN HMM profiles, providing faster execution than traditional HMMER CLI.
- **Key Features**: Lightweight implementation, fast HMM searches via pyhmmer, simplified output format, reduced dependencies.
- **Installation**: `conda install -c bioconda dbcanlight`

## Pitfalls

- **Python Dependencies**: Requires specific Python and pyhmmer versions.
- **Database Path**: Needs correct path to dbCAN HMM database.
- **Memory Usage**: Large protein sets may require significant memory.
- **E-value Threshold**: Default thresholds may need adjustment.
- **Output Format**: Different from run_dbcan output format.

## Examples

### Basic CAZyme annotation
**Args:** `dbcanlight -i proteins.fasta -d dbCAN-HMMdb.txt -o annotations.tsv`
**Explanation:** Annotate CAZymes in protein sequences using dbCAN HMM database.

### Adjust e-value threshold
**Args:** `dbcanlight -i proteins.fasta -d dbCAN-HMMdb.txt -e 1e-10 -o annotations.tsv`
**Explanation:** Use stricter e-value threshold of 1e-10 for domain detection.

### Process multiple files
**Args:** `dbcanlight -i proteins1.fasta,proteins2.fasta -d dbCAN-HMMdb.txt -o combined.tsv`
**Explanation:** Annotate CAZymes in multiple protein files.
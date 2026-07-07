---
name: get_orfs
category: gene-prediction
description: get_orfs - Fast extraction of ORFs in all possible translation tables.
tags: [get_orfs, gene-prediction, ORF, translation]
author: oxo-call-community
source_url: "https://github.com/linsalrob/get_orfs"
---

## Concepts
- **ORF Prediction**: Predicts open reading frames.
- **Translation**: Translates DNA sequences to proteins.
- **Sequence Analysis**: Analyzes nucleotide sequences.
- **Genetic Code**: Supports multiple genetic codes.
- **Gene Finding**: Identifies potential genes.

## Pitfalls
- **Frame Selection**: Requires correct reading frame.
- **Translation Table**: Requires appropriate translation table.
- **Sequence Quality**: Requires high-quality sequence data.
- **Overlapping ORFs**: May detect overlapping ORFs.
- **Result Filtering**: Requires filtering by length.

## Examples
### Extract ORFs
**Args:** `get_orfs -i genome.fasta -o orfs.fasta`
**Explanation:** Extracts ORFs from genome sequence.

### With specific translation table
**Args:** `get_orfs -i genome.fasta -t 11 -o orfs.fasta`
**Explanation:** Uses translation table 11 (bacterial).

### Filter by length
**Args:** `get_orfs -i genome.fasta -m 100 -o orfs.fasta`
**Explanation:** Filters ORFs by minimum length.

### Batch processing
**Args:** `get_orfs -l genomes.txt -o ./orfs/`
**Explanation:** Processes multiple genome files.

### Output proteins
**Args:** `get_orfs -i genome.fasta -p -o proteins.fasta`
**Explanation:** Outputs translated protein sequences.
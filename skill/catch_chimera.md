---
name: catch_chimera
category: qc
description: Ensemble classifier for chimera detection in 16S rRNA sequencing studies
tags: [catch_chimera, chimera-detection, 16s-rrna, amplicon-sequencing, qc]
author: oxo-call-community
source_url: "https://science.sckcen.be/en/Institutes/EHS/MCB/MIC/Bioinformatics/CATCh"
---

## Concepts

- **Tool Overview**: CATCh is an ensemble classifier for chimera detection in 16S rRNA sequencing data.
- **Core Function**: Identifies chimeric sequences in amplicon sequencing datasets.
- **Algorithm**: Uses ensemble machine learning approach for chimera detection.
- **Input**: FASTA file with 16S rRNA sequences.
- **Output**: Classification of sequences as chimeric or non-chimeric.
- **Application**: Quality control for 16S rRNA amplicon sequencing.
- **Installation**: Install via bioconda: `conda install -c bioconda catch_chimera`

## Pitfalls

- **16S Specific**: Designed for 16S rRNA sequences only.
- **Sequence Quality**: Poor quality sequences affect classification accuracy.
- **Training Data**: Model trained on specific datasets; may not generalize to all environments.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Detect chimeras
**Args:** `CATCh -i sequences.fa -o results.txt`
**Explanation:** Identifies chimeric sequences in 16S rRNA dataset.

### Output detailed report
**Args:** `CATCh -i sequences.fa -o results.txt -d`
**Explanation:** Generates detailed chimera detection report.

### Display help
**Args:** `CATCh --help`
**Explanation:** Shows all available options and usage information.
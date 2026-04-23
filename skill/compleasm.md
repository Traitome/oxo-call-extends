---
name: compleasm
category: qc
description: Faster and more accurate reimplementation of BUSCO for genome completeness assessment
tags: [compleasm, busco, genome-completeness, quality, assembly]
author: oxo-call-community
source_url: "https://github.com/huangnengCSU/compleasm"
---

## Concepts

- **Tool Overview**: Compleasm is a faster and more accurate reimplementation of BUSCO, assessing genome assembly completeness using single-copy orthologs.
- **Core Function**: Evaluates genome completeness by searching for conserved single-copy ortholog genes from a lineage-specific database.
- **Input/Output**: Input: Genome assembly (FASTA). Output: Completeness statistics (complete, duplicated, fragmented, missing) and summary report.
- **Lineage Databases**: Uses the same BUSCO lineage databases (bacteria, eukaryota, insects, mammals, etc.).
- **Speed**: Significantly faster than original BUSCO, especially for large genomes.
- **Accuracy**: Improved accuracy in ortholog detection and classification compared to BUSCO.

## Pitfalls

- **Lineage Selection**: Must select appropriate lineage database. Wrong lineage produces misleading results.
- **Database Download**: First run downloads the lineage database. Ensure internet connection or pre-download.
- **Gene Prediction**: Uses different gene predictor than BUSCO. Results may differ slightly.
- **Incomplete Genes**: Fragmented BUSCOs indicate partial genes, suggesting assembly gaps or fragmentation.

## Examples

### Assess bacterial genome completeness
**Args:** `-l bacteria -i genome.fasta -o output_dir`
**Explanation:** Assesses completeness against the bacteria lineage database, outputs statistics and report.

### Assess eukaryotic genome
**Args:** `-l eukaryota -i genome.fasta -o output_dir`
**Explanation:** Uses the eukaryota lineage for general eukaryotic genome assessment.

### Use specific lineage
**Args:** `-l insecta -i genome.fasta -o output_dir`
**Explanation:** Uses insecta-specific lineage for more accurate insect genome assessment.

### Specify number of threads
**Args:** `-l bacteria -i genome.fasta -o output_dir -t 8`
**Explanation:** Uses 8 threads for faster analysis of large genomes.

### Use pre-downloaded database
**Args:** `-l bacteria -i genome.fasta -o output_dir --lineage_path /path/to/bacteria_odb10`
**Explanation:** Uses a pre-downloaded lineage database instead of auto-downloading.

### Skip gene prediction
**Args:** `-l bacteria -i genome.fasta -o output_dir --skip_gene_prediction`
**Explanation:** Skips ab initio gene prediction, useful when analyzing transcriptome or protein data.

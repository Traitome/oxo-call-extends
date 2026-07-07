---
name: splash
category: sequence-analysis
description: Splash - Unsupervised k-mer analysis for sequence variation discovery
tags: [splash, sequence-analysis, k-mer-analysis, sequence-variation, unsupervised]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/splash"
---

## Concepts

- **Tool Overview**: splash (v2.11.0) - A sequence variation discovery tool
- **Core Function**: Discovers regulated sequence variation through k-mer composition analysis
- **Input/Output**: Accepts DNA/RNA sequences; outputs variation patterns
- **Algorithm**: Statistical analysis of k-mer composition
- **Installation**: `conda install -c bioconda splash`
- **Key Features**: K-mer analysis, sequence variation, unsupervised learning

## Pitfalls

- **Input Requirements**: Requires properly formatted DNA/RNA sequences
- **Sequence Quality**: Sequence quality affects variation detection
- **K-mer Size**: K-mer size affects analysis sensitivity
- **Memory Usage**: Large sequence sets require significant memory
- **Output Format**: Output format depends on configuration
- **Variation Detection**: Detection accuracy depends on k-mer parameters

## Examples

### Display help
**Args:** `splash --help`
**Explanation:** Shows available options and usage information.

### Basic k-mer analysis
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv`
**Explanation:** Analyze k-mer composition for variation detection.

### With k-mer size
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv --kmer-size 31`
**Explanation:** Set k-mer size for analysis.

### With configuration file
**Args:** `splash config.yaml`
**Explanation:** Run analysis with configuration file.

### Multiple sequences
**Args:** `splash -i seq1.fasta seq2.fasta -o variation_patterns.tsv`
**Explanation:** Analyze multiple sequence files.

### Output detailed results
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv --detailed`
**Explanation:** Output detailed variation information.

### Output k-mer counts
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv --kmer-counts`
**Explanation:** Output k-mer count information.

### Output statistics
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv --stats`
**Explanation:** Output analysis statistics.

### Generate report
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv --report`
**Explanation:** Generate analysis report.

### With threads
**Args:** `splash -i sequences.fasta -o variation_patterns.tsv -p 8`
**Explanation:** Use multiple threads for analysis.
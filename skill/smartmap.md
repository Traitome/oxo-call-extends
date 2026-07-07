---
name: smartmap
category: alignment
description: SmartMap - Bayesian Analysis of Ambiguously Mapped Reads for improved read mapping accuracy
tags: [smartmap, alignment, bayesian, mapping, ambiguous-reads]
author: oxo-call-community
source_url: "http://shah-rohan.github.io/SmartMap"
---

## Concepts

- **Tool Overview**: smartmap (v1.0.0) - A Bayesian approach for analyzing ambiguously mapped reads
- **Core Function**: Resolves ambiguous read mappings using Bayesian statistical methods
- **Input/Output**: Accepts SAM/BAM files; outputs re-weighted alignments with confidence scores
- **Algorithm**: Uses Bayesian posterior probabilities to reassign ambiguous mappings
- **Installation**: `conda install -c bioconda smartmap`
- **Key Features**: Improves mapping accuracy, handles multi-mapping reads, provides confidence scores

## Pitfalls

- **Input Requirements**: Requires properly aligned SAM/BAM files
- **Reference Genome**: Must match the reference used for initial alignment
- **Computation Time**: Bayesian calculations can be computationally intensive
- **Memory Usage**: Large BAM files require significant memory
- **Parameter Sensitivity**: Results depend on prior probability settings
- **Output Interpretation**: Confidence scores require careful interpretation

## Examples

### Display help
**Args:** `smartmap --help`
**Explanation:** Shows available options and usage information.

### Basic re-mapping
**Args:** `smartmap -i aligned.bam -o reweighted.bam`
**Explanation:** Re-weight ambiguous mappings using Bayesian analysis.

### With custom priors
**Args:** `smartmap -i aligned.bam -o reweighted.bam -p priors.txt`
**Explanation:** Use custom prior probabilities for mapping.

### Generate confidence scores
**Args:** `smartmap -i aligned.bam -o reweighted.bam -c`
**Explanation:** Output confidence scores for each alignment.

### Filter by confidence
**Args:** `smartmap -i aligned.bam -o filtered.bam -t 0.9`
**Explanation:** Filter mappings with confidence < 0.9.

### Multi-threaded processing
**Args:** `smartmap -i aligned.bam -o reweighted.bam -t 4`
**Explanation:** Use 4 threads for parallel processing.

### Output statistics
**Args:** `smartmap -i aligned.bam -o reweighted.bam -s stats.txt`
**Explanation:** Generate mapping statistics report.

### With variant information
**Args:** `smartmap -i aligned.bam -v variants.vcf -o reweighted.bam`
**Explanation:** Incorporate variant information into mapping.
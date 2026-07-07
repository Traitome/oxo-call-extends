---
name: mockinbird
category: utility
description: A fully automatic and reproducible PAR-CLIP analysis pipeline
tags: [mockinbird, utility, rna-binding]
author: oxo-call-community
source_url: "https://github.com/soedinglab/mockinbird"
---

## Concepts

- **Tool Overview**: Mockinbird v1.0.0a1 provides automatic PAR-CLIP analysis pipeline.
- **Core Function**: Analyzes PAR-CLIP data to identify RNA-protein binding sites.
- **PAR-CLIP Analysis**: Processes photoactivatable ribonucleoside-enhanced crosslinking data.
- **Peak Calling**: Identifies binding peaks from sequencing data.
- **Input/Output**: Accepts sequencing reads; outputs binding sites.
- **RNA Biology**: Supports RNA-protein interaction studies.

## Pitfalls

- **PAR-CLIP Specific**: Designed for PAR-CLIP sequencing data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal peak calling.
- **Data Quality**: Results depend on crosslinking efficiency.
- **Reference Genome**: Requires appropriate reference genome.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Run PAR-CLIP analysis
**Args:** `mockinbird -i reads.fastq -g genome.fasta -o results/`
**Explanation:** Runs complete PAR-CLIP analysis pipeline.

### With quality filtering
**Args:** `mockinbird -i reads.fastq -g genome.fasta -q -o results/`
**Explanation:** Applies quality filtering before analysis.

### Peak calling only
**Args:** `mockinbird peak -i alignments.bam -o peaks.bed`
**Explanation:** Performs peak calling only.

### Batch processing
**Args:** `mockinbird -i fastq/ -g genome.fasta -o results/`
**Explanation:** Processes multiple read files.

### Generate report
**Args:** `mockinbird -i reads.fastq -g genome.fasta -o results/ -r report.html`
**Explanation:** Generates analysis report.
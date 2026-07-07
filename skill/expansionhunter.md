---
name: expansionhunter
category: utility
description: "A tool for estimating repeat sizes."
tags: [expansionhunter, utility, repeat-expansion, STR, variant-detection]
author: oxo-call-community
source_url: "https://github.com/Illumina/ExpansionHunter"
---

## Concepts

- **Tool Overview**: ExpansionHunter is a tool for detecting and estimating the size of short tandem repeat (STR) expansions from sequencing data.
- **Core Function**: Identifies and quantifies repeat expansions, which are associated with various genetic disorders.
- **Input/Output**: Input: Aligned reads (BAM), reference genome (FASTA). Output: Repeat expansion calls (VCF/JSON), size estimates.
- **Algorithm**: Uses read-based approaches to detect and measure repeat expansions from sequencing data.
- **Key Features**: STR expansion detection, size estimation, VCF output, support for paired-end reads, clinical variant detection.
- **Installation**: `conda install -c bioconda expansionhunter`

## Pitfalls

- **Read Coverage**: Requires sufficient read coverage in repeat regions.
- **Repeat Complexity**: Complex repeat structures may affect detection accuracy.
- **Reference Quality**: Results depend on reference genome quality.
- **Computation Resources**: Large datasets require significant computational resources.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic repeat expansion detection
**Args:** `ExpansionHunter --reads input.bam --reference ref.fasta --output results.vcf`
**Explanation:** Detects repeat expansions from aligned reads.

### With specific repeat locus
**Args:** `ExpansionHunter --reads input.bam --reference ref.fasta --locus CAG --output results.vcf`
**Explanation:** Focuses on specific repeat locus (e.g., CAG repeats).

### Size estimation
**Args:** `ExpansionHunter --reads input.bam --reference ref.fasta --estimate-size --output results.vcf`
**Explanation:** Estimates repeat sizes for detected expansions.

### JSON output
**Args:** `ExpansionHunter --reads input.bam --reference ref.fasta --json-output results.json`
**Explanation:** Outputs results in JSON format.

### Batch processing
**Args:** `ExpansionHunter --input samples.txt --reference ref.fasta --output results/ --batch`
**Explanation:** Processes multiple samples in batch mode.
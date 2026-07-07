---
name: fastpmr
category: utility
description: "Calculate pairwise mismatch rates (PMRs) between ancient DNA sequences."
tags: [fastpmr, utility, ancient-DNA, mismatch-rate, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ehuangc/fastpmr"
---

## Concepts

- **Tool Overview**: fastpmr is a tool for calculating pairwise mismatch rates (PMRs) between ancient DNA sequences, useful for aDNA quality assessment.
- **Core Function**: Computes mismatch rates between pairs of ancient DNA sequences.
- **Input/Output**: Input: Ancient DNA sequences (FASTA/FASTQ). Output: Mismatch rates, quality statistics.
- **Algorithm**: Uses sequence comparison to calculate mismatch rates.
- **Key Features**: Fast computation, ancient DNA analysis, quality assessment, batch processing, statistical reporting.
- **Installation**: `conda install -c bioconda fastpmr`

## Pitfalls

- **Data Quality**: Requires high-quality ancient DNA sequences.
- **Damage Patterns**: Ancient DNA may have characteristic damage patterns.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic PMR calculation
**Args:** `fastpmr -i sequences.fasta -o pmr_results.txt`
**Explanation:** Calculates pairwise mismatch rates.

### From FASTQ
**Args:** `fastpmr -i reads.fastq -o pmr_results.txt`
**Explanation:** Processes FASTQ formatted data.

### Quality filtering
**Args:** `fastpmr -i sequences.fasta -o pmr_results.txt -q 20`
**Explanation:** Filters by quality score before analysis.

### Batch processing
**Args:** `fastpmr -i fasta_files/ -o results/ --batch`
**Explanation:** Processes multiple files in batch mode.

### Detailed output
**Args:** `fastpmr -i sequences.fasta -o pmr_results.txt -v`
**Explanation:** Generates verbose output with additional details.
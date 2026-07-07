---
name: dunovo
category: utility
description: Du Novo - Pipeline for processing duplex sequencing data to reduce error rates.
tags: [dunovo, utility, duplex-sequencing, error-correction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/dunovo"
---

## Concepts

- **Tool Overview**: Du Novo is a pipeline for processing duplex sequencing data to achieve ultra-high accuracy.
- **Core Function**: Processes paired reads from duplex sequencing to identify and correct sequencing errors.
- **Input/Output**: Input: FASTQ reads from duplex sequencing. Output: Error-corrected consensus sequences.
- **Algorithm**: Uses read pairing and consensus calling to reduce sequencing error rates.
- **Key Features**: Error correction, consensus generation, duplex-specific processing, quality filtering, batch processing.
- **Installation**: `conda install -c bioconda dunovo`

## Pitfalls

- **Input Requirements**: Requires properly formatted duplex sequencing reads; standard reads won't work.
- **Read Pairing**: Incorrectly paired reads will produce unreliable consensus sequences.
- **Error Rate**: Very high error rates may overwhelm the correction algorithm.
- **Memory Usage**: Large datasets may require significant memory resources.
- **Computation Time**: Consensus calling can be computationally intensive for large datasets.
- **Quality Thresholds**: Default quality thresholds may need adjustment for different data.

## Examples

### Process duplex reads
**Args:** `dunovo --input R1.fq R2.fq --output consensus.fa`
**Explanation:** Processes duplex sequencing reads to generate error-corrected consensus sequences.

### With quality filtering
**Args:** `dunovo --input R1.fq R2.fq --output consensus.fa --min-quality 20`
**Explanation:** Filters low-quality reads before consensus generation.

### Batch processing
**Args:** `dunovo --input-dir fastq_files/ --output-dir consensus/`
**Explanation:** Processes multiple duplex read pairs in batch mode.

### Custom error threshold
**Args:** `dunovo --input R1.fq R2.fq --output consensus.fa --error-threshold 0.01`
**Explanation:** Sets a custom error threshold for consensus calling.

### Output as FASTQ
**Args:** `dunovo --input R1.fq R2.fq --output consensus.fq --format fastq`
**Explanation:** Outputs consensus sequences in FASTQ format with quality scores.

### Include statistics
**Args:** `dunovo --input R1.fq R2.fq --output consensus.fa --stats stats.txt`
**Explanation:** Generates statistics about the consensus calling process.
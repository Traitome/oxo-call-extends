---
name: dupre
category: qc
description: DupRe - Duplicate rate estimation using linear programming and hypergeometric distribution.
tags: [dupre, qc, duplicate-detection, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://bitbucket.org/genomeinformatics/dupre/"
---

## Concepts

- **Tool Overview**: DupRe estimates duplicate rates in sequencing data using statistical modeling.
- **Core Function**: Uses linear programming and hypergeometric distribution to estimate PCR duplicate rates.
- **Input/Output**: Input: FASTQ reads or alignment files. Output: Duplicate rate estimates and statistics.
- **Algorithm**: Applies statistical models to estimate duplicate rates without explicit duplicate marking.
- **Key Features**: Accurate estimation, computational efficiency, low memory usage, batch processing, quality assessment.
- **Installation**: `conda install -c bioconda dupre`

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence data; corrupted files cause errors.
- **Sequencing Depth**: Very low coverage affects estimation accuracy.
- **Duplicate Distribution**: Non-random duplicate distribution may affect estimates.
- **Read Length**: Short reads may produce less accurate estimates.
- **Library Preparation**: PCR-free libraries may have different duplicate characteristics.
- **Computational Resources**: Very large datasets may require extended processing time.

## Examples

### Estimate duplicate rate
**Args:** `dupre --input reads.fq --output dupre_results.txt`
**Explanation:** Estimates duplicate rate from FASTQ reads using statistical modeling.

### From BAM file
**Args:** `dupre --input aligned.bam --output dupre_results.txt --bam`
**Explanation:** Estimates duplicate rate from aligned BAM file.

### Batch processing
**Args:** `dupre --input-dir fastq_files/ --output-dir results/`
**Explanation:** Processes multiple FASTQ files in batch mode.

### With custom parameters
**Args:** `dupre --input reads.fq --output results.txt --kmer-size 25`
**Explanation:** Uses 25-mer size for duplicate estimation.

### Output detailed report
**Args:** `dupre --input reads.fq --output results.txt --verbose`
**Explanation:** Generates detailed statistics about duplicate estimation.

### Compare multiple samples
**Args:** `dupre --compare sample1.fq sample2.fq sample3.fq --output comparison.txt`
**Explanation:** Compares duplicate rates across multiple samples.
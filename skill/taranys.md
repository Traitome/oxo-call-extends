---
name: taranys
category: typing
description: cg/wgMLST allele calling software with schema evaluation and allele distance estimation.
tags: [taranys, mlst, allele-calling, epidemiology]
author: oxo-call-community
source_url: "https://github.com/BU-ISCIII/taranys"
---

## Concepts

- **Tool Overview**: taranys (v3.0.1) performs cg/wgMLST allele calling.
- **Core Function**: MLST typing with schema evaluation and distance estimation.
- **Algorithm**: Uses database matching for allele calling.
- **Input/Output**: Input: FASTQ/BAM; Output: Allele profiles, distances.
- **Applications**: Bacterial typing, outbreak research, phylogenetics.
- **Installation**: `conda install -c bioconda taranys` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large databases require significant memory.
- **Schema Compatibility**: Requires compatible MLST schemas.
- **Read Quality**: Poor quality affects allele calling.
- **Computational Time**: Processing large datasets can be slow.
- **False Positives**: May assign incorrect alleles.
- **Distance Calculation**: Depends on complete allele calls.

## Examples

### Display help
**Args:** `taranys --help`
**Explanation:** Shows available options and usage information.

### Basic allele calling
**Args:** `taranys -i reads.fastq -s schema/ -o alleles.txt`
**Explanation:** Call cgMLST alleles from reads.

### Calculate distances
**Args:** `taranys -i alleles.txt -d distances.txt`
**Explanation:** Calculate pairwise allele distances.

### Verbose mode
**Args:** `taranys -i reads.fastq -s schema/ -o alleles.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `taranys -i reads.fastq -s schema/ -o alleles.txt --stats`
**Explanation:** Generate statistics about allele calling.

### Batch processing
**Args:** `for f in fastq/*.fastq; do taranys -i $f -s schema/ -o alleles/${f%.fastq}_alleles.txt; done`
**Explanation:** Process multiple FASTQ files.

### Evaluate schema
**Args:** `taranys -i alleles.txt -e schema_evaluation.txt`
**Explanation:** Evaluate MLST schema quality.

### Include all alleles
**Args:** `taranys -i reads.fastq -s schema/ -o alleles.txt --all`
**Explanation:** Include all allele information.

### Generate report
**Args:** `taranys -i reads.fastq -s schema/ -o alleles.txt --report`
**Explanation:** Generate comprehensive MLST report.

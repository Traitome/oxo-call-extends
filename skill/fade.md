---
name: fade
category: utility
description: "fade is a D program that provides fast identification and removal of enzymatic fragmentation artifacts."
tags: [fade, utility, artifact-removal, sequencing-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/blachlylab/fade"
---

## Concepts

- **Tool Overview**: fade is a fast tool for identifying and removing enzymatic fragmentation artifacts from sequencing data.
- **Core Function**: Detects and removes artifacts introduced during enzymatic fragmentation steps in sequencing library preparation.
- **Input/Output**: Input: Sequencing reads (FASTQ). Output: Cleaned reads (FASTQ), artifact report.
- **Algorithm**: Uses sequence pattern recognition to identify enzymatic fragmentation artifacts.
- **Key Features**: Fast artifact detection, artifact removal, support for multiple enzymes, batch processing, quality reporting.
- **Installation**: `conda install -c bioconda fade`

## Pitfalls

- **Enzyme Specificity**: Requires knowledge of fragmentation enzyme used.
- **Read Quality**: Poor quality reads may affect artifact detection.
- **False Positives**: May incorrectly identify valid sequences as artifacts.
- **Memory Usage**: Large datasets may require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic artifact removal
**Args:** `fade -i reads.fastq -o cleaned_reads.fastq`
**Explanation:** Detects and removes enzymatic fragmentation artifacts.

### Specify enzyme
**Args:** `fade -i reads.fastq -o cleaned_reads.fastq -e tn5`
**Explanation:** Uses TN5 transposase enzyme pattern for artifact detection.

### Generate report
**Args:** `fade -i reads.fastq -o cleaned_reads.fastq -r artifact_report.txt`
**Explanation:** Generates report of detected artifacts.

### Paired-end reads
**Args:** `fade -1 reads_1.fastq -2 reads_2.fastq -o cleaned/`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `fade -i reads/ -o cleaned/ --batch`
**Explanation:** Processes multiple read files in batch mode.
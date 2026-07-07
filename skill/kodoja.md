---
name: kodoja
category: virology
description: Identifying viruses from plant RNA sequencing data
tags: [kodoja, virology, plant-viruses, RNA-Seq, virus-detection]
author: oxo-call-community
source_url: "https://github.com/abaizan/kodoja/"
---

## Concepts

- **Virus Detection**: Identifies viruses from plant RNA-Seq data
- **Plant Virology**: Specialized for plant viral pathogen detection
- **De Novo Assembly**: Uses de novo assembly for virus identification
- **Reference Mapping**: Combines reference-based mapping for validation
- **Multiple Virus Detection**: Can detect multiple viruses in mixed infections
- **Pathogen Discovery**: Enables discovery of novel plant viruses

## Pitfalls

- **Assembly Quality**: Poor assembly affects virus detection sensitivity
- **Low Titer**: Viruses present at low abundance may be missed
- **Novel Viruses**: Novel viruses may not be detected without references
- **Host Contamination**: High host reads reduce detection sensitivity
- **Mixed Infections**: Multiple viruses complicate analysis
- **Database Updates**: Requires updated virus reference databases

## Examples

### Identify viruses from RNA-Seq
**Args:** `kodoja -r reads_1.fastq -r reads_2.fastq -o results/`
**Explanation:** Identifies viruses from paired-end plant RNA-Seq data.

### Single-end reads
**Args:** `kodoja -r reads.fastq -o results/`
**Explanation:** Analyzes single-end reads for virus detection.

### With custom database
**Args:** `kodoja -r reads.fastq -d custom_virus_db/ -o results/`
**Explanation:** Uses custom virus database for detection.

### Threshold adjustment
**Args:** `kodoja -r reads.fastq -o results/ --threshold 0.01`
**Explanation:** Adjusts detection threshold for sensitivity.

### Generate report
**Args:** `kodoja -r reads.fastq -o results/ --report`
**Explanation:** Generates detailed detection report.

### Batch processing
**Args:** `kodoja --batch -d samples/ -o results/`
**Explanation:** Processes multiple plant samples in batch mode.
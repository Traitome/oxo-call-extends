---
name: squid
category: rna-seq
description: SQUID - Detector for fusion-gene and transcriptomic structural variations
tags: [squid, rna-seq, fusion-genes, structural-variation, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/Kingsford-Group/squid"
---

## Concepts

- **Tool Overview**: squid (v1.5) - A structural variation detection tool
- **Core Function**: Detects fusion-gene and non-fusion-gene transcriptomic structural variations
- **Input/Output**: Accepts RNA-seq data; outputs structural variation calls
- **Algorithm**: Fusion-gene and structural variation detection algorithms
- **Installation**: `conda install -c bioconda squid`
- **Key Features**: Fusion-gene detection, structural variation, RNA-seq analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted RNA-seq data
- **Read Quality**: Read quality affects detection accuracy
- **Fusion Detection**: Fusion detection depends on read coverage
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Detection Accuracy**: Accuracy depends on read quality and coverage

## Examples

### Display help
**Args:** `squid --help`
**Explanation:** Shows available options and usage information.

### Basic structural variation detection
**Args:** `squid -i rna_seq.bam -o structural_variations.txt`
**Explanation:** Detect structural variations in RNA-seq data.

### With annotation
**Args:** `squid -i rna_seq.bam -g annotation.gtf -o structural_variations.txt`
**Explanation:** Use gene annotation for detection.

### With fusion detection
**Args:** `squid -i rna_seq.bam -o structural_variations.txt --fusion`
**Explanation:** Enable fusion-gene detection.

### Multiple samples
**Args:** `squid -i sample1.bam sample2.bam -o structural_variations.txt`
**Explanation:** Detect variations in multiple samples.

### Output detailed results
**Args:** `squid -i rna_seq.bam -o structural_variations.txt --detailed`
**Explanation:** Output detailed variation information.

### Output fusions
**Args:** `squid -i rna_seq.bam -o structural_variations.txt --list-fusions`
**Explanation:** Output fusion-gene list.

### Output statistics
**Args:** `squid -i rna_seq.bam -o structural_variations.txt --stats`
**Explanation:** Output detection statistics.

### Generate report
**Args:** `squid -i rna_seq.bam -o structural_variations.txt --report`
**Explanation:** Generate detection report.

### With threads
**Args:** `squid -i rna_seq.bam -o structural_variations.txt -p 8`
**Explanation:** Use multiple threads for detection.
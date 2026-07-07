---
name: isoseq3
category: expression
description: PacBio Iso-Seq 3 - Scalable de novo isoform discovery from long-read transcriptome data.
tags: [isoseq3, expression, long reads, PacBio, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **De Novo Isoform Discovery**: Identifies full-length transcript isoforms without reference genome.
- **PacBio Optimization**: Specifically designed for PacBio SMRT sequencing data.
- **Circular Consensus Sequencing**: Utilizes CCS reads for high-accuracy isoform sequences.
- **Isoform Classification**: Classifies reads into distinct isoform clusters.
- **Full-Length Transcripts**: Generates complete transcript sequences from long reads.
- **Scalable Processing**: Handles large-scale transcriptome datasets efficiently.

## Pitfalls

- **Read Quality**: Poor quality CCS reads affect isoform accuracy.
- **Computational Resources**: Processing large datasets requires significant resources.
- **Memory Requirements**: Memory usage increases with dataset complexity.
- **Isoform Complexity**: Highly similar isoforms may be merged incorrectly.
- **Chimeric Reads**: Chimeric sequences can create false isoforms.
- **Parameter Tuning**: Optimal parameters may vary between datasets.

## Examples

### Basic isoform analysis
**Args:** `isoseq3 refine --input ccs.bam --output polished.bam --report report.txt`
**Explanation:** Refines CCS reads and generates polished isoforms.

### Cluster isoforms
**Args:** `isoseq3 cluster --input polished.bam --output clustered.bam`
**Explanation:** Clusters polished reads into isoform groups.

### Generate consensus sequences
**Args:** `isoseq3 collapse --input clustered.bam --output collapsed.fasta`
**Explanation:** Generates consensus sequences for each isoform cluster.

### Full pipeline
**Args:** `isoseq3 all --input ccs.bam --output results/`
**Explanation:** Runs the complete Iso-Seq pipeline from CCS to collapsed isoforms.

### With reference annotation
**Args:** `isoseq3 collapse --input clustered.bam --reference genome.fasta --annotation genes.gtf --output collapsed.fasta`
**Explanation:** Uses reference annotation to guide isoform collapsing.

### Generate statistics
**Args:** `isoseq3 stats --input collapsed.fasta --output stats.txt`
**Explanation:** Generates statistics about the isoform discovery process.
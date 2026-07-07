---
name: isoseq
category: expression
description: PacBio Iso-Seq analysis tools for de novo transcriptome assembly and isoform discovery.
tags: [isoseq, expression, long reads, PacBio, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **De Novo Transcriptome Assembly**: Assembles full-length transcript sequences from PacBio reads.
- **Isoform Discovery**: Identifies alternative splicing variants and novel isoforms.
- **PacBio Data Processing**: Optimized for PacBio SMRT sequencing technology.
- **Full-Length Reads**: Captures complete transcript sequences from 5' to 3' ends.
- **Isoform Quantification**: Provides expression levels for each isoform.
- **Reference-Guided Analysis**: Can integrate with reference genomes for annotation.

## Pitfalls

- **Data Quality**: Poor quality sequencing data affects assembly accuracy.
- **Computational Complexity**: Assembling large transcriptomes is computationally intensive.
- **Memory Requirements**: Processing millions of reads requires significant memory.
- **Isoform Collapse**: Distinguishing highly similar isoforms is challenging.
- **Chimeric Reads**: Chimeric sequences can create false isoforms.
- **Coverage Bias**: Uneven coverage affects isoform detection sensitivity.

## Examples

### Basic Iso-Seq analysis
**Args:** `isoseq analyze --input subreads.bam --output results/`
**Explanation:** Performs complete Iso-Seq analysis including CCS generation and clustering.

### Generate CCS reads
**Args:** `isoseq ccs --input subreads.bam --output ccs.bam`
**Explanation:** Generates circular consensus sequences from subreads.

### Cluster reads
**Args:** `isoseq cluster --input ccs.bam --output clusters/`
**Explanation:** Clusters CCS reads into isoform groups.

### Collapse to consensus
**Args:** `isoseq collapse --input clusters/ --output isoforms.fasta`
**Explanation:** Collapses clusters into consensus isoform sequences.

### Quantify isoforms
**Args:** `isoseq quantify --input isoforms.fasta --reads mapped.bam --output expression.csv`
**Explanation:** Quantifies isoform expression levels from mapped reads.

### Reference annotation
**Args:** `isoseq annotate --input isoforms.fasta --reference genome.fasta --output annotated.gtf`
**Explanation:** Annotates isoforms against a reference genome.
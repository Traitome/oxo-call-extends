---
name: nanocount
category: expression
description: NanoCount - Transcript abundance estimation from Nanopore direct-RNA sequencing
tags: [nanocount, expression, nanopore, transcript-abundance, direct-rna, quantification]
author: oxo-call-community
source_url: "https://github.com/a-slide/NanoCount/"
---

## Concepts

- **Tool Overview**: NanoCount v1.0.0 estimates transcript abundance from Oxford Nanopore direct-RNA sequencing (dRNA-Seq) data. It handles multi-mapping reads using an expectation-maximization approach.
- **Core Function**: Quantifies transcript expression levels from dRNA-Seq alignments, accounting for reads that map to multiple transcript isoforms.
- **Algorithm**: Uses expectation-maximization to assign multi-mapping reads to transcripts based on alignment scores and transcript lengths. Produces accurate abundance estimates even with complex transcriptomes.
- **Input Format**: Requires sorted BAM files aligned to a transcriptome reference. Can also accept read alignments in SAM format.
- **Output**: Produces tabular files with transcript identifiers, estimated counts, and normalized expression values (TPM, FPKM).
- **Use Case**: Gene expression analysis from dRNA-Seq data, isoform quantification, differential expression studies, and transcriptome profiling.

## Pitfalls

- **Transcriptome Reference**: Requires high-quality transcriptome annotations. Incomplete or incorrect annotations affect quantification accuracy.
- **Alignment Quality**: Accurate mapping is essential. Use aligners optimized for long reads (minimap2 with splice-aware settings).
- **Multi-mapping Reads**: EM algorithm assumptions may not hold for highly similar transcripts. Consider filtering near-identical isoforms.
- **Read Length**: Longer reads improve mapping specificity. Very short reads may map to multiple locations.
- **Strand Specificity**: dRNA-Seq is strand-specific. Ensure strand information is preserved during alignment.
- **Normalization**: Different normalization methods (TPM vs FPKM) produce different results. Choose appropriately for your analysis.

## Examples

### Basic abundance estimation
**Args:** `-i aligned.bam -o abundance.tsv`
**Explanation:** Standard NanoCount workflow. Estimates transcript abundance from alignments.

### Output TPM normalized values
**Args:** `-i aligned.bam -o abundance.tsv -t tpm`
**Explanation:** Outputs TPM (Transcripts Per Million) normalized expression values.

### Handle stranded data
**Args:** `-i aligned.bam -o abundance.tsv --stranded`
**Explanation:** Accounts for strand-specific dRNA-Seq data during quantification.

### Set minimum mapping quality
**Args:** `-i aligned.bam -o abundance.tsv -q 30`
**Explanation:** Filters out reads with mapping quality < 30 before quantification.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.

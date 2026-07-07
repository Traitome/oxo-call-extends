---
name: dirseq
category: expression
description: dirseq - Check RNA-seq read direction agreement with gene predictions.
tags: [dirseq, expression, rna-seq, strand, gene-direction]
author: oxo-call-community
source_url: "https://github.com/wwood/dirseq"
---

## Concepts

- **Tool Overview**: dirseq (v0.4.3+) is a tool for checking if RNA-seq reads agree with predicted gene direction.
- **Core Function**: Verifies strand specificity of RNA-seq data by comparing read orientation with gene annotations.
- **Input/Output**: Input: BAM files (aligned reads), GFF/GTF gene annotations. Output: Direction agreement statistics.
- **Algorithm**: Compares read alignment orientation with gene strand annotations.
- **Key Features**: Strand specificity check, direction agreement statistics, supports paired-end data, multiple annotation formats, visualization.
- **Installation**: `conda install -c bioconda dirseq`

## Pitfalls

- **Input Requirements**: Requires aligned BAM and gene annotation files.
- **Strand Protocol**: Must match library preparation protocol (stranded vs unstranded).
- **Alignment Quality**: Poor mapping affects direction inference.
- **Annotation Quality**: Incomplete annotations affect accuracy.
- **Paired-End Handling**: Proper handling of paired-end read orientation.

## Examples

### Check read direction agreement
**Args:** `dirseq --bam sample.bam --gff genes.gff --output dir_stats.tsv`
**Explanation:** Checks read direction agreement with gene predictions.

### Paired-end mode
**Args:** `dirseq --bam sample.bam --gff genes.gff --output dir_stats.tsv --paired`
**Explanation:** Process paired-end sequencing data.

### Generate visualization
**Args:** `dirseq --bam sample.bam --gff genes.gff --output dir_stats.tsv --plot direction.png`
**Explanation:** Generate visualization of direction agreement.

### Strand-specific protocol
**Args:** `dirseq --bam sample.bam --gff genes.gff --output dir_stats.tsv --strand reverse`
**Explanation:** Specify stranded library protocol.

### Batch processing
**Args:** `dirseq --bam-dir bam_files/ --gff genes.gff --output-dir results/`
**Explanation:** Process multiple BAM files in batch.
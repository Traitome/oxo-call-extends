---
name: corset
category: expression
description: Software for clustering de novo assembled transcripts and counting overlapping reads
tags: [corset, rna-seq, transcript-clustering, expression-quantification, de-novo-assembly]
author: oxo-call-community
source_url: "https://github.com/Oshlack/Corset/wiki"
---

## Concepts

- **Tool Overview**: Corset is a tool for clustering de novo assembled transcripts and counting overlapping reads, designed to improve transcript quantification accuracy.
- **Core Function**: Groups transcripts into clusters based on shared read support, reducing transcript redundancy and improving expression estimation.
- **Algorithm**: Uses graph-based clustering to group transcripts with overlapping read coverage.
- **Input**: Assembled transcripts (FASTA), mapped reads (BAM/SAM), or raw reads (FASTQ).
- **Output**: Cluster assignments, expression counts per cluster, filtered transcriptome.
- **Application**: RNA-seq analysis, transcript quantification, de novo assembly refinement.
- **Installation**: Install via bioconda: `conda install -c bioconda corset`

## Pitfalls

- **Assembly Quality**: Results depend on input assembly quality.
- **Read Mapping**: Requires properly mapped reads for accurate clustering.
- **Cluster Size**: Over-clustering may merge distinct transcripts.
- **Memory Usage**: Large transcriptomes may require significant memory.
- **Parameter Tuning**: May require adjustment of clustering parameters.

## Examples

### Cluster transcripts from BAM
**Args:** `corset -i mapped_reads.bam -t transcripts.fasta -o clusters.txt`
**Explanation:** Clusters transcripts based on read mapping.

### With raw reads
**Args:** `corset -r reads_1.fastq reads_2.fastq -t transcripts.fasta -o clusters.txt`
**Explanation:** Maps reads and clusters transcripts in one step.

### Generate expression matrix
**Args:** `corset -i sample1.bam sample2.bam -t transcripts.fasta -o expression/`
**Explanation:** Generates expression matrix for multiple samples.

### Filter low-expression clusters
**Args:** `corset -i mapped_reads.bam -t transcripts.fasta -m 10 -o clusters.txt`
**Explanation:** Filters clusters with fewer than 10 reads.

### Display help
**Args:** `corset --help`
**Explanation:** Shows all available options and usage information.
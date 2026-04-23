---
name: alfred
category: qc
description: BAM alignment statistics, feature counting and feature annotation for long and short read sequencing
tags: [bam, statistics, qc, feature-counting, alignment, annotation]
author: oxo-call-community
source_url: "https://github.com/tobiasrausch/alfred"
---

## Concepts

- **Tool Overview**: Alfred is a comprehensive tool for BAM alignment quality control, feature counting, and feature annotation supporting both long and short read sequencing data.
- **Core Function**: Computes alignment statistics, counts features, and annotates genomic features with interactive multi-sample visualization.
- **Input/Output**: Input: BAM files. Output: Statistics reports, feature counts, annotation files, interactive HTML reports.
- **Subcommands**: qc (quality control), count_dna/count_rna/count_jct (feature counting), annotate (feature annotation), tracks (track generation).
- **Installation**: Install via bioconda: `conda install -c bioconda alfred`

## Pitfalls

- **BAM Index**: Requires BAM files to be indexed (bai files) for efficient region-based operations.
- **Reference Needed**: Some features require reference genome FASTA for proper annotation.
- **Feature Types**: Different counting modes for DNA (genomic), RNA (transcriptomic), and junction reads.
- **Memory Usage**: Large BAM files may require significant memory - consider region-based processing.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available subcommands and general options.

### Run alignment QC
**Args:** `qc -i aligned.bam -o qc_report/`
**Explanation:** Generates comprehensive alignment quality control statistics and report.

### Count DNA features
**Args:** `count_dna -i aligned.bam -r features.bed -o counts.tsv`
**Explanation:** Counts reads overlapping genomic features from BED file.

### Count RNA features
**Args:** `count_rna -i aligned.bam -g annotation.gtf -o gene_counts.tsv`
**Explanation:** Counts reads per gene from RNA-seq alignment using GTF annotation.

### Count junction reads
**Args:** `count_jct -i aligned.bam -g junctions.bed -o junction_counts.tsv`
**Explanation:** Counts reads spanning splice junctions from RNA-seq data.

### Annotate variants
**Args:** `annotate -i variants.vcf -g annotation.gtf -r reference.fa -o annotated.vcf`
**Explanation:** Adds gene and functional annotations to VCF file.

### Generate browser tracks
**Args:** `tracks -i aligned.bam -o tracks/`
**Explanation:** Creates visualization tracks for genome browsers from BAM file.

### Multi-sample QC
**Args:** `qc -i sample1.bam sample2.bam sample3.bam -o multi_qc/`
**Explanation:** Generates comparative QC report across multiple samples.

### Pairwise alignment statistics
**Args:** `pwalign -i aligned.bam -o alignment_stats.tsv`
**Explanation:** Computes pairwise alignment statistics for comparative analysis.

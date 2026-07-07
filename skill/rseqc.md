---
name: rseqc
category: rna-seq
description: RSeQC (RNA-SeQC) is a comprehensive quality control package for RNA-seq data that evaluates sequence quality, GC bias, strand specificity, coverage uniformity, and transcript integrity.
tags: ["rseqc", "rna-seq", "quality-control", "qc", "strand-specificity", "gene-body-coverage"]
author: oxo-call-community
source_url: "https://rseqc.sourceforge.net/"
---

## Concepts

- **Tool Overview**: RSeQC (v5.0.4, Li Lab) is a Python-based RNA-seq quality control toolkit with modules for assessing sequencing quality, nucleotide composition, GC bias, strand specificity, coverage uniformity, and gene body coverage.
- **Core Function**: Provides over 20 QC modules covering basic sequence quality, RNA-seq specific metrics, and advanced analyses like junction annotation and read distribution across genome features.
- **Algorithm**: Combines statistical analysis with visualization. Uses BAM/SAM files for alignment-based metrics and FASTA/GTF for annotation-based analyses. Generates publication-quality plots.
- **Input Format**: BAM/SAM alignment files, GTF gene annotation files, FASTA reference sequences. Most modules accept multiple BAM files for batch processing.
- **Output Format**: Text reports with QC metrics, PDF/PNG plots, and BED/WIG files for genome browser visualization. Multi-sample heatmaps for gene body coverage comparison.
- **Use Case**: Quality control for RNA-seq experiments, identifying sequencing artifacts, assessing library quality, comparing samples before differential expression analysis.

## Pitfalls

- **Requires sorted BAM files**: Most modules require coordinate-sorted BAM files with index. Use `samtools sort` before running RSeQC.
- **GTF annotation must match genome build**: Mismatched annotations produce incorrect results. Use Ensembl or GENCODE annotations matching your reference genome.
- **Memory issues with large BAM files**: `geneBody_coverage.py` can consume >100GB RAM for human samples with >100M reads. Use `--split` option for large datasets.
- **Python 3 only**: RSeQC v3+ dropped Python 2 support. Use v2.6.5 for Python 2 environments.
- **Strand specificity detection requires known genes**: `infer_experiment.py` needs a GTF file with known gene annotations to infer library strandness.
- **Exon-exon junction detection limited**: `junction_annotation.py` relies on annotated junctions; novel junctions may not be properly classified.

## Examples

### Check sequencing quality
**Args:** `read_quality.py -i input.bam -o output_prefix`
**Explanation:** `-i` input BAM; `-o` output prefix. Generates quality score distribution, base composition, and duplication rate statistics.

### Assess strand specificity
**Args:** `infer_experiment.py -i input.bam -r genes.gtf -o output.txt`
**Explanation:** `-i` input BAM; `-r` gene annotation GTF. Determines if library is stranded or unstranded, critical for quantification tools like HTSeq-count.

### Evaluate gene body coverage
**Args:** `geneBody_coverage.py -i input.bam -r genes.gtf -o output_prefix`
**Explanation:** `-i` input BAM; `-r` gene annotation. Generates coverage profile across gene bodies (5' to 3'). Indicates 3' bias or degradation issues.

### Analyze read distribution
**Args:** `read_distribution.py -i input.bam -r genes.gtf`
**Explanation:** Reports percentage of reads mapping to exonic, intronic, and intergenic regions. High intronic reads may indicate DNA contamination.

### Identify splice junctions
**Args:** `junction_annotation.py -i input.bam -r genes.gtf -o output_prefix`
**Explanation:** Identifies and classifies splice junctions as annotated, novel, or cryptic. Outputs junction coordinates in BED format.

### Calculate inner distance
**Args:** `inner_distance.py -i input.bam -r genes.gtf -o output_prefix`
**Explanation:** Measures insert size distribution for paired-end reads. Important for library quality assessment and downstream analysis.

### Batch processing multiple samples
**Args:** `geneBody_coverage.py -i sample1.bam,sample2.bam,sample3.bam -r genes.gtf -o output_prefix`
**Explanation:** Accepts comma-separated BAM files for batch processing. Generates combined heatmap showing coverage profiles across all samples.
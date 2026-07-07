---
name: star-fusion
category: variant-calling
description: STAR-Fusion fusion variant caller for RNA-seq data.
tags: [star-fusion, fusion-calling, rna-seq, cancer]
author: oxo-call-community
source_url: "https://github.com/STAR-Fusion/STAR-Fusion/wiki"
---

## Concepts

- **Tool Overview**: star-fusion (v1.15.1) is a fast and accurate fusion gene detection tool for RNA sequencing data.
- **Core Function**: Identifies gene fusion events from RNA-seq reads using STAR aligner and custom filtering.
- **Algorithm**: Uses chimeric read detection from STAR alignment followed by rigorous filtering and annotation.
- **Input/Output**: Input: FASTQ reads or STAR-aligned BAM; Output: Fusion candidates with supporting evidence.
- **Annotation**: Integrates FusionInspector and FusionAnnotator for comprehensive fusion characterization.
- **Installation**: `conda install -c bioconda star-fusion` or download from GitHub.

## Pitfalls

- **Alignment Quality**: Poor alignment affects fusion detection accuracy.
- **Read Coverage**: Low coverage at fusion breakpoints may miss true fusions.
- **False Positives**: Transcriptional read-through and artifacts can produce false positive calls.
- **Memory Requirements**: Large datasets require significant memory for alignment.
- **Version Compatibility**: Requires specific STAR version for optimal performance.
- **Filtering Parameters**: Incorrect filtering thresholds affect sensitivity/specificity.

## Examples

### Display help
**Args:** `STAR-Fusion --help`
**Explanation:** Shows available options and usage information.

### Basic fusion calling
**Args:** `STAR-Fusion --left_fq read1.fastq --right_fq read2.fastq --genome_lib_dir genome_lib/ --output_dir results/`
**Explanation:** Detect fusion genes from paired-end RNA-seq reads.

### With pre-aligned BAM
**Args:** `STAR-Fusion --bam Aligned.out.bam --genome_lib_dir genome_lib/ --output_dir results/`
**Explanation:** Detect fusions from pre-aligned BAM file.

### With FusionInspector
**Args:** `STAR-Fusion --left_fq read1.fastq --right_fq read2.fastq --genome_lib_dir genome_lib/ --output_dir results/ --run_FusionInspector`
**Explanation:** Run FusionInspector for detailed fusion validation.

### With FusionAnnotator
**Args:** `STAR-Fusion --left_fq read1.fastq --right_fq read2.fastq --genome_lib_dir genome_lib/ --output_dir results/ --annotate`
**Explanation:** Annotate fusion genes with FusionAnnotator.

### Custom filters
**Args:** `STAR-Fusion --left_fq read1.fastq --right_fq read2.fastq --genome_lib_dir genome_lib/ --output_dir results/ --min_junction_reads 5`
**Explanation:** Set minimum junction reads threshold to 5.

### Verbose mode
**Args:** `STAR-Fusion --left_fq read1.fastq --right_fq read2.fastq --genome_lib_dir genome_lib/ --output_dir results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Build genome library
**Args:** `STAR-Fusion --create_genome_lib --genome_fasta ref.fasta --gtf ref.gtf --output_dir genome_lib/`
**Explanation:** Build genome library for fusion calling.

### Batch processing
**Args:** `STAR-Fusion --batch samples.txt --genome_lib_dir genome_lib/ --output_dir results/`
**Explanation:** Process multiple samples from batch file.

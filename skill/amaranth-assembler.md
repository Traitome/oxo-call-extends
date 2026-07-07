---
name: amaranth-assembler
category: expression
description: Reference-based transcriptome assembler optimized for single-cell RNA-seq data
tags: [amaranth-assembler, RNA-seq, single-cell, transcriptome, assembly, expression]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/amaranth"
---

## Concepts

- **Tool Overview**: Amaranth is a reference-based transcript assembler specifically optimized for single-cell RNA-seq data, developed based on the Scallop2/Scallop assembler series.
- **Core Function**: Assembles full-length transcripts from single-cell RNA-seq reads aligned to a reference genome, handling the unique challenges of scRNA-seq data including low coverage, high dropout rates, and UMI-based quantification.
- **Input/Output**: Inputs: sorted BAM file of aligned reads, reference genome/transcriptome; Outputs: assembled transcripts in FASTA format, GTF annotation file, and expression quantification.
- **Installation**: Available via Bioconda (`conda install -c bioconda amaranth-assembler`) or from source (requires Boost and htslib dependencies).
- **Features**: UMI-aware assembly, efficient handling of low-coverage data, support for both plate-based and droplet-based scRNA-seq protocols, and integration with existing transcript quantification tools.

## Pitfalls

- **BAM File Requirements**: Input BAM must be sorted by coordinate; unsorted BAM files will cause errors.
- **Reference Genome**: Ensure reference genome matches the alignment reference; mismatched references lead to incorrect assemblies.
- **Memory Requirements**: Large genomes or datasets may require significant memory; consider using the `--memory-efficient` mode if available.
- **UMI Processing**: Requires UMI information in read names or tags; ensure proper UMI extraction before alignment.
- **Annotation Compatibility**: Output GTF may require post-processing for compatibility with certain downstream tools.

## Examples

### Basic transcript assembly
**Args:** `amaranth -i aligned_reads.bam -o output_dir -g genome.fasta -a annotation.gtf`
**Explanation:** Assembles transcripts from aligned BAM file using the provided genome and annotation.

### With UMI support
**Args:** `amaranth -i aligned_reads.bam -o output_dir -g genome.fasta --umi-tag UB`
**Explanation:** Processes UMI-tagged reads using the UB tag to improve assembly accuracy for scRNA-seq data.

### Assembly with strand-specific data
**Args:** `amaranth -i aligned_reads.bam -o output_dir -g genome.fasta --strand-specific RF`
**Explanation:** Handles strand-specific sequencing data with RF orientation (forward reads reverse-stranded).

### Generate expression estimates
**Args:** `amaranth -i aligned_reads.bam -o output_dir -g genome.fasta --quant`
**Explanation:** Performs transcript assembly and generates quantification estimates in a single run.

### Memory-efficient mode for large datasets
**Args:** `amaranth -i aligned_reads.bam -o output_dir -g genome.fasta --memory-efficient`
**Explanation:** Uses memory-efficient algorithms for processing large genomes or high-depth sequencing data.
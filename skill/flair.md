---
name: flair
category: utility
description: "FLAIR is a computational tool for correcting, defining isoforms, and analyzing alternative splicing from noisy long-read sequencing data (ONT and PacBio)."
tags: [flair, utility, long-read, isoforms, splicing, alternative-splicing, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BrooksLabUCSC/flair"
---

## Concepts
- **Tool Overview**: FLAIR (Full-Length Alternative Isoform analysis of RNA) processes noisy long-read sequencing data from Oxford Nanopore Technologies and PacBio to identify and quantify alternative splicing events.
- **Core Function**: Corrects sequencing errors, clusters reads into isoforms, and identifies alternative splicing patterns from long-read RNA-Seq data.
- **Multi-step Pipeline**: Consists of five main modules: align, correct, collapse, quantify, and differential. Each step processes data sequentially.
- **Error Correction**: Uses short-read RNA-Seq data or reference-guided approach to correct systematic errors in long reads.
- **Isoform Collapse**: Groups similar reads into unique isoforms using sequence similarity thresholds and splice junction patterns.
- **Splicing Analysis**: Identifies alternative splicing events including skipped exons, retained introns, alternative 5'/3' splice sites, and mutually exclusive exons.
- **Installation**: `conda install -c bioconda flair` or clone from GitHub. Requires Python 3.x, minimap2, samtools, pysam.

## Pitfalls
- **Short-Read Requirement**: Error correction step requires matching short-read RNA-Seq data or high-quality reference transcriptome.
- **Genome Alignment Quality**: Poor genome alignment produces incorrect splice junction calls. Use minimap2 with appropriate settings.
- **Isoform Overcollapsing**: Stringent thresholds may merge distinct isoforms. Adjust similarity thresholds based on data quality.
- **Memory Usage**: Processing large datasets requires significant memory. Consider splitting by chromosome for large genomes.
- **ONT vs PacBio**: Different error profiles require different parameter tuning. Adjust error correction for specific platform.
- **Splice Site Annotation**: Requires comprehensive splice site annotation for accurate alternative splicing classification.

## Examples
### Run complete FLAIR pipeline
**Args:** `flair.py full --reads sample.fastq --genome genome.fa --annotation gtf.gtf --outdir results/`
**Explanation:** Runs complete FLAIR pipeline from alignment to differential splicing analysis.

### Align long reads to genome
**Args:** `flair.py align --reads sample.fastq --genome genome.fa --output sample.bam`
**Explanation:** Aligns ONT/PacBio reads to reference genome using minimap2 with splice-aware settings.

### Correct sequencing errors
**Args:** `flair.py correct --reads sample.bam --shortreads shortreads.fastq --genome genome.fa --output corrected.bam`
**Explanation:** Corrects long-read sequencing errors using matching short-read RNA-Seq data.

### Collapse reads into isoforms
**Args:** `flair.py collapse --reads corrected.bam --genome genome.fa --annotation gtf.gtf --output isoforms.fasta`
**Explanation:** Groups corrected reads into unique isoforms and generates consensus sequences.

### Quantify isoform expression
**Args:** `flair.py quantify --reads sample.bam --isoforms isoforms.fasta --output quantification.txt`
**Explanation:** Quantifies isoform expression levels from aligned reads using expectation-maximization.

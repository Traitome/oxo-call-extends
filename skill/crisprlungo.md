---
name: crisprlungo
category: genome-editing
description: Long-read sequencing analysis pipeline for CRISPR genome editing validation supporting base editors and prime editors
tags: [crisprlungo, CRISPR, long-read, nanopore, amplicon, base-editor, prime-editor, indel, nCATS, UMI]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPRlungo"
---

## Concepts

- **Tool Overview**: CRISPRLungo (v0.1.14+) - A software pipeline designed to analyze genome editing outcomes using long-read sequencing data (Oxford Nanopore, PacBio).
- **Core Function**: Aligns long reads to reference, filters low-quality and chimeric reads, quantifies indels/inversions, and classifies allele groups using the CRISPRLungoAllele submodule.
- **Algorithm**: (1) Align sequencing reads to reference genome. (2) Filter low-quality reads and remove chimeric reads. (3) Cluster UMI-tagged reads and generate consensus (if UMIs present). (4) Perform background error filtering using control samples. (5) Quantify small/large indels and inversions. (6) Classify allele groups and identify PCR-induced chimeras.
- **Input**: Long-read FASTQ files (Oxford Nanopore or PacBio), reference genome (FASTA), amplicon coordinates, optional UMI sequences, optional control samples.
- **Output**: Allele frequency tables, indel distribution plots, chimeric read identification, quality metrics.
- **Application**: CRISPR validation with long amplicons, base editor analysis, prime editor validation, large indel detection, multiplexed gRNA screening.
- **Installation**: `pip install CRISPRLungo` or `conda install -c bioconda crisprlungo`

## Pitfalls

- **Long Amplicon Required**: Designed for long amplicon sequencing (>600bp); short reads may not work well.
- **Chimeric Reads**: Library preparation can generate chimeric reads; CRISPRLungoAllele submodule identifies these.
- **UMI Handling**: If using UMI-tagged sequencing, ensure proper UMI extraction and clustering.
- **Control Samples**: Background error filtering requires control (unedited) samples for accurate quantification.
- **Quality Filtering**: Adjust quality thresholds based on sequencing platform; Nanopore has higher error rates than PacBio.

## Examples

### Basic long-read CRISPR analysis
**Args:** `crisprlungo -i reads.fastq -r reference.fa -o output/`
**Explanation:** Analyze CRISPR editing outcomes from Oxford Nanopore or PacBio reads aligned to reference.

### Paired-end long amplicon analysis
**Args:** `crisprlungo -i reads_R1.fastq reads_R2.fastq -r reference.fa -o output/`
**Explanation:** Process paired-end long amplicon sequencing data for CRISPR editing detection.

### With UMI-tagged reads
**Args:** `crisprlungo -i reads.fastq -r reference.fa --umi --umi-prefix umi.txt -o output/`
**Explanation:** Process UMI-tagged long reads for increased accuracy in allele quantification.

### With control sample for background filtering
**Args:** `crisprlungo -i edited.fastq -r reference.fa --control control.fastq -o output/`
**Explanation:** Use unedited control sample to filter background sequencing errors for more accurate editing quantification.

### Specify target region
**Args:** `crisprlungo -i reads.fastq -r reference.fa -b target_regions.bed -o output/`
**Explanation:** Focus analysis on specific target regions defined in BED file rather than whole genome.

### Base editor analysis
**Args:** `crisprlungo -i reads.fastq -r reference.fa --base-editor -o output/`
**Explanation:** Analyze base editor outcomes including specific nucleotide conversions at target sites.

### Prime editor analysis
**Args:** `crisprlungo -i reads.fastq -r reference.fa --prime-editor -o output/`
**Explanation:** Quantify prime editing outcomes including intended edits and pegRNA-mediated insertions.

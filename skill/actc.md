---
name: actc
category: alignment
description: PacBio utility to align continuous long reads (CLR) to circular consensus sequencing (CCS) reads
tags: [pacbio, clr, ccs, alignment, long-reads]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/actc"
---

## Concepts

- **Tool Overview**: ACTC is a PacBio utility that aligns continuous long reads (CLR) to circular consensus sequencing (CCS/HiFi) reads for quality assessment and read comparison.
- **Core Function**: Aligns CLR subreads to their corresponding CCS reads, enabling evaluation of CCS accuracy and identification of discrepancies.
- **Input/Output**: Input: PacBio BAM files containing CLR and CCS reads. Output: Aligned BAM file and alignment statistics.
- **PacBio Data Types**: Works with PacBio SMRT sequencing data containing both CLR and CCS reads from the same molecules.
- **Installation**: Install via bioconda: `conda install -c bioconda actc`

## Pitfalls

- **Input Requirements**: Requires PacBio BAM format with both CLR and CCS reads - standard FASTQ conversion loses necessary metadata.
- **CCS Generation**: CCS reads must be generated first using the `ccs` tool before running ACTC.
- **Memory Usage**: Large PacBio datasets may require significant memory for alignment.
- **Output Format**: Output BAM uses special tags to indicate CLR-to-CCS alignment relationships.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and parameters for ACTC alignment.

### Basic CLR to CCS alignment
**Args:** `input.subreads.bam input.ccs.bam output.bam`
**Explanation:** Aligns CLR subreads to CCS reads, producing alignment BAM file.

### Alignment with minimum accuracy
**Args:** `--min-accuracy 0.99 subreads.bam ccs.bam output.bam`
**Explanation:** Only reports alignments where CCS accuracy is at least 99%.

### Generate alignment statistics
**Args:** `--stats subreads.bam ccs.bam output.bam`
**Explanation:** Produces detailed alignment statistics including accuracy metrics.

### Specify number of threads
**Args:** `--threads 8 subreads.bam ccs.bam output.bam`
**Explanation:** Uses 8 threads for parallel alignment processing.

### Filter by read length
**Args:** `--min-length 500 subreads.bam ccs.bam output.bam`
**Explanation:** Only aligns reads with minimum length of 500bp.

### Output in SAM format
**Args:** `--output-format SAM subreads.bam ccs.bam output.sam`
**Explanation:** Outputs alignment in SAM format instead of BAM for text inspection.

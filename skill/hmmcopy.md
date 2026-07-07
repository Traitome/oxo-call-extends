---
name: hmmcopy
category: coverage
description: C++ based programs for analyzing BAM files and preparing read counts -- used with bioconductor-hmmcopy for copy number analysis.
tags: [hmmcopy, coverage, copy-number, BAM, GC-bias, mappability, CNA]
author: oxo-call-community
source_url: "http://compbio.bccrc.ca/software/hmmcopy"
---

## Concepts

- **Tool Overview**: hmmcopy (v0.1.1) provides C++ utilities for analyzing BAM files and generating read count data for copy number variation analysis. It works as a preprocessing step for the Bioconductor HMMcopy package, preparing coverage data by counting reads in non-overlapping genomic windows.

- **Read Count Generation**: The tool scans BAM files and counts reads falling within fixed-size genomic windows. It supports configurable window sizes (typically 100bp-10kb) and provides raw coverage metrics that form the basis for downstream copy number estimation.

- **GC Bias Correction**: hmmcopy incorporates GC content bias correction, adjusting read counts based on the GC composition of each window. Regions with extreme GC content (very high or very low) often have biased coverage due to sequencing chemistry.

- **Mappability Correction**: The tool applies mappability correction to account for regions of the genome that are difficult to map due to repetitive sequences or low complexity. This helps reduce false copy number calls in these problematic regions.

- **Input/Output Formats**: hmmcopy accepts sorted and indexed BAM files as input. Output is typically in a tab-delimited format containing chromosome, start position, end position, read count, GC content, and mappability score for each window.

- **Integration with HMMcopy**: The C++ utilities generate input files for the Bioconductor HMMcopy R package, which uses hidden Markov models to segment the genome and call copy number alterations from the processed read counts.

## Pitfalls

- **BAM File Requirements**: Input BAM files must be sorted and indexed. Unsorted BAMs will produce incorrect read counts. Always verify BAM preparation with `samtools index`.

- **Window Size Selection**: Window size significantly affects resolution. Smaller windows (100bp-1kb) provide higher resolution but increased noise; larger windows (5kb-10kb) smooth noise but reduce breakpoint detection sensitivity.

- **Reference Genome Consistency**: GC content and mappability files must match the reference genome used for alignment. Mismatched references will produce invalid bias corrections.

- **Coverage Thresholds**: Low-coverage samples may not provide reliable copy number estimates. Typically requires >30x coverage for WGS or >100x for targeted sequencing.

- **PCR Duplicates**: Failure to mark or remove PCR duplicates can artificially inflate read counts, leading to false positive copy gain calls. Use tools like Picard or samtools to mark duplicates before running hmmcopy.

- **Tumor-Normal Matching**: When comparing tumor and normal samples, ensure both were processed with the same window size and reference genome for valid comparison.

## Examples

### Generate read counts from BAM file
**Args:** `hmmcopy-readcounter -w 1000 -o output_counts.txt input.bam`
**Explanation:** Generates read counts in 1000bp windows from input BAM file. Output contains chromosome, start, end, read count, GC content, and mappability for each window.

### Run with custom window size
**Args:** `hmmcopy-readcounter -w 5000 -o output_5kb.txt tumor.bam`
**Explanation:** Uses 5000bp windows for lower resolution but smoother coverage profile. Suitable for samples with lower coverage or when large-scale copy number events are the focus.

### Process multiple BAM files
**Args:** `for bam in *.bam; do hmmcopy-readcounter -w 1000 -o ${bam%.bam}_counts.txt $bam; done`
**Explanation:** Batch processes all BAM files in a directory, generating separate count files for each sample with the same window size.

### Generate GC content file for reference
**Args:** `hmmcopy-gc -w 1000 -o hg19_gc.txt hg19.fa`
**Explanation:** Precomputes GC content for 1000bp windows across the hg19 reference genome. This file is used during bias correction in read counting.

### Generate mappability file
**Args:** `hmmcopy-mappability -w 1000 -o hg19_mappability.txt hg19.fa`
**Explanation:** Creates mappability scores for each window based on how uniquely mappable each region is. Low mappability regions are flagged for filtering.

### Run with GC and mappability correction
**Args:** `hmmcopy-readcounter -w 1000 -g hg19_gc.txt -m hg19_mappability.txt -o corrected_counts.txt tumor.bam`
**Explanation:** Applies both GC content and mappability corrections during read counting, producing more accurate coverage estimates for downstream HMM analysis.

### Prepare input for HMMcopy R package
**Args:** `hmmcopy-readcounter -w 1000 -g hg19_gc.txt -m hg19_mappability.txt -o tumor_counts.wig tumor.bam`
**Explanation:** Generates WIG format output compatible with the Bioconductor HMMcopy package. The WIG file can be directly imported into R for hidden Markov model-based copy number segmentation.
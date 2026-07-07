---
name: intron-prospector
category: rna-seq
description: Identify putative introns from RNA-Seq alignments of short and long reads
tags: [intron-prospector, rna-seq, intron, splicing, long-reads, alignments]
author: oxo-call-community
source_url: "https://github.com/diekhans/intron-prospector"
---

## Concepts

- **Tool Overview**: Intron-Prospector (v1.5.0) is a bioinformatics tool for identifying putative introns from RNA-Seq alignments. It supports both short-read (Illumina) and long-read (PacBio/ONT) sequencing data, enabling comprehensive analysis of splicing patterns.

- **Intron Detection**: Identifies splice junctions by analyzing alignment gaps in BAM files. Supports canonical (GT-AG, GC-AG, AT-AC) and non-canonical splice sites.

- **Long-Read Support**: Specifically designed to handle long-read RNA-Seq data, which can span entire introns and provide more complete splice junction information compared to short reads.

- **Splice Site Validation**: Validates detected introns against known annotations (GTF/GFF) and can identify novel splice junctions not present in reference databases.

- **Output Formats**: Generates BED files for detected introns, along with detailed statistics and quality metrics for each identified splice junction.

- **Quality Filtering**: Implements filters based on read support, splice site consensus, and alignment quality to reduce false positive intron calls.

## Pitfalls

- **Alignment Quality Dependency**: Results depend heavily on the quality of input BAM files. Poorly aligned reads may produce false intron calls.

- **Reference Genome Compatibility**: Ensure BAM files are aligned to the same reference genome version used for annotation. Mismatched genomes cause coordinate errors.

- **Short Read Limitations**: Short reads may not span entire introns, leading to incomplete splice junction identification. Long reads are recommended for comprehensive intron detection.

- **Novel Intron Validation**: Detected novel introns require experimental validation (e.g., RT-PCR). Computational predictions alone are not sufficient for confirmation.

- **Memory Usage**: Processing large BAM files requires significant memory. Consider splitting large datasets or using subsetting options.

- **Alternative Splicing Complexity**: The tool reports all detected introns but does not distinguish between alternative splicing events without additional analysis.

## Examples

### Basic intron detection from BAM file
**Args:** `intron-prospector --bam sample.bam --genome hg38 --output introns.bed`
**Explanation:** Identifies introns from aligned RNA-Seq reads and outputs detected splice junctions in BED format.

### Include known annotations
**Args:** `intron-prospector --bam sample.bam --gtf genes.gtf --genome hg38 --output introns_with_annot.bed`
**Explanation:** Compares detected introns against known gene annotations and flags novel vs. known splice junctions.

### Long-read specific mode
**Args:** `intron-prospector --bam long_reads.bam --long-reads --min-read-length 1000 --output long_read_introns.bed`
**Explanation:** Optimizes detection parameters for long-read data, requiring minimum read length of 1000bp.

### Filter by read support
**Args:** `intron-prospector --bam sample.bam --min-support 5 --output high_confidence_introns.bed`
**Explanation:** Only reports introns supported by at least 5 reads, reducing false positives but potentially missing rare events.

### Generate statistics report
**Args:** `intron-prospector --bam sample.bam --stats --output introns.bed`
**Explanation:** Produces additional statistics file with intron counts, splice site types, and coverage metrics.

### Validate against reference annotations
**Args:** `intron-prospector --bam sample.bam --gtf ref_annot.gtf --validate --output validated_introns.bed`
**Explanation:** Validates detected introns against reference annotations and outputs only validated splice junctions.
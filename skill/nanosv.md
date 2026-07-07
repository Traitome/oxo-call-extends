---
name: nanosv
category: variant-calling
description: NanoSV is a structural variation detection tool specifically designed for Oxford Nanopore sequencing data.
tags: [nanosv, variant-calling, structural-variation, nanopore, sv]
author: oxo-call-community
source_url: "https://github.com/mroosmalen/nanosv"
---

## Concepts

- **Tool Overview**: NanoSV v1.2.4 is a specialized structural variant caller for Oxford Nanopore long-read sequencing data.
- **Core Function**: Detects various types of structural variants including deletions, insertions, inversions, and translocations.
- **Algorithm**: Uses split-read and read-pair approaches to identify structural variations from aligned reads.
- **Input Format**: Requires coordinate-sorted and indexed BAM files from Nanopore alignments.
- **Output**: Produces VCF files with structural variant calls and supporting evidence information.
- **Use Case**: Detecting structural variants in human genomes, cancer genomics, and population genetics studies.

## Pitfalls

- **Alignment Quality**: SV detection accuracy depends heavily on alignment quality.
- **Reference Bias**: May miss variants in poorly assembled or repetitive genomic regions.
- **False Positives**: Can produce false positives in regions with low mapping quality.
- **Memory Requirements**: Processing large genomes requires significant memory resources.
- **Version Compatibility**: Output formats may vary between versions.
- **Filtering Needs**: Raw calls require quality filtering and manual curation.

## Examples

### Display help
**Args:** `nanosv --help`
**Explanation:** Shows available options and usage instructions.

### Basic SV detection
**Args:** `nanosv -b aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Detects structural variants from Nanopore alignments.

### Custom minimum size
**Args:** `nanosv -b aligned.bam -r ref.fasta -m 50 -o variants.vcf`
**Explanation:** Sets minimum SV size to 50bp for detection.

### With quality filtering
**Args:** `nanosv -b aligned.bam -r ref.fasta -q 20 -o filtered.vcf`
**Explanation:** Filters variants with minimum mapping quality of Q20.

### Output BED format
**Args:** `nanosv -b aligned.bam -r ref.fasta --bed -o variants.bed`
**Explanation:** Outputs structural variants in BED format instead of VCF.

### Parallel processing
**Args:** `nanosv -b aligned.bam -r ref.fasta -t 8 -o variants.vcf`
**Explanation:** Uses 8 threads for parallel variant calling.
---
name: naibr-plus
category: variant-calling
description: NAIBR-plus - Identify novel adjacencies from structural variations using linked-read data
tags: [naibr-plus, variant-calling, structural-variation, linked-reads, novel-adjacency, 10x]
author: oxo-call-community
source_url: "https://github.com/pontushojer/NAIBR"
---

## Concepts

- **Tool Overview**: NAIBR+ v0.5.4 (Novel Adjacency Identification in Linked-Reads) identifies structural variant breakpoints and novel genomic adjacencies from 10x Genomics linked-read sequencing data.
- **Core Function**: Detects deletions, inversions, duplications, and translocations by identifying read pairs that span breakpoints. Leverages linked-read barcodes to phased assembly of breakpoint-spanning reads.
- **Algorithm**: Uses barcoded read clouds to physically phase variants and identify novel adjacencies that are not present in the reference genome but occur in the sample due to structural variations.
- **Input Format**: Requires sorted and indexed BAM files from 10x Genomics linked-read sequencing aligned to a reference genome, along with the reference FASTA file.
- **Output**: Produces VCF and/or TSV files containing called structural variants with breakpoint coordinates, supporting read counts, and phasing information.
- **Use Case**: Cancer genomics structural variant detection, population genetics of structural variations, and Linked-Read analysis for de novo assembly improvement.

## Pitfalls

- **Linked-Read Requirement**: Only works with 10x Genomics linked-read data. Standard short-read data is not compatible.
- **Barcoding Quality**: Poor barcode assignment or low barcode diversity reduces sensitivity. Validate library quality before sequencing.
- **Reference Quality**: Assemblies with many contigs or gaps produce fragmented SV calls. Use high-quality references.
- **Breakpoint Precision**: SV breakpoints are called within Linked-Read resolution (typically within 1-2kb). Fine-mapping may require dedicated validation.
- **Duplicate Filtering**: Avoid duplicate removal before running NAIBR+, as barcoded duplicates carry useful phasing information.
- **VCF Annotation**: Output VCFs may need additional annotation for functional interpretation of SVs.

## Examples

### Basic novel adjacency detection
**Args:** `-b aligned.bam -r reference.fasta -o output_dir`
**Explanation:** Standard NAIBR+ workflow. Analyzes linked-read BAM and calls structural variants.

### Specify output format
**Args:** `-b sample.bam -r ref.fa -o results/ -f vcf`
**Explanation:** Outputs results in VCF format for compatibility with downstream variant tools.

### Set minimum barcode count
**Args:** `-b reads.bam -r genome.fa -o sv_calls/ -bc 10`
**Explanation:** Requires at least 10 reads with the same barcode supporting a call to reduce false positives.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.

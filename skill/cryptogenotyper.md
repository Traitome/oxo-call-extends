---
name: cryptogenotyper
category: variant-calling
description: Tool to subtype the parasite Cryptosporidium based on the 18S and gp60 markers.
tags: [cryptogenotyper, variant-calling, Cryptosporidium, subtyping, parasitology]
author: oxo-call-community
source_url: "https://github.com/phac-nml/CryptoGenotyper"
---

## Concepts

- **Tool Overview**: cryptogenotyper (v1.5.0+) is a bioinformatics tool designed for subtyping the parasitic protozoan Cryptosporidium using two key genetic markers: 18S rRNA and gp60. It provides a streamlined workflow for analyzing sequencing data and assigning specific subtypes.
- **Core Function**: Identifies and subtypes Cryptosporidium species from sequencing reads by comparing against reference sequences of the 18S and gp60 loci. Supports both Illumina and Sanger sequencing data.
- **Input/Output**: Input: FASTA/FASTQ reads or aligned BAM files. Output: Subtype assignments, genotype reports, and variant calls in VCF format.
- **Algorithm**: Uses BLAST-based alignment to identify marker sequences, followed by phylogenetic analysis to determine subtype classification.
- **Key Features**: Automated subtype calling, supports multiple sequencing platforms, provides comprehensive reporting, and includes reference databases for known Cryptosporidium subtypes.
- **Installation**: `conda install -c bioconda cryptogenotyper`

## Pitfalls

- **Input Quality**: Requires high-quality sequencing data for accurate subtype assignment.
- **Marker Coverage**: Incomplete coverage of 18S or gp60 markers may lead to ambiguous results.
- **Reference Database**: Results depend on the completeness of the reference database.
- **Mixed Infections**: May struggle with mixed Cryptosporidium infections in samples.
- **Version Compatibility**: Database formats may change between versions.

## Examples

### Subtype from FASTQ reads
**Args:** `-i reads.fastq -r reference.fasta -o output/`
**Explanation:** Analyze sequencing reads and generate subtype report.

### Analyze aligned BAM file
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads and determine subtype.

### Display help
**Args:** `--help`
**Explanation:** Shows available options and parameters.
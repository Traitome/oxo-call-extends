---
name: clever-toolkit
category: variant-calling
description: CLEVER Toolkit for discovering and genotyping insertions and deletions from paired-end reads
tags: [clever-toolkit, variant-calling, indels, structural-variants, bioinformatics]
author: oxo-call-community
source_url: "https://bitbucket.org/tobiasmarschall/clever-toolkit/wiki/Home"
---

## Concepts

- **Tool Overview**: The CLEVER Toolkit is a suite of tools for analyzing next-generation sequencing data, with a focus on discovering and genotyping insertions and deletions from paired-end reads.
- **Core Function**: Detects and genotypes structural variants, particularly insertions and deletions, from aligned sequencing data.
- **Algorithm**: Uses paired-end read mapping and split-read analysis for variant detection.
- **Input**: Aligned BAM/SAM files and reference genome (FASTA).
- **Output**: VCF file with insertion and deletion calls.
- **Application**: Structural variant analysis, genome variation studies, and population genetics.
- **Installation**: Install via bioconda: `conda install -c bioconda clever-toolkit`

## Pitfalls

- **Data Quality**: Requires high-quality aligned reads for accurate variant calling.
- **Reference Genome**: Must match the reference used for alignment.
- **Computational Resources**: May require significant memory for large datasets.
- **Complex Variants**: May have difficulty with complex structural variants.
- **False Positives**: May detect false variants from mapping artifacts.

## Examples

### Call indels from BAM
**Args:** `clever -i alignments.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls insertions and deletions from aligned paired-end reads.

### With quality filtering
**Args:** `clever -i alignments.bam -r reference.fasta -q 30 -o variants.vcf`
**Explanation:** Filters variants by quality score >= 30.

### Genotype variants
**Args:** `clever-genotype -i alignments.bam -v variants.vcf -o genotyped.vcf`
**Explanation:** Genotypes detected variants from aligned reads.

### Display help
**Args:** `clever --help`
**Explanation:** Shows all available options and usage information.
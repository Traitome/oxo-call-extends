---
name: sat-bsa
category: variant-calling
description: Sat-BSA package for local de novo assembly and structural variant identification
tags: ["sat-bsa", "variant-calling", "de-novo-assembly", "BSA"]
author: oxo-call-community
source_url: "https://github.com/SegawaTenta/Sat-BSA"
---

## Concepts

- **Tool Overview**: Sat-BSA (v1.12) is a bioinformatics package for applying local de novo assembly and identifying structural variants in the assembled regions from bulked segregant analysis data.
- **Core Function**: Performs local assembly of reads around candidate regions and detects structural variants including deletions, insertions, and inversions.
- **Algorithm**: Combines read mapping, local assembly, and variant calling to identify genomic differences between bulked populations.
- **BSA Integration**: Specifically designed for Bulked Segregant Analysis to identify causal variants in genetic mapping experiments.
- **Input/Output**: Accepts BAM files and reference genomes, produces VCF files with structural variant calls.
- **Applications**: Genetic mapping, QTL analysis, and identification of causal variants in segregating populations.

## Pitfalls

- **Read Depth Requirements**: Requires sufficient sequencing depth for reliable variant detection.
- **Reference Genome Quality**: Results depend on the quality and completeness of the reference genome.
- **Complex Regions**: May struggle with repetitive or highly polymorphic genomic regions.
- **False Positives**: May report false structural variants in regions with mapping artifacts.
- **Computational Resources**: Local assembly can be computationally intensive for large genomes.
- **Parameter Tuning**: Requires careful adjustment of assembly and variant calling parameters.

## Examples

### Basic variant calling
**Args:** `sat-bsa -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** `-i` input BAM file; `-r` reference genome; `-o` output VCF with structural variants.

### Targeted region analysis
**Args:** `sat-bsa -i aligned.bam -r reference.fasta -t chr1:100000-200000 -o targeted.vcf`
**Explanation:** `-t` specifies target region for focused analysis.

### With quality filtering
**Args:** `sat-bsa -i aligned.bam -r reference.fasta -q 20 -o filtered.vcf`
**Explanation:** `-q 20` filters variants with quality score below 20.

### Assembly with custom k-mer
**Args:** `sat-bsa -i aligned.bam -r reference.fasta -k 31 -o variants.vcf`
**Explanation:** `-k 31` sets k-mer size to 31 for local assembly.

### Batch processing
**Args:** `sat-bsa -i ./bam_files/ -r reference.fasta -o ./results/ -b`
**Explanation:** `-b` batch mode for processing multiple BAM files.

### Verbose output
**Args:** `sat-bsa -i aligned.bam -r reference.fasta -v -o variants.vcf`
**Explanation:** `-v` enables verbose logging for debugging.

### Generate assembly contigs
**Args:** `sat-bsa -i aligned.bam -r reference.fasta --assembly -o contigs.fasta`
**Explanation:** `--assembly` outputs assembled contigs along with variant calls.
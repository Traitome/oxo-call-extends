---
name: srst2
category: typing
description: Short Read Sequence Typing for Bacterial Pathogens.
tags: [srst2, bacterial-typing, mlst, antibiotic-resistance]
author: oxo-call-community
source_url: "https://github.com/katholt/srst2"
---

## Concepts

- **Tool Overview**: srst2 (v0.2.0) is a tool for in silico typing of bacterial pathogens from short-read sequencing data.
- **Core Function**: Identifies MLST (Multi-Locus Sequence Typing) alleles, antibiotic resistance genes, and virulence factors.
- **Database Integration**: Uses BLAST-based approach to query against curated databases of known sequences.
- **Input/Output**: Input: FASTQ reads or BAM files; Output: Typing results, allele calls, and resistance profiles.
- **MLST Support**: Works with PubMLST databases for species identification and strain typing.
- **Installation**: `conda install -c bioconda srst2` or `pip install srst2`.

## Pitfalls

- **Database Selection**: Using incorrect species database leads to false typing results.
- **Read Coverage**: Low coverage regions may cause incomplete allele calls.
- **Assembly Quality**: Poor assembly affects typing accuracy; use high-quality reads.
- **Allele Variants**: Novel alleles not in database may be missed or misclassified.
- **Mixed Infections**: Mixed populations can produce ambiguous typing results.
- **Version Compatibility**: Database format changes between versions may break compatibility.

## Examples

### Display help
**Args:** `srst2 --help`
**Explanation:** Shows available options and usage information.

### Basic MLST typing
**Args:** `srst2 --input_pe reads_1.fastq reads_2.fastq --output results --mlst_db ecoli_mlst.fasta`
**Explanation:** Perform MLST typing on paired-end reads.

### Single-end reads
**Args:** `srst2 --input_se reads.fastq --output results --mlst_db salmonella_mlst.fasta`
**Explanation:** Type single-end sequencing data.

### Resistance gene detection
**Args:** `srst2 --input_pe r1.fastq r2.fastq --output results --resistance_db resfinder.fasta`
**Explanation:** Identify antibiotic resistance genes from sequencing data.

### Combined MLST and resistance
**Args:** `srst2 --input_pe r1.fastq r2.fastq --output results --mlst_db ecoli_mlst.fasta --resistance_db resfinder.fasta`
**Explanation:** Perform both MLST typing and resistance gene detection.

### With BAM input
**Args:** `srst2 --input_bam sample.bam --output results --mlst_db mlst_db.fasta`
**Explanation:** Type pre-aligned BAM file.

### Verbose output
**Args:** `srst2 --input_pe r1.fastq r2.fastq --output results --mlst_db mlst.fasta --verbose`
**Explanation:** Run with verbose output for debugging.

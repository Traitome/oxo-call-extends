---
name: seqsero2
category: typing
description: seqsero2 - Salmonella serotype prediction from genome sequencing data
tags: ["seqsero2", "typing", "Salmonella", "serotyping"]
author: oxo-call-community
source_url: "https://github.com/denglab/SeqSero2"
---

## Concepts

- **Tool Overview**: seqsero2 (v1.3.2) predicts Salmonella serotype from genome sequencing data.
- **Core Function**: Determines Salmonella serotype using genomic data.
- **Algorithm**: Uses sequence analysis and database matching for serotype prediction.
- **Input/Output**: Accepts FASTA/FASTQ/BAM files and produces serotype predictions.
- **Serotyping**: Focuses on Salmonella serotype determination.
- **Applications**: Clinical microbiology, food safety, and epidemiological studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Database Requirements**: Requires up-to-date serotype database.
- **Input Quality**: Results depend on sequencing data quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Predict serotype
**Args:** `SeqSero2.py -i genome.fasta -o results/`
**Explanation:** `-i` input genome; `-o` output directory.

### From FASTQ
**Args:** `SeqSero2.py -f1 reads_1.fastq -f2 reads_2.fastq -o results/`
**Explanation:** `-f1/-f2` paired-end reads.

### From BAM
**Args:** `SeqSero2.py -b alignments.bam -o results/`
**Explanation:** `-b` input BAM file.

### Verbose logging
**Args:** `SeqSero2.py -i genome.fasta -v -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `SeqSero2.py --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `SeqSero2.py --version`
**Explanation:** Shows current version.

### Detailed output
**Args:** `SeqSero2.py -i genome.fasta -d -o results/`
**Explanation:** `-d` enables detailed output.
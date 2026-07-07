---
name: serotypefinder
category: typing
description: serotypefinder - E. coli serotype identification from sequenced isolates
tags: ["serotypefinder", "typing", "E. coli", "serotyping"]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/serotypefinder"
---

## Concepts

- **Tool Overview**: serotypefinder (v2.0.2) identifies serotypes in E. coli sequenced isolates.
- **Core Function**: Determines E. coli serotype using genomic sequence data.
- **Algorithm**: Uses BLAST-based matching against serotype databases.
- **Input/Output**: Accepts FASTA sequences and produces serotype predictions.
- **Serotyping**: Focuses on E. coli serotype determination.
- **Applications**: Clinical microbiology, food safety, and epidemiological studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Database Requirements**: Requires up-to-date serotype database.
- **Input Quality**: Results depend on sequence quality.
- **Documentation**: Some features have limited documentation.

## Examples

### Predict serotype
**Args:** `serotypefinder.py -i genome.fasta -o results/`
**Explanation:** `-i` input genome; `-o` output directory.

### From FASTQ
**Args:** `serotypefinder.py -f1 reads_1.fastq -f2 reads_2.fastq -o results/`
**Explanation:** `-f1/-f2` paired-end reads.

### Custom database
**Args:** `serotypefinder.py -i genome.fasta -d custom_db -o results/`
**Explanation:** `-d` specifies custom database.

### Verbose logging
**Args:** `serotypefinder.py -v -i genome.fasta -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `serotypefinder.py --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `serotypefinder.py --version`
**Explanation:** Shows current version.

### Update database
**Args:** `serotypefinder.py --update`
**Explanation:** Updates serotype database.
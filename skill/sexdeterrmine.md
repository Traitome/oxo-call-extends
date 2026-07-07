---
name: sexdeterrmine
category: utility
description: sexdeterrmine - Sex determination from sequencing coverage
tags: ["sexdeterrmine", "utility", "sex-determination", "coverage"]
author: oxo-call-community
source_url: "https://github.com/TCLamnidis/Sex.DetERRmine"
---

## Concepts

- **Tool Overview**: sexdeterrmine (v1.1.2) determines sex from sequencing coverage data.
- **Core Function**: Calculates X/Y chromosome coverage ratio for sex prediction.
- **Algorithm**: Uses statistical methods to estimate sex from capture data.
- **Input/Output**: Accepts BAM files and produces sex prediction.
- **Sex Determination**: Focuses on predicting biological sex from sequencing data.
- **Applications**: Population genetics, ancient DNA, and forensic genetics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Quality**: Results depend on sequencing coverage.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Genome**: Requires appropriate reference genome.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Predict sex
**Args:** `Sex.DetERRmine.py -i input.bam -r reference.fasta -o results.txt`
**Explanation:** `-i` input BAM; `-r` reference; `-o` output results.

### With capture regions
**Args:** `Sex.DetERRmine.py -i input.bam -r reference.fasta -b capture.bed -o results.txt`
**Explanation:** `-b` capture regions BED file.

### Verbose logging
**Args:** `Sex.DetERRmine.py -v -i input.bam -r reference.fasta -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `Sex.DetERRmine.py --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `Sex.DetERRmine.py --version`
**Explanation:** Shows current version.

### Multiple samples
**Args:** `Sex.DetERRmine.py -i sample1.bam -i sample2.bam -r reference.fasta -o results.txt`
**Explanation:** Processes multiple samples.
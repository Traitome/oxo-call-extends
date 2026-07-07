---
name: shigapass
category: annotation
description: shigapass - Shigella serotype prediction
tags: ["shigapass", "annotation", "serotyping", "Shigella"]
author: oxo-call-community
source_url: "https://github.com/imanyass/ShigaPass/"
---

## Concepts

- **Tool Overview**: shigapass (v1.5.0) predicts Shigella serotypes in silico.
- **Core Function**: Identifies Shigella serotypes from genomic sequences.
- **Algorithm**: Uses sequence comparison against known serotype markers.
- **Input/Output**: Accepts FASTA sequences and produces serotype predictions.
- **Serotyping**: Focuses on Shigella species identification.
- **Applications**: Clinical microbiology, epidemiology, and pathogen identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Database Updates**: Requires up-to-date serotype database.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Predict serotype
**Args:** `shigapass -i genome.fasta -o results.txt`
**Explanation:** `-i` input genome; `-o` output results.

### With database
**Args:** `shigapass -i genome.fasta -d custom_db -o results.txt`
**Explanation:** `-d` custom database directory.

### Verbose logging
**Args:** `shigapass -v -i genome.fasta -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shigapass --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shigapass --version`
**Explanation:** Shows current version.

### Batch processing
**Args:** `shigapass -i genomes_dir/ -o results_dir/`
**Explanation:** Processes multiple genomes.

### Detailed output
**Args:** `shigapass -i genome.fasta -o results.txt -d`
**Explanation:** `-d` enables detailed output.
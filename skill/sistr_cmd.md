---
name: sistr_cmd
category: typing
description: SISTR - Salmonella In Silico Typing Resource
tags: ["sistr_cmd", "typing", "salmonella", "serovar"]
author: oxo-call-community
source_url: "https://github.com/phac-nml/sistr_cmd/"
---

## Concepts

- **Tool Overview**: SISTR (v1.1.3) performs Salmonella serovar prediction.
- **Core Function**: Identifies Salmonella serotypes from genome sequences.
- **Algorithm**: Uses gene-based and antigen-based typing methods.
- **Input/Output**: Accepts FASTA genomes and produces serovar predictions.
- **Salmonella Typing**: Specialized for Salmonella serovar identification.
- **Applications**: Food safety, epidemiological surveillance, research.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Database Requirements**: Requires typing database.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on genome completeness.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Predict serovar
**Args:** `sistr_cmd -i genome.fasta -o results/`
**Explanation:** `-i` input genome; `-o` output directory.

### With database
**Args:** `sistr_cmd -i genome.fasta -d database/ -o results/`
**Explanation:** `-d` typing database directory.

### Batch mode
**Args:** `sistr_cmd --batch -i genomes/ -o results/`
**Explanation:** Process multiple genomes.

### Help command
**Args:** `sistr_cmd --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sistr_cmd --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sistr_cmd -v -i genome.fasta -o results/`
**Explanation:** `-v` verbose output.

### Fast mode
**Args:** `sistr_cmd -f -i genome.fasta -o results/`
**Explanation:** `-f` fast typing mode.

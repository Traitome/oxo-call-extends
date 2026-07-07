---
name: spatyper
category: microbiology
description: SpaTyper - Computational method for finding spa types
tags: [spatyper, microbiology, spa-typing, staphylococcus, mlst]
author: oxo-call-community
source_url: "https://github.com/HCGB-IGTP/spaTyper"
---

## Concepts

- **Tool Overview**: spatyper (v0.3.3) - A spa typing tool
- **Core Function**: Finds spa types from Staphylococcus aureus sequences
- **Input/Output**: Accepts genome sequences; outputs spa type assignments
- **Algorithm**: Analyzes repeat regions for spa typing
- **Installation**: `conda install -c bioconda spatyper`
- **Key Features**: Spa typing, Staphylococcus aureus, repeat analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted genome sequences
- **Repeat Region**: Requires accurate repeat region detection
- **Database**: Requires spa type database for comparison
- **Memory Usage**: Large genomes require significant memory
- **Output Format**: Output format depends on configuration
- **Type Accuracy**: Type accuracy depends on sequence quality

## Examples

### Display help
**Args:** `spatyper --help`
**Explanation:** Shows available options and usage information.

### Basic spa typing
**Args:** `spatyper -i genome.fasta -o spa_type.txt`
**Explanation:** Determine spa type from genome.

### With database
**Args:** `spatyper -i genome.fasta -d spa_db/ -o spa_type.txt`
**Explanation:** Use specific spa database.

### Multiple genomes
**Args:** `spatyper -i genome1.fasta genome2.fasta -o spa_types.txt`
**Explanation:** Type multiple genomes.

### With detailed output
**Args:** `spatyper -i genome.fasta -o spa_type.txt --detailed`
**Explanation:** Output detailed typing information.

### Output repeat regions
**Args:** `spatyper -i genome.fasta -o spa_type.txt --repeats`
**Explanation:** Output repeat region information.

### Output statistics
**Args:** `spatyper -i genome.fasta -o spa_type.txt --stats`
**Explanation:** Output typing statistics.

### Generate report
**Args:** `spatyper -i genome.fasta -o spa_type.txt --report`
**Explanation:** Generate typing report.

### With threads
**Args:** `spatyper -i genome.fasta -o spa_type.txt -p 8`
**Explanation:** Use multiple threads for typing.
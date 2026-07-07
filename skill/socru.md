---
name: socru
category: assembly
description: SoCru - Order and orientation tool for complete bacterial genomes
tags: [socru, assembly, bacterial, orientation, ordering]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/socru"
---

## Concepts

- **Tool Overview**: socru (v2.2.5) - A tool for ordering and orienting bacterial genomes
- **Core Function**: Determines correct order and orientation of genome contigs
- **Input/Output**: Accepts genome contigs; outputs ordered and oriented genome
- **Algorithm**: Uses reference genomes and synteny for ordering
- **Installation**: `conda install -c bioconda socru`
- **Key Features**: Genome ordering, orientation correction, bacterial genomes

## Pitfalls

- **Input Requirements**: Requires properly formatted genome contigs
- **Reference Genome**: Requires reference genome for ordering
- **Contig Quality**: Quality of contigs affects ordering accuracy
- **Circular Genomes**: Circular genomes may require special handling
- **Memory Usage**: Large genomes require significant memory
- **Output Format**: Output format must match requirements

## Examples

### Display help
**Args:** `socru --help`
**Explanation:** Shows available options and usage information.

### Basic ordering
**Args:** `socru -i contigs.fasta -r reference.fasta -o ordered.fasta`
**Explanation:** Order and orient genome contigs.

### With multiple references
**Args:** `socru -i contigs.fasta -r ref1.fasta ref2.fasta -o ordered.fasta`
**Explanation:** Use multiple references for ordering.

### Circular genome
**Args:** `socru -i contigs.fasta -r reference.fasta -o ordered.fasta --circular`
**Explanation:** Order circular bacterial genome.

### With validation
**Args:** `socru -i contigs.fasta -r reference.fasta -o ordered.fasta --validate`
**Explanation:** Validate ordered genome.

### Output statistics
**Args:** `socru -i contigs.fasta -r reference.fasta -o ordered.fasta --stats`
**Explanation:** Output ordering statistics.

### Generate report
**Args:** `socru -i contigs.fasta -r reference.fasta -o ordered.fasta --report`
**Explanation:** Generate ordering report.

### With threads
**Args:** `socru -i contigs.fasta -r reference.fasta -o ordered.fasta -p 8`
**Explanation:** Use multiple threads for ordering.
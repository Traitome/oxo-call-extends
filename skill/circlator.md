---
name: circlator
category: assembly
description: Tool to circularize genome assemblies
tags: [circlator, assembly, circularization, genome, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/circlator"
---

## Concepts

- **Tool Overview**: Circlator circularizes genome assemblies by identifying overlapping ends of contigs and joining them.
- **Core Function**: Detects and resolves circular DNA sequences in genome assemblies, particularly useful for bacterial and plasmid sequences.
- **Algorithm**: Uses BLAST to identify overlapping ends and performs sequence alignment to verify circularization.
- **Input**: Genome assembly in FASTA format.
- **Output**: Circularized genome assembly with properly closed contigs.
- **Application**: Bacterial genome assembly, plasmid sequencing, and circular genome analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda circlator`

## Pitfalls

- **Assembly Quality**: Requires high-quality input assembly with minimal errors.
- **Repeat Regions**: Repetitive sequences can interfere with circularization.
- **Contig Length**: Short contigs may not have sufficient overlap for detection.
- **Sequence Similarity**: Requires significant sequence overlap at contig ends.
- **Chimeric Contigs**: May incorrectly circularize chimeric sequences.

## Examples

### Circularize assembly
**Args:** `circlator all -i assembly.fasta -o circularized`
**Explanation:** Circularizes genome assembly by identifying overlapping contig ends.

### Check circularization potential
**Args:** `circlator check -i assembly.fasta -o check_report.txt`
**Explanation:** Checks which contigs have potential circularization signals.

### Manual circularization
**Args:** `circlator merge -a contig1.fasta -b contig2.fasta -o merged.fasta`
**Explanation:** Merges two overlapping contigs manually.

### Display help
**Args:** `circlator --help`
**Explanation:** Shows all available commands and options.
---
name: corekaburra
category: formatting
description: Utilizes syntenic information from genomes in pan-genome context
tags: [corekaburra, pan-genome, synteny, genomics, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/milnus/Corekaburra/wiki"
---

## Concepts

- **Tool Overview**: Corekaburra is a command-line tool that utilizes syntenic information from multiple genomes to analyze pan-genome structure and organization.
- **Core Function**: Identifies core and accessory genes across multiple genomes using synteny conservation patterns.
- **Algorithm**: Uses syntenic block detection to classify genes into core, accessory, and unique categories.
- **Input**: Multiple genome sequences, gene annotations in GFF format.
- **Output**: Pan-genome classification, core gene sets, accessory gene lists.
- **Application**: Pan-genome analysis, comparative genomics, evolutionary studies.
- **Installation**: Install via bioconda: `conda install -c bioconda corekaburra`

## Pitfalls

- **Genome Quality**: Requires high-quality genome assemblies and annotations.
- **Synteny Conservation**: Works best with closely related species.
- **Annotation Consistency**: Requires consistent gene annotation formats.
- **Computational Resources**: May require significant resources for large datasets.
- **Orthology Detection**: Relies on accurate ortholog identification.

## Examples

### Analyze pan-genome
**Args:** `corekaburra -g genomes.txt -a annotations.gff -o pan_genome/`
**Explanation:** Analyzes pan-genome using genome sequences and annotations.

### With synteny threshold
**Args:** `corekaburra -g genomes.txt -a annotations.gff -t 0.8 -o pan_genome/`
**Explanation:** Sets synteny conservation threshold to 80%.

### Output core genes only
**Args:** `corekaburra -g genomes.txt -a annotations.gff --core-only -o core_genes.txt`
**Explanation:** Outputs only core gene set.

### Display help
**Args:** `corekaburra --help`
**Explanation:** Shows all available options and usage information.
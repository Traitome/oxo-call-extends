---
name: chromosomer
category: assembly
description: Reference-assisted assembly tool for producing draft chromosome sequences
tags: [chromosomer, assembly, reference-guided, scaffolding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gtamazian/chromosomer"
---

## Concepts

- **Tool Overview**: Chromosomer is a reference-assisted assembly tool that produces draft chromosome sequences using a closely related reference genome.
- **Core Function**: Orders and orients contigs/scaffolds using a reference genome to produce chromosome-scale assemblies.
- **Algorithm**: Uses synteny information from reference genome to guide scaffold ordering and orientation.
- **Input**: Assembled contigs/scaffolds and a reference genome.
- **Output**: Chromosome-scale draft assembly.
- **Application**: Genome assembly improvement, scaffolding, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda chromosomer`

## Pitfalls

- **Reference Quality**: Requires high-quality reference genome for accurate scaffolding.
- **Sequence Divergence**: Works best with closely related species; may fail with highly divergent genomes.
- **Assembly Quality**: Input contigs/scaffolds must be of reasonable quality.
- **Misassembly Risk**: May introduce misassemblies if reference has structural differences.
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Assemble using reference
**Args:** `chromosomer assemble -i contigs.fasta -r reference.fasta -o chromosomes.fasta`
**Explanation:** Produces draft chromosome sequences using reference-guided assembly.

### Scaffold only
**Args:** `chromosomer scaffold -i contigs.fasta -r reference.fasta -o scaffolds.fasta`
**Explanation:** Scaffolds contigs without full assembly.

### With mapping file
**Args:** `chromosomer assemble -i contigs.fasta -r reference.fasta -m mapping.txt -o chromosomes.fasta`
**Explanation:** Uses custom mapping file for scaffold ordering.

### Display help
**Args:** `chromosomer --help`
**Explanation:** Shows all available commands and options.
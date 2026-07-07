---
name: clsify
category: utility
description: Haplotyping of C. Liberibacter solanacearum from Sanger sequencing data
tags: [clsify, haplotyping, liberibacter, sanger-sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/holtgrewe/clsify"
---

## Concepts

- **Tool Overview**: clsify is a specialized tool for haplotyping Candidatus Liberibacter solanacearum from Sanger sequencing data.
- **Core Function**: Identifies and reconstructs haplotypes from Sanger sequence data for C. Liberibacter solanacearum.
- **Algorithm**: Uses sequence analysis to resolve haplotypes from mixed infections or heterogeneous populations.
- **Input**: Sanger sequencing reads (FASTA/AB1 format) from C. Liberibacter solanacearum samples.
- **Output**: Haplotype sequences with frequency estimates.
- **Application**: Phytopathology, bacterial pathogen analysis, and population genetics of C. Liberibacter.
- **Installation**: Install via bioconda: `conda install -c bioconda clsify`

## Pitfalls

- **Species Specific**: Designed specifically for C. Liberibacter solanacearum.
- **Sanger Data**: Optimized for Sanger sequencing data, not NGS.
- **Data Quality**: Requires high-quality Sanger sequences.
- **Mixed Infections**: Works best with samples containing multiple haplotypes.
- **Reference Genome**: May require reference sequence for analysis.

## Examples

### Haplotyping from Sanger data
**Args:** `clsify -i sanger_reads.fasta -o haplotypes.fasta`
**Explanation:** Identifies and reconstructs haplotypes from Sanger sequencing data.

### With reference sequence
**Args:** `clsify -i reads.fasta -r reference.fasta -o haplotypes.fasta`
**Explanation:** Uses reference sequence for improved haplotype calling.

### With quality filtering
**Args:** `clsify -i reads.fasta -q -o haplotypes.fasta`
**Explanation:** Applies quality filtering to input reads.

### Display help
**Args:** `clsify --help`
**Explanation:** Shows all available options and usage information.
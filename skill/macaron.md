---
name: macaron
category: variant-calling
description: Multi-bAse Codon-Associated variant Re-annotatiON
tags: [macaron, variant-calling, annotation, codon]
author: oxo-call-community
source_url: "https://github.com/waqasuddinkhan/MACARON-GenMed-LabEx"
---

## Concepts

- **Tool Overview**: macaron v1.0 is a tool for re-annotating variants based on codon associations.
- **Core Function**: Re-annotates genetic variants with focus on codon-level effects.
- **Annotation Strategy**: Considers multiple bases and their combined effect on codon function.
- **Input/Output**: Input: VCF file with variants; Output: Re-annotated VCF with codon-level annotations.
- **Installation**: `conda install -c bioconda macaron`
- **Key Features**: Codon-aware annotation, handles complex variant combinations, supports multiple organisms.

## Pitfalls

- **VCF Format**: Requires properly formatted VCF input.
- **Reference Genome**: Depends on reference genome for annotation.
- **Memory Usage**: Processing large VCF files may require significant memory.
- **Computation Time**: Can be slow for large variant datasets.
- **Organism Support**: May have limited support for non-model organisms.
- **Annotation Quality**: Depends on reference genome annotation quality.

## Examples

### Re-annotate variants
**Args:** `macaron -i variants.vcf -r reference.fasta -o reannotated.vcf`
**Explanation:** Re-annotates variants with codon-level information.

### With annotation database
**Args:** `macaron -i variants.vcf -r reference.fasta -d annotation.db -o reannotated.vcf`
**Explanation:** Uses custom annotation database for re-annotation.

### Threads
**Args:** `macaron -i variants.vcf -r reference.fasta -t 4 -o reannotated.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `macaron -i variants.vcf -r reference.fasta -f json -o annotations.json`
**Explanation:** Outputs annotations in JSON format.

### Verbose mode
**Args:** `macaron -i variants.vcf -r reference.fasta -v -o reannotated.vcf`
**Explanation:** Outputs detailed annotation information.

### Help documentation
**Args:** `macaron --help`
**Explanation:** Displays all available options and parameters.
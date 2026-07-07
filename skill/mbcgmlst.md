---
name: mbcgmlst
category: variant-calling
description: cgMLST allele calling pipeline with Ridom-style output for bacterial typing.
tags: [mbcgmlst, cgMLST, bacterial-typing]
author: oxo-call-community
source_url: "https://github.com/liviurotiul/mbcgmlst"
---

## Concepts

- **Tool Overview**: mbcgmlst performs cgMLST allele calling for bacterial typing.
- **Core Function**: Maps allele sequences against assembled genomes.
- **Allele Calling**: Identifies alleles in assembled contigs.
- **Ridom Output**: Produces Ridom-style CSV output.
- **Input/Output**: Accepts FASTA alleles and genomes, produces CSV results.
- **Installation**: `conda install -c bioconda mbcgmlst`

## Pitfalls

- **Genome Quality**: Requires high-quality assembled genomes.
- **Allele Database**: Requires comprehensive allele database.
- **Memory Requirements**: Large datasets may require memory.
- **Output Format**: Ridom format may need conversion.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **Ambiguity Handling**: May struggle with ambiguous calls.

## Examples

### Run cgMLST calling
**Args:** `mbcgmlst -a alleles.fasta -g genome.fasta -o results.csv`
**Explanation:** Calls alleles from genome against database.

### Multiple genomes
**Args:** `mbcgmlst -a alleles.fasta -g genome1.fasta genome2.fasta -o results/`
**Explanation:** Processes multiple genomes.

### Set identity threshold
**Args:** `mbcgmlst -a alleles.fasta -g genome.fasta -i 0.95 -o results.csv`
**Explanation:** Sets 95% identity threshold.

### Verbose output
**Args:** `mbcgmlst -a alleles.fasta -g genome.fasta -v -o results.csv`
**Explanation:** Shows detailed processing information.

### Help documentation
**Args:** `mbcgmlst --help`
**Explanation:** Displays available commands and options.

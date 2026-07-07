---
name: cladebreaker
category: population-genomics
description: Nextflow pipeline for phylogenetic analysis
tags: [cladebreaker, phylogenetics, nextflow, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/andriesfeder/cladebreaker"
---

## Concepts

- **Tool Overview**: cladebreaker is a Nextflow pipeline for phylogenetic analysis, designed to reconstruct evolutionary relationships from genomic data.
- **Core Function**: Automates phylogenetic tree construction, including multiple sequence alignment, model selection, and tree inference.
- **Features**: Supports multiple alignment tools, phylogenetic inference methods, and visualization options.
- **Input**: Genomic sequences (FASTA), VCF files, or aligned sequences.
- **Output**: Phylogenetic trees (Newick format), alignments, and visualization files.
- **Application**: Evolutionary analysis, population genetics, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cladebreaker`

## Pitfalls

- **Nextflow Dependency**: Requires Nextflow to be installed and configured.
- **Computational Resources**: May require significant compute resources for large datasets.
- **Alignment Quality**: Depends on input sequence quality and alignment parameters.
- **Model Selection**: Appropriate substitution model must be chosen.
- **Memory Usage**: Large alignments may require substantial memory.

## Examples

### Run phylogenetic pipeline
**Args:** `nextflow run andriesfeder/cladebreaker --input sequences.fasta --output results/`
**Explanation:** Runs the complete phylogenetic analysis pipeline.

### With VCF input
**Args:** `nextflow run andriesfeder/cladebreaker --vcf genotypes.vcf --output results/`
**Explanation:** Performs phylogenetic analysis from VCF file.

### Specify alignment tool
**Args:** `nextflow run andriesfeder/cladebreaker --input seqs.fasta --aligner mafft --output results/`
**Explanation:** Uses MAFFT for multiple sequence alignment.

### Display help
**Args:** `nextflow run andriesfeder/cladebreaker --help`
**Explanation:** Shows all available options and usage information.
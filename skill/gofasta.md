---
name: gofasta
category: bioinformatics
description: GoFasta provides genomic epidemiology utilities for processing and analyzing short genome alignments.
tags: [gofasta, genomic-epidemiology, alignment, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/virus-evolution/gofasta"
---

## Concepts

- **Alignment Processing**: GoFasta processes multiple sequence alignments for genomic epidemiology applications, including variant calling and phylogenetic analysis.

- **Variant Identification**: Identifies single nucleotide variants (SNVs) and indels from aligned sequences, supporting variant calling workflows.

- **Consensus Generation**: Generates consensus sequences from alignments, with options for handling ambiguous bases and quality filtering.

- **Masking**: Supports masking of low-quality regions, repeat regions, and user-defined intervals to improve analysis accuracy.

- **Phylogenetic Preparation**: Prepares alignments for phylogenetic tree construction, including trimming and filtering operations.

- **FASTA Manipulation**: Provides utilities for FASTA file manipulation, including subsetting, renaming, and format conversion.

## Pitfalls

- **Alignment Quality**: Results depend heavily on alignment quality. Use high-quality alignments from trusted tools like MAFFT or Clustal.

- **Reference Selection**: The choice of reference sequence affects variant calling. Use appropriate references for your study organism.

- **Ambiguity Handling**: Ambiguous bases can complicate variant calling. Define clear criteria for handling Ns and ambiguous codes.

- **Masking Strategy**: Over-masking can remove biologically relevant sites. Carefully define masking criteria based on your research goals.

- **Large Datasets**: Processing very large alignments may require significant memory. Consider splitting or downsampling when necessary.

## Examples

### Generate consensus sequence
**Args:** `gofasta consensus -i alignment.fasta -o consensus.fasta`
**Explanation:** Generates a consensus sequence from the input alignment, resolving ambiguous positions.

### Call variants
**Args:** `gofasta variants -i alignment.fasta -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants in the alignment compared to the reference sequence and outputs in VCF format.

### Mask low-quality regions
**Args:** `gofasta mask -i alignment.fasta -q 20 -o masked.fasta`
**Explanation:** Masks positions with quality scores below 20 in the alignment.

### Trim alignment ends
**Args:** `gofasta trim -i alignment.fasta -o trimmed.fasta`
**Explanation:** Trims columns with high gap content from the beginning and end of the alignment.

### Subset sequences
**Args:** `gofasta subset -i alignment.fasta -l ids.txt -o subset.fasta`
**Explanation:** Extracts sequences with IDs listed in ids.txt from the alignment.

### Convert alignment format
**Args:** `gofasta convert -i alignment.fasta -f phylip -o alignment.phylip`
**Explanation:** Converts the alignment from FASTA format to Phylip format.

### Remove duplicate sequences
**Args:** `gofasta deduplicate -i alignment.fasta -o unique.fasta`
**Explanation:** Removes identical sequences from the alignment, keeping only one copy of each unique sequence.
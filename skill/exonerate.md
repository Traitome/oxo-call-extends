---
name: exonerate
category: alignment
description: "Exonerate - A generic tool for pairwise sequence comparison / alignment."
tags: [exonerate, alignment, sequence-comparison, pairwise-alignment]
author: oxo-call-community
source_url: "http://ftp.ebi.ac.uk/pub/software/vertebrategenomics/exonerate"
---

## Concepts

- **Tool Overview**: Exonerate is a versatile pairwise sequence alignment tool supporting various alignment strategies.
- **Core Function**: Performs flexible sequence alignment with support for multiple alignment models.
- **Input/Output**: Input: Sequence files (FASTA). Output: Alignment results in various formats.
- **Algorithm**: Uses dynamic programming with configurable scoring matrices and gap penalties.
- **Key Features**: Global/local alignment, spliced alignment, protein-DNA alignment, configurable parameters.
- **Installation**: `conda install -c bioconda exonerate`

## Pitfalls

- **Parameter Tuning**: Requires careful parameter selection for optimal results.
- **Computation Time**: Complex alignments can be computationally intensive.
- **Memory Usage**: Large sequences require significant RAM.
- **Output Format**: Multiple output formats available; choose appropriate format.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic pairwise alignment
**Args:** `exonerate query.fa target.fa`
**Explanation:** Aligns query sequence against target sequence.

### Spliced alignment
**Args:** `exonerate --model est2genome query.fa target.fa`
**Explanation:** Performs spliced alignment (EST to genome).

### Protein-DNA alignment
**Args:** `exonerate --model protein2genome protein.fa genome.fa`
**Explanation:** Aligns protein sequence against DNA genome.

### Global alignment
**Args:** `exonerate --model global query.fa target.fa`
**Explanation:** Performs global sequence alignment.

### Output in GFF format
**Args:** `exonerate --model est2genome query.fa target.fa --showtargetgff`
**Explanation:** Outputs alignment in GFF format.
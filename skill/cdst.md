---
name: cdst
category: sequence-analysis
description: "CoDing Sequence Typer (CDST): MD5 hash-based genome typing and clustering"
tags: [cdst, genome-typing, clustering, md5-hash, cds]
author: oxo-call-community
source_url: "https://github.com/l1-mh/CDST"
---
## Concepts

- **Tool Overview**: CDST performs MD5 hash-based genome typing and clustering using coding sequences.
- **Core Function**: Generates unique MD5 hashes from CDS sequences for rapid genome comparison.
- **Algorithm**: Uses MD5 hashing of concatenated CDS sequences for efficient genome identification.
- **Input**: FASTA files with coding sequences or whole genomes.
- **Output**: Hash-based genome types and clustering results.
- **Application**: Rapid strain identification and genome clustering in epidemiology.
- **Installation**: Install via bioconda: `conda install -c bioconda cdst`

## Pitfalls

- **CDS Quality**: Requires complete and accurate CDS annotations.
- **Hash Collision**: Extremely rare but possible with MD5.
- **Genome Completeness**: Partial genomes may produce incomplete hashes.
- **Strain Resolution**: May not distinguish very closely related strains.

## Examples

### Generate genome type
**Args:** `cdst -i genome.fasta -o genome_type.txt`
**Explanation:** Generates MD5 hash-based type for genome.

### Cluster genomes
**Args:** `cdst cluster -i genomes/ -o clustering.tsv`
**Explanation:** Clusters multiple genomes based on CDS hashes.

### Compare two genomes
**Args:** `cdst compare -i genome1.fa genome2.fa`
**Explanation:** Compares two genomes using CDS hash similarity.

### Display help
**Args:** `cdst --help`
**Explanation:** Shows all available options and usage information.
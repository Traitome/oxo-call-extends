---
name: el_gato
category: assembly
description: "Perform Legionella pneumophila Sequence Based Typing (SBT) from short reads or assemblies."
tags: [el_gato, assembly, Legionella, SBT, typing]
author: oxo-call-community
source_url: "https://github.com/CDCgov/el_gato/blob/1.22.0/README.md"
---

## Concepts

- **Tool Overview**: EL_GATO is a bioinformatics tool for performing Sequence Based Typing (SBT) of Legionella pneumophila from short reads or genome assemblies.
- **Core Function**: Determines the sequence type (ST) of Legionella pneumophila isolates by comparing against the official SBT database.
- **Input/Output**: Input: Short reads (FASTQ) or genome assemblies (FASTA). Output: SBT results, sequence type assignments, allele profiles.
- **Algorithm**: Uses BLAST or mapping-based approaches to identify allele sequences and determine sequence types.
- **Key Features**: Support for both reads and assemblies, automatic allele calling, database updates, quality filtering, batch processing.
- **Installation**: `conda install -c bioconda el_gato`

## Pitfalls

- **Reference Database**: Requires up-to-date SBT database for accurate typing.
- **Sequence Quality**: Poor quality reads may lead to incorrect allele calls.
- **Assembly Completeness**: Incomplete assemblies may miss some alleles.
- **Database Updates**: Regular database updates are required for new sequence types.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic SBT from reads
**Args:** `el_gato -i reads.fastq -o sbt_results.txt`
**Explanation:** Performs SBT typing from short read data.

### SBT from assembly
**Args:** `el_gato -i assembly.fasta -o sbt_results.txt -a`
**Explanation:** Performs SBT typing from genome assembly.

### Update database
**Args:** `el_gato --update-db`
**Explanation:** Updates the SBT database to latest version.

### Batch processing
**Args:** `el_gato -i samples/ -o results/ --batch`
**Explanation:** Processes multiple samples in batch mode.

### Verbose output
**Args:** `el_gato -i reads.fastq -o sbt_results.txt -v`
**Explanation:** Generates verbose output with detailed allele information.
---
name: refseq_masher
category: utility
description: RefSeq Masher finds NCBI RefSeq genomes matching sequence data using MinHash-based Mash algorithm.
tags: [refseq_masher, utility, genome-matching, mash]
author: oxo-call-community
source_url: "https://github.com/phac-nml/refseq_masher"
---

## Concepts

- **Tool Overview**: refseq_masher matches genomes.
- **Core Function**: Genome matching.
- **Algorithm**: Uses MinHash methods.
- **Input Format**: Accepts sequence data.
- **Output**: Produces genome matches.
- **Use Case**: Sequence identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Sequence Quality**: Affects matching.
- **Parameters**: Must be configured.
- **Runtime**: Matching may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `refseq_masher --help`
**Explanation:** Shows available options and usage instructions.

### Match genomes
**Args:** `refseq_masher match -i sequence.fasta -o matches.txt`
**Explanation:** Finds matching RefSeq genomes.

### With parameters
**Args:** `refseq_masher match -i sequence.fasta -p params.yaml -o matches.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `refseq_masher -v match -i sequence.fasta -o matches.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `refseq_masher -t 4 match -i sequence.fasta -o matches.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `refseq_masher match -i sequence.fasta -d refseq_db.msh -o matches.txt`
**Explanation:** Uses custom database.

### Generate report
**Args:** `refseq_masher match -i sequence.fasta -o matches.txt --report report.html`
**Explanation:** Generates HTML report.
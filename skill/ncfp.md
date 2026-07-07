---
name: ncfp
category: utility
description: ncfp (nucleotide coding frame prediction) finds nucleotide sequences that encode given protein sequences.
tags: [ncfp, utility, nucleotide, protein, sequence]
author: oxo-call-community
source_url: "http://widdowquinn.github.io/ncfp/"
---

## Concepts

- **Tool Overview**: ncfp is a tool for recovering nucleotide sequences from NCBI that encode input protein sequences.
- **Core Function**: Identifies nucleotide sequences corresponding to given amino acid sequences using NCBI databases.
- **Algorithm**: Queries NCBI's protein and nucleotide databases to find matching sequences.
- **Input Format**: Accepts protein FASTA files or individual sequences.
- **Output**: Produces nucleotide sequences in FASTA format with corresponding annotations.
- **Use Case**: Recovering coding sequences, primer design, and comparative genomics.

## Pitfalls

- **Network Dependency**: Requires internet access to NCBI servers.
- **Database Updates**: Results depend on NCBI database version.
- **Multiple Matches**: May return multiple nucleotide sequences for a single protein.
- **Version Differences**: Options may vary between versions.
- **Ambiguity**: Degenerate codons can lead to multiple possible nucleotide sequences.
- **Rate Limiting**: NCBI may block excessive requests.

## Examples

### Display help
**Args:** `ncfp --help`
**Explanation:** Shows available options and usage instructions.

### Basic usage
**Args:** `ncfp -i protein.faa -o nucleotide.fasta`
**Explanation:** Finds nucleotide sequences encoding input proteins.

### Batch processing
**Args:** `ncfp -i proteins/ -o nucleotides/`
**Explanation:** Processes multiple protein files in batch.

### Specify organism
**Args:** `ncfp -i protein.faa -s "Escherichia coli" -o output.fasta`
**Explanation:** Restricts search to specific organism.

### Output coding sequence only
**Args:** `ncfp -i protein.faa --cds-only -o cds.fasta`
**Explanation:** Outputs only coding sequences without flanking regions.

### Verbose output
**Args:** `ncfp -i protein.faa -v -o output.fasta`
**Explanation:** Produces verbose output with additional information.
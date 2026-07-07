---
name: ncbi-stxtyper
category: annotation
description: StxTyper identifies and types Shiga toxin operons from assembled genomic sequences.
tags: [ncbi-stxtyper, annotation, shiga-toxin, stx, ecoli]
author: oxo-call-community
source_url: "https://github.com/ncbi/stxtyper"
---

## Concepts

- **Tool Overview**: NCBI StxTyper identifies and types Shiga toxin (Stx) operons from assembled genomic sequences.
- **Core Function**: Detects Stx operons and determines their subtype using a standardized algorithm.
- **Algorithm**: Compares input sequences against a curated database of known Stx operon sequences.
- **Input Format**: Accepts FASTA files containing assembled genomic sequences.
- **Output**: Produces reports with Stx operon types, locations, and confidence scores.
- **Use Case**: Identifying Shiga toxin-producing E. coli (STEC), food safety testing, epidemiological analysis.

## Pitfalls

- **Database Updates**: Requires regular database updates for new Stx variants.
- **Assembly Quality**: Results depend on input sequence quality and completeness.
- **False Negatives**: May miss divergent or novel Stx variants.
- **Version Differences**: Options may vary between versions.
- **Reference Bias**: Database may not include all known Stx subtypes.
- **Partial Operons**: May fail to detect partial or fragmented operons.

## Examples

### Display help
**Args:** `stxtyper --help`
**Explanation:** Shows available options and usage instructions.

### Basic Stx typing
**Args:** `stxtyper -i input.fasta -o stx_results.tsv`
**Explanation:** Identifies and types Stx operons in input sequence.

### Update database
**Args:** `stxtyper --update-db`
**Explanation:** Updates the Stx reference database.

### Verbose output
**Args:** `stxtyper -i input.fasta -o results.tsv -v`
**Explanation:** Produces verbose output with detailed information.

### Custom database
**Args:** `stxtyper -i input.fasta -d custom_db/ -o results.tsv`
**Explanation:** Uses custom Stx reference database.

### Output JSON format
**Args:** `stxtyper -i input.fasta --json -o results.json`
**Explanation:** Outputs results in JSON format.
---
name: refseq-plasmid-dl
category: utility
description: RefSeq Plasmid DL is a command-line tool to download and curate RefSeq plasmid sequences from NCBI.
tags: [refseq-plasmid-dl, utility, plasmid, ncbi]
author: oxo-call-community
source_url: "https://github.com/erinyoung/refseq-plasmid-dl"
---

## Concepts

- **Tool Overview**: refseq-plasmid-dl downloads plasmids.
- **Core Function**: Plasmid sequence download.
- **Algorithm**: Uses NCBI API methods.
- **Input Format**: Accepts NCBI identifiers.
- **Output**: Produces plasmid sequences.
- **Use Case**: Plasmid collection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large downloads require memory.
- **Network Quality**: Affects download.
- **Parameters**: Must be configured.
- **Runtime**: Download may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `refseq-plasmid-dl --help`
**Explanation:** Shows available options and usage instructions.

### Download plasmids
**Args:** `refseq-plasmid-dl download -o plasmid_sequences.fasta`
**Explanation:** Downloads RefSeq plasmid sequences.

### With parameters
**Args:** `refseq-plasmid-dl download -p params.yaml -o plasmid_sequences.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `refseq-plasmid-dl -v download -o plasmid_sequences.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `refseq-plasmid-dl -t 4 download -o plasmid_sequences.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With filters
**Args:** `refseq-plasmid-dl download -f "length>1000" -o plasmid_sequences.fasta`
**Explanation:** Filters plasmids by criteria.

### Generate report
**Args:** `refseq-plasmid-dl download -o plasmid_sequences.fasta --report report.html`
**Explanation:** Generates HTML report.
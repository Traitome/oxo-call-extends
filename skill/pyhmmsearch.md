---
name: pyhmmsearch
category: utility
description: pyhmmsearch is a fast HMMSEARCH implementation optimized for high-memory systems.
tags: [pyhmmsearch, utility, hmm, sequence-search]
author: oxo-call-community
source_url: "https://github.com/jolespin/pyhmmsearch/blob/main/README.md"
---

## Concepts

- **Tool Overview**: pyhmmsearch performs HMM searches.
- **Core Function**: Sequence homology search.
- **Algorithm**: Uses HMMER algorithms.
- **Input Format**: Accepts HMM profiles and FASTA files.
- **Output**: Produces search results.
- **Use Case**: Protein domain analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **HMM Quality**: Results depend on HMM profile.
- **E-value Threshold**: Affects sensitivity.
- **Runtime**: Search may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyhmmsearch --help`
**Explanation:** Shows available options and usage instructions.

### Run HMM search
**Args:** `pyhmmsearch search -h profile.hmm -i sequences.fasta -o results.txt`
**Explanation:** Searches sequences against HMM profile.

### With parameters
**Args:** `pyhmmsearch search -h profile.hmm -i sequences.fasta -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyhmmsearch -v search -h profile.hmm -i sequences.fasta -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyhmmsearch -t 4 search -h profile.hmm -i sequences.fasta -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### E-value cutoff
**Args:** `pyhmmsearch search -h profile.hmm -i sequences.fasta -e 0.001 -o results.txt`
**Explanation:** Sets E-value cutoff.

### Generate report
**Args:** `pyhmmsearch search -h profile.hmm -i sequences.fasta -o results.txt --report report.html`
**Explanation:** Generates HTML report.
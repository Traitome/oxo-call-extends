---
name: phipack
category: programming
description: phipack tests for recombination in sequence data.
tags: [phipack, programming, recombination, statistics]
author: oxo-call-community
source_url: "https://www.maths.otago.ac.nz/~dbryant/software.html"
---

## Concepts

- **Tool Overview**: phipack tests recombination.
- **Core Function**: Statistical recombination test.
- **Algorithm**: Uses recombination detection methods.
- **Input Format**: Accepts sequence alignment files.
- **Output**: Produces recombination test results.
- **Use Case**: Recombination analysis, sequence statistics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Statistical Power**: May miss weak recombination signals.
- **Runtime**: Testing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phipack --help`
**Explanation:** Shows available options and usage instructions.

### Test recombination
**Args:** `phipack -i alignment.fasta -o recombination_results.txt`
**Explanation:** Tests for recombination.

### With parameters
**Args:** `phipack -i alignment.fasta -p params.yaml -o recombination_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phipack -v -i alignment.fasta -o recombination_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phipack -t 4 -i alignment.fasta -o recombination_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phipack -i alignment.fasta -o recombination_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phipack -i alignment.fasta -o recombination_results.txt --report report.html`
**Explanation:** Generates HTML report.
---
name: pyngost
category: utility
description: pyngoST performs fast and accurate sequence typing of Neisseria gonorrhoeae genomes.
tags: [pyngost, utility, typing, gonorrhoeae]
author: oxo-call-community
source_url: "https://github.com/leosanbu/pyngoST"
---

## Concepts

- **Tool Overview**: pyngost types Neisseria gonorrhoeae.
- **Core Function**: Sequence typing.
- **Algorithm**: Uses allele matching.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces ST types.
- **Use Case**: ST analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Allele Database**: Must be current.
- **Sequence Quality**: Affects typing.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyngost --help`
**Explanation:** Shows available options and usage instructions.

### Run typing
**Args:** `pyngost type -i genome.fasta -d database/ -o result.txt`
**Explanation:** Determines ST type for genome.

### With parameters
**Args:** `pyngost type -i genome.fasta -p params.yaml -o result.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyngost -v type -i genome.fasta -o result.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyngost -t 4 type -i genome.fasta -o result.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Batch processing
**Args:** `pyngost batch -i genomes/ -d database/ -o results/`
**Explanation:** Processes multiple genomes.

### Generate report
**Args:** `pyngost type -i genome.fasta -o result.txt --report report.html`
**Explanation:** Generates HTML report.
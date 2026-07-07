---
name: pmlst
category: annotation
description: pmlst performs plasmid multi-locus sequence typing.
tags: [pmlst, annotation, plasmid, mlst]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/pmlst"
---

## Concepts

- **Tool Overview**: pmlst types plasmid sequences.
- **Core Function**: Plasmid MLST typing.
- **Algorithm**: Uses sequence matching methods.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces MLST typing results.
- **Use Case**: Plasmid epidemiology, bacterial analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Typing Accuracy**: May have classification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pmlst --help`
**Explanation:** Shows available options and usage instructions.

### Type plasmids
**Args:** `pmlst -i plasmids.fasta -o typing.txt`
**Explanation:** Performs plasmid MLST typing.

### With parameters
**Args:** `pmlst -i plasmids.fasta -p params.yaml -o typing.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pmlst -v -i plasmids.fasta -o typing.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pmlst -t 4 -i plasmids.fasta -o typing.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pmlst -i plasmids.fasta -o typing.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pmlst -i plasmids.fasta -o typing.txt --report report.html`
**Explanation:** Generates HTML report.
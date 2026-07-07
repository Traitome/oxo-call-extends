---
name: pyani
category: containerization
description: pyani calculates genome-scale Average Nucleotide Identity (ANI) between genomes for taxonomic classification.
tags: [pyani, containerization, ANI, genome-comparison]
author: oxo-call-community
source_url: "https://widdowquinn.github.io/pyani"
---

## Concepts

- **Tool Overview**: pyani computes ANI values.
- **Core Function**: Average Nucleotide Identity calculation.
- **Algorithm**: Uses BLAST/ANI methods.
- **Input Format**: Accepts FASTA genome files.
- **Output**: Produces ANI matrix.
- **Use Case**: Taxonomic classification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Genome Completeness**: Affects ANI accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyani --help`
**Explanation:** Shows available options and usage instructions.

### Calculate ANI
**Args:** `pyani run -i genomes/ -o ani_results/`
**Explanation:** Computes ANI between all genomes in directory.

### With parameters
**Args:** `pyani run -i genomes/ -p params.yaml -o ani_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyani -v run -i genomes/ -o ani_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyani -t 4 run -i genomes/ -o ani_results/`
**Explanation:** Uses 4 threads for parallel processing.

### Generate matrix
**Args:** `pyani matrix -i ani_results/ -o matrix.txt`
**Explanation:** Generates ANI distance matrix.

### Generate report
**Args:** `pyani run -i genomes/ -o ani_results/ --report report.html`
**Explanation:** Generates HTML report.
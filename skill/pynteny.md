---
name: pynteny
category: population-genomics
description: Pynteny performs HMM-based synteny analysis across multiple genomes.
tags: [pynteny, population-genomics, synteny, hmm]
author: oxo-call-community
source_url: "https://robaina.github.io/Pynteny/"
---

## Concepts

- **Tool Overview**: pynteny analyzes synteny.
- **Core Function**: Synteny detection.
- **Algorithm**: Uses HMM models.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces synteny blocks.
- **Use Case**: Comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Model Training**: May need training.
- **Genome Quality**: Affects results.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pynteny --help`
**Explanation:** Shows available options and usage instructions.

### Run synteny search
**Args:** `pynteny search -i genomes/ -o synteny.txt`
**Explanation:** Searches for syntenic regions.

### With parameters
**Args:** `pynteny search -i genomes/ -p params.yaml -o synteny.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pynteny -v search -i genomes/ -o synteny.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pynteny -t 4 search -i genomes/ -o synteny.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Train model
**Args:** `pynteny train -i training_data.txt -o model.pkl`
**Explanation:** Trains HMM model.

### Generate report
**Args:** `pynteny search -i genomes/ -o synteny.txt --report report.html`
**Explanation:** Generates HTML report.
---
name: pasty
category: utility
description: PASTy performs in silico serogrouping of Pseudomonas aeruginosa isolates.
tags: [pasty, utility, serogrouping, pseudomonas]
author: oxo-call-community
source_url: "https://github.com/rpetit3/pasty"
---

## Concepts

- **Tool Overview**: PASTy determines serogroups of Pseudomonas aeruginosa.
- **Core Function**: Performs in silico serogroup prediction.
- **Algorithm**: Uses sequence-based serogroup identification.
- **Input Format**: Accepts genome sequences in FASTA format.
- **Output**: Produces serogroup predictions.
- **Use Case**: Clinical microbiology, pathogen typing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on input quality.
- **Database Updates**: Requires updated serogroup database.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pasty --help`
**Explanation:** Shows available options and usage instructions.

### Serogroup prediction
**Args:** `pasty -i genome.fasta -o result.txt`
**Explanation:** Predicts serogroup from genome.

### Batch processing
**Args:** `pasty -d genomes/ -o results/`
**Explanation:** Processes multiple genomes.

### Verbose mode
**Args:** `pasty -v -i genome.fasta -o result.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pasty -t 4 -i genome.fasta -o result.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pasty -i genome.fasta -o result.json --json`
**Explanation:** Outputs in JSON format.

### Database update
**Args:** `pasty_update_db -o new_db/`
**Explanation:** Updates serogroup database.
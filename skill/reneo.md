---
name: reneo
category: qc
description: Reneo unravels viral genomes from metagenomes for viral discovery and analysis.
tags: [reneo, qc, viral-genomics, metagenomics]
author: oxo-call-community
source_url: "https://github.com/Vini2/reneo"
---

## Concepts

- **Tool Overview**: reneo extracts viruses.
- **Core Function**: Viral genome extraction.
- **Algorithm**: Uses classification methods.
- **Input Format**: Accepts metagenomic data.
- **Output**: Produces viral sequences.
- **Use Case**: Viral discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Affects extraction.
- **Parameters**: Must be configured.
- **Runtime**: Extraction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reneo --help`
**Explanation:** Shows available options and usage instructions.

### Extract viruses
**Args:** `reneo extract -i metagenome.fastq -o viral_sequences.fasta`
**Explanation:** Extracts viral genomes from metagenome.

### With parameters
**Args:** `reneo extract -i metagenome.fastq -p params.yaml -o viral_sequences.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reneo -v extract -i metagenome.fastq -o viral_sequences.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reneo -t 4 extract -i metagenome.fastq -o viral_sequences.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `reneo extract -i metagenome.fastq -d viral_db.fasta -o viral_sequences.fasta`
**Explanation:** Uses custom viral database.

### Generate report
**Args:** `reneo extract -i metagenome.fastq -o viral_sequences.fasta --report report.html`
**Explanation:** Generates HTML report.
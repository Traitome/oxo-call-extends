---
name: refgenie
category: population-genomics
description: Refgenie creates a standardized folder structure for reference genome files and indexes for genome management.
tags: [refgenie, population-genomics, genome-management, reference-genomes]
author: oxo-call-community
source_url: "http://refgenie.databio.org"
---

## Concepts

- **Tool Overview**: refgenie manages genomes.
- **Core Function**: Reference genome management.
- **Algorithm**: Uses indexing methods.
- **Input Format**: Accepts genome files.
- **Output**: Produces indexed genomes.
- **Use Case**: Genome indexing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Index Quality**: Affects management.
- **Parameters**: Must be configured.
- **Runtime**: Indexing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `refgenie --help`
**Explanation:** Shows available options and usage instructions.

### Initialize genome
**Args:** `refgenie init -g genome_name -f genome.fasta -o output_dir`
**Explanation:** Initializes reference genome.

### With parameters
**Args:** `refgenie init -g genome_name -f genome.fasta -p params.yaml -o output_dir`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `refgenie -v init -g genome_name -f genome.fasta -o output_dir`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `refgenie -t 4 init -g genome_name -f genome.fasta -o output_dir`
**Explanation:** Uses 4 threads for parallel processing.

### Pull genome
**Args:** `refgenie pull -g genome_name -s source_url -o output_dir`
**Explanation:** Pulls genome from source.

### Generate report
**Args:** `refgenie init -g genome_name -f genome.fasta -o output_dir --report report.html`
**Explanation:** Generates HTML report.
---
name: radiant
category: annotation
description: Radiant annotates proteomes with protein domains for functional analysis.
tags: [radiant, annotation, protein-domains, proteomics]
author: oxo-call-community
source_url: "https://domainworld.uni-muenster.de/data/radiant-db/index.html"
---

## Concepts

- **Tool Overview**: radiant annotates protein domains.
- **Core Function**: Protein domain annotation.
- **Algorithm**: Uses database matching.
- **Input Format**: Accepts protein sequences.
- **Output**: Produces domain annotations.
- **Use Case**: Functional annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large proteomes require memory.
- **Database**: Must be up-to-date.
- **Parameters**: Must be configured.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `radiant --help`
**Explanation:** Shows available options and usage instructions.

### Annotate proteome
**Args:** `radiant annotate -i proteome.fasta -o annotations.txt`
**Explanation:** Annotates protein domains.

### With parameters
**Args:** `radiant annotate -i proteome.fasta -p params.yaml -o annotations.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `radiant -v annotate -i proteome.fasta -o annotations.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `radiant -t 4 annotate -i proteome.fasta -o annotations.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `radiant annotate -i proteome.fasta -d pfam/ -o annotations.txt`
**Explanation:** Uses custom database.

### Generate report
**Args:** `radiant annotate -i proteome.fasta -o annotations.txt --report report.html`
**Explanation:** Generates HTML report.
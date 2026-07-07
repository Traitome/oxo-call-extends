---
name: ratt
category: alignment
description: RATT (Rapid Annotation Transfer Tool) transfers annotations between closely related genomes.
tags: [ratt, alignment, annotation, genome-comparison]
author: oxo-call-community
source_url: "http://ratt.sourceforge.net"
---

## Concepts

- **Tool Overview**: ratt transfers annotations.
- **Core Function**: Annotation transfer.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts genome files.
- **Output**: Produces transferred annotations.
- **Use Case**: Genome annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Genome Similarity**: Affects transfer.
- **Parameters**: Must be configured.
- **Runtime**: Transfer may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ratt --help`
**Explanation:** Shows available options and usage instructions.

### Transfer annotations
**Args:** `ratt transfer -i target.fasta -r reference.fasta -a annotation.gff -o transferred.gff`
**Explanation:** Transfers annotations.

### With parameters
**Args:** `ratt transfer -i target.fasta -p params.yaml -o transferred.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ratt -v transfer -i target.fasta -o transferred.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ratt -t 4 transfer -i target.fasta -o transferred.gff`
**Explanation:** Uses 4 threads for parallel processing.

### With threshold
**Args:** `ratt transfer -i target.fasta -s 0.8 -o transferred.gff`
**Explanation:** Uses similarity threshold.

### Generate report
**Args:** `ratt transfer -i target.fasta -o transferred.gff --report report.html`
**Explanation:** Generates HTML report.
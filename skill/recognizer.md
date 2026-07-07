---
name: recognizer
category: expression
description: reCOGnizer performs domain-based annotation with the COG (Clusters of Orthologous Groups) database.
tags: [recognizer, expression, cog-database, domain-annotation]
author: oxo-call-community
source_url: "https://github.com/iquasere/reCOGnizer/blob/master/README.md"
---

## Concepts

- **Tool Overview**: recognizer annotates domains.
- **Core Function**: COG domain annotation.
- **Algorithm**: Uses database methods.
- **Input Format**: Accepts protein sequences.
- **Output**: Produces COG annotations.
- **Use Case**: Functional annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Quality**: Affects annotation.
- **Parameters**: Must be configured.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recognizer --help`
**Explanation:** Shows available options and usage instructions.

### Annotate domains
**Args:** `recognizer annotate -i proteins.fasta -o cog_annotations.tsv`
**Explanation:** Annotates COG domains.

### With parameters
**Args:** `recognizer annotate -i proteins.fasta -p params.yaml -o cog_annotations.tsv`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recognizer -v annotate -i proteins.fasta -o cog_annotations.tsv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recognizer -t 4 annotate -i proteins.fasta -o cog_annotations.tsv`
**Explanation:** Uses 4 threads for parallel processing.

### With COG database
**Args:** `recognizer annotate -i proteins.fasta -d cog_db.fasta -o cog_annotations.tsv`
**Explanation:** Uses COG database.

### Generate report
**Args:** `recognizer annotate -i proteins.fasta -o cog_annotations.tsv --report report.html`
**Explanation:** Generates HTML report.
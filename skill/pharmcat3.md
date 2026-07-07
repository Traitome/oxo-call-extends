---
name: pharmcat3
category: annotation
description: pharmcat3 provides pharmacogenomics clinical annotation tools.
tags: [pharmcat3, annotation, pharmacogenomics, clinical]
author: oxo-call-community
source_url: "https://github.com/PharmGKB/PharmCAT"
---

## Concepts

- **Tool Overview**: pharmcat3 annotates pharmacogenomics data.
- **Core Function**: Provides clinical annotation pipeline.
- **Algorithm**: Uses pharmacogenomics annotation methods.
- **Input Format**: Accepts genetic data files.
- **Output**: Produces clinical annotation results.
- **Use Case**: Pharmacogenomics, clinical annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Clinical Database**: Requires proper clinical database.
- **Genotype Quality**: Results depend on genotype quality.
- **Runtime**: Annotation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pharmcat3 --help`
**Explanation:** Shows available options and usage instructions.

### Annotate genotypes
**Args:** `pharmcat3 -i genotypes.txt -o annotations.txt`
**Explanation:** Annotates pharmacogenomics genotypes.

### With database
**Args:** `pharmcat3 -i genotypes.txt -d clinical_db.fasta -o annotations.txt`
**Explanation:** Uses specific clinical database.

### Verbose mode
**Args:** `pharmcat3 -v -i genotypes.txt -o annotations.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pharmcat3 -t 4 -i genotypes.txt -o annotations.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pharmcat3 -i genotypes.txt -o annotations.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pharmcat3 -i genotypes.txt -o annotations.txt --report report.html`
**Explanation:** Generates HTML report.
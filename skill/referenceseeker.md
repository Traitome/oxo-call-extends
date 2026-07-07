---
name: referenceseeker
category: programming
description: ReferenceSeeker rapidly determines appropriate reference genomes for comparative genomics.
tags: [referenceseeker, programming, reference-genomes, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/oschwengers/referenceseeker"
---

## Concepts

- **Tool Overview**: referenceseeker finds references.
- **Core Function**: Reference genome selection.
- **Algorithm**: Uses comparison methods.
- **Input Format**: Accepts query genomes.
- **Output**: Produces reference rankings.
- **Use Case**: Comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Genome Quality**: Affects selection.
- **Parameters**: Must be configured.
- **Runtime**: Selection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `referenceseeker --help`
**Explanation:** Shows available options and usage instructions.

### Find reference
**Args:** `referenceseeker find -i query.fasta -o reference_rankings.txt`
**Explanation:** Finds appropriate reference genomes.

### With parameters
**Args:** `referenceseeker find -i query.fasta -p params.yaml -o reference_rankings.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `referenceseeker -v find -i query.fasta -o reference_rankings.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `referenceseeker -t 4 find -i query.fasta -o reference_rankings.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `referenceseeker find -i query.fasta -d ref_db.fasta -o reference_rankings.txt`
**Explanation:** Uses reference database.

### Generate report
**Args:** `referenceseeker find -i query.fasta -o reference_rankings.txt --report report.html`
**Explanation:** Generates HTML report.
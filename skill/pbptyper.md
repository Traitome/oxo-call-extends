---
name: pbptyper
category: assembly
description: pbptyper performs in silico PBP typing for Streptococcus pneumoniae assemblies.
tags: [pbptyper, assembly, pbp, typing, streptococcus]
author: oxo-call-community
source_url: "https://github.com/rpetit3/pbptyper"
---

## Concepts

- **Tool Overview**: pbptyper types PBP alleles.
- **Core Function**: Identifies PBP types in S. pneumoniae.
- **Algorithm**: Uses sequence alignment and typing.
- **Input Format**: Accepts genome assemblies.
- **Output**: Produces PBP type assignments.
- **Use Case**: Bacterial typing, antibiotic resistance.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Depends on assembly size.
- **Species Specific**: Designed for S. pneumoniae only.
- **Database Quality**: Results depend on reference database.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbptyper --help`
**Explanation:** Shows available options and usage instructions.

### Type PBP alleles
**Args:** `pbptyper -i assembly.fasta -o pbp_types.txt`
**Explanation:** Types PBP alleles from assembly.

### With database
**Args:** `pbptyper -i assembly.fasta -d pbp_database.fasta -o pbp_types.txt`
**Explanation:** Uses custom PBP database.

### Verbose mode
**Args:** `pbptyper -v -i assembly.fasta -o pbp_types.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbptyper -t 4 -i assembly.fasta -o pbp_types.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbptyper -i assembly.fasta -o pbp_types.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pbptyper -i assembly.fasta -o pbp_types.txt --report report.html`
**Explanation:** Generates HTML report.
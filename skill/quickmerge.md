---
name: quickmerge
category: assembly
description: QuickMerge improves contiguity of genome assemblies using long molecule sequences and linked-reads.
tags: [quickmerge, assembly, genome-assembly, scaffolding]
author: oxo-call-community
source_url: "https://github.com/mahulchak/quickmerge"
---

## Concepts

- **Tool Overview**: quickmerge merges assemblies.
- **Core Function**: Assembly improvement.
- **Algorithm**: Uses overlap detection.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces improved assembly.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Sequence Quality**: Affects merging.
- **Parameters**: Must be configured.
- **Runtime**: Merging may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quickmerge --help`
**Explanation:** Shows available options and usage instructions.

### Run merge
**Args:** `quickmerge merge -i assembly.fasta -l long_reads.fasta -o merged.fasta`
**Explanation:** Merges assembly with long reads.

### With parameters
**Args:** `quickmerge merge -i assembly.fasta -p params.yaml -o merged.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quickmerge -v merge -i assembly.fasta -o merged.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quickmerge -t 4 merge -i assembly.fasta -o merged.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With gap filling
**Args:** `quickmerge merge -i assembly.fasta -g -o merged.fasta`
**Explanation:** Enables gap filling.

### Generate report
**Args:** `quickmerge merge -i assembly.fasta -o merged.fasta --report report.html`
**Explanation:** Generates HTML report.
---
name: ref-solver
category: formatting
description: Ref-Solver identifies reference genomes from BAM/SAM headers for sequence analysis.
tags: [ref-solver, formatting, bam, sam, reference-genome]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/ref-solver/blob/v0.3.0/README.md"
---

## Concepts

- **Tool Overview**: ref-solver identifies references.
- **Core Function**: Reference genome identification.
- **Algorithm**: Uses parsing methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces reference info.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Header Quality**: Affects identification.
- **Parameters**: Must be configured.
- **Runtime**: Identification may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ref-solver --help`
**Explanation:** Shows available options and usage instructions.

### Solve reference
**Args:** `ref-solver solve -i alignment.bam -o reference_info.txt`
**Explanation:** Identifies reference from BAM header.

### With parameters
**Args:** `ref-solver solve -i alignment.bam -p params.yaml -o reference_info.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ref-solver -v solve -i alignment.bam -o reference_info.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ref-solver -t 4 solve -i alignment.bam -o reference_info.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `ref-solver solve -i alignment.bam -d ref_db.fasta -o reference_info.txt`
**Explanation:** Uses reference database.

### Generate report
**Args:** `ref-solver solve -i alignment.bam -o reference_info.txt --report report.html`
**Explanation:** Generates HTML report.
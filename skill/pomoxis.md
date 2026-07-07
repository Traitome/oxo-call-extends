---
name: pomoxis
category: qc
description: pomoxis provides assembly and consensus tools for nanopore data.
tags: [pomoxis, qc, nanopore, assembly]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/pomoxis"
---

## Concepts

- **Tool Overview**: pomoxis processes nanopore sequencing data.
- **Core Function**: Assembly, consensus, and analysis.
- **Algorithm**: Uses ONT research methods.
- **Input Format**: Accepts nanopore sequencing reads.
- **Output**: Produces assemblies and consensus sequences.
- **Use Case**: Nanopore data analysis, genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Assembly Accuracy**: May have assembly errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pomoxis --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `pomoxis assemble -i reads.fastq -o assembly/`
**Explanation:** Assembles nanopore sequencing data.

### With parameters
**Args:** `pomoxis assemble -i reads.fastq -p params.yaml -o assembly/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pomoxis -v assemble -i reads.fastq -o assembly/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pomoxis -t 4 assemble -i reads.fastq -o assembly/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pomoxis assemble -i reads.fastq -o assembly.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `pomoxis assemble -i reads.fastq -o assembly/ --report report.html`
**Explanation:** Generates HTML report.
---
name: pyfastaq
category: formatting
description: pyfastaq is a tool for manipulating FASTA and FASTQ files.
tags: [pyfastaq, formatting, fasta, fastq]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/Fastaq"
---

## Concepts

- **Tool Overview**: pyfastaq manipulates sequence files.
- **Core Function**: FASTA/FASTQ processing.
- **Algorithm**: Uses sequence parsing.
- **Input Format**: Accepts FASTA/FASTQ files.
- **Output**: Produces sequence files.
- **Use Case**: Sequence manipulation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Format Compatibility**: Must match input type.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyfastaq --help`
**Explanation:** Shows available options and usage instructions.

### Convert FASTQ to FASTA
**Args:** `pyfastaq fastq_to_fasta -i reads.fastq -o reads.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### With parameters
**Args:** `pyfastaq fastq_to_fasta -i reads.fastq -p params.yaml -o reads.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyfastaq -v fastq_to_fasta -i reads.fastq -o reads.fasta`
**Explanation:** Runs with verbose output.

### Reverse complement
**Args:** `pyfastaq reverse_complement -i sequence.fasta -o rc.fasta`
**Explanation:** Creates reverse complement.

### Trim reads
**Args:** `pyfastaq trim -i reads.fastq -l 100 -o trimmed.fastq`
**Explanation:** Trims sequences to length.

### Generate report
**Args:** `pyfastaq fastq_to_fasta -i reads.fastq -o reads.fasta --report report.html`
**Explanation:** Generates HTML report.
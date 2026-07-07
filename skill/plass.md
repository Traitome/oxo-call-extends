---
name: plass
category: assembly
description: plass performs protein-level sequence assembly.
tags: [plass, assembly, protein, sequence]
author: oxo-call-community
source_url: "https://github.com/soedinglab/plass"
---

## Concepts

- **Tool Overview**: plass assembles sequences at protein level.
- **Core Function**: Protein-level sequence assembly.
- **Algorithm**: Uses protein-guided assembly methods.
- **Input Format**: Accepts short read sequencing files.
- **Output**: Produces protein or DNA contigs.
- **Use Case**: Metagenomics, protein sequence assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Assembly Accuracy**: May have assembly errors.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plass --help`
**Explanation:** Shows available options and usage instructions.

### Assemble reads
**Args:** `plass assemble -i reads.fastq -o contigs.fasta`
**Explanation:** Assembles short reads into contigs.

### With parameters
**Args:** `plass assemble -i reads.fastq -p params.yaml -o contigs.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plass assemble -v -i reads.fastq -o contigs.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plass assemble -t 4 -i reads.fastq -o contigs.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plass assemble -i reads.fastq -o contigs.protein --protein`
**Explanation:** Outputs protein sequences.

### Generate report
**Args:** `plass assemble -i reads.fastq -o contigs.fasta --report report.html`
**Explanation:** Generates HTML report.
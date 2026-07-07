---
name: ribotin
category: assembly
description: RiboTin assembles ribosomal DNA sequences.
tags: [ribotin, assembly, rdna, ribosomal-dna]
author: oxo-call-community
source_url: "https://github.com/maickrau/ribotin/blob/v1.5/README.md"
---

## Concepts

- **Tool Overview**: ribotin assembles rDNA.
- **Core Function**: Ribosomal DNA assembly.
- **Algorithm**: Uses assembly methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces rDNA contigs.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Repeat Complexity**: Affects assembly.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ribotin --help`
**Explanation:** Shows available options and usage instructions.

### Assemble rDNA
**Args:** `ribotin assemble -i reads.fastq -o assembly/`
**Explanation:** Assembles ribosomal DNA.

### With parameters
**Args:** `ribotin assemble -i reads.fastq -p params.yaml -o assembly/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ribotin -v assemble -i reads.fastq -o assembly/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ribotin -t 4 assemble -i reads.fastq -o assembly/`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `ribotin assemble -i reads.fastq -r reference.fasta -o assembly/`
**Explanation:** Uses reference sequence.

### Generate report
**Args:** `ribotin assemble -i reads.fastq -o assembly/ --report report.html`
**Explanation:** Generates HTML report.
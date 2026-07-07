---
name: ra
category: alignment
description: RA (RNA Assembler) is a C++ implementation of an overlap-layout-consensus transcriptome assembler.
tags: [ra, alignment, transcriptome, assembly]
author: oxo-call-community
source_url: "https://github.com/mariokostelac/ra"
---

## Concepts

- **Tool Overview**: ra assembles transcripts.
- **Core Function**: Transcriptome assembly.
- **Algorithm**: Uses overlap-layout-consensus.
- **Input Format**: Accepts RNA-seq reads.
- **Output**: Produces transcripts.
- **Use Case**: Transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects assembly.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ra --help`
**Explanation:** Shows available options and usage instructions.

### Assemble transcripts
**Args:** `ra assemble -i reads.fastq -o transcripts.fasta`
**Explanation:** Assembles transcriptome.

### With parameters
**Args:** `ra assemble -i reads.fastq -p params.yaml -o transcripts.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ra -v assemble -i reads.fastq -o transcripts.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ra -t 4 assemble -i reads.fastq -o transcripts.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Paired-end mode
**Args:** `ra assemble -i reads_1.fastq -j reads_2.fastq -o transcripts.fasta`
**Explanation:** Processes paired-end reads.

### Generate report
**Args:** `ra assemble -i reads.fastq -o transcripts.fasta --report report.html`
**Explanation:** Generates HTML report.
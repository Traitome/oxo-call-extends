---
name: razers3
category: alignment
description: RazerS 3 provides faster, fully sensitive read mapping for high-throughput sequencing data.
tags: [razers3, alignment, read-mapping, sequencing]
author: oxo-call-community
source_url: "https://www.seqan.de/apps/razers3.html"
---

## Concepts

- **Tool Overview**: razers3 maps reads.
- **Core Function**: Read mapping.
- **Algorithm**: Uses sensitive methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces alignments.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects mapping.
- **Parameters**: Must be configured.
- **Runtime**: Mapping may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `razers3 --help`
**Explanation:** Shows available options and usage instructions.

### Map reads
**Args:** `razers3 map -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Maps reads to reference.

### With parameters
**Args:** `razers3 map -i reads.fastq -p params.yaml -o alignments.sam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `razers3 -v map -i reads.fastq -o alignments.sam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `razers3 -t 4 map -i reads.fastq -o alignments.sam`
**Explanation:** Uses 4 threads for parallel processing.

### With error rate
**Args:** `razers3 map -i reads.fastq -e 0.05 -o alignments.sam`
**Explanation:** Uses specific error rate.

### Generate report
**Args:** `razers3 map -i reads.fastq -o alignments.sam --report report.html`
**Explanation:** Generates HTML report.
---
name: ratatosk
category: utility
description: Ratatosk performs hybrid error correction of long reads using colored de Bruijn graphs.
tags: [ratatosk, utility, error-correction, long-reads]
author: oxo-call-community
source_url: "https://github.com/DecodeGenetics/Ratatosk/blob/v0.9.0/README.md"
---

## Concepts

- **Tool Overview**: ratatosk corrects reads.
- **Core Function**: Hybrid error correction.
- **Algorithm**: Uses de Bruijn graphs.
- **Input Format**: Accepts long reads.
- **Output**: Produces corrected reads.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects correction.
- **Parameters**: Must be configured.
- **Runtime**: Correction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ratatosk --help`
**Explanation:** Shows available options and usage instructions.

### Correct reads
**Args:** `ratatosk correct -i long_reads.fastq -s short_reads.fastq -o corrected.fastq`
**Explanation:** Corrects long reads.

### With parameters
**Args:** `ratatosk correct -i long_reads.fastq -p params.yaml -o corrected.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ratatosk -v correct -i long_reads.fastq -o corrected.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ratatosk -t 4 correct -i long_reads.fastq -o corrected.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `ratatosk correct -i long_reads.fastq -k 21 -o corrected.fastq`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `ratatosk correct -i long_reads.fastq -o corrected.fastq --report report.html`
**Explanation:** Generates HTML report.
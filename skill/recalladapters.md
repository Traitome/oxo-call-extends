---
name: recalladapters
category: qc
description: RecallAdapters is a tool to recall adapters for PacBio sequencing data quality control.
tags: [recalladapters, qc, pacbio, adapter-removal]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: recalladapters recalls adapters.
- **Core Function**: Adapter detection.
- **Algorithm**: Uses scanning methods.
- **Input Format**: Accepts PacBio reads.
- **Output**: Produces adapter info.
- **Use Case**: PacBio QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recalladapters --help`
**Explanation:** Shows available options and usage instructions.

### Recall adapters
**Args:** `recalladapters recall -i pacbio_reads.fastq -o adapters.txt`
**Explanation:** Recalls adapter sequences.

### With parameters
**Args:** `recalladapters recall -i pacbio_reads.fastq -p params.yaml -o adapters.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recalladapters -v recall -i pacbio_reads.fastq -o adapters.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recalladapters -t 4 recall -i pacbio_reads.fastq -o adapters.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Remove adapters
**Args:** `recalladapters remove -i pacbio_reads.fastq -a adapters.txt -o clean_reads.fastq`
**Explanation:** Removes adapter sequences.

### Generate report
**Args:** `recalladapters recall -i pacbio_reads.fastq -o adapters.txt --report report.html`
**Explanation:** Generates HTML report.
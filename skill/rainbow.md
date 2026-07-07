---
name: rainbow
category: hpc
description: Rainbow efficiently clusters and assembles short reads, especially for RAD (Restriction site Associated DNA) sequencing data.
tags: [rainbow, hpc, clustering, assembly]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/bio-rainbow"
---

## Concepts

- **Tool Overview**: rainbow clusters reads.
- **Core Function**: Read clustering and assembly.
- **Algorithm**: Uses clustering methods.
- **Input Format**: Accepts short reads.
- **Output**: Produces assembled contigs.
- **Use Case**: RAD-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects clustering.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rainbow --help`
**Explanation:** Shows available options and usage instructions.

### Cluster reads
**Args:** `rainbow cluster -i reads.fastq -o clusters.txt`
**Explanation:** Clusters similar reads.

### With parameters
**Args:** `rainbow cluster -i reads.fastq -p params.yaml -o clusters.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rainbow -v cluster -i reads.fastq -o clusters.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rainbow -t 4 cluster -i reads.fastq -o clusters.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Assemble clusters
**Args:** `rainbow assemble -i clusters.txt -o contigs.fasta`
**Explanation:** Assembles read clusters.

### Generate report
**Args:** `rainbow cluster -i reads.fastq -o clusters.txt --report report.html`
**Explanation:** Generates HTML report.
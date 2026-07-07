---
name: ngspeciesid
category: metagenomics
description: NGSpeciesID performs reference-free clustering and consensus forming for long-read amplicon sequencing.
tags: [ngspeciesid, metagenomics, long-reads, clustering]
author: oxo-call-community
source_url: "https://github.com/ksahlin/NGSpeciesID"
---

## Concepts

- **Tool Overview**: NGSpeciesID clusters long-read amplicon sequences and generates consensus sequences.
- **Core Function**: Groups similar sequences and creates consensus sequences.
- **Algorithm**: Uses isONclust clustering with consensus and polishing features.
- **Input Format**: Accepts FASTQ files with long reads.
- **Output**: Produces clustered sequences and consensus sequences.
- **Use Case**: Amplicon sequencing analysis, species identification, and metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Quality**: Results depend on input read quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Clustering can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Primer Removal**: Requires proper primer sequences.

## Examples

### Display help
**Args:** `ngspeciesid --help`
**Explanation:** Shows available options and usage instructions.

### Basic clustering
**Args:** `ngspeciesid --reads reads.fastq --out output/`
**Explanation:** Clusters reads and generates consensus.

### Primer removal
**Args:** `ngspeciesid --reads reads.fastq --primer_fwd forward.fasta --primer_rev reverse.fasta --out output/`
**Explanation:** Removes primers before clustering.

### Minimum read count
**Args:** `ngspeciesid --reads reads.fastq --min_reads 10 --out output/`
**Explanation:** Sets minimum reads per cluster.

### Threads
**Args:** `ngspeciesid --reads reads.fastq --threads 8 --out output/`
**Explanation:** Uses 8 threads for parallel processing.

### Polishing
**Args:** `ngspeciesid --reads reads.fastq --polish --out output/`
**Explanation:** Enables consensus polishing.

### Verbose mode
**Args:** `ngspeciesid --reads reads.fastq --verbose --out output/`
**Explanation:** Runs with verbose output.
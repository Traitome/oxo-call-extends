---
name: owl
category: utility
description: OWL performs microsatellite analysis for HiFi sequencing data.
tags: [owl, utility, microsatellite, hifi-sequencing]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/owl"
---

## Concepts

- **Tool Overview**: OWL analyzes microsatellites in HiFi sequencing data.
- **Core Function**: Identifies and characterizes microsatellite repeats.
- **Algorithm**: Uses pattern matching for repeat detection.
- **Input Format**: Accepts BAM files and reference sequences.
- **Output**: Produces microsatellite calls and statistics.
- **Use Case**: Genome analysis, microsatellite instability, and genetic variation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Repeat Complexity**: Complex repeats may be missed.
- **Reference Bias**: Results depend on reference quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `owl --help`
**Explanation:** Shows available options and usage instructions.

### Analyze microsatellites
**Args:** `owl analyze -i alignments.bam -r reference.fasta -o microsatellites.txt`
**Explanation:** Identifies microsatellites in HiFi data.

### With VCF output
**Args:** `owl analyze -i alignments.bam -r reference.fasta -o microsatellites.vcf --vcf`
**Explanation:** Outputs in VCF format.

### Statistics
**Args:** `owl stats -i microsatellites.txt -o stats.txt`
**Explanation:** Generates statistics report.

### Verbose mode
**Args:** `owl analyze -i alignments.bam -v -o microsatellites.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `owl batch -d bams/ -r reference.fasta -o results/`
**Explanation:** Processes multiple samples.

### Repeat filtering
**Args:** `owl analyze -i alignments.bam -r reference.fasta -m 10 -o microsatellites.txt`
**Explanation:** Sets minimum repeat length.
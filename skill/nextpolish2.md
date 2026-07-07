---
name: nextpolish2
category: assembly
description: NextPolish2 is a repeat-aware genome polishing tool for HiFi long-read assemblies.
tags: [nextpolish2, assembly, polishing, hifi, long-reads]
author: oxo-call-community
source_url: "https://github.com/Nextomics/NextPolish2"
---

## Concepts

- **Tool Overview**: NextPolish2 polishes genome assemblies using HiFi long reads.
- **Core Function**: Improves assembly accuracy through repeat-aware polishing.
- **Algorithm**: Uses mapping-based consensus calling with repeat handling.
- **Input Format**: Accepts FASTA assembly and HiFi read FASTQ files.
- **Output**: Produces polished genome assembly.
- **Use Case**: Genome assembly improvement, especially for complex regions.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Quality**: Results depend on HiFi read quality.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Polishing can be computationally intensive.
- **Repeat Regions**: Complex repeats may require additional handling.
- **Reference Dependencies**: Requires proper input file preparation.

## Examples

### Display help
**Args:** `nextPolish2 --help`
**Explanation:** Shows available options and usage instructions.

### Basic polishing
**Args:** `nextPolish2 -g assembly.fasta -r hifi_reads.fastq -o polished.fasta`
**Explanation:** Polishes assembly with HiFi reads.

### Multiple read files
**Args:** `nextPolish2 -g assembly.fasta -r reads1.fastq reads2.fastq -o polished.fasta`
**Explanation:** Uses multiple read files for polishing.

### Quality threshold
**Args:** `nextPolish2 -g assembly.fasta -r hifi_reads.fastq -q 30 -o polished.fasta`
**Explanation:** Filters reads by quality score.

### Threads
**Args:** `nextPolish2 -g assembly.fasta -r hifi_reads.fastq -t 16 -o polished.fasta`
**Explanation:** Uses 16 threads for parallel processing.

### Output VCF
**Args:** `nextPolish2 -g assembly.fasta -r hifi_reads.fastq --vcf -o polished.fasta`
**Explanation:** Outputs variant calls in VCF format.

### Debug mode
**Args:** `nextPolish2 -g assembly.fasta -r hifi_reads.fastq -d -o polished.fasta`
**Explanation:** Enables debug mode for troubleshooting.
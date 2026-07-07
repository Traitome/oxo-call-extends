---
name: remag
category: assembly
description: ReMag recovers high-quality eukaryotic genomes from complex metagenomes for metagenomic analysis.
tags: [remag, assembly, metagenomics, eukaryotic-genomes]
author: oxo-call-community
source_url: "https://github.com/danielzmbp/remag"
---

## Concepts

- **Tool Overview**: remag recovers genomes.
- **Core Function**: Eukaryotic genome recovery.
- **Algorithm**: Uses binning methods.
- **Input Format**: Accepts metagenomic reads.
- **Output**: Produces eukaryotic genomes.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Community Complexity**: Affects recovery.
- **Parameters**: Must be configured.
- **Runtime**: Recovery may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `remag --help`
**Explanation:** Shows available options and usage instructions.

### Recover genome
**Args:** `remag recover -i metagenome.fastq -o recovered_genome.fasta`
**Explanation:** Recovers eukaryotic genome from metagenome.

### With parameters
**Args:** `remag recover -i metagenome.fastq -p params.yaml -o recovered_genome.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `remag -v recover -i metagenome.fastq -o recovered_genome.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `remag -t 4 recover -i metagenome.fastq -o recovered_genome.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With coverage
**Args:** `remag recover -i metagenome.fastq -c 10 -o recovered_genome.fasta`
**Explanation:** Uses coverage threshold.

### Generate report
**Args:** `remag recover -i metagenome.fastq -o recovered_genome.fasta --report report.html`
**Explanation:** Generates HTML report.
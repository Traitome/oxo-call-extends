---
name: hapog
category: bioinformatics
description: HapOG performs haplotype-aware polishing of genome assemblies.
tags: [hapog, genome-polishing, haplotype-aware, bioinformatics]
author: oxo-call-community
source_url: "https://www.genoscope.cns.fr/hapog"
---

## Concepts

- **Haplotype-Aware Polishing**: HapOG performs haplotype-aware genome polishing.

- **Genome Assembly**: Improves genome assembly quality.

- **Long Read Data**: Optimized for long read sequencing data.

- **Haplotype Resolution**: Resolves individual haplotypes during polishing.

- **Error Correction**: Corrects sequencing errors in assemblies.

- **Diploid Genomes**: Handles diploid genome polishing.

## Pitfalls

- **Read Depth**: Requires sufficient sequencing depth.

- **Haplotype Diversity**: High diversity may complicate polishing.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large genomes may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Polish genome
**Args:** `hapog -i assembly.fasta -r reads.fastq -o polished.fasta`
**Explanation:** Polishes genome assembly with long reads.

### Haplotype-aware polishing
**Args:** `hapog -i assembly.fasta -r reads.fastq -haplotype -o polished.fasta`
**Explanation:** Performs haplotype-aware polishing.

### With phased variants
**Args:** `hapog -i assembly.fasta -r reads.fastq -vcf phased.vcf -o polished.fasta`
**Explanation:** Uses phased variants for improved polishing.

### Batch processing
**Args:** `for f in *.fasta; do hapog -i $f -r reads.fastq -o ${f%.fasta}_polished.fasta; done`
**Explanation:** Processes multiple assembly files.

### Quality filtering
**Args:** `hapog -i assembly.fasta -r reads.fastq -q 20 -o polished.fasta`
**Explanation:** Filters reads by quality score.

### Generate statistics
**Args:** `hapog -i assembly.fasta -r reads.fastq -stats -o stats.txt`
**Explanation:** Generates polishing statistics.

### Help command
**Args:** `hapog --help`
**Explanation:** Shows available options and usage information.
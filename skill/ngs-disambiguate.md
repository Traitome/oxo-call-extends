---
name: ngs-disambiguate
category: alignment
description: NGS-disambiguate distinguishes reads aligned to mixed human-mouse genomes.
tags: [ngs-disambiguate, alignment, human-mouse, disambiguation]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/disambiguate"
---

## Concepts

- **Tool Overview**: NGS-disambiguate separates reads from mixed species alignments.
- **Core Function**: Identifies reads originating from human or mouse in xenograft experiments.
- **Algorithm**: Compares mapping quality scores between species.
- **Input Format**: Accepts BAM files aligned to combined genomes.
- **Output**: Produces species-specific BAM files and statistics.
- **Use Case**: Xenograft sequencing, chimeric analysis, and contamination detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Alignment Quality**: Results depend on mapping quality.
- **Genome Combination**: Requires properly combined reference genomes.
- **Memory Usage**: Large datasets require memory.
- **Threshold Settings**: Requires careful threshold tuning.
- **Ambiguous Reads**: Some reads may remain ambiguous.

## Examples

### Display help
**Args:** `ngs-disambiguate --help`
**Explanation:** Shows available options and usage instructions.

### Basic disambiguation
**Args:** `ngs-disambiguate -i alignment.bam -o output/`
**Explanation:** Separates human and mouse reads.

### Specify species
**Args:** `ngs-disambiguate -i alignment.bam -s human,mouse -o output/`
**Explanation:** Specifies species order.

### Quality threshold
**Args:** `ngs-disambiguate -i alignment.bam -q 30 -o output/`
**Explanation:** Sets mapping quality threshold.

### Output statistics
**Args:** `ngs-disambiguate -i alignment.bam -o output/ --stats`
**Explanation:** Generates statistics report.

### Force mode
**Args:** `ngs-disambiguate -i alignment.bam -o output/ -f`
**Explanation:** Forces processing even with warnings.

### Threads
**Args:** `ngs-disambiguate -i alignment.bam -o output/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.
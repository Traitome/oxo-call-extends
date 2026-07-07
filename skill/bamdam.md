---
name: bamdam
category: alignment
description: bamdam - Post-mapping toolkit for ancient DNA analysis
tags: [bamdam, alignment, BAM, ancient-dna, aDNA]
author: oxo-call-community
source_url: "https://github.com/bdesanctis/bamdam"
---

## Concepts

- **Tool Overview**: bamdam is a post-mapping, post-least-common-ancestor toolkit specifically designed for ancient DNA (aDNA) analysis. Version 0.4.3.
- **Core Function**: Processes aligned ancient DNA reads to assess damage patterns and authenticity.
- **Damage Analysis**: Identifies characteristic aDNA damage patterns (e.g., C->T transitions at read ends).
- **LCA Processing**: Works with least-common-ancestor mapped reads for metagenomic aDNA analysis.
- **Authenticity Assessment**: Helps validate ancient DNA authenticity through damage signatures.
- **Input/Output**: Accepts BAM alignment files, outputs damage statistics and filtered alignments.
- **Installation**: `conda install -c bioconda bamdam`.

## Pitfalls

- **Ancient DNA Specific**: Designed for ancient DNA. Modern DNA may produce unexpected results.
- **Damage Patterns**: Requires sufficient sequencing depth to detect damage patterns.
- **Contamination**: Modern DNA contamination can obscure true damage patterns.
- **Reference Quality**: Requires appropriate reference genomes for accurate LCA mapping.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Basic damage analysis
**Args:** `bamdam damage -i alignments.bam -o damage_stats.txt`
**Explanation:** Analyzes aDNA damage patterns in aligned reads.

### LCA filtering
**Args:** `bamdam lca -i lca_alignments.bam -o filtered.bam`
**Explanation:** Filters LCA-mapped reads for downstream analysis.

### Damage filtering
**Args:** `bamdam filter -i alignments.bam -o filtered.bam --min-damage 0.1`
**Explanation:** Filters reads based on damage level threshold.

### Statistics generation
**Args:** `bamdam stats -i alignments.bam -o stats.txt`
**Explanation:** Generates comprehensive statistics about aDNA alignments.

### Verbose mode
**Args:** `bamdam damage -i alignments.bam -o stats.txt -v`
**Explanation:** Shows detailed damage analysis progress.

### Custom quality threshold
**Args:** `bamdam filter -i alignments.bam -o filtered.bam --min-qual 30`
**Explanation:** Filters reads with minimum mapping quality.

### Display help
**Args:** `bamdam --help`
**Explanation:** Shows all available command-line options and usage information.
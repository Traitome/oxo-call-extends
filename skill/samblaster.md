---
name: samblaster
category: alignment
description: Mark duplicates and extract discordant/split reads from SAM files
tags: ["samblaster", "duplicate marking", "discordant reads", "split reads", "SV detection"]
author: oxo-call-community
source_url: "https://github.com/GregoryFaust/samblaster/blob/v.0.1.26/README.md"
---

## Concepts

- **Tool Overview**: Samblaster (v0.1.26) is a lightweight tool for marking duplicates and extracting discordant and split reads from SAM/BAM files, commonly used in structural variant detection pipelines.
- **Core Function**: Identifies and marks duplicate reads, extracts discordant read pairs (potential SVs), and identifies split reads (translocations, inversions).
- **Algorithm**: Uses efficient duplicate marking algorithm based on read coordinates and UMIs, detects discordant pairs by checking mapping orientation and distance.
- **Input Format**: SAM/BAM alignment files, optionally with UMI tags.
- **Output Format**: Deduplicated SAM/BAM, discordant read files, split read files, statistics.
- **Use Case**: Preprocessing for variant calling, structural variant detection, quality control.

## Pitfalls

- **Input sorting**: Requires coordinate-sorted input for proper duplicate marking.
- **UMI handling**: UMI-based deduplication requires proper UMI tagging.
- **Memory usage**: Large BAM files require significant memory.
- **Paired-end only**: Optimized for paired-end sequencing data.
- **SV detection**: Discordant reads alone may not confirm structural variants.
- **Performance**: May be slower than dedicated duplicate marking tools for large files.

## Examples

### Mark duplicates
**Args:** `samblaster -i input.sam -o deduplicated.sam`
**Explanation:** `-i` input SAM; `-o` deduplicated output.

### Extract discordant reads
**Args:** `samblaster -i input.sam -d discordant.sam`
**Explanation:** `-d` output file for discordant read pairs.

### Extract split reads
**Args:** `samblaster -i input.sam -s split.sam`
**Explanation:** `-s` output file for split reads.

### UMI-based deduplication
**Args:** `samblaster -i input.sam -o deduplicated.sam --umi-tag UB`
**Explanation:** `--umi-tag` specifies UMI tag (e.g., UB).

### Output stats
**Args:** `samblaster -i input.sam -o deduplicated.sam -t stats.txt`
**Explanation:** `-t` output statistics file.

### Stream mode
**Args:** `samtools view -h input.bam | samblaster | samtools view -Sb -o output.bam`
**Explanation:** Pipeline-friendly streaming mode.

### Force processing
**Args:** `samblaster -i input.sam -o deduplicated.sam --force`
**Explanation:** `--force` processes unsorted input (not recommended).
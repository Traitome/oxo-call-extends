---
name: nxtrim
category: qc
description: NxTrim removes Nextera Mate Pair adapters and categorizes reads based on adapter orientation.
tags: [nxtrim, qc, adapter-trimming, mate-pair]
author: oxo-call-community
source_url: "https://github.com/sequencing/NxTrim"
---

## Concepts

- **Tool Overview**: NxTrim trims Nextera Mate Pair adapters and categorizes read orientations.
- **Core Function**: Removes adapters and classifies reads based on adapter location.
- **Algorithm**: Uses sequence matching for adapter detection and trimming.
- **Input Format**: Accepts FASTQ sequencing reads.
- **Output**: Produces trimmed reads with orientation categories.
- **Use Case**: Mate-pair sequencing data processing, adapter trimming, and QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Adapter Sequence**: Requires correct adapter sequence.
- **Read Quality**: Results depend on input read quality.
- **Orientation Detection**: May miscategorize some reads.
- **Memory Usage**: Large datasets require memory.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `nxtrim --help`
**Explanation:** Shows available options and usage instructions.

### Trim adapters
**Args:** `nxtrim -1 reads_1.fastq -2 reads_2.fastq -o trimmed/`
**Explanation:** Trims adapters from paired-end reads.

### Single-end mode
**Args:** `nxtrim -s reads.fastq -o trimmed/`
**Explanation:** Processes single-end reads.

### Output categories
**Args:** `nxtrim -1 reads_1.fastq -2 reads_2.fastq -o trimmed/ --cat all`
**Explanation:** Outputs all read categories.

### Minimum length
**Args:** `nxtrim -1 reads_1.fastq -2 reads_2.fastq -o trimmed/ -m 50`
**Explanation:** Sets minimum trimmed read length to 50.

### Quality filtering
**Args:** `nxtrim -1 reads_1.fastq -2 reads_2.fastq -o trimmed/ -q 30`
**Explanation:** Filters by minimum quality score.

### Verbose mode
**Args:** `nxtrim -1 reads_1.fastq -2 reads_2.fastq -o trimmed/ -v`
**Explanation:** Runs with verbose output.
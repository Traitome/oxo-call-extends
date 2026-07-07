---
name: reviewer
category: alignment
description: REViewer visualizes alignments of reads in tandem repeat regions.
tags: [reviewer, alignment, visualization, tandem-repeats]
author: oxo-call-community
source_url: "https://github.com/Illumina/REViewer"
---

## Concepts

- **Tool Overview**: reviewer visualizes alignments.
- **Core Function**: Alignment visualization.
- **Algorithm**: Uses graphical methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces visualizations.
- **Use Case**: Repeat analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Repeat Complexity**: Affects visualization.
- **Parameters**: Must be configured.
- **Runtime**: Visualization may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reviewer --help`
**Explanation:** Shows available options and usage instructions.

### Visualize alignment
**Args:** `reviewer view -i alignments.bam -r region.bed -o visualization.png`
**Explanation:** Visualizes reads in tandem repeat regions.

### With parameters
**Args:** `reviewer view -i alignments.bam -p params.yaml -o visualization.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reviewer -v view -i alignments.bam -o visualization.png`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reviewer -t 4 view -i alignments.bam -o visualization.png`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `reviewer view -i alignments.bam -r reference.fasta -o visualization.png`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `reviewer view -i alignments.bam -o visualization.png --report report.html`
**Explanation:** Generates HTML report.
---
name: metastrand
category: utility
description: "Metastrand: Making sense of antisense"
tags: [metastrand, utility, strand-specific]
author: oxo-call-community
source_url: "https://gitlab.com/mpust/metastrand"
---
## Concepts

- **Tool Overview**: Metastrand v0.1.1 is a tool for analyzing strand-specific sequencing data and making sense of antisense transcription.
- **Core Function**: Analyzes strand-specific RNA-seq data to identify sense and antisense transcripts.
- **Strand-Specific Analysis**: Differentiates between sense and antisense transcription in RNA-seq data.
- **Antisense Detection**: Identifies antisense transcripts and their expression levels.
- **Input/Output**: Accepts strand-specific RNA-seq data; outputs strand-specific expression profiles.
- **Visualization**: Generates visualizations of strand-specific expression patterns.

## Pitfalls

- **Strand Orientation**: Requires correct strand orientation information.
- **Data Quality**: Analysis quality depends on input data quality.
- **Mapping Quality**: Poor mapping quality can affect strand assignment.
- **False Positives**: May detect false positive antisense transcripts.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Memory Requirements**: Processing large datasets may require significant memory.

## Examples

### Analyze strand-specific data
**Args:** `metastrand -i reads.bam -o results/`
**Explanation:** Analyzes strand-specific sequencing data.

### Detect antisense transcripts
**Args:** `metastrand -i reads.bam -o results/ --antisense`
**Explanation:** Focuses on antisense transcript detection.

### Generate strand-specific counts
**Args:** `metastrand -i reads.bam -o counts.txt --counts`
**Explanation:** Generates strand-specific expression counts.

### Visualize strand bias
**Args:** `metastrand -i reads.bam -o strand_bias.png --plot`
**Explanation:** Generates visualization of strand bias.

### Batch processing
**Args:** `metastrand -i bam/ -o results/`
**Explanation:** Processes multiple BAM files in batch mode.
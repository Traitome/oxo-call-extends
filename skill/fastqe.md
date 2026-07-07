---
name: fastqe
category: formatting
description: "A emoji based bioinformatics command line tool."
tags: [fastqe, formatting, FASTQ, emoji, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fastqe/fastqe"
---

## Concepts

- **Tool Overview**: fastqe is an emoji-based bioinformatics command line tool that visualizes FASTQ quality scores using emojis.
- **Core Function**: Reads FASTQ files and represents quality scores as emojis for quick visual inspection.
- **Input/Output**: Input: FASTQ files. Output: Emoji-based quality visualization.
- **Algorithm**: Computes min/max/mean quality scores per position and maps to emojis.
- **Key Features**: Emoji-based visualization, quality statistics, quick quality assessment, multiple file support, color output.
- **Installation**: `conda install -c bioconda fastqe`

## Pitfalls

- **Visual Limitations**: Emoji representation may not be precise for detailed analysis.
- **Terminal Support**: Requires emoji-supporting terminal.
- **File Size**: Large files may produce excessive output.
- **Quality Interpretation**: Emoji mapping requires understanding.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic visualization
**Args:** `fastqe reads.fastq`
**Explanation:** Displays emoji-based quality visualization.

### Multiple files
**Args:** `fastqe reads1.fastq reads2.fastq`
**Explanation:** Visualizes multiple FASTQ files.

### Statistics only
**Args:** `fastqe --stats reads.fastq`
**Explanation:** Shows quality statistics without emojis.

### Color output
**Args:** `fastqe --color reads.fastq`
**Explanation:** Enables color output in terminal.

### Save to file
**Args:** `fastqe reads.fastq > quality_report.txt`
**Explanation:** Saves output to file.
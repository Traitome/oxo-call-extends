---
name: occultercut
category: utility
description: OcculterCut measures local GC-content bias in genomes and identifies fungal species.
tags: [occultercut, utility, gc-content, fungal-genomics]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/occultercut"
---

## Concepts

- **Tool Overview**: OcculterCut analyzes GC-content bias and identifies fungal sequences.
- **Core Function**: Measures local GC-content and detects fungal contamination.
- **Algorithm**: Uses sliding window approach for GC-content analysis.
- **Input Format**: Accepts FASTA genome sequences.
- **Output**: Produces GC-content profiles and contamination reports.
- **Use Case**: Genome analysis, contamination detection, and fungal identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Fungal Specific**: Optimized for fungal detection.
- **Window Size**: Requires appropriate window size selection.
- **Memory Usage**: Large genomes require memory.
- **False Positives**: May report false contamination signals.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `occultercut --help`
**Explanation:** Shows available options and usage instructions.

### Analyze genome
**Args:** `occultercut -i genome.fasta -o gc_profile.txt`
**Explanation:** Analyzes GC-content of genome.

### With window size
**Args:** `occultercut -i genome.fasta -w 1000 -o gc_profile.txt`
**Explanation:** Sets sliding window size to 1000bp.

### Detect contamination
**Args:** `occultercut -i genome.fasta -o report.txt --detect`
**Explanation:** Detects potential fungal contamination.

### Output plot
**Args:** `occultercut -i genome.fasta -o gc_plot.png --plot`
**Explanation:** Generates GC-content plot.

### Minimum length
**Args:** `occultercut -i genome.fasta -m 1000 -o gc_profile.txt`
**Explanation:** Filters sequences by minimum length.

### Verbose mode
**Args:** `occultercut -i genome.fasta -v -o gc_profile.txt`
**Explanation:** Runs with verbose output.
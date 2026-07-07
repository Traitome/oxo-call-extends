---
name: tandemtwister
category: annotation
description: Detection of interleaved and embedded tandem repeats from long reads.
tags: [tandemtwister, tandem-repeats, long-reads, annotation]
author: oxo-call-community
source_url: "https://github.com/Lionward/tandemtwister"
---

## Concepts

- **Tool Overview**: tandemtwister (v0.2.0) detects complex tandem repeats.
- **Core Function**: Identifies interleaved and embedded tandem repeats.
- **Algorithm**: Uses pattern recognition for repeat detection.
- **Input/Output**: Input: FASTA reads; Output: Repeat annotations.
- **Applications**: Repeat annotation, genome analysis, sequence characterization.
- **Installation**: `conda install -c bioconda tandemtwister` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large sequences require significant memory.
- **Computational Time**: Processing long reads can be slow.
- **Repeat Complexity**: Very complex repeats may be missed.
- **False Positives**: May detect spurious repeats.
- **Read Quality**: Poor quality affects accuracy.
- **Performance**: Slow on large datasets.

## Examples

### Display help
**Args:** `tandemtwister --help`
**Explanation:** Shows available options and usage information.

### Basic repeat detection
**Args:** `tandemtwister -i reads.fasta -o repeats.gff`
**Explanation:** Detect tandem repeats from FASTA.

### With minimum length
**Args:** `tandemtwister -i reads.fasta -o repeats.gff -m 10`
**Explanation:** Minimum repeat unit length of 10.

### Verbose mode
**Args:** `tandemtwister -i reads.fasta -o repeats.gff -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tandemtwister -i reads.fasta -o repeats.gff --stats`
**Explanation:** Generate statistics about repeats.

### Batch processing
**Args:** `for f in fasta/*.fasta; do tandemtwister -i $f -o annotations/${f%.fasta}_repeats.gff; done`
**Explanation:** Process multiple FASTA files.

### Filter by score
**Args:** `tandemtwister -i reads.fasta -o repeats.gff -s 0.9`
**Explanation:** Minimum score threshold.

### Include all repeats
**Args:** `tandemtwister -i reads.fasta -o repeats.gff --all`
**Explanation:** Include all repeat types.

### Generate report
**Args:** `tandemtwister -i reads.fasta -o repeats.gff --report`
**Explanation:** Generate comprehensive repeat report.

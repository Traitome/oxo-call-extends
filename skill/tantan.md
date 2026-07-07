---
name: tantan
category: sequence-analysis
description: Masks simple regions (low complexity & short-period tandem repeats) in biological sequences.
tags: [tantan, sequence-analysis, masking, repeats]
author: oxo-call-community
source_url: "https://gitlab.com/mcfrith/tantan/-/blob/main/README.rst"
---

## Concepts

- **Tool Overview**: tantan (v51) masks low complexity and tandem repeat regions.
- **Core Function**: Identifies and masks repetitive sequences.
- **Algorithm**: Uses statistical methods to detect repetitive patterns.
- **Input/Output**: Input: FASTA sequences; Output: Masked sequences.
- **Applications**: Sequence analysis, repeat masking, genome annotation.
- **Installation**: `conda install -c bioconda tantan` or download from GitLab.

## Pitfalls

- **Memory Requirements**: Large sequences require significant memory.
- **Parameter Tuning**: Incorrect parameters affect masking.
- **False Positives**: May mask non-repetitive regions.
- **Performance**: Processing large genomes can be slow.
- **Sensitivity**: May miss complex repeats.
- **Sequence Quality**: Poor quality affects accuracy.

## Examples

### Display help
**Args:** `tantan --help`
**Explanation:** Shows available options and usage information.

### Basic masking
**Args:** `tantan -i input.fasta -o masked.fasta`
**Explanation:** Mask repetitive regions in sequence.

### With custom threshold
**Args:** `tantan -i input.fasta -o masked.fasta -t 0.5`
**Explanation:** Use custom masking threshold.

### Verbose mode
**Args:** `tantan -i input.fasta -o masked.fasta -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tantan -i input.fasta -o masked.fasta --stats`
**Explanation:** Generate statistics about masking.

### Batch processing
**Args:** `for f in fasta/*.fasta; do tantan -i $f -o masked/${f%.fasta}_masked.fasta; done`
**Explanation:** Process multiple FASTA files.

### Mask with lowercase
**Args:** `tantan -i input.fasta -o masked.fasta -l`
**Explanation:** Mask with lowercase letters.

### Include soft masking
**Args:** `tantan -i input.fasta -o masked.fasta -s`
**Explanation:** Use soft masking instead of hard masking.

### Generate report
**Args:** `tantan -i input.fasta -o masked.fasta --report`
**Explanation:** Generate comprehensive masking report.

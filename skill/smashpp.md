---
name: smashpp
category: structural-variation
description: A fast tool to find and visualize rearrangements in DNA sequences using suffix arrays
tags: [smashpp, structural-variation, rearrangements, visualization, suffix-array]
author: oxo-call-community
source_url: "https://github.com/smortezah/smashpp"
---

## Concepts

- **Tool Overview**: smashpp (v23.09) - A fast tool for detecting and visualizing genomic rearrangements
- **Core Function**: Identifies structural variations and rearrangements in DNA sequences
- **Input/Output**: Accepts FASTA sequences; outputs rearrangement predictions and visualizations
- **Algorithm**: Uses suffix array-based pattern matching for fast rearrangement detection
- **Installation**: `conda install -c bioconda smashpp`
- **Key Features**: Fast detection, visualization support, handles large genomes

## Pitfalls

- **Sequence Quality**: Requires high-quality input sequences
- **Memory Usage**: Large genomes may require significant memory
- **Detection Sensitivity**: May miss small rearrangements
- **Visualization Requirements**: Visual output requires additional tools
- **Parameter Tuning**: Optimal parameters depend on dataset characteristics
- **Output Interpretation**: Rearrangement calls require manual verification

## Examples

### Display help
**Args:** `smashpp --help`
**Explanation:** Shows available options and usage information.

### Detect rearrangements
**Args:** `smashpp -i genome.fasta -o rearrangements.txt`
**Explanation:** Detect rearrangements in input sequence.

### With reference genome
**Args:** `smashpp -i query.fasta -r reference.fasta -o results.txt`
**Explanation:** Compare query against reference for rearrangements.

### Generate visualization
**Args:** `smashpp -i genome.fasta -o rearrangements.txt -v`
**Explanation:** Generate visualization of detected rearrangements.

### Specify minimum size
**Args:** `smashpp -i genome.fasta -o results.txt -m 100`
**Explanation:** Only report rearrangements >= 100bp.

### Multi-threaded processing
**Args:** `smashpp -i genome.fasta -o results.txt -t 8`
**Explanation:** Use 8 threads for parallel processing.

### Output in BED format
**Args:** `smashpp -i genome.fasta -o results.bed -f bed`
**Explanation:** Output results in BED format.

### Detailed output
**Args:** `smashpp -i genome.fasta -o results.txt -d`
**Explanation:** Generate detailed rearrangement report.
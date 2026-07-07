---
name: dnp-mapping
category: utility
description: DNPattern tools - Nucleosome positioning using dinucleotide pattern analysis.
tags: [dnp-mapping, utility, nucleosome, dinucleotide, genome-mapping, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/erinijapranckeviciene/mapping_CC"
---

## Concepts

- **Tool Overview**: dnp-mapping predicts nucleosome positions based on dinucleotide periodicity patterns.
- **Core Function**: Maps nucleosome occupancy using the 10-bp dinucleotide periodicity signal.
- **Input/Output**: Input: FASTA DNA sequences. Output: Predicted nucleosome positions in BED format.
- **Algorithm**: Uses dinucleotide pattern periodicity to identify nucleosome binding regions.
- **Key Features**: Nucleosome prediction, dinucleotide periodicity analysis, BED output, visualization support.
- **Installation**: `conda install -c bioconda dnp-mapping`

## Pitfalls

- **Input Requirements**: Requires DNA sequences; works best with eukaryotic genomes.
- **Sequence Length**: Minimum sequence length required for periodicity detection.
- **Species Specificity**: Trained on specific organisms; performance varies.
- **Accuracy**: Predictions are probabilistic; experimental validation recommended.
- **Repetitive Regions**: Highly repetitive sequences may produce false positives.
- **Output Interpretation**: Predicted positions are probabilistic, not definitive.

## Examples

### Predict nucleosome positions
**Args:** `dnp-mapping --input sequences.fa --output nucleosomes.bed`
**Explanation:** Predicts nucleosome positions using dinucleotide periodicity.

### With confidence threshold
**Args:** `dnp-mapping --input sequences.fa --output nucleosomes.bed --confidence 0.8`
**Explanation:** Filters predictions by minimum confidence score of 0.8.

### Score only output
**Args:** `dnp-mapping --input sequences.fa --output scores.bed --score-only`
**Explanation:** Outputs nucleosome occupancy scores instead of discrete positions.

### Plot-ready output
**Args:** `dnp-mapping --input sequences.fa --output plot_data.tsv --plot`
**Explanation:** Generates data suitable for visualization of nucleosome occupancy.

### Multiple sequences
**Args:** `dnp-mapping --input-dir fasta_files/ --output-dir predictions/`
**Explanation:** Processes multiple sequences and generates separate predictions.

### Include flanking regions
**Args:** `dnp-mapping --input sequences.fa --output nucleosomes.bed --flank 50`
**Explanation:** Includes 50bp flanking regions in the output.
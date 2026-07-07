---
name: altair-mf
category: alignment
description: C toolkit for alignment-free and temporal analysis of multi-FASTA data
tags: [altair-mf, AltaiR, alignment-free, multi-FASTA, sequence-analysis, compression, bioinformatics]
author: oxo-call-community
source_url: "https://cobilab.github.io/altair/"
---

## Concepts

- **Tool Overview**: AltaiR (altair-mf) is a high-performance C toolkit for alignment-free analysis of multi-FASTA sequence data, designed for large-scale datasets such as viral genomes from epidemic/pandemic events.
- **Core Function**: Provides six main analysis modules: average filtering, sequence filtering, frequency analysis, Normalized Compression (NC), Normalized Compression Distance (NCD), and Relative Absent Words (RAWs) computation.
- **Input/Output**: Accepts multi-FASTA format sequences; outputs CSV files with computed metrics and filtered FASTA files.
- **Performance**: Implemented in multi-threaded C for high speed, with no external dependencies for core functionality.
- **Installation**: Available via Bioconda (`conda install -c bioconda altair-mf`) or from source.

## Pitfalls

- **Sequence Quality**: Low-quality sequences can skew compression-based metrics; pre-filtering is recommended.
- **Memory Requirements**: Very large datasets (>1M sequences) may require significant memory; consider splitting inputs.
- **Alphabet Filtering**: Non-standard alphabet characters may cause unexpected behavior; use filter module to validate sequences.
- **Reference Selection**: NCD analysis requires a reference sequence; choice of reference affects distance calculations.
- **Header Parsing**: Header patterns are used for temporal analysis; ensure headers contain required metadata.

## Examples

### Filter sequences by length and quality
**Args:** `filter -i input.fasta -o filtered.fasta -l 1000 -L 10000 -c 0.95`
**Explanation:** Filters sequences to retain those between 1000-10000 bp with 95% completeness. The `-l` and `-L` flags set minimum/maximum length, while `-c` sets completeness threshold.

### Compute nucleotide frequency
**Args:** `frequency -i sequences.fasta -o freq_output.csv -a DNA`
**Explanation:** Calculates nucleotide frequencies (A, T, C, G) for each sequence and outputs results to CSV. The `-a` flag specifies the alphabet type.

### Calculate Normalized Compression (NC)
**Args:** `nc -i input.fasta -o nc_results.csv -l 5`
**Explanation:** Computes Normalized Compression values using compression level 5. NC measures sequence complexity based on compressibility.

### Compute NCD matrix with reference
**Args:** `ncd -i genomes.fasta -o ncd_matrix.csv -r reference.fasta`
**Explanation:** Calculates Normalized Compression Distance between each sequence and a reference sequence, useful for phylogenetic analysis without alignment.

### Identify Relative Absent Words (RAWs)
**Args:** `raw -i sequences.fasta -o raws_output.csv -k 9`
**Explanation:** Identifies Relative Absent Words of length 9, which can reveal unique sequence characteristics and signatures.

### Moving average filtering
**Args:** `average -i values.csv -o smoothed.csv -w 10`
**Explanation:** Applies a moving average filter with window size 10 to a column of float values in CSV format, useful for temporal analysis.
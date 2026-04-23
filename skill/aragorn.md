---
name: aragorn
category: annotation
description: ARAGORN - Detect tRNA and tmRNA genes in genomic sequences using heuristic secondary structure prediction
tags: [trna, tmrna, gene-detection, genome-annotation, secondary-structure]
author: oxo-call-community
source_url: "http://www.ansikte.se/ARAGORN/"
---

## Concepts

- **Tool Overview**: ARAGORN identifies tRNA (transfer RNA) and tmRNA (transfer-messenger RNA) genes in genomic sequences using heuristic algorithms to predict tRNA secondary structure. Version 1.2.41.
- **Detection Method**: Uses homology with known tRNA sequences and heuristic secondary structure prediction to identify tRNA genes. Faster than tRNAscan-SE for large genomes.
- **Sensitivity**: Comparable or better sensitivity than other heuristic tRNA search algorithms, especially for eubacterial and archaeal genomes. Comparable to tRNAscan-SE overall.
- **tmRNA Detection**: Also detects transfer-messenger RNA (tmRNA/SsrA) genes involved in trans-translation, a quality control mechanism in bacteria.
- **Input Format**: Accepts FASTA format genomic sequences. Can process single sequences or entire genome files.
- **Output Format**: Reports detected tRNA/tmRNA positions, anticodons, and predicted secondary structures. Multiple output options available.
- **Web Interface**: Available as web tool at www.trna.se for quick analyses without local installation.

## Pitfalls

- **Sequence Quality**: Poor quality sequences with many errors may produce false negatives or incorrect anticodon predictions.
- **Organism Type**: Performance varies by organism type. Best for eubacterial and archaeal genomes; slightly less sensitive for eukaryotic nuclear genomes.
- **Anticodon Assignment**: Some tRNAs with unusual anticodons may be misassigned. Verify anticodon predictions for unusual cases.
- **Partial Genes**: Partial tRNA genes at assembly boundaries may be missed or incorrectly annotated.
- **tmRNA Complexity**: tmRNA detection may be less accurate for organisms with unusual tmRNA structures.

## Examples

### Basic tRNA detection
**Args:** `aragorn -t genome.fasta > trna_results.txt`
**Explanation:** Detects tRNA genes in genome FASTA file. Outputs positions, anticodons, and secondary structure predictions. Default tRNA-only search.

### Detect both tRNA and tmRNA
**Args:** `aragorn -t -m genome.fasta > all_results.txt`
**Explanation:** Searches for both tRNA and tmRNA genes. Comprehensive search for all transfer RNA types in bacterial genomes.

### tmRNA-only detection
**Args:** `aragorn -m genome.fasta > tmrna_results.txt`
**Explanation:** Detects only tmRNA genes, skipping tRNA search. Useful when tRNAs are already annotated or tmRNA-specific analysis needed.

### Circular genome input
**Args:** `aragorn -t -c plasmid.fasta > circular_trna.txt`
**Explanation:** Treats input as circular genome (e.g., plasmids, mitochondrial genomes). Searches across sequence boundaries for tRNAs spanning the origin.

### Batch processing multiple genomes
**Args:** `for f in genomes/*.fa; do aragorn -t "$f" > "${f%.fa}_trna.txt"; done`
**Explanation:** Processes multiple genome files in directory. Outputs separate tRNA annotation files for each genome. Useful for comparative analysis.

### Detailed output format
**Args:** `aragorn -t -w genome.fasta > detailed_trna.txt`
**Explanation:** Outputs detailed results including full secondary structure predictions. More comprehensive output than default format.

### Quick web-based analysis
**Args:** Upload FASTA at www.trna.se, select "both" for tRNA and tmRNA detection
**Explanation:** Uses web interface for quick analysis without installation. Maximum 50MB file size. Good for small genomes or quick verification.
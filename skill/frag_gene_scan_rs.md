---
name: frag_gene_scan_rs
category: annotation
description: Rust implementation of the gene prediction model for short and error-prone reads.
tags: [frag_gene_scan_rs, gene prediction, Rust, long reads]
author: oxo-call-community
source_url: "https://github.com/unipept/FragGeneScanRs"
---

## Concepts
- **Rust Implementation**: Rewritten in Rust for improved performance and memory efficiency.
- **Error-Prone Reads**: Designed to handle noisy reads from long-read sequencing.
- **Gene Prediction**: Predicts genes from fragmented sequencing data.
- **Parallel Processing**: Supports multi-threaded gene prediction.
- **Compatibility**: Maintains compatibility with original FragGeneScan output.

## Pitfalls
- **Training Data**: Requires appropriate training models for different sequencing technologies.
- **Memory Requirements**: Processing large datasets requires significant memory.
- **Output Format**: Limited output format options compared to original.
- **Model Selection**: Default models may not suit all datasets.
- **Performance**: May be slower on certain operations compared to specialized tools.

## Examples
### Basic gene prediction
**Args:** `frag_gene_scan_rs -i reads.fastq -o genes.faa -m illumina`
**Explanation:** Predicts genes from Illumina reads.

### Long-read prediction
**Args:** `frag_gene_scan_rs -i reads.fastq -o genes.faa -m nanopore`
**Explanation:** Predicts genes from Oxford Nanopore reads.

### Parallel processing
**Args:** `frag_gene_scan_rs -i reads.fastq -o genes.faa -m illumina -t 8`
**Explanation:** Uses 8 threads for faster prediction.

### Output GFF format
**Args:** `frag_gene_scan_rs -i reads.fastq -o genes.gff -f gff`
**Explanation:** Outputs predictions in GFF format.

### Train custom model
**Args:** `frag_gene_scan_rs train -i training_data.fasta -o custom_model`
**Explanation:** Trains a custom gene prediction model.
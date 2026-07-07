---
name: kssd
category: kmer
description: K-mer substring space decomposition for large-scale sequence sketching and analysis
tags: [kssd, kmer, sequence-similarity, sketching, containment-analysis]
author: oxo-call-community
source_url: "https://github.com/yhg926/public_kssd"
---

## Concepts

- **K-mer Sketching**: Creates sequence sketches using k-mer sampling
- **Space Decomposition**: Decomposes sequence space using k-mer substrings
- **Large-scale Analysis**: Handles large-scale sequence datasets efficiently
- **Resemblance Analysis**: Computes resemblance between sequence sets
- **Containment Analysis**: Calculates containment metrics between sequences
- **Multiple Formats**: Supports FASTA and FASTQ, gzipped or not

## Pitfalls

- **K-mer Size**: K-mer size affects sketching accuracy
- **Memory Usage**: Large datasets require significant memory
- **Sketch Size**: Sketch size affects precision of results
- **Sample Quality**: Low-quality sequences affect sketching
- **Hash Functions**: Different hash functions may give different results
- **Computational Time**: Very large datasets take long to process

## Examples

### Sketch sequences
**Args:** `kssd sketch -i sequences.fasta -o sketch.txt`
**Explanation:** Creates k-mer sketch from sequence file.

### Compute resemblance
**Args:** `kssd compare -i sketch1.txt -i sketch2.txt -o resemblance.txt`
**Explanation:** Computes resemblance between two sketches.

### Containment analysis
**Args:** `kssd containment -i query.sketch -i ref.sketch -o containment.txt`
**Explanation:** Calculates containment of query in reference.

### Specify k-mer size
**Args:** `kssd sketch -i sequences.fasta -k 31 -o sketch.txt`
**Explanation:** Uses k-mer size of 31 for sketching.

### Batch processing
**Args:** `kssd batch -d sequences/ -o sketches/`
**Explanation:** Creates sketches for multiple sequences.

### Export statistics
**Args:** `kssd stats -i sketch.txt -o statistics.txt`
**Explanation:** Exports sketching statistics.
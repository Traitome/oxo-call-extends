---
name: mash
category: utility
description: Fast sequence distance estimator that uses MinHash for rapid genome comparison.
tags: [mash, MinHash, distance estimation, genome comparison]
author: oxo-call-community
source_url: "https://github.com/marbl/Mash"
---

## Concepts

- **Tool Overview**: Mash is a fast sequence distance estimator using MinHash for comparing genomic sequences.
- **Core Function**: Estimates evolutionary distances between sequences without full alignment.
- **MinHash Algorithm**: Uses locality-sensitive hashing to create compact "sketches" of sequences.
- **Distance Metric**: Computes Jaccard index-based distances between sequence sketches.
- **Input/Output**: Accepts FASTA/Q files, produces distance matrices or sketch files (.msh).
- **Installation**: `conda install -c bioconda mash`

## Pitfalls

- **Sketch Size Impact**: Smaller sketch sizes are faster but less accurate; larger sketches improve precision.
- **k-mer Selection**: k-mer size (-k) must be appropriate for sequence length and diversity.
- **Memory Usage**: Sketching very large genomes may require significant memory.
- **Taxonomic Bias**: May not perform well on highly divergent sequences or metagenomic data.
- **Output Interpretation**: Distances are estimates, not exact evolutionary distances.
- **File Format**: Ensure input files are in proper FASTA/Q format without corrupted headers.

## Examples

### Create genome sketch
**Args:** `mash sketch -o ecoli.msh ecoli.fasta`
**Explanation:** Creates MinHash sketch of E. coli genome.

### Compare two genomes
**Args:** `mash dist ecoli.msh salmonella.msh`
**Explanation:** Computes Mash distance between two genome sketches.

### Sketch with custom parameters
**Args:** `mash sketch -o output.msh -k 31 -s 1000 input.fasta`
**Explanation:** Uses k=31 and sketch size of 1000.

### Compare multiple sketches
**Args:** `mash dist *.msh > distances.txt`
**Explanation:** Creates distance matrix from all sketch files.

### Screen for containment
**Args:** `mash screen ref.msh query.fasta`
**Explanation:** Checks if query sequences are contained in reference.

### Reduce sketch size
**Args:** `mash sketch -o small.msh -r 0.5 large.msh`
**Explanation:** Reduces existing sketch by 50%.

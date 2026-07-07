---
name: appspam
category: phylogenetics
description: App-SpaM - Alignment-free Phylogenetic Placement algorithm based on Spaced-word Matches
tags: [appspam, phylogenetic-placement, alignment-free, spaced-word, metagenomics]
author: oxo-call-community
source_url: "https://github.com/matthiasblanke/App-SpaM"
---

## Concepts

- **Tool Overview**: App-SpaM (v1.03) - An efficient alignment-free phylogenetic placement algorithm based on Filtered Spaced Word Matches (FSWM).
- **Core Function**: Places query sequences (short reads) onto a reference phylogenetic tree without requiring sequence alignments. Uses spaced-word matches to estimate pairwise phylogenetic distances.
- **Key Features**:
  - Alignment-free approach: No multiple sequence alignment required
  - Fast: Two orders of magnitude faster than traditional methods
  - High accuracy: Produces results comparable to best available methods
  - Handles short reads efficiently
  - Outputs in JPlace format for downstream analysis
- **Spaced Word Matches**: Uses patterns of match and don't-care positions to identify conserved sequence motifs
- **Applications**: 
  - Metabarcoding analysis
  - Metagenomic read classification
  - Taxonomic identification of short reads
  - Large-scale phylogenetic placement
- **Installation**: `conda install -c bioconda appspam`

## Pitfalls

- **Reference Tree Required**: Needs a precomputed reference tree for placement
- **Memory Usage**: May require significant memory for large datasets
- **Short Read Focus**: Optimized for short reads; may not perform optimally with long sequences
- **Parameter Tuning**: Spaced-word pattern and other parameters may need optimization for specific datasets

## Examples

### Basic phylogenetic placement
**Args:** `appspam -r reference.fasta -t reference_tree.newick -q queries.fastq -o placements.jplace`
**Explanation:** Places query reads onto reference tree using default settings.

### With custom spaced-word pattern
**Args:** `appspam -r ref.fasta -t tree.nwk -q reads.fq -o out.jplace -p "11100111"`
**Explanation:** Uses custom spaced-word pattern (1=match, 0=don't care).

### Multiple query files
**Args:** `appspam -r ref.fasta -t tree.nwk -q reads1.fq reads2.fq -o combined.jplace`
**Explanation:** Processes multiple query files and produces combined placements.

### Using distance-based heuristic
**Args:** `appspam -r ref.fasta -t tree.nwk -q reads.fq -o out.jplace -m distance`
**Explanation:** Uses distance-based placement heuristic instead of match-based.

### Help documentation
**Args:** `appspam --help`
**Explanation:** Shows available options and parameters.
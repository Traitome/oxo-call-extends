---
name: rnaclust
category: utility
description: A Perl pipeline for clustering RNAs by secondary-structure similarity using RNAfold, LocARNA, and WPGMA hierarchical clustering.
tags: ["rnaclust", "rna-clustering", "secondary-structure", "locarna", "rnafold", "wpgma"]
author: oxo-call-community
source_url: "http://www.bioinf.uni-leipzig.de/~kristin/Software/RNAclust/"
---

## Concepts

- **Tool Overview**: RNAclust (v1.3, Kristin Reiche / Leipzig) is a Perl pipeline for clustering a set of RNA sequences by their predicted secondary structures. It chains three established tools — RNAfold, LocARNA, and WPGMA — into a single workflow that ends in a NEWICK tree and an optimal cluster assignment per sequence.
- **Core Function**: Takes a multi-FASTA of RNA sequences as input, runs pairwise structural alignments to build a distance matrix, infers a hierarchical tree, cuts the tree at the optimal depth, and writes the clusters and the tree to disk. The main entry point is the `RNAclustel.pl` script (sometimes aliased to `rnaclustel`).
- **Algorithm**: Three stages: (1) `RNAfold --noLP --mea` (or `RNAfold -p`) computes base-pair probability matrices per sequence; (2) LocARNA (or `pmcomp` in older versions) performs sequence-structure-aware pairwise alignments and emits a distance score; (3) WPGMA (Weighted Pair Group Method with Arithmetic Mean) builds a hierarchical tree, and an automatic cluster-cutting step picks the optimal number of clusters from the longest branch gaps.
- **Input Format**: A single multi-FASTA file with one RNA sequence per record. Sequences should be roughly the same length (or a length-normalized LocARNA scoring is used); very long transcripts (≥ 5000 nt) make pairwise alignment slow. For very large input sets, use `pmcomp` instead of LocARNA via `--score-mode pmcomp`.
- **Output Format**: (1) a NEWICK tree of all sequences, (2) a cluster assignment file mapping each sequence ID to a cluster number, (3) per-cluster FASTA files in a sub-directory, and (4) the pairwise distance matrix. Files are written to a user-named output directory created by the script.
- **Use Case**: Grouping non-coding RNA homologs (miRNA precursors, snoRNAs, riboswitches, tRNAs) from a de novo annotation into structural families before downstream multiple alignment with `cmbuild`/`cmalign` from Infernal, or before running `RNAz` on each cluster.

## Pitfalls

- **CRITICAL — `RNAclustel.pl` is the canonical entry point**: Many users call `rnaclust` and get "command not found". The actual script installed by the Bioconda recipe is `RNAclustel.pl` (sometimes wrapped as `rnaclustel`); if the conda package is installed, it is on PATH. The original Leipzig site also distributes a tarball where the script is named differently.
- **LocARNA must be installed and on PATH**: RNAclust calls `locarna` internally; on macOS with conda this often pulls an old LocARNA that needs an extra `locarna-lib` companion. Verify with `locarna --version` before launching a large run.
- **RNAfold `--noLP` is recommended for non-coding inputs**: Without `--noLP`, RNAfold reports isolated base pairs as paired, which inflates the structural distance between genuine homologs. The Leipzig example data set explicitly uses `--noLP`; mirror that for reproducibility.
- **All-vs-all alignment is O(n²)**: A 200-sequence input set requires ~20,000 LocARNA jobs; expect hours of wall time for 500+ sequences. Use `--max-seqs` (or split the input) for initial exploration, then run the full set overnight.
- **WPGMA optimal cut is heuristic**: The "best" number of clusters is selected by a penalty function over branch lengths; it can over-split on data sets with strong gradations of similarity. Always inspect the NEWICK tree in FigTree or iTOL rather than trusting the auto-cut.
- **No strand/sequence-name sanitization**: FASTA headers containing whitespace, pipes, or non-ASCII characters will break the cluster-file parser. Pre-clean with `seqkit rename` (`seqkit rename input.fa -o input.clean.fa`) before running.

## Examples

### Basic clustering run
**Args:** `RNAclustel.pl --in input.fa --out cluster_run --mode locarna`
**Explanation:** `--in` is the input multi-FASTA, `--out` is the directory that will be created to hold results, `--mode locarna` selects the LocARNA-based distance metric (the default in v1.3). All other parameters use sensible defaults derived from the Leipzig example data set.

### Force ViennaRNA's `--noLP` flag
**Args:** `RNAclustel.pl --in input.fa --out run_nolp --mode locarna --rf-args "--noLP --mea"`
**Explanation:** `--rf-args` is forwarded to `RNAfold`; `--noLP` disables lonely pairs (improves clustering of ncRNA families) and `--mea` enables maximum-expected-accuracy base-pair probabilities, the recommended pair of flags for ncRNA families.

### Use pmcomp for very large input sets
**Args:** `RNAclustel.pl --in big_set.fa --out big_run --mode pmcomp --max-seqs 1000`
**Explanation:** `--mode pmcomp` switches to the faster pmcomp distance metric (single-base-pair probability comparison, no sequence-structure alignment), suitable for >1000 sequences. `--max-seqs 1000` is a safety cap; remove it for the full run.

### Customize WPGMA tree cutting
**Args:** `RNAclustel.pl --in input.fa --out run --mode locarna --cut 0.45`
**Explanation:** `--cut` is the branch-length threshold for cutting the WPGMA tree into flat clusters; lower values produce more clusters. The value 0.45 corresponds to a medium-resolution cut suitable for ncRNA families of moderate diversity.

### Skip the alignment visualization
**Args:** `RNAclustel.pl --in input.fa --out run --mode locarna --no-vis`
**Explanation:** `--no-vis` disables the LocARNA dot-plot PDF generation that RNAclust triggers by default; useful on headless servers or when only the cluster assignment and NEWICK tree are needed.

### Convert cluster assignments to a BED-like table
**Args:** `ls run/clusters/cluster_*.fa | awk '{print $1"\t"$1}' | sed 's|run/clusters/cluster_||;s|\.fa||'`
**Explanation:** Quick shell snippet to tabulate the cluster files produced under `run/clusters/`; the first column is the original FASTA header basename and the second is the cluster number, ready to be loaded into R or pyhton for downstream filtering.

### Parallelize on a multi-core host
**Args:** `RNAclustel.pl --in input.fa --out run --mode locarna --threads 16`
**Explanation:** `--threads` (also accepted as `-j`) controls the number of concurrent LocARNA jobs; the default is 1, which under-utilizes modern servers. Set this to the number of physical cores (or less, to leave room for memory-hungry LocARNA instances).

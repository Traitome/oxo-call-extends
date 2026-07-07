---
name: fasttree
category: phylogenomics
description: "FastTree 2 (v2.2.0, by Price, Dehal & Arkin) infers approximately-maximum-likelihood phylogenetic trees from large nucleotide or protein alignments 100-1000x faster than PhyML/RAxML. Default support values are SH-like local supports, not full bootstraps."
tags: [fasttree, phylogenomics, maximum-likelihood, tree, newick, fasta, phylip, JTT, GTR, WAG, LG, SH-test, bootstrap]
author: oxo-call-community
source_url: "https://morgannprice.github.io/fasttree/"
---

## Concepts

- **Tool Overview**: FastTree 2 (v2.2.0, by Morgan N. Price, Adam P. Arkin et al., Lawrence Berkeley National Lab) builds approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences. It scales to ~1,000,000 sequences and runs 100–1000x faster than PhyML 3.0 or RAxML 7. The output is a Newick tree (default on stdout).
- **Five Internal Stages**: (1) Heuristic neighbor-joining (top-hits + relaxed-NJ + fast-NJ heuristics) to get an initial topology; (2) Minimum-evolution NNI (nearest-neighbor interchange, ~4·log2(N) rounds); (3) Minimum-evolution SPR (subtree-prune-regraft, default 2 rounds); (4) Maximum-likelihood NNIs (default 2·log(N) rounds, branch lengths optimized); (5) Local support values via Shimodaira–Hasegawa (SH) test on local rearrangements.
- **Input Formats**: FASTA or PHYLIP interleaved. Read from a file argument or stdin (no file = stdin). Compression: pipe through `gzip -dc | FastTree ...` — FastTree does not auto-decompress.
- **Output**: Newick tree to stdout. Use `-out file.nwk` or shell redirection `> file.nwk`. Use `-log logfile` to save intermediate trees, the per-site rate categories, and the final model parameters (also enables resuming crashed runs).
- **Substitution Models**:
  - **Protein (default)**: JTT (Jones–Taylor–Thornton 1992). Alternatives: `-wag` (Whelan–Goldman 2001), `-lg` (Le–Gascuel 2008). Custom: `-trans matrixfile`.
  - **Nucleotide**: Jukes–Cantor (default). Use `-nt -gtr` for the generalized time-reversible model (recommended for most nt data). Custom GTR rates: `-gtrrates ac ag at cg ct gt` and `-gtrfreq A C G T`.
- **Rate Heterogeneity**: CAT approximation (default 20 rate categories, configurable with `-cat N`; `-nocat` = single rate). `-gamma` rescales branch lengths post-hoc to optimize the Gamma20 likelihood — recommended for final published trees (adds ~5% runtime).
- **Support Values**: By default FastTree computes SH-like local supports (same as PhyML 3's "SH-like local supports"). These are NOT traditional bootstrap values — they are computed from a single tree by testing local rearrangements, so they are fast but conservative. For traditional bootstrap, use PHYLIP `seqboot` to generate resampled alignments, then `FastTree -n 100 -boot 1000 in.phy > trees.nwk`, then `CompareToBootstrap.pl`.
- **Parallelism**: The OpenMP-enabled build (`fasttreeMP`, also packaged as `FastTreeMP`) uses `-threads N` (default 1). Speed-up is sub-linear. SSE3 build is ~2x faster than the vanilla build.
- **Memory & Scaling**: Heuristic NJ uses O(N·log N) memory via top-hits cache and profile storage (not the O(N²) distance matrix of classic NJ). For >50,000 sequences use `-fastest` (faster NJ, lower memory). For >1 million sequences, consider splitting or using a distance-matrix method.
- **Installation**:
  - Bioconda: `conda install -c bioconda fasttree` (provides `FastTree`, `FastTreeMP`, `fasttree`).
  - Pixi: `pixi global install fasttree`.
  - From source (with SSE3 + OpenMP): `gcc -DOPENMP -fopenmp -DUSE_DOUBLE -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree-2.2.0.c -lm`.
- **Citation**: Price MN, Dehal PS, Arkin AP. FastTree 2 — Approximately Maximum-Likelihood Trees for Large Alignments. PLoS ONE 5(3):e9490, 2010. doi:10.1371/journal.pone.0009490. (FastTree 1: MBE 26:1641-1650, 2009.)

## Pitfalls

- **Options must precede the alignment file**: `FastTree -nt -gtr aln.fa` works; `FastTree -nt aln.fa -gtr` silently ignores `-gtr`. This is the most common source of "wrong tree" reports.
- **`-nt` is required for nucleotide alignments**: Default (no `-nt`) treats input as protein. A nucleotide alignment run as protein produces a meaningless tree with no error message.
- **SH-like supports ≠ bootstrap supports**: Default support values are local SH-test supports, computed from a single alignment. They are NOT comparable to traditional bootstrap values (which require resampling). For publishable bootstraps, use `seqboot` + `-n` + `CompareToBootstrap.pl`, or use RAxML/IQ-TREE instead.
- **`-gamma` rescales branch lengths, not topology**: `-gamma` re-optimizes branch lengths under the Gamma20 model AFTER the topology search is finished under CAT. It does not improve the topology — only the branch-length realism.
- **`-boot N` is fast/approximate, not rigorous**: `-boot 1000` runs FastTree's internal fast bootstrap. For rigorous ML bootstrap use `seqboot` + `-n 100` + `consense`, or use RAxML/IQ-TREE which implement proper bootstrap under ML.
- **Sequence names restrictions**: Default FastTree rejects names containing spaces, commas, parentheses, or colons. Use `-quote` to allow them in FASTA input (but FastTree cannot read its own quoted trees back in).
- **No native gzip support**: FastTree does not auto-decompress `.gz`. Use `gzip -dc aln.fa.gz | FastTree -nt -gtr > tree.nwk`.
- **`-pseudo` for highly gapped alignments**: Default distance estimation fails for sequences with little overlap. Use `-pseudo` (with optional weight, default 1.0) to add pseudocounts. Without `-pseudo`, such pairs get inflated distances.
- **`-fastest` sacrifices accuracy for speed**: Recommended only for >50,000 sequences. For <50k, the default settings give better topology recovery; the time savings are minimal.
- **No site-rate heterogeneity during search (only CAT)**: CAT assigns each site a single rate; the ML search does not use a true Gamma model. Use `-gamma` only at the end if Gamma20 branch lengths are needed for likelihood comparisons across runs.
- **`-intree` ignores branch lengths**: When using `-intree tree.nwk` to start from a fixed topology, any branch lengths in the input are discarded and re-optimized.
- **OpenMP build name differs**: Single-threaded binary is `FastTree`; multi-threaded binary is `FastTreeMP` (or `fasttreeMP`). The `-threads N` option works only on the OpenMP build.
- **For publication-grade phylogeny, prefer RAxML-NG or IQ-TREE**: FastTree is excellent for exploratory analysis and large-scale surveys, but its approximations (heuristic NJ, CAT rates, SH supports) trade accuracy for speed. Final published trees should be re-run with a slower, more rigorous ML tool.

## Examples

### Build a nucleotide tree with GTR+Gamma model
**Args:** `-nt -gtr -gamma < aln.fa > tree.nwk`
**Explanation:** `-nt` selects nucleotide mode; `-gtr` uses the generalized time-reversible model (recommended for most nt data, vs default Jukes–Cantor); `-gamma` rescales branch lengths under Gamma20 after the CAT-based search (adds ~5% runtime); `<` reads the FASTA/PHYLIP alignment from stdin; `>` writes the Newick tree to a file. This is the standard recipe for nucleotide phylogeny.

### Build a protein tree with JTT+Gamma (default model)
**Args:** `-gamma proteins.aln.fa > protein_tree.nwk`
**Explanation:** Without `-nt`, input is treated as protein; default model is JTT; `-gamma` rescales branch lengths under Gamma20. Use `-lg` or `-wag` to switch protein model.

### Build a protein tree with the WAG model and save a log
**Args:** `-wag -gamma -log run.log proteins.aln -out tree.nwk`
**Explanation:** `-wag` selects the Whelan–Goldman 2001 amino-acid model; `-log run.log` saves intermediate trees and per-site rates (also enables resume after crash); `-out tree.nwk` writes the final Newick tree directly instead of using stdout redirection.

### Build a nucleotide tree with GTR+CAT (faster, no Gamma rescale)
**Args:** `-nt -gtr aln.fa > tree.nwk`
**Explanation:** Omitting `-gamma` saves ~5% runtime but leaves branch lengths in CAT units (less comparable across runs). Suitable for exploratory analysis or when relative branch lengths suffice.

### Use the Le-Gascuel (LG) protein model with OpenMP multi-threading
**Args:** `-lg -gamma -threads 8 -quote aln.fa > tree.nwk`
**Explanation:** `-lg` selects the Le–Gascuel 2008 model (often more accurate than JTT for diverse proteins); `-threads 8` uses 8 cores on the `FastTreeMP` build; `-quote` allows sequence names containing spaces, commas, or parentheses in the FASTA header (FastTree cannot read its own quoted trees back in, so use only for output). Run as `FastTreeMP -lg ...` (not `FastTree`) to enable `-threads`.

### Suppress informational output for pipelines
**Args:** `-nt -gtr -gamma -quiet -nopr aln.fa > tree.nwk 2> run.err`
**Explanation:** `-quiet` suppresses the options summary and likelihood reports from stderr; `-nopr` suppresses the progress indicator (the `.` stream); `2> run.err` keeps any actual error messages. Useful when running many FastTree invocations in a Snakemake/Nextflow pipeline to keep logs clean.

### Use pseudocounts for highly gapped alignments
**Args:** `-nt -gtr -pseudo -gamma aln.fa > tree.nwk`
**Explanation:** `-pseudo` (default weight 1.0) adds pseudocounts to distance estimation between sequences with little overlap. Without `-pseudo`, such pairs get unreliable or infinite distances and the NJ phase may fail or place them incorrectly. Use `-pseudo 0.5` to weaken the pseudocount.

### Refine branch lengths on a fixed topology
**Args:** `-nome -mllen -intree starting.nwk -nt -gtr aln.fa > refined.nwk`
**Explanation:** `-nome` disables minimum-evolution NNI and SPR; `-mllen` optimizes branch lengths only (no ML NNI); `-intree starting.nwk` uses the provided Newick topology as fixed; combined, this re-optimizes branch lengths on a pre-existing topology without changing it. Useful for testing topology hypotheses or updating branch lengths after sequence additions.

### Run global bootstrap with PHYLIP seqboot
**Args:** `seqboot -seed=1 < aln.phy > boot.phy && FastTree -nt -gtr -n 100 boot.phy > boot_trees.nwk && CompareToBootstrap.pl original.nwk boot_trees.nwk > support.txt`
**Explanation:** `seqboot` generates 100 resampled alignments in interleaved PHYLIP format; `-n 100` tells FastTree to read 100 alignments from a single file and emit 100 trees (one per line) to stdout; `CompareToBootstrap.pl` (shipped with FastTree source) counts how often each split in `original.nwk` appears in the 100 resampled trees, yielding rigorous bootstrap supports. This is the canonical pipeline for publishable FastTree bootstrap.

### Use -fastest for very large alignments (>50,000 sequences)
**Args:** `-nt -gtr -fastest -gamma -nosupport big_aln.fa > big_tree.nwk`
**Explanation:** `-fastest` speeds up the NJ phase by reducing the candidate-join search (sacrifices minor accuracy, recommended for >50k sequences); `-nosupport` skips SH-like local supports (saves runtime on huge trees where support is anyway noisy); `-gamma` still rescales branch lengths at the end. For >1 million sequences consider also adding more memory or splitting.

### Constrain the topology search with a binary alignment
**Args:** `-nt -gtr -constraints constraints.fa -constraintWeight 100 aln.fa > constrained.nwk`
**Explanation:** `-constraints constraints.fa` reads a separate alignment of 1s/0s that defines which sequences must group together (1) or may split (0); `-constraintWeight 100` is the relative weight of the constraint vs the ML score (default 100, raise to enforce more strictly). Used to enforce monophyly of known clades when FastTree's topology search would otherwise violate them.

### Compute a distance matrix instead of a tree
**Args:** `-nt -makematrix aln.fa > dist.phy`
**Explanation:** `-makematrix` skips all tree-building and emits a PHYLIP-format distance matrix to stdout. Combine with `-rawdist` for raw percent-different distances or `-nomatrix` to use Jukes–Cantor without a BLOSUM-like correction. Useful as input to other tools (e.g., neighbor, BIONJ).

### Resume a crashed run from a log file
**Args:** `-nt -gtr -log run.log -intree1 run.log aln.fa > resumed.nwk`
**Explanation:** `-log run.log` from the previous run saved intermediate trees; `-intree1 run.log` reads the last tree from the log as the starting topology and continues the search from that point. Combined with `-nome -mllen` you can also use this to re-optimize branch lengths on the crashed run's tree.

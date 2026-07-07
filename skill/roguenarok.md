---
name: roguenarok
category: phylogenetics
description: Identifies "rogue taxa" — leaves whose unstable position across a set of bootstrap / Bayesian trees destabilizes the consensus topology, with options to prune or downweight them.
tags: ["roguenarok", "rogue-taxa", "phylogenetics", "bootstrap", "consensus-tree", "tree-stability"]
author: oxo-call-community
source_url: "https://github.com/aberer/RogueNaRok"
---

## Concepts

- **Tool Overview**: RogueNaRok (v1.0.1, Aberer / MPI-EVA) is a tool for identifying "rogue taxa" in a set of phylogenetic trees (e.g., bootstrap replicates or a Bayesian posterior). A rogue taxon is a leaf whose unstable position destabilizes the consensus tree; pruning or downweighting the rogue improves the consensus's resolution and support.
- **Core Function**: Takes a Newick file with many trees (e.g., 1000 bootstrap replicates) and reports, for each leaf, a "rogue score" indicating how much that leaf's position varies across the tree set. The output includes the raw scores, a pruned tree set (with the top-N rogues removed), and the consensus tree of the pruned set.
- **Algorithm**: A leaf is a rogue if its position in the tree set has high bipartition entropy. RogueNaRok computes, for each leaf, the average Robinson-Foulds distance to the consensus over the tree set (or, alternatively, the increase in the consensus's bipartition support when the leaf is removed). Leaves with the highest distances are flagged.
- **Input Format**: A Newick file with one or more trees (one per line) and a corresponding taxon-name mapping (sometimes required for files that lack internal labels). The trees must be rooted or unrooted consistently; mixing rooted and unrooted is allowed but produces noisy results.
- **Output Format**: A TSV with one row per leaf: `taxon, raw_rogue_score, normalized_score, dropped_in_top_N`. Additional files include the pruned tree set (`pruned.trees`), the consensus of the pruned set (`pruned_consensus.nwk`), and a per-leaf stability plot (PDF).
- **Use Case**: Cleaning up a low-resolution phylogeny where a few taxa with long branches or missing data destabilize the consensus (a routine step before publishing a tree), improving the support values on a Bayesian posterior tree set, and identifying candidate taxa for re-sequencing or re-annotation in a problematic clade.

## Pitfalls

- **CRITICAL — Input trees must be unrooted (or consistently rooted)**: A mix of rooted and unrooted trees in the same file produces a meaningless consensus. Root them all with the same outgroup via `nw_reroot` first, or convert to unrooted with `nw_undirected`.
- **CRITICAL — The "drop top N" is not a hypothesis test**: RogueNaRok scores a leaf's instability, not its likelihood of being misplaced. A leaf that is unstable due to legitimate biological reasons (e.g., ILS, hybridization) is flagged but should not be removed from the final analysis.
- **The default tree-count threshold is 1%**: Trees in which a leaf appears < 1% of the time are dropped from the analysis; the leaf's "stability" is computed on the remaining 99%. For very large tree sets, this is fine; for small sets (e.g., 100 bootstrap replicates), the threshold is too low and the per-leaf scores are noisy.
- **The "raw" and "normalized" rogue scores are NOT directly comparable across datasets**: The raw score is the average RF distance to the consensus; the normalized is the raw divided by the maximum. Use the normalized for within-dataset comparison, and report the consensus topology alongside the score.
- **Pruning changes the tree's leaf set**: The "pruned" consensus has fewer leaves; downstream visualizations (e.g., iTOL) need to know which leaves were removed. RogueNaRok writes a `dropped_taxa.txt` for this purpose.
- **The bipartition entropy is computed once per leaf, not per branch**: A leaf can be unstable on a single branch and stable on others; the per-leaf score is the average. For per-branch analysis, use the `bipartitionSupport` companion tool (if installed).

## Examples

### Basic rogue-taxon analysis
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/`
**Explanation:** `-i` is the input Newick file with many trees, `-o` is the output directory. Produces `rogue_out/scores.tsv`, `rogue_out/pruned.trees`, and `rogue_out/pruned_consensus.nwk`. The default drop threshold is the top 5% most unstable leaves.

### Specify the number of trees to drop
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/ -d 10`
**Explanation:** `-d 10` drops the top 10 most unstable leaves (default is 5% of the leaf set). For a 100-taxon tree, this drops the top 10; for a 1000-taxon tree, the default 5% is 50 leaves. Adjust to taste.

### Use the raw RF distance (no normalization)
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/ --no-normalize`
**Explanation:** `--no-normalize` outputs the raw Robinson-Foulds distance, not the normalized score. Useful for comparing across datasets with different leaf counts.

### Drop a custom set of taxa
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/ --drop-taxa taxa_to_drop.txt`
**Explanation:** `--drop-taxa` specifies a file with one taxon name per line to drop from the analysis. The output consensus excludes these taxa. Useful for testing the effect of dropping suspected contaminants or outgroups.

### Output a per-leaf stability plot
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/ --plot`
**Explanation:** `--plot` writes a PDF with the per-leaf stability scores, sorted from most to least stable. Useful for a quick visual identification of the worst offenders.

### Use bipartition support as the metric
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/ --method bipartition`
**Explanation:** `--method bipartition` (if supported) uses bipartition support as the rogue metric instead of RF distance. A leaf that destabilizes a specific bipartition is flagged for removal.

### Generate a pruned consensus for downstream visualization
**Args:** `roguenarok -i bootstrap_trees.nwk -o rogue_out/ -d 20 && iTOL --tree rogue_out/pruned_consensus.nwk --metadata rogue_out/dropped_taxa.txt`
**Explanation:** Composite: run rogue analysis, then upload the pruned consensus to iTOL for interactive annotation. The `dropped_taxa.txt` is included as a metadata track to show which leaves were removed.

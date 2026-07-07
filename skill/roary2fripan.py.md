---
name: roary2fripan.py
category: utility
description: Converts the pan-genome matrix from Roary (gene_presence_absence.csv) into a FriPan-compatible TSV, enabling visual comparison of gene presence/absence across a Roary pangenome.
tags: ["roary2fripan", "fripan", "roary", "pangenome", "visualization", "presence-absence"]
author: oxo-call-community
source_url: "https://github.com/kwongj/roary2fripan"
---

## Concepts

- **Tool Overview**: roary2fripan (v0.1, kwongj) is a small Python helper that converts the Roary pan-genome matrix (`gene_presence_absence.csv`) into a FriPan-compatible TSV. FriPan is a Java tool for visualizing presence/absence patterns in a pan-genome; this script bridges the two.
- **Core Function**: Reads the Roary CSV, extracts the gene IDs and the per-genome presence/absence calls, and writes a TSV where rows are genes and columns are genomes (1/0 for present/absent). The output is loaded directly into FriPan for visual comparison.
- **Algorithm**: A straightforward Python `pandas`-based reformatting. No complex computation; the script reads the Roary CSV, transposes to the FriPan convention (genes as rows, genomes as columns), and writes a TSV with a header row of genome names.
- **Input Format**: The Roary `gene_presence_absence.csv` (or a Roary `gene_presence_absence.Rtab` for a binary form). Roary writes this file to its output directory by default. The script accepts a path to the CSV via `-i` or as the first positional argument.
- **Output Format**: A FriPan-compatible TSV with one row per gene group and one column per genome. Cells contain `1` (gene present) or `0` (absent). The first column is the Roary gene group ID; subsequent columns are the genome names. A metadata file with the genome order and grouping is also written.
- **Use Case**: Visualizing a Roary pan-genome in FriPan for a quick side-by-side comparison of gene content across isolates, generating a publication-quality presence/absence heatmap, comparing accessory-genome patterns between pathogenic and non-pathogenic strains, and identifying genes that are unique to a clade.

## Pitfalls

- **CRITICAL — The Roary CSV must be the post-Roary, not the pre-Roary version**: The `gene_presence_absence.csv` is written by Roary in its output directory. A CSV produced by some pre-processing tools has a different schema and produces a malformed FriPan file. Verify the header matches `Gene, Non-unique Gene name, Annotation, ...`.
- **CRITICAL — Roary's accessory gene column may contain commas in gene names**: If gene names contain commas (e.g., `Klebsiella, partial`), the CSV parsing breaks. Pre-process with `sed -i 's/,/_/g' gene_presence_absence.csv` to replace commas with underscores.
- **FriPan requires the gene names to be unique**: If two gene groups have the same name (e.g., both annotated as `hypothetical_protein`), FriPan will not deduplicate. Use the Roary `Gene` column (which is unique) as the first column instead of the `Non-unique Gene name` column.
- **The default FriPan coloring collapses identical columns**: If two genomes have identical gene content, FriPan shows them as the same color; verify the genome order matches the input.
- **Roary writes `gene_presence_absence.Rtab` as a binary form**: `roary2fripan.py` accepts `.Rtab` directly via `--input rtab`, but the output TSV is identical.
- **The script does not include paralog handling**: If a gene group contains paralogs in a genome, Roary's CSV shows the count; FriPan treats any non-zero as present. For paralog-aware analysis, use the Roary spreadsheet with the `Number of paralogs` column.

## Examples

### Convert a Roary CSV to FriPan TSV
**Args:** `roary2fripan.py -i gene_presence_absence.csv -o fripan_input.tsv`
**Explanation:** `-i` is the Roary CSV, `-o` is the FriPan-compatible TSV. The output can be opened with `java -jar FriPan.jar fripan_input.tsv` to visualize the pan-genome.

### Use the Roary Rtab as input
**Args:** `roary2fripan.py -i gene_presence_absence.Rtab --input-format rtab -o fripan_input.tsv`
**Explanation:** `--input-format rtab` tells the script to expect the Roary binary Rtab format (one row per gene, one column per genome, 0/1 values). Equivalent output to the CSV conversion.

### Specify a custom gene-ID column
**Args:** `roary2fripan.py -i gene_presence_absence.csv -o fripan_input.tsv --gene-id-column Gene`
**Explanation:** `--gene-id-column Gene` (default) uses the unique Roary gene group ID as the FriPan row ID. Change to `Non-unique Gene name` for more descriptive row labels, but be aware of duplicates.

### Restrict to accessory genes
**Args:** `roary2fripan.py -i gene_presence_absence.csv -o fripan_accessory.tsv --accessory-only`
**Explanation:** `--accessory-only` filters out genes that are present in all genomes (the core genome), keeping only the accessory genes. Useful for visualizing the variable portion of the pan-genome.

### Sort genes by frequency
**Args:** `roary2fripan.py -i gene_presence_absence.csv -o fripan_sorted.tsv --sort-by-frequency`
**Explanation:** `--sort-by-frequency` sorts the gene rows by the number of genomes in which they are present (descending), so the core genes are at the top and the rare genes are at the bottom. The standard FriPan ordering for quick visual scanning.

### Output a grouping file
**Args:** `roary2fripan.py -i gene_presence_absence.csv -o fripan_input.tsv --groups grouping.tsv`
**Explanation:** `--groups` writes an additional file with the genome order and a user-supplied grouping (e.g., pathotype, lineage). FriPan uses this to color the columns. The grouping file is a TSV: `genome<TAB>group`.

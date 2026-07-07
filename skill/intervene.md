---
name: intervene
category: visualization
description: A tool for intersection of multiple gene or genomic region sets and visualization as Venn diagrams, UpSet plots or pairwise heatmaps
tags: [intervene, visualization, venn, upset, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/asntech/intervene"
---

## Concepts

- **Tool Overview**: Intervene (v0.6.5) is a Python-based tool for the intersection and visualization of multiple gene or genomic region sets. It provides three main modules: venn for Venn diagrams (up to 6-way), upset for UpSet plots, and pairwise for intersection heatmaps.

- **Venn Diagram Module**: Generates classic Venn diagrams for 2-6 sets of genomic regions (BED/GTF/GFF) or gene lists. Supports custom colors, labels, and output formats including PDF, SVG, and PNG.

- **UpSet Plot Module**: Creates UpSet plots to visualize intersections of multiple sets using horizontal bar charts. Particularly useful when dealing with more than 4 sets where Venn diagrams become cluttered.

- **Pairwise Intersection Module**: Computes and visualizes pairwise intersections of N genomic region sets as clustered heatmaps. Supports Jaccard statistics, Fisher's exact test, and overlap fraction calculations.

- **Input Formats**: Supports genomic regions in BED, GTF, GFF, and VCF formats, as well as plain text lists of gene/SNP identifiers.

- **Interactive Web Application**: Intervene also provides a Shiny-based web application for interactive exploration of set intersections without command-line usage.

## Pitfalls

- **Set Size Limit**: Venn diagrams are limited to 6 sets. For more sets, use the UpSet module instead.

- **Input Format Compatibility**: Ensure all input files use the same genome build and coordinate system. Mixed formats may cause incorrect overlap calculations.

- **Memory for Large Datasets**: Processing many large BED files simultaneously can consume significant memory. Consider filtering or splitting large datasets.

- **Output Directory Overwrite**: By default, results are saved to `Intervene_results` directory. Use `-o` flag to specify a custom location and avoid overwriting previous results.

- **R Dependency for UpSet**: The UpSet plot module requires R and the UpSetR package. If R is not available, use `--scriptonly` to generate an R script for later execution.

- **Bed File Sorting**: Unsorted BED files may cause unexpected behavior. Sort input BED files by chromosome and start position before processing.

## Examples

### Generate a 3-way Venn diagram of ChIP-seq peaks
**Args:** `intervene venn -i H3K27ac.bed H3Kme3.bed H3K27me3.bed --names H3K27ac,H3Kme3,H3K27me3 --figtype png --dpi 300 -o venn_results/`
**Explanation:** Creates a 3-way Venn diagram showing overlaps between three histone modification ChIP-seq peak sets. Outputs a high-resolution PNG file.

### Create UpSet plot for multiple genomic region sets
**Args:** `intervene upset -i peaks/*.bed --filenames --order freq --ninter 30 --figsize 12 8 -o upset_results/`
**Explanation:** Generates an UpSet plot showing the top 30 intersection combinations from all BED files in the peaks directory, ordered by frequency.

### Pairwise intersection heatmap with Jaccard statistics
**Args:** `intervene pairwise -i super_enhancers/*.bed --filenames --compute jaccard --htype color -o pairwise_results/`
**Explanation:** Computes Jaccard similarity coefficients between all pairs of super-enhancer sets and visualizes as a color-coded heatmap.

### Run Venn module with test data
**Args:** `intervene venn --test -o test_output/`
**Explanation:** Runs the Venn module using built-in test data for quick verification of installation.

### Custom colors and figure size
**Args:** `intervene venn -i set1.bed set2.bed set3.bed --colors r,b,k --figsize 10 10 --fontsize 12 -o custom_plot/`
**Explanation:** Creates a Venn diagram with custom colors (red, blue, black), larger figure size, and adjusted font size.

### List mode for gene sets
**Args:** `intervene venn -i gene_list1.txt gene_list2.txt gene_list3.txt --type list --fill percentage --names Control,Treatment1,Treatment2 -o gene_venn/`
**Explanation:** Processes gene lists (not genomic regions) and displays intersection sizes as percentages rather than raw counts.
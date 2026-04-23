---
name: aniclustermap
category: metagenomics
description: Draw ANI clustermap for all-vs-all microbial genome comparison and visualization
tags: [ani, fastani, skani, clustermap, visualization, microbial-genomics]
author: oxo-call-community
source_url: "https://github.com/moshi4/ANIclustermap"
---

## Concepts

- **Tool Overview**: ANIclustermap calculates and visualizes Average Nucleotide Identity (ANI) between all-vs-all microbial genomes as a clustered heatmap. Version 2.0.1.
- **ANI Calculation**: Uses fastANI (default) or skani for computing pairwise ANI values between genomes. Skani may be more accurate for fragmented assemblies.
- **Clustering**: Applies scipy UPGMA hierarchical clustering to ANI matrix for dendrogram ordering. Groups similar genomes together visually.
- **Visualization**: Generates publication-quality clustered heatmap using seaborn with customizable colors, dimensions, and annotations.
- **Output Files**: PNG/SVG heatmap, TSV ANI matrix (clustered), and Newick dendrogram tree file.
- **Input Format**: Directory of genome FASTA files (*.fa, *.fna, *.fasta, optionally gzipped).
- **Customizable Colors**: Supports continuous and discrete color maps with configurable ranges for species boundary visualization (e.g., 95% ANI threshold).

## Pitfalls

- **Computation Time**: All-vs-all ANI calculation scales quadratically with genome count. Large collections (>100 genomes) may take hours.
- **Memory Usage**: Large genome collections require substantial memory for ANI matrix storage. Monitor memory for >500 genomes.
- **Fragmented Assemblies**: Highly fragmented assemblies may produce lower ANI values. Consider using skani mode for better handling of fragmented genomes.
- **File Naming**: Input FASTA filenames are used as genome labels. Use descriptive filenames before running.
- **Gzipped Input**: Supports gzipped FASTA (.fa.gz, .fna.gz) but may slow down ANI calculation.

## Examples

### Basic ANI clustermap
**Args:** `ANIclustermap -i ./genomes/ -o ./results/`
**Explanation:** Calculates all-vs-all ANI using fastANI and generates clustered heatmap. Input directory contains genome FASTA files. Outputs PNG heatmap, TSV matrix, and Newick tree.

### Use skani for fragmented genomes
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ --mode skani`
**Explanation:** Uses skani instead of fastANI for ANI calculation. Skani handles fragmented assemblies and lower-quality genomes better. Recommended for draft assemblies.

### Custom figure dimensions
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ --fig_width 14 --fig_height 12`
**Explanation:** Creates larger heatmap (14x12 inches) for better readability with many genomes. Adjust dimensions based on number of genomes and label length.

### Discrete color map with species boundary
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ --cmap_ranges 80,90,95,100`
**Explanation:** Uses discrete color ranges at 80%, 90%, 95%, 100% ANI. Highlights 95% species boundary commonly used for species delineation. Useful for taxonomic classification.

### Show ANI values on heatmap
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ --annotation --annotation_fmt .1f`
**Explanation:** Displays ANI values as annotations on each cell of the heatmap. Format .1f shows one decimal place. Only practical for small genome collections (<20).

### Multi-threaded calculation
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ -t 16`
**Explanation:** Uses 16 threads for parallel ANI calculation. Significantly speeds up analysis for large genome collections. Default uses max_threads - 1.

### Custom color scheme
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ --cmap_colors lime,yellow,orange,red --cmap_gamma 0.8`
**Explanation:** Custom color gradient from lime to red through yellow and orange. Gamma 0.8 adjusts color distribution. Useful for emphasizing differences in specific ANI ranges.

### Overwrite previous results
**Args:** `ANIclustermap -i ./genomes/ -o ./results/ --overwrite`
**Explanation:** Overwrites existing ANI calculation results in output directory. Use when re-running with different parameters or after adding new genomes.
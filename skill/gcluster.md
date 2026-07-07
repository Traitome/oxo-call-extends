---
name: gcluster
category: utility
description: Gcluster visualizes and compares genome contexts for numerous genomes using linear maps and homologous gene clustering
tags: [gcluster, genome, visualization, perl, MCL, BLAST, orthoMCL, phylogenetic]
author: oxo-call-community
source_url: "https://github.com/Xiangyang1984/Gcluster"
---

## Concepts

- **Tool Overview**: Gcluster is a standalone Perl application for visualizing and comparing genome contexts across numerous genomes. It creates high-quality linear maps showing genes flanking regions of interest, with homologous genes clustered together.
- **Core Function**: Gcluster takes GenBank-formatted genome annotations and a list of locus tags for genes of interest, then generates publication-quality figures comparing gene neighborhoods across genomes.
- **Input Data**: Requires two mandatory inputs: (1) a directory containing GenBank (.gbk/.gbff) files with annotated genomes, and (2) a locus tag file listing genes of interest (one locus tag per genome).
- **Optional Inputs**: phylogenetic_tree.nwk (Newick format) for phylogeny-aware ordering; strain_reorder_file.txt for custom genome ordering.
- **Output Formats**: PNG (raster) and SVG (vector graphics) output with customizable fonts, colors, and figure dimensions.
- **Dependencies**: Requires MCL (Markov Clustering), NCBI BLAST+, and Perl modules (GD, GD::SVG, Bio::SeqIO, Bio::Tree::NodeI, Bio::TreeIO).
- **Installation**: Available via conda: `conda install -c bioconda gcluster`. Source installation requires setting paths for blastp, makeblastdb, and mcl in the Perl scripts.
- **Citation**: Li X, Chen F, Chen Y. Gcluster: a simple-to-use tool for visualizing and comparing genome contexts for numerous genomes. Bioinformatics 2020;36(12):3871-3873.

## Pitfalls

- **Dependency complexity**: Gcluster requires multiple external programs (BLAST+, MCL) and Perl modules. Installation via conda is recommended to resolve all dependencies automatically.
- **GenBank annotation requirement**: All input genomes must be annotated GenBank files. Draft genomes with partial annotations may produce incomplete visualizations.
- **Locus tag format**: Each genome must have exactly one locus tag entry in the interested_gene_file. File names must match exactly between the GenBank directory and the locus tag file.
- **Memory usage**: Processing hundreds of genomes with BLAST comparisons can be memory-intensive. Use the `-m` option for multi-threading to distribute computation.
- **Special characters in file names**: GenBank file names cannot contain special characters or spaces. Use underscores or alphanumeric characters only.
- **Phylogenetic tree matching**: When using phylogenetic_file, all tree node names must exactly match GenBank file names (without .gbk extension).
- **Perl execution**: When running from source, use `perl Gcluster.pl`; when installed via conda, can execute directly as `Gcluster.pl`.

## Examples

### Basic genome context visualization
**Args:** `Gcluster.pl -dir ./genomes -gene interested_genes.txt -out ./output`
**Explanation:** The fundamental Gcluster operation requires a directory of GenBank files and a gene-of-interest file. Each genome's gene neighborhood is extracted, homologous genes are clustered via MCL/BLAST, and a comparative figure is generated showing conserved gene contexts.

### Generate gene-of-interest file via BLAST
**Args:** `interested_gene_generation.pl -dir ./genomes -db homologous_proteins.fasta -m 8`
**Explanation:** When you have a protein sequence homologous to your gene of interest, interested_gene_generation.pl performs reciprocal BLASTP against all genomes to identify the best matching locus tag in each genome. The `-m 8` enables 8-threaded parallel processing for large genome sets.

### Phylogeny-aware genome ordering
**Args:** `Gcluster.pl -dir ./genomes -gene genes.txt -tree phylogeny.nwk -out ./output`
**Explanation:** Providing a Newick-format phylogenetic tree causes Gcluster to order genomes according to their evolutionary relationships. Homologous gene clusters are then arranged to highlight both vertical descent (phylogeny) and horizontal gene transfer (conserved gene neighborhoods across divergent lineages).

### Custom genome ordering
**Args:** `Gcluster.pl -dir ./genomes -gene genes.txt -reorder strain_order.txt -out ./output`
**Explanation:** The strain_reorder_file is a two-column tab-delimited file with strain names and numerical order. This overrides automatic ordering to present genomes in a user-specified arrangement, useful for presenting results in manuscript figures with specific layouts.

### High-resolution SVG output
**Args:** `Gcluster.pl -dir ./genomes -gene genes.txt -format svg -w 2000 -h 1200 -out ./output`
**Explanation:** SVG output produces vector graphics suitable for publication at any resolution. The `-w 2000 -h 1200` specifies pixel dimensions for the figure canvas. SVG files can be edited in vector graphics software (Illustrator, Inkscape) to fine-tune labels and colors.

### Batch processing with multiple threads
**Args:** `Gcluster.pl -dir ./genomes -gene genes.txt -m 16 -out ./output`
**Explanation:** The `-m 16` parameter enables parallel processing using 16 threads, significantly accelerating BLAST searches and MCL clustering when analyzing large genome collections. Memory usage scales with thread count.

### Color scheme customization
**Args:** `Gcluster.pl -dir ./genomes -gene genes.txt -color Configure/color_schema.txt -out ./output`
**Explanation:** GCluster supports custom color schemes via a configuration file. Colors can be assigned to gene functional categories, protein families, or taxonomic groups, enhancing visual distinction between homologous gene clusters across genomes.

### Font size adjustment for large genomes
**Args:** `Gcluster.pl -dir ./genomes -gene genes.txt -font 8 -out ./output`
**Explanation:** When visualizing many genomes with limited horizontal space, reducing font size with `-font 8` (8pt) prevents label overlap while maintaining readability. The default font size is typically 10-12pt depending on figure dimensions.

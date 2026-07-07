---
name: fishtaco
category: metagenomics
description: "FishTaco is a computational framework for decomposing functional shifts in metagenomic data by identifying which taxa are driving disease-associated microbiome changes."
tags: [fishtaco, metagenomics, microbiome, functional-analysis, taxa, bioinformatics, bacterial, microbial]
author: oxo-call-community
source_url: "https://github.com/borenstein-lab/fishtaco/"
---

## Concepts
- **Tool Overview**: FishTaco (Functional Interpretation of Metagenomic Data) is a computational framework for decomposing functional shifts observed in comparative metagenomic analyses into individual taxon-level contributions.
- **Core Function**: Identifies which specific taxa are driving functional enrichment or depletion between two conditions (e.g., disease vs healthy). Goes beyond taxonomic profiling to explain functional consequences of microbiome changes.
- **Statistical Approach**: Uses permutation-based testing with normalization and scaling schemes that preserve community taxonomic characteristics. Accounts for inter-species dependencies using game-theory mathematics.
- **Input Files**: Requires (1) taxa abundance matrix (taxa x samples), (2) function abundance matrix (KO/pathways x samples), (3) sample labels (case/control), (4) genomic content file (taxa x functions).
- **Output**: Quantifies each taxon's contribution to functional shifts, classified as: driver (enriching), attenuator (depleting), case-associated, or control-associated.
- **Application**: Particularly useful for linking taxonomic composition changes to functional consequences in diseases like IBD, diabetes, and other microbiome-associated conditions.
- **Installation**: `pip install fishtaco` or clone from GitHub. Requires Python 2.7+ (Python 3 not supported), R for visualization package.

## Pitfalls
- **Python 2 Dependency**: FishTaco requires Python 2.7 and does not support Python 3. Consider using conda environment or Docker container for compatibility.
- **Input File Format Strictness**: Files must be tab-delimited with exact headers. Incorrect formatting causes silent failures or wrong results. Validate formats before running.
- **Taxonomic Level Consistency**: Taxa names in abundance file must exactly match those in genomic content file. Case sensitivity matters.
- **Minimum Sample Size**: Requires sufficient samples per group for permutation testing. Very small cohorts (<5 per group) may produce unreliable results.
- **Reference Genome Quality**: Genomic content file quality depends on reference database completeness. Poorly characterized taxa may show minimal contributions due to incomplete genomes.
- **Multiple Testing**: When analyzing many functions, apply FDR correction. FishTaco outputs many taxa-function pairs which can lead to false discoveries.

## Examples
### Run FishTaco analysis
**Args:** `fishtaco.py --taxa taxa_abundance.txt --functions function_abundance.txt --labels sample_labels.txt --genomic_content genomic_content.txt --output results/`
**Explanation:** Main FishTaco command. All input files are tab-delimited text files. Output directory will contain main results file and summary statistics.

### Generate visualization plots
**Args:** `MultiFunctionTaxaContributionPlots(input_dir="results/", input_prefix="fishtaco_output", input_taxa_taxonomy="taxonomy.txt", plot_type="bars")`
**Explanation:** R command to generate FishTaco visualization plots from analysis results. Requires FishTacoPlot R package installed separately.

### Filter significant taxa-functions
**Args:** `fishtaco.py --taxa taxa.txt --functions funcs.txt --labels labels.txt --genomic genomic.txt --output out/ --fdr 0.05`
**Explanation:** Applies FDR correction with 0.05 threshold to identify statistically significant taxon-function relationships. Only significant pairs reported in output.

### Specify taxonomic level
**Args:** `fishtaco.py --taxa species_abundance.txt --functions kegg.txt --labels labels.txt --genomic species_ko.txt --output out/ --taxa-level species`
**Explanation:** Analyzes at specific taxonomic level (species, genus, family). Ensure all input files are at the same taxonomic level.

### Custom function list
**Args:** `fishtaco.py --taxa taxa.txt --functions funcs.txt --labels labels.txt --genomic genomic.txt --output out/ --function-filter ko00020,ko00540`
**Explanation:** Only analyzes specified KEGG orthologs or functions. Useful for focused analysis on pathways of interest rather than genome-wide.

### Online visualization
**Args:** `http://elbo-spice.cs.tau.ac.il/shiny/FishTacoPlot/`
**Explanation:** Upload FishTaco results to web tool for interactive visualization without installing R packages. Supports browsing by function or taxon.

### Batch processing multiple comparisons
**Args:** `for labels in labels1.txt labels2.txt labels3.txt; do fishtaco.py --taxa taxa.txt --functions funcs.txt --labels $labels --genomic genomic.txt --output out_$labels; done`
**Explanation:** Scripts multiple FishTaco runs for different case/control definitions. Useful for comparing disease subtypes or treatment groups.

### View detailed output
**Args:** `head -20 results/*_main_output_*`
**Explanation:**查看主要输出文件内容。输出文件包含每个taxon对每个功能的贡献值，格式为"mode:value"。

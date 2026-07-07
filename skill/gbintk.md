---
name: gbintk
category: metagenomics
description: "GraphBin-Tk: assembly graph-based metagenomic binning toolkit combining GraphBin, GraphBin2, and MetaCoAG"
tags: [gbintk, metagenomics, binning, contigs, assembly-graph, graphbin, magnis]
author: oxo-call-community
source_url: "https://github.com/metagentools/gbintk"
---
## Concepts

- **Tool Overview**: GraphBin-Tk (gbintk) is a comprehensive metagenomic binning toolkit that combines assembly graph-based binning and refinement techniques from GraphBin, GraphBin2, and MetaCoAG into a unified workflow.
- **Core Function**: Performs assembly graph-based binning of metagenomic contigs, assigning contigs to bins representing potential genome assemblies (MAGs - Metagenome-Assembled Genomes).
- **Graph-Based Approach**: Uses assembly graph connectivity information (from tools like SPAdes, MEGAHIT) to improve binning accuracy beyond composition-based methods alone.
- **Key Subcommands**:
  - `gbintk bin` - Initial binning of contigs
  - `gbintk refine` - Refinement of existing bins using graph information
  - `gbintk evaluate` - Quality assessment of bins
  - `gbintk visualize` - Visualization of results
- **Input Requirements**:
  - Assembly graph file (GFA format) from SPAdes/MEGAHIT
  - Initial binning results (from MetaBAT2, MaxBin2, VAMB, etc.)
  - Coverage information (from Bowtie2, BBMap, etc.)
- **Output**: Refined bins in FASTA format, along with quality metrics and visualization files.
- **Installation**: `conda install -c bioconda gbintk` or `pip install gbintk`

## Pitfalls

- **CRITICAL: Graph File Format**: gbintk requires assembly graphs in GFA format. Ensure your assembler outputs GFA (not just FASTG). SPAdes with `-- assembler` option produces GFA files.
- **CRITICAL: Compatible Assemblers**: Only SPAdes and MEGAHIT assembly graphs are directly compatible. Other assemblers may require format conversion.
- **Input Consistency**: The contig names in the assembly graph must exactly match contig names in the coverage and initial binning files. Any mismatch will cause errors.
- **Coverage File Format**: Coverage files must be tab-separated with columns: contig_id, coverage_value. Header is optional but recommended.
- **Memory Intensive**: Large metagenomes with millions of contigs require significant RAM (32GB+ recommended).
- **Initial Binning Quality**: gbintk refines existing bins; if initial binning is very poor, refinement may not fully correct errors. Consider using multiple binning tools and comparing results.
- **Python Version**: Requires Python 3.9-3.12. Python 3.13 is not supported.
- **Execution Time**: Refinement on large datasets can take hours to complete. Plan accordingly.

## Examples

### Run initial binning with GraphBin approach
**Args:** `gbintk bin --graph assembly_graph.gfa --paths contigs.paths --coverage coverage.tsv --output refined_bins/`
**Explanation:** This command performs initial binning using the assembly graph and coverage information. The `--paths` file maps contigs to their paths in the graph. Output will be stored in the specified directory.

### Refine existing bins from MetaBAT2
**Args:** `gbintk refine --graph assembly.gfa --bins metabat2_bins/ --output refined/ --prefix metaB2`
**Explanation:** Takes existing bins from MetaBAT2 (or any other binning tool) and refines them using assembly graph connectivity. The prefix is used for output file naming.

### Refine bins from multiple binning tools
**Args:** `gbintk refine --graph assembly.gfa --bins maxbin2_bins/ --bins metabat2_bins/ --output combined_refined/`
**Explanation:** One of gbintk's strengths is combining information from multiple binning tools. Providing multiple bin directories allows the tool to leverage consensus between different methods.

### Evaluate bin quality with CheckM-style metrics
**Args:** `gbintk evaluate --bins refined_bins/ --output quality_report.tsv`
**Explanation:** Assesses bin quality using completeness and contamination estimates. The report includes standard MAG quality metrics following MIMAG standards (high, medium, low quality).

### Visualize binning results on the assembly graph
**Args:** `gbintk visualize --graph assembly.gfa --bins refined_bins/ --output viz/`
**Explanation:** Creates visualization files showing how contigs were binned relative to the assembly graph structure. Useful for understanding bin boundaries and potential misassignments.

### Use with SPAdes hybrid assembly graph
**Args:** `gbintk bin --graph spades_assembly/gfa-contigs.gfa --paths spades_assembly/contigs.paths --coverage abundance.tsv --output spades_bins/`
**Explanation:** When working with SPAdes hybrid assemblies (Illumina+Oxford Nanopore, for example), provide the GFA and paths files from the SPAdes output directory.

### Specify minimum contig length
**Args:** `gbintk bin --graph assembly.gfa --min-length 1500 --coverage cov.tsv --output bins/`
**Explanation:** Filter out contigs shorter than the specified length before binning. 1500bp is a common threshold as it approximates single-copy gene detection limits for genome binning.

### Parallel execution on multiple cores
**Args:** `gbintk refine --graph large_assembly.gfa --bins initial_bins/ --output refined/ --threads 16`
**Explanation:** Use the --threads option to enable parallel processing. This significantly speeds up computation on large datasets with many contigs.

### Combine composition and graph-based features
**Args:** `gbintk bin --graph assembly.gfa --composition --coverage cov.tsv --output bins/`
**Explanation:** The --composition flag enables use of k-mer composition features in addition to graph topology. This hybrid approach often improves binning accuracy for challenging datasets.

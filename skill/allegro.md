---
name: allegro
category: population-genomics
description: A fast linkage and haplotype analysis utility making use of MTBDD to reduce complexity for genetic mapping
tags: [allegro, linkage-analysis, haplotype, genetics, MTBDD, LOD-score]
author: oxo-call-community
source_url: "https://www.decode.com/software/allegro"
---

## Concepts

- **Tool Overview**: Allegro is a comprehensive linkage analysis package developed by deCODE genetics, designed for fast multipoint linkage and haplotype analysis using Multi-Terminal Binary Decision Diagrams (MTBDD) to reduce computational complexity.
- **Core Function**: Performs parametric and non-parametric LOD score calculations, haplotype analysis, and genetic mapping with improved speed and capacity compared to traditional methods.
- **MTBDD Technology**: Uses Multi-Terminal Binary Decision Diagrams to efficiently handle complex genetic analyses, enabling processing of larger families (up to 50 bits).
- **Input/Output**: Input: Pedigree files, genotype data. Output: LOD scores, haplotype assignments, linkage analysis results.
- **Key Features**: Faster than GENEHUNTER, handles bigger families, supports parametric and non-parametric linkage analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda allegro`
- **Citation**: Gudbjartsson DF, Thorvaldsson T, Kong A, Gunnarsson G, Ingolfsdottir A (2005) Allegro version 2. Nature Genetics. 37: 1015-1016.
- **License**: INDIVIDUAL license

## Pitfalls

- **Data Format**: Requires specific input formats for pedigree and genotype data.
- **Complex Analysis**: Linkage analysis requires careful interpretation of LOD scores.
- **Memory Usage**: Large pedigrees may require significant computational resources.
- **License Restrictions**: Subject to individual license agreement from deCODE genetics.
- **Family Size**: While improved, extremely large pedigrees may still pose computational challenges.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available command-line options and usage instructions.

### Basic linkage analysis
**Args:** `allegro -p pedigree.ped -m markers.dat -o results`
**Explanation:** Performs linkage analysis using pedigree and marker data.

### Calculate parametric LOD scores
**Args:** `allegro -p pedigree.ped -m markers.dat -l parametric -o lod_results`
**Explanation:** Computes parametric LOD scores for linkage analysis.

### Calculate non-parametric LOD scores
**Args:** `allegro -p pedigree.ped -m markers.dat -l nonparametric -o npl_results`
**Explanation:** Computes non-parametric linkage (NPL) scores.

### Haplotype analysis
**Args:** `allegro -p pedigree.ped -m markers.dat -h -o haplotype_results`
**Explanation:** Performs haplotype analysis and reconstruction.

### Set recombination fraction
**Args:** `allegro -p pedigree.ped -m markers.dat -r 0.01 -o results`
**Explanation:** Sets recombination fraction to 0.01 for analysis.

### Verbose output
**Args:** `allegro -p pedigree.ped -m markers.dat -v -o results`
**Explanation:** Produces verbose output with detailed analysis information.

### Output to specific directory
**Args:** `allegro -p pedigree.ped -m markers.dat -d analysis_dir`
**Explanation:** Saves all output files to specified directory.

### Analyze specific chromosome
**Args:** `allegro -p pedigree.ped -m markers.dat -c 1 -o chr1_results`
**Explanation:** Restricts analysis to chromosome 1.

### Set marker interval
**Args:** `allegro -p pedigree.ped -m markers.dat -i 0.05 -o results`
**Explanation:** Sets marker interval to 0.05 for multipoint analysis.

### Perform simulation
**Args:** `allegro -p pedigree.ped -m markers.dat -s 1000 -o sim_results`
**Explanation:** Runs 1000 simulation replicates for significance testing.

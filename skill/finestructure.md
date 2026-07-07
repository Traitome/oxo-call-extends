---
name: finestructure
category: population-genomics
description: "fineSTRUCTURE is a fast and powerful algorithm for identifying population structure using dense sequencing data through chromosome painting."
tags: [finestructure, population-genomics, population-structure, haplotype, chromosome-painting, bioinformatics, genetics, admixture]
author: oxo-call-community
source_url: "https://people.maths.bris.ac.uk/~madjl/finestructure/finestructure.html"
---

## Concepts

- **Tool Overview**: fineSTRUCTURE is a Bayesian clustering algorithm for identifying population structure using dense sequencing data. It works in conjunction with ChromoPainter to perform haplotype-based "chromosome painting" that reveals fine-scale population structure invisible to frequency-based methods.
- **Core Function**: Uses haplotype sharing patterns to infer population structure and ancestry relationships. Each individual is painted as a combination of donor haplotypes, and these painting patterns are used for clustering.
- **Input/Output**: Input: Phased genotype data (VCF, phased haplotypes) and genetic map. Output: Co-ancestry matrix, population cluster assignments, phylogenetic tree, and uncertainty estimates.
- **Algorithm**: Two-phase pipeline: (1) ChromoPainter uses the Li-Stephens model to "paint" each haplotype as a mosaic of donor haplotypes, (2) fineSTRUCTURE performs MCMC clustering on the painting patterns to identify populations.
- **Key Features**: Model-based Bayesian inference, handles millions of SNPs, supports thousands of individuals, provides full assignment uncertainty, enables both discrete and continuous population structure modeling, integrates with GLOBETROTTER for admixture dating.
- **Installation**: Download from http://www.paintmychromosomes.com or `conda install -c bioconda finestructure`. Requires chromosome painting data from ChromoPainter.

## Pitfalls

- **Phasing Requirement**: Input data must be phased. Use tools like SHAPEIT or Beagle for phasing before running ChromoPainter.
- **Genetic Map Quality**: Results depend on accurate recombination maps. Use population-specific maps when available, or acknowledge limitations of using generic maps.
- **Computational Demands**: Large datasets (thousands of individuals, millions of SNPs) require substantial memory and CPU time. Consider chunking the genome for parallel processing.
- **MCMC Convergence**: Insufficient iterations lead to unreliable results. Run multiple chains and use built-in convergence diagnostics.
- **LD Proxy Assumption**: The method assumes haplotypes copy from other study individuals, which works well for dense data but may not suit low-density markers.

## Examples

### Phase genetic data with SHAPEIT
**Args:** `shapeit --input data.bcf --output data.phased --map genetic_map.b38.gz --thread 8`
**Explanation:** Phases genotype data before chromosome painting. High-quality phasing is critical for accurate population structure inference.

### Run ChromoPainter in EM mode
**Args:** `ChromoPainterv2 -g input.genotypes -r 100 -f -em 1 -o output`
**Explanation:** First phase estimates effective population size (Ne) and mutation rate using Expectation-Maximization. The -r specifies number of samples to use in initial run.

### Paint haplotypes with ChromoPainter
**Args:** `ChromoPainterv2 -g input.phased -r 200 -f -i 1000000 -o painted`
**Explanation:** Performs full chromosome painting with 200 samples per iteration and 1M iterations. Outputs chunk counts/lengths for each recipient-donor pair.

### Combine multiple chromosomes
**Args:** `ChromoCombine -i painted_chr1.out painted_chr2.out -o combined`
**Explanation:** Merges painting results across chromosomes to create a genome-wide co-ancestry matrix for fineSTRUCTURE.

### Run fineSTRUCTURE MCMC
**Args:** `finestructure -x 100000 -y 1000000 -z 1000 combined.chunkcounts.out combined.mcmc.xml`
**Explanation:** Full MCMC run with 100K burn-in, 1M iterations, sampling every 1000. Adjust based on dataset size and complexity.

### Extract best clustering
**Args:** `finestructure -m T combined.mcmc.xml`
**Explanation:** Extracts the best (maximum posterior probability) population assignment for each individual from the MCMC chain.

### Build population tree
**Args:** `finestructure -m S combined.mcmc.xml`
**Explanation:** Infs a hierarchical tree of population relationships using the SAM (Structural Arrangements Model).

### Use GLOBETROTTER for admixture dating
**Args:** `Rscript globetrotter.R painted.chunkcounts.out`
**Explanation:** After fineSTRUCTURE clustering, use GLOBETROTTER to date admixture events and identify source populations. Input the ChromoPainter output directly to GLOBETROTTER.

### Assess convergence
**Args:** `finestructure -m C combined.mcmc.xml`
**Explanation:** Checks MCMC convergence by comparing variation within and between chains. Look for Gelman-Rubin statistics close to 1.0.

### Run in parallel with genome chunking
**Args:** `for chr in $(seq 1 22); do ChromoPainterv2 -g chr${chr}.phased -o painted_chr${chr} & done`
**Explanation:** For chromosome-level data, split genome into chunks and run ChromoPainter in parallel, then merge with ChromoCombine to reduce overall runtime while maintaining accuracy.

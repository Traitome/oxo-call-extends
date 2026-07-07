---
name: flexsweep
category: utility
description: "Flexsweep is a versatile tool for detecting selective sweeps in population genomic data using multiple complementary statistics."
tags: [flexsweep, utility, population-genomics, selective-sweeps, natural-selection, bioinformatics, genetics]
author: oxo-call-community
source_url: "https://github.com/jmurga/flexsweep"
---

## Concepts
- **Tool Overview**: Flexsweep detects selective sweeps in population genomic data by combining multiple statistical methods for robust signal detection.
- **Core Function**: Identifies genomic regions under positive selection by analyzing patterns of genetic variation and haplotype structure.
- **Input/Output**: Input: VCF files, genotype matrices, or SNP data. Output: Candidate sweep regions with significance scores.
- **Statistical Methods**: Implements multiple complementary statistics including XP-EHH, iHS, CLR, and Tajima's D for cross-validation.
- **Population Comparison**: Supports comparison between populations to identify population-specific sweeps.
- **Visualization**: Generates Manhattan plots and regional visualization of sweep signals for candidate regions.
- **Installation**: `conda install -c bioconda flexsweep` or clone from GitHub. Requires Python 3.x and numpy.

## Pitfalls
- **Population Structure**: Population stratification can produce false positives. Use appropriate controls or PCA correction.
- **Sample Size**: Requires sufficient sample size for reliable statistics. Small populations may produce unstable results.
- **Linkage Disequilibrium**: High LD regions may confound sweep signals. Use LD pruning before analysis.
- **Selection Strength**: Weak or incomplete sweeps may be missed. Combine multiple statistics for better detection.
- **Demographic History**: Population bottlenecks or expansions can mimic sweep signals. Use demographic models for correction.
- **Reference Genome**: Poor reference genome quality affects variant calling and sweep detection.

## Examples
### Detect sweeps from VCF
**Args:** `flexsweep --vcf population.vcf --output sweeps.txt --method xpehh,ihs,clr`
**Explanation:** Runs multiple sweep detection methods on VCF file and outputs candidate regions.

### Population comparison
**Args:** `flexsweep --vcf population1.vcf --vcf2 population2.vcf --output comparison.txt`
**Explanation:** Compares two populations to identify population-specific selective sweeps.

### Generate Manhattan plot
**Args:** `flexsweep --vcf population.vcf --plot manhattan.png --threshold 5`
**Explanation:** Generates Manhattan plot showing sweep signals across the genome.

### Regional analysis
**Args:** `flexsweep --vcf population.vcf --region chr1:1000000-2000000 --output region_sweeps.txt`
**Explanation:** Focuses analysis on specific genomic region for detailed examination.

### Combine statistics
**Args:** `flexsweep --vcf population.vcf --output combined.txt --combine-method fisher`
**Explanation:** Combines multiple statistical methods using Fisher's method for improved detection power.

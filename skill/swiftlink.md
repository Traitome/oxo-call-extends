---
name: swiftlink
category: population-genetics
description: Multipoint parametric linkage analysis tool for large consanguineous pedigrees.
tags: [swiftlink, linkage-analysis, pedigree, genetics]
author: oxo-call-community
source_url: "https://github.com/ajm/swiftlink"
---

## Concepts

- **Tool Overview**: swiftlink (v1.0) performs multipoint linkage analysis for large pedigrees.
- **Core Function**: Analyzes genetic linkage in large consanguineous families.
- **Algorithm**: Uses Markov chain Monte Carlo (MCMC) for linkage analysis.
- **Input/Output**: Input: Pedigree file, marker data; Output: LOD scores.
- **Applications**: Genetic mapping, disease gene identification.
- **Installation**: `conda install -c bioconda swiftlink` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large pedigrees require significant memory.
- **Computational Time**: Analysis of large pedigrees can be slow.
- **Parameter Tuning**: Incorrect parameters affect results.
- **Pedigree Quality**: Requires accurate pedigree information.
- **Marker Density**: May require sufficient marker coverage.
- **Population Structure**: May be affected by population substructure.

## Examples

### Display help
**Args:** `swiftlink --help`
**Explanation:** Shows available options and usage information.

### Basic linkage analysis
**Args:** `swiftlink -i pedigree.ped -m markers.txt -o lod_scores.txt`
**Explanation:** Perform linkage analysis on pedigree.

### With VCF input
**Args:** `swiftlink -i pedigree.ped -v variants.vcf -o lod_scores.txt`
**Explanation:** Use VCF file for marker data.

### Verbose mode
**Args:** `swiftlink -i pedigree.ped -m markers.txt -o lod_scores.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `swiftlink -i pedigree.ped -m markers.txt -o lod_scores.txt --stats`
**Explanation:** Generate statistics about linkage analysis.

### Batch processing
**Args:** `for ped in pedigrees/*.ped; do swiftlink -i $ped -m markers.txt -o results/${ped%.ped}.txt; done`
**Explanation:** Process multiple pedigrees.

### Filter by significance
**Args:** `swiftlink -i pedigree.ped -m markers.txt -o lod_scores.txt -p 0.05`
**Explanation:** Filter by significance threshold.

### Include haplotypes
**Args:** `swiftlink -i pedigree.ped -m markers.txt -o lod_scores.txt --haplotype`
**Explanation:** Include haplotype analysis.

### Generate report
**Args:** `swiftlink -i pedigree.ped -m markers.txt -o lod_scores.txt --report`
**Explanation:** Generate comprehensive linkage analysis report.

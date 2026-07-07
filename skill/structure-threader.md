---
name: structure-threader
category: hpc
description: A program to parallelize runs of STRUCTURE, fastStructure and MavericK.
tags: [structure-threader, parallel-processing, population-genetics, hpc]
author: oxo-call-community
source_url: "https://gitlab.com/StuntsPT/Structure_threader"
---

## Concepts

- **Tool Overview**: structure-threader (v1.3.11) is a tool for parallelizing population structure analysis tools.
- **Core Function**: Runs multiple replicates of STRUCTURE, fastStructure, or MavericK in parallel.
- **Algorithm**: Manages parallel execution and aggregates results from multiple runs.
- **Input/Output**: Input: Genotype data and configuration; Output: Aggregated results.
- **Applications**: Population genetics, large-scale population structure analysis.
- **Installation**: `conda install -c bioconda structure-threader` or download from GitHub.

## Pitfalls

- **Resource Management**: Requires proper resource allocation for parallel runs.
- **Memory Requirements**: Parallel runs require significant memory.
- **Version Compatibility**: May not work with all versions of underlying tools.
- **Parameter Tuning**: Incorrect parameters affect parallelization efficiency.
- **Result Aggregation**: Poor aggregation affects final results.
- **Error Handling**: Individual run failures may affect overall results.

## Examples

### Display help
**Args:** `structure-threader --help`
**Explanation:** Shows available options and usage information.

### Basic parallel analysis
**Args:** `structure-threader -i genotypes.str -o results/ -K 3 -t 8`
**Explanation:** Run STRUCTURE with K=3 using 8 threads.

### With fastStructure
**Args:** `structure-threader -i genotypes.str -o results/ -K 5 -t 12 --program faststructure`
**Explanation:** Use fastStructure with 12 threads.

### Verbose mode
**Args:** `structure-threader -i genotypes.str -o results/ -K 3 -t 8 -v`
**Explanation:** Run with detailed logging for debugging.

### Run multiple K values
**Args:** `structure-threader -i genotypes.str -o results/ -K 2-10 -t 8`
**Explanation:** Run analysis for K values from 2 to 10.

### Batch processing
**Args:** `structure-threader -i genotypes_dir/ -o results/ -K 3 -t 8`
**Explanation:** Process multiple genotype files together.

### Filter by quality
**Args:** `structure-threader -i genotypes.str -o results/ -K 3 -t 8 -q 0.9`
**Explanation:** Use minimum confidence threshold of 0.9.

### Include Evanno analysis
**Args:** `structure-threader -i genotypes.str -o results/ -K 2-10 -t 8 --evanno`
**Explanation:** Run Evanno analysis for optimal K selection.

### Generate report
**Args:** `structure-threader -i genotypes.str -o results/ -K 3 -t 8 --report`
**Explanation:** Generate comprehensive HTML report.

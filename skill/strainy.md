---
name: strainy
category: metagenomics
description: Assembly-based metagenomic strain phasing using long reads.
tags: [strainy, metagenomics, strain-phasing, long-reads]
author: oxo-call-community
source_url: "https://github.com/katerinakazantseva/strainy"
---

## Concepts

- **Tool Overview**: strainy (v1.2) is a tool for assembly-based metagenomic strain phasing using long-read sequencing data.
- **Core Function**: Assembles and phases strains from complex microbial communities using long reads.
- **Algorithm**: Uses assembly graph construction and variant phasing to separate strains.
- **Input/Output**: Input: Long-read sequencing reads (FASTQ); Output: Phased strain assemblies.
- **Applications**: Strain-resolved metagenomics, microbial population analysis, pathogen tracking.
- **Installation**: `conda install -c bioconda strainy` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality long reads affect assembly accuracy.
- **Community Complexity**: Very complex communities are hard to phase.
- **Strain Similarity**: Highly similar strains are hard to distinguish.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Assembly and phasing can be computationally intensive.
- **Reference Dependence**: May require reference genomes for accurate phasing.

## Examples

### Display help
**Args:** `strainy --help`
**Explanation:** Shows available options and usage information.

### Basic strain phasing
**Args:** `strainy -i reads.fastq -o results/`
**Explanation:** Phase strains from long-read metagenomic data.

### With reference genome
**Args:** `strainy -i reads.fastq -r reference.fasta -o results/`
**Explanation:** Use reference genome for guided phasing.

### Verbose mode
**Args:** `strainy -i reads.fastq -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strainy -i reads.fastq -o results/ --plot`
**Explanation:** Generate visualization of phased strains.

### Custom parameters
**Args:** `strainy -i reads.fastq -o results/ -k 31`
**Explanation:** Use k-mer size of 31 for assembly.

### Batch processing
**Args:** `strainy -i batch/ -o results/`
**Explanation:** Process multiple long-read samples together.

### Filter by coverage
**Args:** `strainy -i reads.fastq -o results/ -m 10`
**Explanation:** Minimum coverage threshold of 10x.

### Generate report
**Args:** `strainy -i reads.fastq -o results/ --report`
**Explanation:** Generate comprehensive HTML report.

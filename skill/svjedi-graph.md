---
name: svjedi-graph
category: variant-calling
description: Structural variation genotyper for long-read data using variation graphs.
tags: [svjedi-graph, structural-variants, variation-graph, genotyping]
author: oxo-call-community
source_url: "https://github.com/SandraLouise/SVJedi-graph"
---

## Concepts

- **Tool Overview**: svjedi-graph (v1.2.1) genotypes SVs using variation graph representation.
- **Core Function**: Genotypes structural variants from long reads using graph-based approach.
- **Algorithm**: Builds variation graphs to represent SVs and genotypes reads against them.
- **Input/Output**: Input: BAM file, SV VCF, reference genome; Output: Genotyped VCF.
- **Applications**: SV genotyping, population genetics, variant validation.
- **Installation**: `conda install -c bioconda svjedi-graph` or download from GitHub.

## Pitfalls

- **Graph Construction**: Requires time to build variation graphs.
- **Memory Requirements**: Large graphs require significant memory.
- **Computational Time**: Graph-based genotyping can be slow.
- **Parameter Tuning**: Incorrect parameters affect genotyping accuracy.
- **Input Quality**: Requires high-quality SV calls as input.
- **Graph Complexity**: Complex graphs may cause issues.

## Examples

### Display help
**Args:** `svjedi-graph --help`
**Explanation:** Shows available options and usage information.

### Basic SV genotyping
**Args:** `svjedi-graph -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype SVs using variation graph.

### Build graph only
**Args:** `svjedi-graph build -v sv.vcf -r reference.fasta -o graph.gfa`
**Explanation:** Build variation graph from SV calls.

### Verbose mode
**Args:** `svjedi-graph -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svjedi-graph -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --stats`
**Explanation:** Generate statistics about genotyping.

### Batch processing
**Args:** `svjedi-graph -i bams/ -v sv.vcf -r reference.fasta -o results/`
**Explanation:** Process multiple samples together.

### Filter by quality
**Args:** `svjedi-graph -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -q 0.9`
**Explanation:** Filter by confidence score.

### Include phasing
**Args:** `svjedi-graph -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --phase`
**Explanation:** Include phasing information.

### Generate report
**Args:** `svjedi-graph -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --report`
**Explanation:** Generate comprehensive HTML report.

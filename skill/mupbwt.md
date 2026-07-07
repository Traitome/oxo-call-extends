---
name: mupbwt
category: formatting
description: A light pbwt-based index for haplotype data
tags: [mupbwt, pbwt, haplotype, vcf, bcf, genotype, index, ukbb]
author: oxo-call-community
source_url: "https://github.com/dlcgold/muPBWT"
---

## Concepts

- **Tool Overview**: μ-PBWT (muPBWT) is a lightweight PBWT (Positional Burrows-Wheeler Transform) based index for efficiently querying large-scale genotype data like UK Biobank. It enables fast haplotype matching and SMEM (Set Maximal Exact Matches) queries against indexed genotype panels.
- **Core Function**: Builds an index from a VCF/BCF panel file, enabling rapid queries to find matching haplotypes between query samples and the reference panel. Useful for haplotype phasing, imputation validation, and genetic similarity search.
- **Algorithm**: Implements a memory-efficient PBWT variant that compresses haplotype data while allowing fast random access queries. The index stores runs and haplotype information in a compact format.
- **Input Format**: Accepts VCF/BCF files for both panel (reference) and query datasets. Only biallelic SNPs are supported. BCF format is recommended for large panels.
- **Output**: Produces SMEM (Set Maximal Exact Matches) output in Durbin's standard format. Each match line contains: query index, row index, starting column, ending column, and SMEM length.
- **Performance**: Memory-efficient design for UK Biobank scale data (900 haplotypes in example with 499 sites uses ~0.7MB for RL-PBWT structure). Index building is fast (~0.016s for example data).

## Pitfalls

- **Biallelic Only**: μ-PBWT only supports biallelic variants. Multiallelic sites must be filtered before indexing using bcftools (`bcftools view -m2 -M2 -v snps`).
- **VCF vs BCF**: BCF format is binary and more efficient for large panels. VCF is supported but BCF is recommended for production use.
- **Haplotype Ordering**: Output row indices correspond to haplotype order in the file. For diploid samples, rows 0,1 are first sample's haplotypes, rows 2,3 are second sample's haplotypes, etc.
- **Index Persistence**: The `-s` flag saves the index to disk, but this is not required. You can query without building a persistent index each time.
- **Query File Format**: Query files must be in the same format (VCF/BCF) as the panel. Use `-m` flag for MaCS format files.
- **Sample Name Resolution**: Row indices in output need to be mapped to sample names. Use `bcftools query -l input.vcf > samples.txt` to get the sample name list.

## Examples

### Build an index from a BCF panel
**Args:** `-i panel.bcf -s index.ser`
**Explanation:** Builds and saves an index from the panel file. The index is stored in serialized form (.ser file). This step is optional but speeds up repeated queries.

### Query without building index
**Args:** `-i panel.bcf -q query.bcf -o output.txt`
**Explanation:** Queries the panel directly without saving an index. Useful for one-off queries or when index persistence isn't needed.

### Query with pre-built index
**Args:** `-l index.ser -q query.bcf -o output.txt`
**Explanation:** Loads the pre-built index and queries. Faster when querying the same panel multiple times with different queries.

### Build index and query in one command
**Args:** `-i panel.bcf -s index.ser -q query.bcf -o output.txt`
**Explanation:** Builds index, saves it, and runs query in a single command. Combines the two operations efficiently.

### Print memory usage details
**Args:** `-l index.ser -d`
**Explanation:** Loads the index and prints detailed memory usage statistics including run counts, memory breakdown by structure, and estimated dense size.

### Filter VCF to biallelic SNPs only
**Args:** `bcftools view -m2 -M2 -v snps input.vcf > filtered.vcf`
**Explanation:** μ-PBWT only accepts biallelic variants. Use bcftools to filter out multiallelic sites and indels before indexing.

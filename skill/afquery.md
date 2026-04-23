---
name: afquery
category: utility
description: Genomic allele frequency query engine with bitmap-encoded genotypes for fast local cohort queries
tags: [allele-frequency, query, bitmap, genotypes, cohort]
author: oxo-call-community
source_url: "https://github.com/dlopez-bioinfo/afquery"
---

## Concepts

- **Tool Overview**: AFQuery is a bitmap-indexed engine enabling fast allele frequency queries on user-defined subsets of local genomic cohorts without rescanning VCFs.
- **Core Function**: Pre-indexes genotype data using bitmaps for rapid allele frequency queries on arbitrary sample subsets.
- **Input/Output**: Input: VCF files and sample metadata. Output: Allele frequency statistics for queried regions/samples.
- **Performance**: Uses bitmap encoding for efficient storage and retrieval, avoiding repeated VCF parsing.
- **Installation**: Install via bioconda: `conda install -c bioconda afquery`

## Pitfalls

- **Indexing Required**: Must build index before querying - initial indexing can be time-consuming for large cohorts.
- **Memory Usage**: Bitmap indices require memory proportional to cohort size and variant count.
- **Sample Subsets**: Define sample subsets precisely - ambiguous definitions may cause unexpected results.
- **VCF Compatibility**: Requires properly formatted VCF files with consistent genotype encoding.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for AFQuery.

### Build index from VCF
**Args:** `index -i cohort.vcf -o afquery_index/`
**Explanation:** Creates bitmap index from VCF file for fast subsequent queries.

### Query allele frequency
**Args:** `query -i afquery_index/ -r chr1:1000000-2000000 -o results.tsv`
**Explanation:** Queries allele frequencies for specified genomic region.

### Query with sample subset
**Args:** `query -i afquery_index/ -s samples.txt -o subset_af.tsv`
**Explanation:** Queries allele frequencies for specific sample subset defined in file.

### Query specific variant
**Args:** `query -i afquery_index/ -v chr1:123456 -o variant_af.tsv`
**Explanation:** Queries allele frequency for a single specific variant position.

### Update index with new samples
**Args:** `update -i afquery_index/ -n new_samples.vcf`
**Explanation:** Adds new samples to existing index without full rebuild.

### Export frequency statistics
**Args:** `export -i afquery_index/ -o cohort_stats.tsv`
**Explanation:** Exports genome-wide allele frequency statistics for the entire cohort.

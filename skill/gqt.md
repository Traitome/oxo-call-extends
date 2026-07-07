---
name: gqt
category: bioinformatics
description: GQT (Genotype Query Tool) is a fast genotype query interface for efficiently querying genotype data from large VCF files.
tags: [gqt, genotype, VCF, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ryanlayer/gqt"
---

## Concepts

- **Genotype Query**: GQT provides fast random access to genotype data stored in VCF files, enabling efficient querying of specific variants and samples.

- **Indexing**: Creates indexes for VCF files to enable fast querying without loading entire files into memory.

- **Multi-sample Query**: Supports querying genotypes across multiple samples simultaneously.

- **Range Queries**: Allows querying genotypes within specific genomic regions or coordinate ranges.

- **Output Formats**: Supports various output formats including VCF, BED, and custom tabular formats.

- **Performance Optimization**: Optimized for speed using efficient data structures and indexing strategies.

## Pitfalls

- **VCF Format**: Ensure VCF files are properly formatted and indexed. Unindexed files will be slow to query.

- **Memory Usage**: Querying very large regions or many samples may require significant memory.

- **Index Maintenance**: Indexes need to be regenerated when VCF files are updated.

- **Sample Names**: Ensure sample names in queries match those in the VCF header.

- **Coordinate System**: Be aware of 0-based vs 1-based coordinate systems when specifying regions.

## Examples

### Build index for VCF
**Args:** `gqt build -i genotypes.vcf.gz -o genotypes.gqt`
**Explanation:** Creates a GQT index for fast genotype querying.

### Query genotypes by position
**Args:** `gqt query -i genotypes.gqt -c chr1:1000000-2000000`
**Explanation:** Queries genotypes in the specified genomic region.

### Query specific samples
**Args:** `gqt query -i genotypes.gqt -c chr1:1000000-2000000 -s sample1,sample2`
**Explanation:** Queries genotypes for specific samples in the region.

### Output to VCF format
**Args:** `gqt query -i genotypes.gqt -c chr1:1000000-2000000 -f vcf -o output.vcf`
**Explanation:** Outputs query results in VCF format.

### Count genotypes
**Args:** `gqt count -i genotypes.gqt -c chr1:1000000-2000000`
**Explanation:** Counts genotypes without returning full data.

### Batch queries
**Args:** `gqt batch -i genotypes.gqt -b regions.bed -o results.txt`
**Explanation:** Processes multiple regions from a BED file.

### Get sample list
**Args:** `gqt samples -i genotypes.gqt`
**Explanation:** Lists all samples in the indexed VCF file.
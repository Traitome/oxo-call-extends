---
name: sam2lca
category: taxonomy
description: Lowest Common Ancestor assignment from SAM/BAM/CRAM alignment files
tags: ["sam2lca", "LCA", "taxonomy", "alignment", "BAM"]
author: oxo-call-community
source_url: "https://github.com/maxibor/sam2lca"
---

## Concepts

- **Tool Overview**: sam2lca (v1.1.4) is a tool for assigning taxonomic labels to sequencing reads aligned against a reference database using the Lowest Common Ancestor (LCA) algorithm.
- **Core Function**: Determines the taxonomic origin of sequencing reads by analyzing their alignments and computing the LCA from multiple database hits.
- **Algorithm**: Uses alignment information from SAM/BAM/CRAM files to identify matching reference sequences and compute their LCA using NCBI taxonomy.
- **Input Format**: SAM/BAM/CRAM alignment files, reference database with taxonomic annotations.
- **Output Format**: Taxonomic assignments per read, summary statistics, abundance estimates.
- **Use Case**: Metagenomic analysis, contamination detection, read classification, biodiversity studies.

## Pitfalls

- **Reference database**: Requires properly annotated reference database.
- **Alignment quality**: Poor alignments may lead to incorrect LCA assignments.
- **Multi-mapping reads**: Ambiguous mappings require careful handling.
- **Database completeness**: Depends on database coverage for accurate taxonomy.
- **Memory usage**: Large BAM files require significant memory.
- **Taxonomic resolution**: Limited by the granularity of the reference database.

## Examples

### Basic LCA assignment
**Args:** `sam2lca -i alignments.bam -d reference.db -o results.tsv`
**Explanation:** `-i` input BAM file; `-d` reference database; `-o` output TSV.

### With CRAM input
**Args:** `sam2lca -i alignments.cram -d reference.db -r reference.fasta -o results.tsv`
**Explanation:** `-r` reference genome for CRAM decoding.

### Minimum alignment quality
**Args:** `sam2lca -i alignments.bam -d reference.db -o results.tsv -q 30`
**Explanation:** `-q` minimum mapping quality threshold.

### Output per-read assignments
**Args:** `sam2lca -i alignments.bam -d reference.db -o results.tsv --per-read`
**Explanation:** `--per-read` outputs LCA for each individual read.

### Summary statistics
**Args:** `sam2lca -i alignments.bam -d reference.db -o results.tsv --summary`
**Explanation:** `--summary` generates taxonomic summary report.

### Parallel processing
**Args:** `sam2lca -i alignments.bam -d reference.db -o results.tsv -t 8`
**Explanation:** `-t` number of threads for parallel processing.

### Filter by coverage
**Args:** `sam2lca -i alignments.bam -d reference.db -o results.tsv -c 0.8`
**Explanation:** `-c` minimum alignment coverage threshold.
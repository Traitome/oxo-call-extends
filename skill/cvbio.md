---
name: cvbio
category: formatting
description: Tools for working with genomic and sequencing data, including multi-species read disambiguation
tags: [cvbio, formatting, SAM, BAM, read-disambiguation]
author: oxo-call-community
source_url: "https://github.com/clintval/cvbio"
---

## Concepts

- **Tool Overview**: cvbio (v3.0.0+) provides tools for working with genomic and sequencing data, with special focus on multi-species read disambiguation.
- **Core Function**: Disambiguates reads from mixed-species sequencing experiments (e.g., host-pathogen samples) and provides BAM/SAM manipulation utilities.
- **Input/Output**: Input: BAM/SAM alignment files, multi-species references. Output: Disambiguated BAM files, statistics reports.
- **Algorithm**: Uses alignment scores and species-specific markers to assign reads to correct species.
- **Key Features**: Multi-species read separation, BAM filtering, duplicate marking, quality filtering.
- **Installation**: `conda install -c bioconda cvbio`

## Pitfalls

- **Reference Preparation**: Requires properly indexed reference genomes for all species.
- **Ambiguous Reads**: Some reads may remain unassigned due to sequence similarity between species.
- **Memory Usage**: Large BAM files may require significant memory.
- **Performance**: Disambiguation can be computationally intensive for large datasets.
- **Output Interpretation**: Unassigned reads should be carefully evaluated.

## Examples

### Disambiguate multi-species reads
**Args:** `cvbio disambiguate -i aligned.bam -r host.fasta pathogen.fasta -o disambiguated/`
**Explanation:** Separate reads from mixed host-pathogen sequencing data.

### Filter BAM by mapping quality
**Args:** `cvbio filter -i input.bam -o filtered.bam --min-mapq 30`
**Explanation:** Filter BAM file to retain only reads with mapping quality >= 30.

### Mark duplicates
**Args:** `cvbio dedup -i input.bam -o deduplicated.bam`
**Explanation:** Mark duplicate reads in BAM file.

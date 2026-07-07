---
name: maf2synteny
category: alignment
description: A tool that postprocesses whole genome alignment (for two or more genomes) and produces coarse-grained synteny blocks.
tags: [maf2synteny, alignment, synteny, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/fenderglass/maf2synteny"
---

## Concepts

- **Tool Overview**: maf2synteny v1.2 - A tool for postprocessing whole genome alignments to identify synteny blocks across multiple genomes.
- **Core Function**: Converts MAF (Multiple Alignment Format) files into coarse-grained synteny blocks for comparative genomic analysis.
- **Input/Output**: Input: MAF alignment files; Output: Synteny blocks in various formats (BED, GFF, custom).
- **Installation**: `conda install -c bioconda maf2synteny`
- **MAF Format**: Works with the Multiple Alignment Format commonly used for whole-genome alignments.
- **Coarse-grained Blocks**: Identifies large-scale syntenic regions rather than fine-grained alignments.

## Pitfalls

- **MAF Format**: Requires properly formatted MAF files with correct syntax.
- **Genome Order**: The order of genomes in the MAF file affects output.
- **Alignment Quality**: Poor quality alignments produce unreliable synteny blocks.
- **Memory Usage**: Large MAF files may require significant memory.
- **Filtering Parameters**: Incorrect threshold settings can miss true synteny or include spurious blocks.
- **Output Format**: Different output formats have different requirements and use cases.

## Examples

### Generate synteny blocks from MAF
**Args:** `maf2synteny -i alignments.maf -o synteny_blocks.bed`
**Explanation:** Converts MAF alignment to BED format synteny blocks.

### With custom minimum block size
**Args:** `maf2synteny -i alignments.maf -o synteny_blocks.bed -m 10000`
**Explanation:** Sets minimum synteny block size to 10,000 bp.

### Output in GFF format
**Args:** `maf2synteny -i alignments.maf -o synteny_blocks.gff -f gff`
**Explanation:** Outputs synteny blocks in GFF format.

### Filter by identity
**Args:** `maf2synteny -i alignments.maf -o synteny_blocks.bed -id 0.9`
**Explanation:** Filters blocks with minimum 90% sequence identity.

### Multiple genomes
**Args:** `maf2synteny -i alignments.maf -o synteny_blocks.bed -g genome1 genome2 genome3`
**Explanation:** Processes specific genomes from multi-genome alignment.

### Verbose mode
**Args:** `maf2synteny -i alignments.maf -o synteny_blocks.bed -v`
**Explanation:** Provides detailed processing information.
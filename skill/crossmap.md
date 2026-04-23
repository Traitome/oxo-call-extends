---
name: crossmap
category: formatting
description: Convert genome coordinates and annotation files between assemblies
tags: [crossmap, liftover, coordinate-conversion, genome-assembly, annotation]
author: oxo-call-community
source_url: "https://github.com/liguowang/CrossMap"
---

## Concepts

- **Tool Overview**: CrossMap is a program for convenient conversion of genome coordinates and annotation files between different reference assemblies (e.g., hg19 to hg38, mm9 to mm10).
- **Core Function**: Lifts over genomic coordinates from one assembly to another using chain files from UCSC, maintaining coordinate accuracy.
- **Input/Output**: Supports multiple file formats: BED, BAM/SAM, CRAM, VCF, GFF/GTF, Wiggle, BigWig, and BEDGraph.
- **Chain Files**: Requires chain files from UCSC that describe the mapping between assemblies. Download from UCSC or use pre-packaged files.
- **Reciprocal Mapping**: Can map coordinates in both directions (e.g., hg19→hg38 or hg38→hg19) depending on chain file.
- **Accuracy**: Reports unmapped regions and provides detailed statistics on mapping success rate.

## Pitfalls

- **Chain File Required**: Must have the correct chain file for the assembly conversion. Using wrong chain file produces incorrect results.
- **Unmapped Regions**: Some regions cannot be lifted over (e.g., sequences not in target assembly). Check unmapped output.
- **Strand Orientation**: Some regions map to opposite strand. CrossMap handles this automatically but verify results.
- **File Format**: Ensure input file format matches the tool used (e.g., use `CrossMap.py bed` for BED files).
- **Chromosome Naming**: UCSC chain files use chr-prefix. Ensure input files match or use `--chrom-map` for conversion.

## Examples

### Convert BED file from hg19 to hg38
**Args:** `bed hg19ToHg38.over.chain.gz input.bed output.bed`
**Explanation:** Lifts over BED file coordinates from hg19 assembly to hg38 using the appropriate chain file.

### Convert VCF file
**Args:** `vcf hg19ToHg38.over.chain.gz input.vcf output.vcf`
**Explanation:** Converts VCF variant coordinates between assemblies, maintaining variant information and filters.

### Convert BAM file
**Args:** `bam hg19ToHg38.over.chain.gz input.bam output.bam`
**Explanation:** Lifts over BAM alignment coordinates, useful for reusing alignments on new assembly.

### Convert GTF annotation
**Args:** `gtf hg19ToHg38.over.chain.gz input.gtf output.gtf`
**Explanation:** Converts gene annotation coordinates, maintaining gene structure and attributes.

### Convert BigWig file
**Args:** `bigwig hg19ToHg38.over.chain.gz input.bw output.bw`
**Explanation:** Lifts over continuous signal data like coverage tracks.

### Convert with chromosome mapping
**Args:** `bed hg19ToHg38.over.chain.gz input.bed output.bed --chrom-map chrom_map.txt`
**Explanation:** Uses chromosome name mapping file for non-standard chromosome naming conventions.

### Check chain file info
**Args:** `--info hg19ToHg38.over.chain.gz`
**Explanation:** Displays information about the chain file including source and target assemblies.

### Convert and keep unmapped
**Args:** `bed hg19ToHg38.over.chain.gz input.bed output.bed --unmapped-output unmapped.bed`
**Explanation:** Saves regions that could not be lifted over to a separate file for inspection.

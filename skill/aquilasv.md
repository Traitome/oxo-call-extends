---
name: aquilasv
category: variant-calling
description: Region-based diploid assembly and variant calling tool
tags: [aquilasv, variant-calling, diploid-assembly, region-based, genome-analysis]
author: oxo-call-community
source_url: "https://github.com/maiziezhoulab/AquilaSV"
---

## Concepts

- **Tool Overview**: AquilaSV is a region-based diploid assembly and variant calling tool designed for analyzing genomic regions of interest. It combines haplotype assembly with variant detection to provide phased variant calls.
- **Region-based Analysis**: Focuses analysis on specific genomic regions rather than whole-genome scanning, improving efficiency for targeted studies.
- **Diploid Assembly**: Constructs separate haplotype sequences for maternal and paternal chromosomes, enabling accurate phasing of genetic variants.
- **Multi-platform Support**: Works with data from various sequencing platforms including Illumina short reads, 10X Genomics linked reads, and stLFR data.
- **Variant Types**: Detects single-nucleotide variants (SNVs), insertions/deletions (indels), and structural variants within target regions.
- **Installation**: `conda install -c bioconda aquilasv` or download source code from GitHub repository.

## Pitfalls

- **Region Definition**: Requires BED file or chromosome range specification for region-based analysis. Invalid region definitions cause errors.
- **Reference Genome**: Must provide indexed reference genome in FASTA format. Ensure BWA index files exist in the same directory.
- **Input BAM Requirements**: BAM files must be coordinate-sorted, indexed, and contain proper read group information.
- **Memory Usage**: Assembly operations can be memory-intensive, especially for large target regions. Monitor system resources carefully.
- **Phasing Quality**: Variant phasing accuracy depends on read coverage and linkage information. Low-coverage regions may produce unreliable phase calls.
- **Version Compatibility**: Command-line interface may change between versions. Always verify with `--help` before running analysis.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options, including region specification, input/output parameters, and advanced configuration.

### Basic region-based variant calling
**Args:** `-i aligned.bam -r reference.fasta -b target_regions.bed -o output.vcf`
**Explanation:** Analyzes specific genomic regions defined in target_regions.bed, calling variants and performing haplotype assembly within those regions. Outputs phased VCF file.

### Chromosome range analysis
**Args:** `-i aligned.bam -r reference.fasta --chr chr1 --start 1000000 --end 2000000 -o chr1_region.vcf`
**Explanation:** Focuses analysis on a specific chromosomal range (chr1:1,000,000-2,000,000). Useful for targeted resequencing projects or validation studies.

### Enable verbose output
**Args:** `-i aligned.bam -r reference.fasta -b regions.bed -o output.vcf -v --logfile aquilasv.log`
**Explanation:** Runs analysis with verbose logging, writing detailed progress information and intermediate results to the specified log file.

### Adjust assembly parameters
**Args:** `-i aligned.bam -r reference.fasta -b regions.bed -o output.vcf --min_coverage 10 --max_coverage 100 --threads 8`
**Explanation:** Sets minimum coverage threshold to 10x, maximum coverage to 100x, and uses 8 threads for parallel processing. Adjust based on data quality and computational resources.

### Phase-aware variant calling
**Args:** `-i aligned.bam -r reference.fasta -b regions.bed -o output.vcf --phase --haplotype_output haplotypes.fasta`
**Explanation:** Enables haplotype phasing and outputs assembled haplotype sequences to a FASTA file. Useful for downstream phasing analysis and visualization.
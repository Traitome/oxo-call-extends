---
name: flopp
category: programming
description: "Flopp is a software package for single individual haplotype phasing of polyploid organisms from long-read sequencing data."
tags: [flopp, programming, haplotype-phasing, polyploid, long-read, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/flopp"
---

## Concepts
- **Tool Overview**: Flopp performs haplotype phasing for polyploid organisms using long-read sequencing data, enabling reconstruction of individual haplotypes.
- **Core Function**: Reconstructs haplotypes from long reads by identifying and phasing variants across the genome.
- **Input/Output**: Input: BAM file with aligned long reads, VCF with variants. Output: Phased haplotypes in VCF or HAP format.
- **Polyploid Support**: Handles various ploidy levels (triploid, tetraploid, etc.) beyond diploid organisms.
- **Long-Read Advantage**: Leverages long reads to phase variants across larger genomic regions compared to short-read methods.
- **Phasing Algorithm**: Uses a combination of read-based phasing and statistical methods for accurate haplotype reconstruction.
- **Installation**: `conda install -c bioconda flopp` or clone from GitHub. Requires Python 3.x and pysam.

## Pitfalls
- **Read Length**: Requires sufficiently long reads to span multiple variants. Short reads reduce phasing accuracy.
- **Variant Density**: Low variant density makes phasing difficult. Ensure sufficient heterozygous sites.
- **Ploidy Complexity**: Higher ploidy levels (e.g., hexaploid) require more computational resources.
- **Memory Usage**: Large genomes or high ploidy require significant memory. Consider chromosome-level processing.
- **Error Rates**: Long-read errors can affect variant calling and phasing. Use error-corrected reads.
- **Phase Blocks**: Recombination events break haplotype blocks. Expect multiple phase blocks per chromosome.

## Examples
### Basic haplotype phasing
**Args:** `flopp phase --bam long_reads.bam --vcf variants.vcf --output phased.vcf`
**Explanation:** Phases variants from VCF using long reads from BAM file.

### Specify ploidy
**Args:** `flopp phase --bam long_reads.bam --vcf variants.vcf --ploidy 4 --output phased.vcf`
**Explanation:** Sets ploidy level to 4 for tetraploid organism phasing.

### Phase with reference
**Args:** `flopp phase --bam long_reads.bam --vcf variants.vcf --ref reference.fasta --output phased.vcf`
**Explanation:** Uses reference genome for improved phasing accuracy.

### Generate haplotype statistics
**Args:** `flopp stats --vcf phased.vcf --output stats.txt`
**Explanation:** Generates statistics about phased haplotypes including block sizes.

### Visualize haplotypes
**Args:** `flopp plot --vcf phased.vcf --output haplotypes.png`
**Explanation:** Creates visualization of phased haplotypes across the genome.

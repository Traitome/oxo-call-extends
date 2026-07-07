---
name: hapcut2
category: bioinformatics
description: HapCUT2 performs haplotype assembly from sequencing data, enabling phased variant calling and haplotype reconstruction.
tags: [hapcut2, haplotype-assembly, phasing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vibansal/HapCUT2"
---

## Concepts

- **Haplotype Assembly**: HapCUT2 assembles haplotypes from sequencing data.

- **Variant Phasing**: Determines phase of genetic variants.

- **Read-Based Phasing**: Uses sequencing reads for phasing.

- **Diploid Genomes**: Handles diploid genome phasing.

- **Population Data**: Supports population-scale phasing.

- **Long Reads**: Optimized for long-read sequencing data.

## Pitfalls

- **Read Quality**: Low-quality reads may affect phasing accuracy.

- **Coverage Depth**: Requires sufficient sequencing coverage.

- **Complex Regions**: Complex genomic regions may be challenging.

- **Reference Genome**: Ensure compatibility with reference genome.

- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Phase variants
**Args:** `HapCUT2 -i input.bam -v variants.vcf -o haplotypes.txt`
**Explanation:** Performs haplotype assembly from BAM and VCF files.

### With long reads
**Args:** `HapCUT2 -i long_reads.bam -v variants.vcf -l -o haplotypes.txt`
**Explanation:** Optimized for long-read sequencing data.

### Population phasing
**Args:** `HapCUT2 -i population.bam -v variants.vcf -p -o haplotypes.txt`
**Explanation:** Performs population-scale haplotype phasing.

### Generate phased VCF
**Args:** `HapCUT2 -i input.bam -v variants.vcf -o phased.vcf -f`
**Explanation:** Outputs phased variants in VCF format.

### Batch processing
**Args:** `for f in *.bam; do HapCUT2 -i $f -v variants.vcf -o ${f%.bam}_haplotypes.txt; done`
**Explanation:** Processes multiple BAM files.

### Quality filtering
**Args:** `HapCUT2 -i input.bam -v variants.vcf -q 30 -o haplotypes.txt`
**Explanation:** Filters variants by quality score.

### Help command
**Args:** `HapCUT2 --help`
**Explanation:** Shows available options and usage information.
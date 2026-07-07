---
name: lrphase
category: variant-calling
description: Phasing individual long reads using known haplotype information.
tags: [lrphase, variant-calling, phasing, haplotype]
author: oxo-call-community
source_url: "https://github.com/Boyle-Lab/LRphase.git"
---

## Concepts

- **Tool Overview**: lrphase v1.1.2 phases individual long reads using known haplotype information from variant calls.
- **Core Function**: Assigns haplotype phase to each long read based on overlapping variants.
- **Phasing Strategy**: Uses variant positions to determine which haplotype each read belongs to.
- **Input/Output**: Input: BAM file with aligned long reads, VCF file with phased variants; Output: Phased BAM with haplotype tags.
- **Installation**: `conda install -c bioconda lrphase`
- **Applications**: Improves variant calling accuracy, enables haplotype-specific analysis, and aids in structural variant detection.

## Pitfalls

- **Variant Quality**: Poor-quality variants can lead to incorrect phasing assignments.
- **Read Coverage**: Requires sufficient coverage across variant positions.
- **Complex Regions**: Difficult to phase in regions with high variant density or repeats.
- **Phase Switch Errors**: May occur due to mapping errors or complex genomic regions.
- **Memory Usage**: Processing large BAM files may require significant memory.
- **VCF Format**: Requires properly formatted and phased VCF input.

## Examples

### Phase reads
**Args:** `lrphase -i reads.bam -v variants.vcf -o phased_reads.bam`
**Explanation:** Phases long reads using known haplotype information.

### Threads
**Args:** `lrphase -i reads.bam -v variants.vcf -o phased_reads.bam -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum mapping quality
**Args:** `lrphase -i reads.bam -v variants.vcf -o phased_reads.bam -q 30`
**Explanation:** Filters reads with mapping quality < 30.

### Output statistics
**Args:** `lrphase -i reads.bam -v variants.vcf -o phased_reads.bam -s stats.txt`
**Explanation:** Generates phasing statistics including switch error rate.

### Ignore indels
**Args:** `lrphase -i reads.bam -v variants.vcf -o phased_reads.bam --no-indels`
**Explanation:** Ignores indel variants during phasing.

### Help documentation
**Args:** `lrphase --help`
**Explanation:** Displays all available options and parameters.
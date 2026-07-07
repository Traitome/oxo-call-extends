---
name: haphic
category: bioinformatics
description: HapHiC is a fast, reference-independent, allele-aware scaffolding tool using Hi-C data for haplotype-resolved genome assembly.
tags: [haphic, Hi-C, scaffolding, genome-assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/zengxiaofei/HapHiC"
---

## Concepts

- **Hi-C Scaffolding**: HapHiC uses Hi-C data for genome scaffolding.

- **Reference-Independent**: Works without reference genome.

- **Allele-Aware**: Resolves haplotype-specific scaffolds.

- **Genome Assembly**: Assembles and scaffolds draft genomes.

- **Long-Range Interactions**: Uses Hi-C long-range interaction data.

- **Haplotype Resolution**: Resolves haplotypes during scaffolding.

## Pitfalls

- **Hi-C Data Quality**: Results depend on Hi-C data quality.

- **Assembly Quality**: Requires good quality draft assembly.

- **Contig Length**: Longer contigs improve scaffolding.

- **Computational Resources**: May require significant resources.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Run HapHiC scaffolding
**Args:** `haphic -a assembly.fasta -c hic_reads.fastq -o scaffolds.fasta`
**Explanation:** Performs Hi-C based scaffolding.

### With paired-end Hi-C reads
**Args:** `haphic -a assembly.fasta -1 hic_1.fastq -2 hic_2.fastq -o scaffolds.fasta`
**Explanation:** Processes paired-end Hi-C reads.

### Haplotype-aware scaffolding
**Args:** `haphic -a assembly.fasta -c hic_reads.fastq -hap -o haplotype_scaffolds/`
**Explanation:** Performs allele-aware scaffolding.

### Quality filtering
**Args:** `haphic -a assembly.fasta -c hic_reads.fastq -q 20 -o scaffolds.fasta`
**Explanation:** Filters reads by quality score.

### Batch processing
**Args:** `for f in *.fasta; do haphic -a $f -c hic_reads.fastq -o ${f%.fasta}_scaffolds.fasta; done`
**Explanation:** Processes multiple assembly files.

### Generate statistics
**Args:** `haphic -a assembly.fasta -c hic_reads.fastq -stats -o stats.txt`
**Explanation:** Generates scaffolding statistics.

### Help command
**Args:** `haphic --help`
**Explanation:** Shows available options and usage information.
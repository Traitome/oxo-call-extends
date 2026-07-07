---
name: stacks
category: variant-calling
description: Stacks is a software pipeline for building loci from short-read sequences.
tags: [stacks, population-genomics, snps, genotyping]
author: oxo-call-community
source_url: "https://catchenlab.life.illinois.edu/stacks"
---

## Concepts

- **Tool Overview**: stacks (v2.68) is a pipeline for building loci and calling variants from short-read sequencing data, particularly for population genomics.
- **Core Function**: Assembles short reads into loci, discovers SNPs, and performs genotyping across populations.
- **Workflow Components**: ustacks (individual samples) → cstacks (catalog building) → sstacks (matching) → populations (population genetics).
- **Input/Output**: Input: FASTQ files per sample; Output: Catalog of loci, SNP calls, and population genetics statistics.
- **Applications**: Population genetics, SNP discovery, linkage mapping, and population structure analysis.
- **Installation**: `conda install -c bioconda stacks` or download from Catchen Lab website.

## Pitfalls

- **Coverage Depth**: Low coverage affects locus assembly and SNP calling accuracy.
- **Read Quality**: Poor quality reads increase false positive variant calls.
- **Sample Size**: Small populations may produce unreliable allele frequency estimates.
- **Memory Requirements**: Large datasets require significant memory for catalog building.
- **Parameter Tuning**: Incorrect stack depth and mismatch parameters affect results.
- **Repetitive Regions**: Highly repetitive regions cause misassembly and false loci.

## Examples

### Display help
**Args:** `stacks --help`
**Explanation:** Shows available options and usage information.

### Build loci for single sample
**Args:** `ustacks -f sample1.fastq -o stacks_out/ -i 1`
**Explanation:** Build stacks for individual sample.

### Build catalog
**Args:** `cstacks -n 3 -P stacks_out/ -M populations_map.txt`
**Explanation:** Build catalog from multiple samples.

### Match samples to catalog
**Args:** `sstacks -c stacks_out/batch_1 -s stacks_out/sample1 -o stacks_out/`
**Explanation:** Match individual sample stacks to catalog.

### Population genetics analysis
**Args:** `populations -P stacks_out/ -M populations_map.txt -r 0.8`
**Explanation:** Run population genetics analysis with 80% minimum coverage.

### Variant calling
**Args:** `populations -P stacks_out/ -M populations_map.txt --vcf`
**Explanation:** Output variants in VCF format.

### With paired-end reads
**Args:** `ustacks -f read1.fastq -r read2.fastq -o stacks_out/ -i 1`
**Explanation:** Process paired-end sequencing data.

### Quality filtering
**Args:** `ustacks -f sample.fastq -o stacks_out/ -i 1 -q 20`
**Explanation:** Apply quality filter to reads.

### Advanced mode
**Args:** `ustacks -f sample.fastq -o stacks_out/ -i 1 -m 3 -M 5`
**Explanation:** Set minimum stack depth (m) and maximum mismatches (M).

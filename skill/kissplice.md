---
name: kissplice
category: variant-calling
description: A local transcriptome assembler for SNPs, indels and AS events
tags: [kissplice, variant-calling, transcriptome, assembly, SNPs, indels]
author: oxo-call-community
source_url: "http://kissplice.prabi.fr"
---

## Concepts

- **Local Transcriptome Assembly**: Assembles transcript sequences from RNA-Seq data
- **SNP Detection**: Identifies single nucleotide polymorphisms from sequencing reads
- **Indel Detection**: Detects insertions and deletions in transcript sequences
- **Alternative Splicing**: Identifies alternative splicing events
- **De Novo Assembly**: Performs de novo assembly without reference genome
- **Variant Calling**: Calls genetic variants from assembled transcripts

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory
- **Computational Time**: Assembly can be computationally intensive
- **Read Quality**: Poor quality reads affect assembly accuracy
- **Reference Genome**: De novo mode may produce fragmented assemblies
- **Parameter Sensitivity**: Results sensitive to k-mer size and other parameters
- **Alternative Splicing Complexity**: Complex splicing patterns may be missed

## Examples

### Assemble transcriptome from RNA-Seq
**Args:** `kissplice -r reads_1.fastq -r reads_2.fastq -o output_dir/`
**Explanation:** Performs de novo transcriptome assembly from paired-end RNA-Seq reads.

### Detect SNPs and indels
**Args:** `kissplice --snps --indels -r reads.fastq -o variants.vcf`
**Explanation:** Detects SNPs and indels from sequencing reads.

### Identify alternative splicing
**Args:** `kissplice --as-events -r reads.fastq -o as_events.txt`
**Explanation:** Identifies alternative splicing events from RNA-Seq data.

### With reference genome
**Args:** `kissplice -g genome.fa -r reads.fastq -o output_dir/`
**Explanation:** Uses reference genome-guided assembly approach.

### Quality filtering
**Args:** `kissplice -r reads.fastq -o output_dir/ --min-quality 20`
**Explanation:** Filters low-quality reads before assembly.

### Batch processing
**Args:** `kissplice --batch -d read_dir/ -o results_dir/`
**Explanation:** Processes multiple read files in batch mode.
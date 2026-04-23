---
name: besst
category: assembly
description: BESST - Scaffolder for genomic assemblies
tags: [scaffolding, assembly, paired-end, mate-pair]
author: oxo-call-community
source_url: "https://github.com/ksahlin/BESST"
---

## Concepts
- **Tool Overview**: BESST (Best Explicit Scaffolding Tool) is a scaffolder for genomic assemblies that uses paired-end and mate-pair read information to order and orient contigs into scaffolds.
- **Scaffolding**: Uses read pair information to determine the relative order and orientation of contigs, estimating distances between them.
- **Statistical Model**: Employs statistical models to distinguish true links from false positives caused by repeats or misassemblies.
- **Library Support**: Supports multiple library types including paired-end, mate-pair, and long-insert libraries.

## Pitfalls
- **Input Requirements**: Requires properly aligned BAM files from mapping reads to contigs.
- **Insert Size**: Accurate insert size estimation is critical. Incorrect insert sizes lead to poor scaffolding.
- **Repeat Regions**: Repeats can cause false links. BESST attempts to filter these but may not catch all.
- **Coverage**: Requires sufficient coverage for reliable link detection.

## Examples
### Scaffold assembly with paired-end reads
**Args:** `python BESST -c contigs.fasta -b aligned.bam -f fastq1.fq -r fastq2.fq`
**Explanation:** Scaffolds contigs using paired-end read information.

### Use multiple libraries
**Args:** `python BESST -c contigs.fasta -b pe.bam mp.bam -f pe_1.fq mp_1.fq -r pe_2.fq mp_2.fq`
**Explanation:** Scaffolds using both paired-end and mate-pair libraries for better resolution.

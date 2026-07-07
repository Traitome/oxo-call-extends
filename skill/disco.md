---
name: disco
category: assembly
description: DISCO - De novo assembly of circular genomes.
tags: [disco, assembly, circular-genome, prokaryote, plasmid]
author: oxo-call-community
source_url: "https://github.com/yechengxi/disco"
---

## Concepts

- **Tool Overview**: DISCO is a de novo assembly tool for circular genomes like bacterial chromosomes and plasmids.
- **Core Function**: Assembles circular genomes from sequencing data with special handling for circular structures.
- **Input/Output**: Input: Paired-end reads (FASTQ). Output: Circular genome assemblies (FASTA).
- **Algorithm**: Uses de Bruijn graph assembly optimized for circular genomes.
- **Key Features**: Circular genome assembly, plasmid detection, complete circularization, gap closure, quality assessment.
- **Installation**: `conda install -c bioconda disco`

## Pitfalls

- **Input Requirements**: Requires paired-end sequencing reads.
- **Circularity**: Designed specifically for circular genomes.
- **Coverage**: Requires sufficient coverage for complete assembly.
- **Repeat Regions**: May struggle with repetitive sequences.
- **Contamination**: Contaminating sequences can affect assembly.

## Examples

### Assemble circular genome
**Args:** `disco --reads R1.fq R2.fq --output assembly/`
**Explanation:** Assembles circular genome from paired-end reads.

### With quality filtering
**Args:** `disco --reads R1.fq R2.fq --output assembly/ --min-quality 20`
**Explanation:** Apply quality filtering to reads before assembly.

### Plasmid assembly mode
**Args:** `disco --reads R1.fq R2.fq --output assembly/ --plasmid`
**Explanation:** Optimize for plasmid assembly.

### Gap closure
**Args:** `disco --reads R1.fq R2.fq --output assembly/ --close-gaps`
**Explanation:** Attempt gap closure in assembly.

### Quality assessment
**Args:** `disco --reads R1.fq R2.fq --output assembly/ --quality-report report.tsv`
**Explanation:** Generate quality report for assembly.
---
name: iva
category: assembly
description: Iterative Virus Assembler - de novo assembly of viral genomes from NGS data.
tags: [iva, assembly, virus, genome, sequencing]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/iva"
---

## Concepts

- **Tool Overview**: iva (v1.0.11) - An iterative de novo assembler specifically designed for viral genomes, handling both small and large viral genomes.
- **Iterative Assembly**: Builds initial contigs and iteratively extends them using paired-end reads.
- **Reference-guided Assembly**: Can use a reference genome to guide assembly and improve accuracy.
- **Variant Calling**: Identifies SNPs and indels relative to reference sequences.
- **Coverage Analysis**: Provides depth of coverage statistics across assembled genomes.
- **Quality Trimming**: Automatically trims low-quality bases and adapters from reads.

## Pitfalls

- **Repeats and Duplications**: Viral genomes with repeated sequences can cause misassembly.
- **Coverage Variation**: Uneven coverage across the genome may lead to fragmented assemblies.
- **Host Contamination**: Host DNA contamination can interfere with viral assembly.
- **Read Length Limitations**: Short reads may struggle with highly divergent regions.
- **Mixed Infections**: Multiple viral strains in a sample can complicate assembly.
- **Computational Resources**: Large datasets require significant memory and processing time.

## Examples

### Basic viral assembly
**Args:** `iva -f R1.fastq -r R2.fastq -o output/`
**Explanation:** Assembles viral genome from paired-end FASTQ files.

### With reference guidance
**Args:** `iva -f R1.fastq -r R2.fastq -o output/ --reference ref.fasta`
**Explanation:** Uses reference genome to guide assembly process.

### Specify k-mer size
**Args:** `iva -f R1.fastq -r R2.fastq -o output/ --kmer 27`
**Explanation:** Sets k-mer size to 27 for assembly (default is auto-detected).

### Include variant calling
**Args:** `iva -f R1.fastq -r R2.fastq -o output/ --call-variants`
**Explanation:** Calls variants relative to the assembled consensus sequence.

### Adjust coverage threshold
**Args:** `iva -f R1.fastq -r R2.fastq -o output/ --min-coverage 10`
**Explanation:** Requires minimum coverage of 10x for consensus calling.

### Trim adapters
**Args:** `iva -f R1.fastq -r R2.fastq -o output/ --trim-adapters`
**Explanation:** Automatically detects and trims sequencing adapters.
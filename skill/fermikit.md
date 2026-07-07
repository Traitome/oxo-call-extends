---
name: fermikit
category: variant-calling
description: "FermiKit is a de novo assembly based variant calling pipeline for deep Illumina resequencing data."
tags: [fermikit, variant-calling, de-novo-assembly, Illumina, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lh3/fermikit"
---

## Concepts

- **Tool Overview**: FermiKit is a de novo assembly-based variant calling pipeline designed for deep Illumina resequencing data.
- **Core Function**: Calls variants by performing de novo assembly of sequencing reads.
- **Input/Output**: Input: Illumina sequencing reads. Output: Variant calls (VCF), assembly contigs.
- **Algorithm**: Uses Fermi assembly approach for variant detection.
- **Key Features**: De novo assembly, variant calling, Illumina support, deep sequencing, structural variant detection.
- **Installation**: `conda install -c bioconda fermikit`

## Pitfalls

- **Sequencing Depth**: Requires deep sequencing for accurate assembly.
- **Read Length**: Performance varies with read length.
- **Memory Usage**: Large datasets may require significant memory.
- **Assembly Quality**: Results depend on assembly quality.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic variant calling
**Args:** `fermikit var -i reads.fastq -o variants.vcf`
**Explanation:** Calls variants from sequencing data.

### With reference
**Args:** `fermikit var -i reads.fastq -r reference.fasta -o variants.vcf`
**Explanation:** Uses reference for guided variant calling.

### Assembly-based calling
**Args:** `fermikit assemble -i reads.fastq -o contigs.fasta`
**Explanation:** Performs de novo assembly.

### Structural variants
**Args:** `fermikit sv -i reads.fastq -o structural_variants.vcf`
**Explanation:** Detects structural variants.

### Quality filtering
**Args:** `fermikit var -i reads.fastq -o variants.vcf -q 30`
**Explanation:** Filters variants by quality.
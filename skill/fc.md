---
name: fc
category: assembly
description: "Accurate Assembly of Full-length Consensus for Viral Quasispecies."
tags: [fc, assembly, viral-quasispecies, consensus-assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/qdu-bioinfo/fc-virus"
---

## Concepts

- **Tool Overview**: fc (Full-length Consensus) is a tool for accurate assembly of full-length consensus sequences from viral quasispecies data.
- **Core Function**: Assembles consensus sequences from viral sequencing data accounting for quasispecies diversity.
- **Input/Output**: Input: Viral sequencing reads. Output: Full-length consensus sequences, variation profiles.
- **Algorithm**: Uses hierarchical assembly approach for consensus generation.
- **Key Features**: Full-length consensus, viral quasispecies, accurate assembly, variation detection, haploid reconstruction.
- **Installation**: `conda install -c bioconda fc`

## Pitfalls

- **Read Depth**: Requires sufficient sequencing depth.
- **Genome Complexity**: Complex viral genomes may affect assembly.
- **Memory Usage**: Large datasets may require significant memory.
- **Quasispecies Diversity**: High diversity may complicate consensus assembly.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic consensus assembly
**Args:** `fc assemble -i reads.fastq -o consensus.fasta`
**Explanation:** Assembles full-length consensus from reads.

### With reference
**Args:** `fc assemble -i reads.fastq -r reference.fasta -o consensus.fasta`
**Explanation:** Uses reference for guided assembly.

### Variation detection
**Args:** `fc assemble -i reads.fastq -o consensus.fasta --detect-variation`
**Explanation:** Detects sequence variations.

### Multiple samples
**Args:** `fc batch -i samples/ -o results/`
**Explanation:** Processes multiple viral samples.

### Verbose output
**Args:** `fc assemble -i reads.fastq -o consensus.fasta -v`
**Explanation:** Shows detailed assembly progress.
---
name: consent
category: alignment
description: Long read self-correction and assembly polishing with MSA
tags: [consent, long-reads, error-correction, polishing, multiple-sequence-alignment]
author: oxo-call-community
source_url: "https://github.com/morispi/CONSENT"
---

## Concepts

- **Tool Overview**: CONSENT is a scalable tool for long read self-correction and assembly polishing using multiple sequence alignment, designed for Nanopore and PacBio data.
- **Core Function**: Corrects errors in long reads and polishes genome assemblies through efficient multiple sequence alignment.
- **Algorithm**: Uses overlapping read alignment and consensus calling to correct systematic sequencing errors.
- **Input**: Long reads in FASTQ/FASTA format or genome assemblies.
- **Output**: Corrected reads or polished assemblies.
- **Application**: Long-read error correction, genome assembly polishing, and sequence accuracy improvement.
- **Installation**: Install via bioconda: `conda install -c bioconda consent`

## Pitfalls

- **Memory Usage**: Large datasets require significant memory.
- **Overlap Detection**: Requires sufficient read coverage for overlap detection.
- **Error Profiles**: Different error profiles for Nanopore vs PacBio.
- **Polishing Rounds**: Multiple rounds may be needed for optimal results.
- **Chimeric Reads**: May not handle chimeric reads correctly.

## Examples

### Self-correct long reads
**Args:** `consent correct -i reads.fastq -o corrected_reads/`
**Explanation:** Performs self-correction on long sequencing reads.

### Polish genome assembly
**Args:** `consent polish -i assembly.fasta -r reads.fastq -o polished_assembly.fasta`
**Explanation:** Polishes genome assembly using long reads.

### With custom overlap threshold
**Args:** `consent correct -i reads.fastq -t 0.8 -o corrected_reads/`
**Explanation:** Sets 80% identity threshold for overlap detection.

### Display help
**Args:** `consent --help`
**Explanation:** Shows all available options and usage information.
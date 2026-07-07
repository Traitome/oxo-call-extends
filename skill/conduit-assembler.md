---
name: conduit-assembler
category: expression
description: Long- and short-read hybrid de novo transcriptome assembly
tags: [conduit-assembler, transcriptome, hybrid-assembly, long-reads, short-reads]
author: oxo-call-community
source_url: "https://github.com/NatPRoach/conduit"
---

## Concepts

- **Tool Overview**: Conduit is a long- and short-read hybrid de novo transcriptome assembler that combines the accuracy of short reads with the continuity of long reads for comprehensive transcript reconstruction.
- **Core Function**: Assembles full-length transcripts by integrating Illumina short reads with Oxford Nanopore or PacBio long reads.
- **Algorithm**: Uses error correction of long reads with short reads, followed by assembly and isoform resolution.
- **Input**: Short-read FASTQ files (Illumina) and long-read FASTQ files (Nanopore/PacBio).
- **Output**: Assembled transcriptome in FASTA format with isoform annotations.
- **Application**: Transcriptome assembly, isoform discovery, and gene expression analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda conduit-assembler`

## Pitfalls

- **Read Balance**: Optimal results require balanced short and long read coverage.
- **Error Correction**: Long read error rate affects assembly quality.
- **Isoform Resolution**: May struggle with highly similar isoforms.
- **Computational Resources**: Hybrid assembly requires significant memory and CPU.
- **Chimeric Reads**: Long-read chimeras may produce artificial transcripts.

## Examples

### Run hybrid assembly
**Args:** `conduit-assembler -s short_reads.fastq -l long_reads.fastq -o transcriptome/`
**Explanation:** Assembles transcriptome using both short and long reads.

### With reference guidance
**Args:** `conduit-assembler -s short_reads.fastq -l long_reads.fastq -r reference.fasta -o transcriptome/`
**Explanation:** Uses reference genome to guide assembly.

### Specify assembly parameters
**Args:** `conduit-assembler -s short_reads.fastq -l long_reads.fastq -k 25 -o transcriptome/`
**Explanation:** Uses k-mer size of 25 for assembly.

### Display help
**Args:** `conduit-assembler --help`
**Explanation:** Shows all available options and usage information.
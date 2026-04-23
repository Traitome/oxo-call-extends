---
name: bowtie2
category: alignment
description: Fast and sensitive gapped read aligner for sequencing reads
tags: [bowtie2, alignment, short-read, rna-seq, dna-seq]
author: oxo-call-community
source_url: "https://github.com/BenLangmead/bowtie2"
---

## Concepts

- **Tool Overview**: Bowtie2 is a fast and memory-efficient tool for aligning sequencing reads to long reference sequences.
- **Alignment Modes**: Supports end-to-end (full read alignment) and local (soft-clipping allowed) alignment modes.
- **Paired-End Support**: Handles paired-end reads with proper insert size constraints.
- **Index Building**: Use `bowtie2-build` to create FM-index from reference sequences.
- **Preset Options**: Built-in presets (--very-fast, --fast, --sensitive, --very-sensitive) for ease of use.
- **Installation**: Install via bioconda: `conda install -c bioconda bowtie2`

## Pitfalls

- **Index Required**: Must build index with bowtie2-build before alignment.
- **Thread Count**: Use `-p` to specify threads; default is 1 thread.
- **Quality Encoding**: Ensure correct quality encoding (--phred33 or --phred64).
- **Large Genomes**: For references >4GB, use `--large-index` during index building.
- **Memory Usage**: Sensitive mode uses more memory; adjust based on available resources.

## Examples

### Build genome index
**Args:** `bowtie2-build genome.fa genome_index`
**Explanation:** Creates Bowtie2 index files from reference FASTA for subsequent alignment.

### Single-end alignment
**Args:** `bowtie2 -x genome_index -U reads.fq -S aligned.sam`
**Explanation:** Aligns single-end reads to the indexed reference genome.

### Paired-end alignment
**Args:** `bowtie2 -x genome_index -1 reads_R1.fq -2 reads_R2.fq -S aligned.sam`
**Explanation:** Aligns paired-end reads with proper pair handling.

### Alignment with threads
**Args:** `bowtie2 -x genome_index -1 R1.fq -2 R2.fq -p 8 -S aligned.sam`
**Explanation:** Uses 8 threads for faster alignment of paired-end reads.

### Sensitive local alignment
**Args:** `bowtie2 -x genome_index -U reads.fq --very-sensitive-local -S aligned.sam`
**Explanation:** Uses sensitive local alignment mode allowing soft-clipping at read ends.

### End-to-end alignment with preset
**Args:** `bowtie2 -x genome_index -U reads.fq --very-sensitive -S aligned.sam`
**Explanation:** Performs end-to-end alignment with very sensitive settings.

### Output sorted BAM directly
**Args:** `bowtie2 -x genome_index -U reads.fq | samtools sort -o aligned.bam`
**Explanation:** Pipes output to samtools for direct BAM conversion and sorting.

### Limit reported alignments
**Args:** `bowtie2 -x genome_index -U reads.fq -k 5 -S aligned.sam`
**Explanation:** Reports up to 5 valid alignments per read for multi-mapping analysis.

### Inspect index information
**Args:** `bowtie2-inspect -s genome_index`
**Explanation:** Displays summary information about the reference sequences in the index.

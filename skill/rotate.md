---
name: rotate
category: utility
description: Simple utility for rotating a circular DNA sequence to start at a given position or at the first occurrence of a given substring; useful for normalizing the origin of replication in microbial genomes.
tags: ["rotate", "circular-sequence", "origin-of-replication", "dna-rotation", "biopython"]
author: oxo-call-community
source_url: "https://github.com/richarddurbin/rotate"
---

## Concepts

- **Tool Overview**: rotate (v1.0, Richard Durbin / Sanger) is a small command-line utility for rotating a circular DNA sequence so it starts at a specified position or at the first occurrence of a specified substring. It is the canonical tool for normalizing the start of circular genomes (mitochondrial, plastid, bacterial) to a consistent origin (typically the `dnaA` gene for bacteria, or a defined start position for organelles).
- **Core Function**: Takes a single-sequence FASTA (circular DNA) and an optional position or substring, and writes a new FASTA in which the sequence has been rotated to start at the specified position (or at the first occurrence of the substring). The original length is preserved; the rotation is a circular shift.
- **Algorithm**: A simple substring search (`memmem`-style) followed by a circular shift. For position-based rotation, the sequence is split at the position and re-joined in the reverse order. For substring-based rotation, the first occurrence of the substring is located and the sequence is rotated to start at that position.
- **Input Format**: A single-sequence FASTA file (one record only; multi-FASTA is rejected). The sequence is assumed to be circular; rotation is well-defined. The output is also a single-sequence FASTA.
- **Output Format**: A single-sequence FASTA with the rotated sequence. The header is preserved (or updated to include the rotation offset, depending on the flag). The output is a circular rotation of the input — the original sequence can be recovered by rotating back.
- **Use Case**: Normalizing the start of a bacterial genome to the `dnaA` gene for consistent comparative genomics, rotating a mitochondrial genome to the `cox1` start codon for phylogenetics, preparing a circular reference for a tool that requires a specific start (e.g., some variant callers), and producing a "canonical" representation of a circular sequence for display in a genome browser.

## Pitfalls

- **CRITICAL — Input must be a single-sequence FASTA**: rotate rejects multi-FASTA files. If the input has multiple records, only the first is rotated; the rest are silently ignored. Pre-extract with `samtools faidx contig.fa chr1 > single.fa` first.
- **CRITICAL — The substring is searched in BOTH strands by default**: A substring that appears in the reverse complement will match in the reverse strand, and the rotation will be to the reverse-complemented start. Use `--forward-only` to restrict to the forward strand.
- **The position is 1-indexed, not 0-indexed**: `rotate -p 100` rotates to start at position 100, where position 1 is the first base. A 0-indexed position is silently treated as "1" (out-of-range positions are clamped to 1 or the sequence length).
- **The rotation is a circular shift, not a reversal**: rotate does not reverse-complement the sequence. To get the reverse-complement, use `seqkit seq -r -p` first.
- **The input sequence is assumed to be circular**: For a linear sequence (e.g., a chromosome arm), the rotation produces a sequence that is NOT the same as the input — the bases at the start are moved to the end. This is usually not what you want for linear sequences.
- **The output FASTA's sequence length is the same as the input**: rotate does not truncate or pad. A 5,000,000-bp circular genome produces a 5,000,000-bp rotated output.

## Examples

### Rotate to a specific position
**Args:** `rotate -i genome.fa -p 1000 -o rotated.fa`
**Explanation:** `-i` is the input single-sequence FASTA, `-p 1000` is the 1-indexed start position, `-o` is the output FASTA. The output starts at position 1000 of the input and the original first 999 bases are moved to the end.

### Rotate to the start of a substring
**Args:** `rotate -i genome.fa -s "ATGAGTGATA" -o rotated.fa`
**Explanation:** `-s "ATGAGTGATA"` rotates the sequence to start at the first occurrence of the substring (typically a start codon or origin of replication marker). Useful for normalizing a bacterial genome to the `dnaA` gene.

### Restrict to the forward strand
**Args:** `rotate -i genome.fa -s "ATGAGTGATA" --forward-only -o rotated.fa`
**Explanation:** `--forward-only` restricts the substring search to the forward strand. Default is both strands. Useful when the substring is asymmetric (e.g., a known start codon).

### Use a different output header
**Args:** `rotate -i genome.fa -p 1000 -o rotated.fa --header "genome_rotated_to_dnaA"`
**Explanation:** `--header` specifies a custom header for the output FASTA. Default is to preserve the input header.

### Read from stdin
**Args:** `cat genome.fa | rotate -s "ATGAGTGATA" -o rotated.fa`
**Explanation:** Reads the input from stdin when `-i` is `-` (or empty). Useful for piping from another tool.

### Rotate to a position relative to a feature
**Args:** `grep -m1 -B1 "gene=dnaA" genome.gff | head -1 | awk '{print $4}' | rotate -i genome.fa -p $(cat) -o rotated.fa`
**Explanation:** Composite: extract the `dnaA` start position from a GFF file via `grep` + `awk`, then rotate the genome to start at that position. The output starts at the `dnaA` gene.

### Use rotate in a Snakemake rule
**Args:** `rule rotate_genome: input: 'genome.fa'; output: 'genome_rotated.fa'; shell: 'rotate -i {input} -s \"ATGAGTGATA\" -o {output}'`
**Explanation:** Example Snakemake rule. The shell command runs rotate to normalize the genome to the `dnaA` start codon.

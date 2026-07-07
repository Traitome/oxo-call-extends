---
name: goalign
category: alignment
description: Goalign is a toolkit for manipulating multiple sequence alignments, supporting FASTA, Phylip, Nexus, and Clustal formats.
tags: [goalign, alignment, sequences, phylogenetics, Go]
author: oxo-call-community
source_url: "https://github.com/evolbioinfo/goalign"
---

## Concepts

- **Multiple Sequence Alignment Manipulation**: Goalign provides a comprehensive set of commands for manipulating and analyzing multiple sequence alignments. It supports reading from local files, remote URLs, and compressed files (gzip, xz, bzip2).

- **Input/Output Formats**: Goalign handles four major alignment formats: FASTA, Phylip, Nexus, and Clustal. Results can be printed to standard output for piping between commands.

- **Core Commands**: Key operations include sequence filtering (addid, dedup), gap cleaning (clean sites/seqs), evolutionary distance computation, entropy calculation, alignment concatenation, and drawing visualizations.

- **Bootstrap Support**: The build seqboot command generates bootstrap alignments for phylogenetic analysis.

- **Codon Alignment**: The codonalign command aligns nucleotide sequences using a corresponding amino acid alignment as a guide.

- **Distance Calculation**: Compute evolutionary distances between sequences using various distance models.

## Pitfalls

- **Format Compatibility**: Ensure input files match the expected format. Mixed formats in a single file can cause parsing errors. Use `goalign info` to check file format before processing.

- **Compressed File Handling**: While gzip, xz, and bzip2 are supported, ensure file extensions match the actual compression type (.gz, .xz, .bz2).

- **Large Alignments**: Very large alignments may require significant memory. Consider using divide command to split large alignments into smaller chunks.

- **Remote URL Requirements**: When using HTTP/HTTPS URLs, ensure network connectivity and proper URL encoding for special characters.

- **Pipe Compatibility**: Some commands modify headers or sequence order. Always verify output format when piping between goalign commands.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available commands and their brief descriptions. Use this to explore goalign's capabilities and get quick reference information.

### Convert alignment format from FASTA to Phylip
**Args:** `convert -i input.fasta -f phylip -o output.phylip`
**Explanation:** Converts an alignment from FASTA format to Phylip format. The -f flag specifies output format; supported formats include fasta, phylip, nexus, and clustal.

### Remove gap-only sites from alignment
**Args:** `clean sites -i input.fasta -o cleaned.fasta`
**Explanation:** Removes columns (sites) that contain only gap characters from the alignment. This is useful for reducing alignment size and focusing on informative positions.

### Compute evolutionary distances
**Args:** `compute distances -i input.fasta -o distances.txt`
**Explanation:** Calculates pairwise evolutionary distances between sequences. The output file contains a distance matrix suitable for phylogenetic tree construction.

### Concatenate multiple alignments
**Args:** `concat -i align1.fasta align2.fasta align3.fasta -o concatenated.fasta`
**Explanation:** Combines multiple alignments into a single concatenated alignment. All input alignments must have the same sequences in the same order.

### Generate bootstrap alignments
**Args:** `build seqboot -i input.fasta -n 100 -o bootstrap/`
**Explanation:** Creates 100 bootstrap replicate alignments by resampling sites with replacement. Outputs are written to the bootstrap directory with sequential naming.

### Remove duplicate sequences
**Args:** `dedup -i input.fasta -o unique.fasta`
**Explanation:** Identifies and removes sequences with identical residues, keeping only one copy of each unique sequence in the alignment.

### Draw alignment visualization
**Args:** `draw biojs -i input.fasta -o alignment.html`
**Explanation:** Generates an interactive HTML visualization of the alignment using BioJS. Open the resulting file in a web browser to explore the alignment interactively.

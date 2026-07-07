---
name: gpatch
category: assembly
description: GPatch produces chromosome-scale pseudoassemblies by patching gaps between mapped contigs using sequences from a reference genome.
tags: [gpatch, genome-assembly, pseudoassembly, gap-closing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/adadiehl/GPatch"
---

## Concepts

- **Pseudoassembly**: GPatch creates chromosome-scale pseudoassemblies by aligning contigs to a reference genome and filling gaps between mapped contigs with reference sequences.

- **Gap Patching**: Fills gaps between contigs using sequences from a reference genome, improving contiguity and completeness.

- **Misjoin Correction**: Identifies and corrects misjoins in the original contig assembly to improve assembly quality.

- **Dot-plot Generation**: Produces dot-plots of patched pseudoassemblies against reference assemblies for visual validation.

- **Liftover Chain Generation**: Generates chrom.sizes and liftover chains for converting coordinates between assemblies.

- **Workflow Automation**: Provides helper scripts to automate GPatch workflows for large-scale projects.

## Pitfalls

- **Reference Dependency**: Results depend heavily on the quality and completeness of the reference genome.

- **Alignment Quality**: Poor alignments can lead to incorrect gap filling. Ensure high-quality alignments.

- **Contig Quality**: Low-quality contigs with many errors can compromise the pseudoassembly.

- **Misjoin Detection**: Not all misjoins may be detected. Manual inspection is recommended.

- **Computational Resources**: Processing large genomes may require significant memory and time.

## Examples

### Generate pseudoassembly
**Args:** `gpatch -i contigs.fasta -r reference.fasta -a alignments.sam -o pseudoassembly.fasta`
**Explanation:** Creates a pseudoassembly by patching gaps between contigs aligned to a reference.

### Correct misjoins
**Args:** `gpatch correct -i contigs.fasta -r reference.fasta -o corrected.fasta`
**Explanation:** Identifies and corrects misjoins in the contig assembly using the reference genome.

### Generate dot-plot
**Args:** `gpatch dotplot -i pseudoassembly.fasta -r reference.fasta -o dotplot.png`
**Explanation:** Creates a dot-plot visualization comparing the pseudoassembly to the reference.

### Generate liftover chains
**Args:** `gpatch liftover -i pseudoassembly.fasta -r reference.fasta -o liftover.chain`
**Explanation:** Generates liftover chains for coordinate conversion between assemblies.

### Run automated workflow
**Args:** `gpatch workflow -i contigs.fasta -r reference.fasta -o output_dir/`
**Explanation:** Runs the complete GPatch workflow including alignment, patching, and quality control.

### Set minimum alignment length
**Args:** `gpatch -i contigs.fasta -r reference.fasta -m 1000 -o pseudoassembly.fasta`
**Explanation:** Only uses contigs with alignments longer than 1000 base pairs.

### Verbose output
**Args:** `gpatch -i contigs.fasta -r reference.fasta -v -o pseudoassembly.fasta`
**Explanation:** Provides verbose output including progress updates and statistics.
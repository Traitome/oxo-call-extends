---
name: gblocks
category: alignment
description: Selection of conserved blocks from multiple sequence alignments for phylogenetic analysis
tags: [gblocks, multiple-sequence-alignment, conserved-blocks, phylogenetic-analysis, alignment-filtering]
author: oxo-call-community
source_url: "https://molevol-ibe.csic.es/Gblocks/"
---

## Concepts

- **Tool Overview**: Gblocks is a computer program written in C that removes poorly aligned positions and divergent regions from DNA or protein sequence alignments, selecting only conserved blocks suitable for phylogenetic analysis.
- **Core Function**: Identifies and extracts conserved sequence blocks from multiple sequence alignments (MSA) by evaluating conservation at each position and removing poorly aligned or ambiguous regions.
- **Algorithm**: Gblocks selects blocks following criteria similar to manual curation but in a reproducible, automated manner:
  - Blocks must lack large stretches of contiguous nonconserved positions
  - Blocks must have low density of gap positions
  - Flanking positions must be highly conserved to anchor the block
- **Input Format**: Gblocks accepts aligned sequences in several formats: FASTA, NBRF/PIR, CLUSTAL, and other common alignment formats. The alignment must be pre-prepared using tools like MAFFT, Muscle, or ClustalW.
- **Output**: Creates two output files:
  - `[alignment].fa-gb`: The filtered alignment containing only selected conserved positions
  - `[alignment].fa-gb.html`: HTML visualization showing which positions were kept (highlighted in yellow) and removed
- **Parameters**: Five key parameters control block selection:
  - b1 (Minimum number of sequences for a conserved position): Fraction of sequences that must have a conserved position
  - b2 (Minimum number of sequences for a flank position): Similar threshold for flanking positions
  - b3 (Maximum number of contiguous nonconserved positions): Rejects segments exceeding this threshold
  - b4 (Minimum length of a block): Removes blocks shorter than this value
  - b5 (Treatment of gap positions): Defines what constitutes a gap
- **Stringency**: Default settings are stringent. Relaxed settings (higher b1/b2, higher b3) are better for shorter alignments.
- **Installation**: `conda install -c bioconda gblocks`. Alternative: Download from https://molevol-ibe.csic.es/Gblocks/

## Pitfalls

- **CRITICAL: Input Must Be Pre-Aligned**: Gblocks does not perform alignment. Input sequences must already be aligned using a multiple sequence alignment tool. Feeding unaligned sequences will produce meaningless results.
- **CRITICAL: Stringent Defaults**: The default parameter settings are stringent (strict block selection). For shorter alignments, this may remove too many positions. Use relaxed parameters (-b1=0.5 -b2=0.5) for datasets with higher sequence divergence.
- **Sequence Quality**: Gblocks assumes the input alignment is reasonably correct. Highly erroneous alignments (from divergent sequences or poor alignment tools) will produce unreliable block selections.
- **Gap Treatment**: The b5 parameter has three modes: "n" (no gaps allowed), "h" (50% threshold), "a" (all gaps allowed). Mode "n" is most stringent and may exclude useful data if some sequences have missing data.
- **Version**: Version 0.91b is the most widely used. Version 1.0 was released October 2025. Check documentation for version-specific behavior.
- **Phylogenetic Scope**: Gblocks is designed for phylogenetic analysis, not for other purposes like motif finding or alignment visualization. Output may not be suitable for other downstream applications.
- **File Format Issues**: Some alignment formats may not be recognized correctly. FASTA format is the most reliable.

## Examples

### Basic block selection with defaults
**Args:** `Gblocks alignment.fasta -t=d -e=-gb`
**Explanation:** The simplest usage for DNA alignments. Takes a FASTA-formatted alignment, applies default stringent parameters, and outputs files with "-gb" suffix. The alignment file is assumed to be DNA (use -t=p for protein).

### Protein alignment with default settings
**Args:** `Gblocks protein_alignment.fasta -t=p -e=-gb`
**Explanation:** For protein alignments, use -t=p (protein). The output files will be `protein_alignment.fasta-gb` (filtered alignment) and `protein_alignment.fasta-gb.html` (visualization).

### Relaxed parameters for divergent sequences
**Args:** `Gblocks divergent_align.fasta -t=d -b1=0.5 -b2=0.5 -b3=8 -b4=2 -b5=a -e=-gb`
**Explanation:** Relaxed parameters prevent over-filtering of divergent alignments. b1=0.5 means half the sequences must have a conserved position (less strict). b3=8 allows longer stretches of nonconserved positions.

### Codon alignment analysis
**Args:** `Gblocks codon_alignment.fasta -t=c -e=-gb`
**Explanation:** Use -t=c for codon alignments. This treats gaps at codon positions differently, preserving reading frame integrity. Useful for phylogenetics of coding sequences.

### Interactive mode
**Args:** `Gblocks alignment.fasta`
**Explanation:** Running without -e parameter opens the interactive menu interface. This allows manual adjustment of parameters and preview of results before saving. Useful for exploring different stringency levels.

### Specify output suffix
**Args:** `Gblocks input.aln -t=p -e=.gblocks`
**Explanation:** The -e parameter defines the output file suffix. Without it, Gblocks uses its default (usually "-gb"). Custom suffixes help organize multiple runs.

### Use with Phytest tools
**Args:** `Gblocks mafft_output.fasta -t=p -e=-gb && FastTree -wag -nosupport msa.fasta-gb > tree.nwk`
**Explanation:** After Gblocks filtering, use the cleaned alignment for phylogenetic tree building with tools like FastTree, RAxML, or IQ-TREE. The filtered alignment typically produces more accurate trees.

### Process multiple files with a loop
**Args:** `for f in *.fasta; do Gblocks "$f" -t=d -e=-gb; done`
**Explanation:** Use a bash loop to process multiple alignment files in batch. Each file gets processed independently, creating corresponding "-gb" output files.

### View HTML output for visualization
**Args:** `firefox alignment.fasta-gb.html`
**Explanation:** The HTML output file can be opened in any web browser. It shows the original alignment with conserved positions highlighted in yellow and removed positions in red. This helps validate Gblocks decisions.

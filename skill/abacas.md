---
name: abacas
category: assembly
description: ABACAS aligns, orders, and orients shotgun assembled contigs based on a reference sequence using MUMmer alignment.
tags: [abacas, assembly, scaffolding, contig, ordering, primer-design, mummer]
author: oxo-call-community
source_url: "https://abacas.sourceforge.net/"
---

## Concepts

- **Tool Overview**: ABACAS (Algorithm Based Automatic Contiguation of Assembled Sequences) orders and orients contigs based on a reference genome. Version 1.3.1.
- **Core Function**: Takes shotgun assembled contigs and a reference sequence, aligns them using MUMmer, orders and orients contigs to match the reference, generates visualization files for ACT, and designs primers for gap closure.
- **Input/Output**: Input is contigs (FASTA) and reference genome (FASTA); output is ordered/oriented contigs (pseudomolecule), visualization files for ACT, and primer sequences for gap filling.
- **Installation**: Install via bioconda: `conda install -c bioconda abacas`
- **Platform Support**: Platform-independent (Perl-based)
- **MUMmer Dependency**: Uses NUCmer or PROmer from the MUMmer package for contig-to-reference alignment.
- **ACT Visualization**: Generates comparison files that can be visualized using Artemis Comparison Tool (ACT).

## Pitfalls

- **CRITICAL: Command Name**: The command is `abacas.pl`, not `abacas`. Use `abacas.pl` to invoke the tool.
- **Reference Dependency**: Quality of ordering depends heavily on reference similarity. Distant references produce poor ordering.
- **MUMmer Required**: Requires MUMmer to be installed and in PATH. ABACAS calls MUMmer externally.
- **Gap Size Estimation**: Gap sizes are estimated from reference and may not reflect actual gap sizes in the assembly.
- **Primer3 Required**: Primer design functionality requires Primer3 to be installed.

## Examples

### Display help information
**Args:** `abacas.pl -h`
**Explanation:** Shows all available command-line options and usage information.

### Order contigs using NUCmer
**Args:** `abacas.pl -r reference.fasta -q contigs.fasta -p nucmer`
**Explanation:** Aligns contigs to the reference using NUCmer and outputs ordered/oriented contigs with gap information. NUCmer is best for closely related sequences.

### Order contigs using PROmer
**Args:** `abacas.pl -r reference.fasta -q contigs.fasta -p promer`
**Explanation:** Uses PROmer for alignment, which translates sequences in all six frames. Best for more divergent sequences or when comparing different species.

### Run with default parameters
**Args:** `abacas.pl -r ref.fa -q contigs.fa -p nucmer -d`
**Explanation:** Uses default NUCmer parameters instead of the more sensitive --maxmatch option. Useful for larger genomes or when high sensitivity is not required.

### Generate ordered contigs file
**Args:** `abacas.pl -r ref.fa -q contigs.fa -p nucmer -m`
**Explanation:** Prints ordered and oriented contigs to a separate file for further analysis.

### Skip contig ordering, go directly to primer design
**Args:** `abacas.pl -r ref.fa -q ordered_contigs.fa -e`
**Explanation:** Skips the contig ordering step and proceeds directly to primer design for gap closure. Useful when contigs are already ordered.
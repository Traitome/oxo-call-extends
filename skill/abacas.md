---
name: abacas
category: assembly
description: ABACAS is intended to rapidly contiguate (align, order, orientate), visualize and design primers to close gaps on shotgun assembled contigs based on a reference sequence.
tags: [abacas, assembly, scaffolding, contig, ordering, primer-design]
author: oxo-call-community
source_url: "https://abacas.sourceforge.net/"
---

## Concepts

- **Tool Overview**: Algorithm Based Automatic Contiguation of Assembled Sequences - orders and orients contigs based on a reference genome. Version 1.3.1.
- **Core Function**: Takes shotgun assembled contigs and a reference sequence, then aligns, orders, and orients the contigs to match the reference, visualizes the alignment, and designs primers for gap closure.
- **Input/Output**: Input is contigs (FASTA) and reference genome (FASTA); output is ordered/oriented contigs, visualization, and primer sequences for gap filling.
- **Installation**: Install via bioconda: `conda install -c bioconda abacas`
- **Platform Support**: Platform-independent (noarch, Perl)
- **MUMmer Dependency**: Uses MUMmer for contig-to-reference alignment. Requires MUMmer to be installed.
- **Primer Design**: Automatically designs primers flanking gaps for PCR-based gap closure.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Reference Dependency**: Quality of ordering depends heavily on reference similarity. Distant references produce poor ordering.
- **MUMmer Required**: Requires MUMmer to be installed and in PATH. ABACAS calls MUMmer externally.
- **Gap Size Estimation**: Gap sizes are estimated from reference and may not reflect actual gap sizes in the assembly.
- **Contig Naming**: Output contig names may be modified. Track original names for downstream analysis.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Order contigs against a reference
**Args:** `contigs.fasta reference.fasta`
**Explanation:** Aligns contigs to the reference using MUMmer and outputs ordered/oriented contigs with gap information.

### Run with specific MUMmer parameters
**Args:** `-m mummer -c contigs.fasta -r reference.fasta -o ordered_contigs.fasta`
**Explanation:** Uses MUMmer alignment with default parameters. The -m flag specifies the alignment method (mummer, nucmer, or promer).

### Generate primers for gap closure
**Args:** `--primer contigs.fasta reference.fasta -o output_prefix`
**Explanation:** Orders contigs and designs primers flanking each gap for PCR amplification and Sanger sequencing to close gaps.

### Output visualization file
**Args:** `--draw contigs.fasta reference.fasta -o output_prefix`
**Explanation:** Generates a visualization of contig alignment to the reference, showing order, orientation, and gap positions.

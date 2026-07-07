---
name: catfasta2phyml
category: formatting
description: Concatenates FASTA files into PHYLIP format for phylogenetic analysis
tags: [catfasta2phyml, formatting, fasta, phylip, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/nylander/catfasta2phyml"
---

## Concepts

- **Tool Overview**: catfasta2phyml concatenates multiple FASTA files into a single PHYLIP-formatted alignment.
- **Core Function**: Combines aligned sequence files for phylogenetic analysis.
- **Input**: Multiple aligned FASTA files with matching sequence names.
- **Output**: Concatenated PHYLIP format alignment file.
- **Application**: Preparing multi-locus alignments for phylogeny reconstruction.
- **Installation**: Install via bioconda: `conda install -c bioconda catfasta2phyml`

## Pitfalls

- **Sequence Names**: All input files must have matching sequence identifiers.
- **Alignment Length**: Sequences in each file must be aligned and same length.
- **Order Consistency**: Sequence order may affect downstream analysis.
- **Format Compatibility**: Outputs PHYLIP format; some tools require specific variants.

## Examples

### Concatenate FASTA files
**Args:** `catfasta2phyml -f gene1.fa gene2.fa gene3.fa > concatenated.phy`
**Explanation:** Concatenates multiple gene alignments into PHYLIP format.

### With output file
**Args:** `catfasta2phyml -f *.fa -o concatenated.phy`
**Explanation:** Concatenates all FASTA files in directory to PHYLIP format.

### Display help
**Args:** `catfasta2phyml --help`
**Explanation:** Shows all available options and usage information.
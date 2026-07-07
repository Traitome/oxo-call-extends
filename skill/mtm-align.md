---
name: mtm-align
category: alignment
description: Align multiple protein structures
tags: [mtm-align, alignment, protein-structure, TM-score, MSTA]
author: oxo-call-community
source_url: "http://yanglab.nankai.edu.cn/mTM-align/help/"
---

## Concepts

- **Tool Overview**: mTM-align v20220104 performs fast and accurate multiple protein structure alignment.
- **Core Function**: Extends TM-align pairwise alignment to multiple structure alignment (MSTA).
- **Algorithm**: Uses progressive merging of pairwise structure alignments guided by a phylogenetic tree.
- **Benchmark Performance**: Outperforms other MSTA algorithms on HOMSTRAD, SABmark_sup, SABmark_twi, and SISY-multiple datasets.
- **Server Capability**: Provides web server for structure database search and multiple alignment.
- **Speed**: Takes 2-5 minutes for database search and a few seconds for ~10 medium-size structures.

## Pitfalls

- **Structure Quality**: Alignment accuracy depends on quality of input protein structures.
- **Format Requirements**: Input structures must be in PDB format.
- **Server Dependency**: Web server may have latency; command-line version preferred for large batches.
- **Missing Domains**: Structures with large missing regions may produce suboptimal alignments.
- **Homology Assumption**: Works best when structures share evolutionary relationships.
- **Memory Usage**: Large structure sets may require substantial memory for alignment.

## Examples

### Align multiple structures
**Args:** `mtm-align input.structures output.aln`
**Explanation:** Aligns multiple protein structures and outputs alignment file.

### Database search mode
**Args:** `mtm-align -d database.pdb query.pdb`
**Explanation:** Searches PDB database for structures similar to query.

### Specify output format
**Args:** `mtm-align -i structures/ -o result.aln -f fasta`
**Explanation:** Specifies FASTA output format for alignment results.

### Adjustable parameters
**Args:** `mtm-align -i pdbs/ --gap-open 10.0 --gap-extend 0.5`
**Explanation:** Customizes gap penalties for alignment refinement.

### Display version
**Args:** `mtm-align --version`
**Explanation:** Shows version and basic usage information.

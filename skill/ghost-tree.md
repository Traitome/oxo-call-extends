---
name: ghost-tree
category: phylogenetics
description: ghost-tree - Combines sequence data from two genetic marker databases into one phylogenetic tree.
tags: [ghost-tree, phylogenetics, marker-genes, phylogenetic-tree]
author: oxo-call-community
source_url: "https://github.com/JTFouquier/ghost-tree"
---

## Concepts
- **Marker Gene Combination**: Combines different marker genes.
- **Phylogenetic Tree Building**: Builds phylogenetic trees.
- **Database Integration**: Integrates multiple databases.
- **Diversity Analysis**: Analyzes microbial diversity.
- **Sequence Analysis**: Analyzes genetic sequences.

## Pitfalls
- **Database Compatibility**: Requires compatible databases.
- **Sequence Quality**: Requires high-quality sequences.
- **Tree Construction**: May produce unreliable trees.
- **Parameter Selection**: Requires careful parameter selection.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Combine markers
**Args:** `ghost-tree -i marker1.fasta marker2.fasta -o combined_tree.nwk`
**Explanation:** Combines two marker genes.

### With taxonomy
**Args:** `ghost-tree -i marker1.fasta marker2.fasta -t taxonomy.txt -o combined_tree.nwk`
**Explanation:** Includes taxonomy information.

### Specify database
**Args:** `ghost-tree -i marker.fasta -d silva -o tree.nwk`
**Explanation:** Uses specific database.

### Generate report
**Args:** `ghost-tree -i marker1.fasta marker2.fasta -r -o report.html`
**Explanation:** Generates analysis report.

### Batch processing
**Args:** `ghost-tree -l samples.txt -o ./results/`
**Explanation:** Processes multiple samples.
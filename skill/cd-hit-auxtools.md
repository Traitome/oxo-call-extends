---
name: cd-hit-auxtools
category: sequence-analysis
description: Auxiliary tools for CD-HIT sequence clustering
tags: [cd-hit-auxtools, cd-hit, sequence-clustering, auxiliary-tools]
author: oxo-call-community
source_url: "https://github.com/weizhongli/cdhit"
---

## Concepts

- **Tool Overview**: cd-hit-auxtools provides auxiliary utilities for CD-HIT sequence clustering suite.
- **Core Function**: Helper tools for manipulating and analyzing CD-HIT clustering results.
- **Tools Included**: cd-hit-est-2d, cd-hit-2d, psi-cd-hit, and other specialized clustering tools.
- **Input**: FASTA sequences and CD-HIT clustering results.
- **Output**: Clustered sequences and analysis reports.
- **Application**: Sequence clustering, redundancy reduction, and ortholog detection.
- **Installation**: Install via bioconda: `conda install -c bioconda cd-hit-auxtools`

## Pitfalls

- **CD-HIT Required**: Works alongside main CD-HIT tools.
- **Memory Usage**: Clustering large datasets requires significant memory.
- **Similarity Threshold**: Adjust threshold based on desired clustering stringency.
- **Sequence Length**: Short sequences may affect clustering quality.

## Examples

### Compare two sequence datasets
**Args:** `cd-hit-2d -i1 db1.fa -i2 db2.fa -o result.clstr`
**Explanation:** Compares sequences between two databases.

### Cluster nucleotide sequences
**Args:** `cd-hit-est -i sequences.fa -o clustered.fa -c 0.9`
**Explanation:** Clusters nucleotide sequences at 90% identity.

### Use PSI-CD-HIT
**Args:** `psi-cd-hit -i proteins.fa -o psi_clustered.fa`
**Explanation:** Uses PSI-BLAST profiles for more sensitive clustering.

### Display help
**Args:** `cd-hit-2d --help`
**Explanation:** Shows available options for cd-hit-2d.
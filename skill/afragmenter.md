---
name: afragmenter
category: annotation
description: Schema-free, tunable protein domain segmentation tool for AlphaFold structures based on network analysis
tags: [protein-domains, alphafold, segmentation, pae, structure]
author: oxo-call-community
source_url: "https://github.com/sverwimp/AFragmenter"
---

## Concepts

- **Tool Overview**: AFragmenter is a flexible protein domain segmentation tool for AlphaFold structures, using network analysis of Predicted Aligned Error (PAE) matrices.
- **Core Function**: Segments protein structures into domains based on PAE values, without relying on predefined domain schemas or databases.
- **Input/Output**: Input: AlphaFold PAE matrix and structure file. Output: Domain boundaries and segmented structures.
- **Tunable Parameters**: Resolution and threshold parameters allow users to control domain granularity - higher resolution yields more, smaller domains.
- **Installation**: Install via bioconda: `conda install -c bioconda afragmenter`

## Pitfalls

- **PAE Required**: Requires PAE (Predicted Aligned Error) matrix from AlphaFold predictions - not applicable to experimental structures alone.
- **Parameter Tuning**: Default parameters may not work for all proteins - experiment with resolution (0.4-0.8) and threshold (0-4).
- **Small Domains**: Very small domains may be filtered out by min_size parameter - adjust if needed.
- **Non-contiguous Domains**: Some domains may have non-contiguous residue ranges - review output carefully.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and parameters for AFragmenter.

### Segment protein with default parameters
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv`
**Explanation:** Segments protein using default resolution (0.7) and threshold (2).

### Custom resolution for more domains
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --resolution 0.8`
**Explanation:** Uses higher resolution to identify more, smaller domains.

### Adjust PAE threshold
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --threshold 3`
**Explanation:** Uses higher PAE threshold for more permissive domain boundary detection.

### Set minimum domain size
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --min-size 25`
**Explanation:** Filters out domains smaller than 25 residues.

### Filter by average PAE
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --min-avg-pae 15`
**Explanation:** Removes domains with average PAE > 15, indicating low confidence.

### Use CPM objective function
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --objective-function cpm`
**Explanation:** Uses CPM instead of modularity for clustering, producing more small domains.

### Disable domain merging
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --no-merge`
**Explanation:** Disables automatic merging of small domains with adjacent larger ones.

### Save segmented FASTA
**Args:** `segment -i structure.pdb -p pae.json -o domains.csv --fasta domains.fasta`
**Explanation:** Outputs domain sequences as separate FASTA entries.

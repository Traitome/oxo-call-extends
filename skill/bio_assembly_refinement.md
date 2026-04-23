---
name: bio_assembly_refinement
category: assembly
description: Assembly refinement tools for PacBio bacterial assemblies
tags: [assembly-refinement, pacbio, bacterial-genome]
author: oxo-call-community
source_url: "https://github.com/nds/bio_assembly_refinement"
---

## Concepts
- **Tool Overview**: bio_assembly_refinement provides tools for refining genome assemblies, particularly useful for PacBio bacterial genome assemblies.
- **Refinement Operations**: Includes contig circularization, overlap detection, and assembly polishing.
- **Applications**: Bacterial genome assembly improvement, circular genome processing.

## Pitfalls
- **Bacterial Focus**: Primarily designed for bacterial assemblies; may not suit eukaryotic genomes.
- **PacBio Optimization**: Optimized for PacBio data; may need adjustment for other platforms.

## Examples
### Circularize assembly
**Args:** `assembly_refinement circularize -i assembly.fa -o circular.fa`
**Explanation:** Detects and resolves overlapping ends for circularization.

### Detect assembly overlaps
**Args:** `assembly_refinement detect-overlaps -i assembly.fa -o overlaps.tsv`
**Explanation:** Identifies overlapping regions at contig ends.

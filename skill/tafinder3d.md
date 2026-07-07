---
name: tafinder3d
category: structural-biology
description: Toxin-antitoxin system identification with 3D structure-based searching.
tags: [tafinder3d, toxin-antitoxin, protein-structure, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/schmigle/TAfinder3D"
---

## Concepts

- **Tool Overview**: tafinder3d (v1.0.9) identifies toxin-antitoxin systems using 3D structures.
- **Core Function**: Detects toxin-antitoxin pairs based on structural similarity.
- **Algorithm**: Uses structural comparison for TA system identification.
- **Input/Output**: Input: Protein sequences/structures; Output: TA system predictions.
- **Applications**: Genome annotation, toxin-antitoxin research, microbial genomics.
- **Installation**: `conda install -c bioconda tafinder3d` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large structure databases require significant memory.
- **Computational Time**: Structure comparisons can be slow.
- **Structure Quality**: Requires high-quality protein structures.
- **Template Coverage**: Limited by available template structures.
- **False Positives**: May produce false positive predictions.
- **Sequence Similarity**: Distant homologs may be missed.

## Examples

### Display help
**Args:** `tafinder3d --help`
**Explanation:** Shows available options and usage information.

### Basic TA detection
**Args:** `tafinder3d -i proteins.fasta -o ta_systems.txt`
**Explanation:** Identify toxin-antitoxin systems from sequences.

### With structure
**Args:** `tafinder3d -i protein.pdb -o ta_systems.txt`
**Explanation:** Use 3D structure for identification.

### Verbose mode
**Args:** `tafinder3d -i proteins.fasta -o ta_systems.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tafinder3d -i proteins.fasta -o ta_systems.txt --stats`
**Explanation:** Generate statistics about TA detection.

### Batch processing
**Args:** `for f in proteins/*.fasta; do tafinder3d -i $f -o results/${f%.fasta}.txt; done`
**Explanation:** Process multiple protein files.

### Filter by confidence
**Args:** `tafinder3d -i proteins.fasta -o ta_systems.txt -c 0.9`
**Explanation:** Filter by confidence threshold.

### Include all types
**Args:** `tafinder3d -i proteins.fasta -o ta_systems.txt --all-types`
**Explanation:** Detect all types of TA systems.

### Generate report
**Args:** `tafinder3d -i proteins.fasta -o ta_systems.txt --report`
**Explanation:** Generate comprehensive TA detection report.

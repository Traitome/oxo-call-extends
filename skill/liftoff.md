---
name: liftoff
category: annotation
description: Liftoff - Accurate GFF3/GTF annotation lift over pipeline
tags: [liftoff, annotation, lift-over, GFF3, GTF, genome-annotation]
author: oxo-call-community
source_url: "https://github.com/agshumate/Liftoff"
---

## Concepts

- **Annotation Lift-over**: Transfers annotations between genome assemblies
- **GFF3/GTF Support**: Handles GFF3 and GTF annotation formats
- **Accurate Mapping**: Precise coordinate conversion
- **Gene Structure**: Preserves gene structure during lift-over
- **Multiple Assemblies**: Supports lift-over between multiple assemblies
- **Quality Control**: Built-in validation of lifted annotations

## Pitfalls

- **Assembly Divergence**: Highly divergent assemblies may fail
- **Coordinate System**: Zero-based vs one-based considerations
- **Complex Regions**: Repeat regions may cause mapping issues
- **File Format**: Strict format requirements
- **Memory Usage**: Memory-intensive for large annotation files
- **Parameter Tuning**: Requires careful parameter optimization

## Examples

### Lift annotations
**Args:** `liftoff -g annotation.gff -r reference.fasta -t target.fasta -o lifted.gff`
**Explanation:** Lifts over annotations from reference to target.

### GTF input
**Args:** `liftoff -g annotation.gtf -r reference.fasta -t target.fasta -o lifted.gtf`
**Explanation:** Processes GTF annotation format.

### Include unmapped
**Args:** `liftoff -g annotation.gff -r ref.fasta -t target.fasta -o lifted.gff -u unmapped.txt`
**Explanation:** Outputs unmapped features.

### Threads
**Args:** `liftoff -g annotation.gff -r ref.fasta -t target.fasta -o lifted.gff -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Strict mode
**Args:** `liftoff -g annotation.gff -r ref.fasta -t target.fasta -o lifted.gff --strict`
**Explanation:** Strict mode for higher accuracy.

### Chain file
**Args:** `liftoff -g annotation.gff -r ref.fasta -t target.fasta -o lifted.gff -c chain.txt`
**Explanation:** Uses chain file for lift-over.
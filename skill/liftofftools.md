---
name: liftofftools
category: annotation
description: LiftoffTools - Tool for comparing annotations across genome assemblies
tags: [liftofftools, annotation, genome-assembly, comparison, gff3, gtf]
author: oxo-call-community
source_url: "https://github.com/agshumate/LiftoffTools"
---

## Concepts

- **Annotation Comparison**: Compares annotations between different genome assemblies
- **Lift-over Validation**: Validates the accuracy of annotation lift-over results
- **GFF3/GTF Support**: Handles GFF3 and GTF annotation formats
- **Feature Mapping**: Maps features between reference and target assemblies
- **Quality Assessment**: Assesses the quality of lifted annotations
- **Synteny Analysis**: Analyzes synteny conservation between assemblies

## Pitfalls

- **Assembly Divergence**: Highly divergent assemblies may produce unreliable results
- **File Format**: Strict format requirements for GFF3/GTF files
- **Memory Usage**: Memory-intensive for large annotation files
- **Coordinate System**: Zero-based vs one-based considerations
- **Feature Complexity**: Complex gene structures may cause mapping issues
- **Version Compatibility**: API may change between versions

## Examples

### Compare annotations
**Args:** `liftofftools compare -g ref_annotation.gff -t target_annotation.gff -o comparison.txt`
**Explanation:** Compares annotations between reference and target assemblies.

### Validate lift-over
**Args:** `liftofftools validate -l lifted.gff -r ref_annotation.gff -o validation.txt`
**Explanation:** Validates the accuracy of lifted annotations.

### Generate report
**Args:** `liftofftools report -g annotation.gff -r reference.fasta -o report.html`
**Explanation:** Generates HTML report of annotation comparison.

### Feature mapping
**Args:** `liftofftools map -f feature_list.txt -r ref.fasta -t target.fasta -o mapped.txt`
**Explanation:** Maps specific features between assemblies.

### Synteny analysis
**Args:** `liftofftools synteny -g annotation.gff -r ref.fasta -t target.fasta -o synteny.txt`
**Explanation:** Analyzes synteny conservation between assemblies.

### Filter unmapped
**Args:** `liftofftools filter -i lifted.gff -u unmapped.txt -o filtered.gff`
**Explanation:** Filters out unmapped features from lift-over results.
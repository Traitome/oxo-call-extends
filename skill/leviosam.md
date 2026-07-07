---
name: leviosam
category: alignment
description: Lift-over of alignments for variant-aware references
tags: [leviosam, alignment, lift-over, variant-aware, reference-genome]
author: oxo-call-community
source_url: "https://github.com/alshai/levioSAM"
---

## Concepts

- **Variant-aware Lift-over**: Handles alignments with variant-aware references
- **Reference Conversion**: Converts alignments between different references
- **Variant Integration**: Incorporates known variants into liftover
- **Alignment Preservation**: Maintains alignment quality during conversion
- **Multi-reference**: Works with multiple reference versions
- **Accurate Mapping**: Preserves biological meaning of alignments

## Pitfalls

- **Variant Database**: Requires comprehensive variant database
- **Reference Compatibility**: References must be compatible
- **Complex Variants**: Complex structural variants may fail
- **Performance**: Large datasets require significant resources
- **Memory Usage**: Memory-intensive for large genomes
- **Ambiguous Mappings**: Some regions may map ambiguously

## Examples

### Lift over to variant-aware reference
**Args:** `leviosam lift -i aln.bam -v variants.vcf -r reference.fasta -o lifted.bam`
**Explanation:** Lifts over alignments using variant information.

### Create index
**Args:** `leviosam index -r reference.fasta -o index/`
**Explanation:** Creates index for reference genome.

### Specify chain file
**Args:** `leviosam lift -i aln.bam -c chain.txt -o lifted.bam`
**Explanation:** Uses chain file for liftover.

### Quality filtering
**Args:** `leviosam lift -i aln.bam -v variants.vcf -q 30 -o lifted.bam`
**Explanation:** Filters low quality alignments.

### Statistics
**Args:** `leviosam stats -i lifted.bam`
**Explanation:** Shows liftover statistics.

### Dry run
**Args:** `leviosam lift -i aln.bam -v variants.vcf --dry-run`
**Explanation:** Shows what would be lifted over.
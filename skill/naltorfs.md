---
name: naltorfs
category: annotation
description: nAltORFs - Identify nested alternate open reading frames
tags: [naltorfs, annotation, orf, open-reading-frame, nested, translation]
author: oxo-call-community
source_url: "https://github.com/BlankenbergLab/nAltORFs"
---

## Concepts

- **Tool Overview**: nAltORFs v0.1.2 (Nested Alternate Open Reading Frames) identifies alternative open reading frames nested within known coding sequences. These are regulatory ORFs that may produce alternative protein isoforms.
- **Core Function**: Scans annotated gene regions to identify in-frame and out-of-frame ORFs that could potentially be translated, even when nested within known protein-coding sequences.
- **Algorithm**: Systematically enumerates all possible ORFs in annotated gene regions, evaluating their coding potential based on sequence composition and conservation.
- **Input Format**: Accepts gene annotation files in GFF3 or GTF format along with the corresponding genome sequence in FASTA format.
- **Output**: Produces GFF3 annotation files containing predicted nested ORFs with coordinates, coding potential scores, and comparative conservation evidence if available.
- **Use Case**: Discover novel regulatory ORFs in known genes, study alternative translation start sites, and identify small proteins or peptides encoded by nested ORFs.

## Pitfalls

- **Annotation Dependence**: Quality of predictions depends heavily on the quality of input gene annotations. Incomplete annotations lead to missed nested ORFs.
- **Coding Potential**: Nested ORFs predicted by sequence alone require experimental validation. Not all predicted ORFs are actually translated.
- **Start Codon Context**: Proper start codon context (Kozak sequence) affects translation efficiency. Predictions should consider this.
- **Overlapping ORFs**: Nested ORFs may be in different frames relative to the main ORF. This affects whether they can be co-translated.
- **Conservation Evidence**: Without comparative genomics evidence, distinguishing real nested ORFs from random sequence spans is difficult.
- **Ribosome Profiling**: For validation, ribosome profiling data provides stronger evidence than sequence-based predictions alone.

## Examples

### Basic nested ORF prediction
**Args:** `-i annotation.gff3 -g genome.fasta -o naltorfs.gff3`
**Explanation:** Standard nAltORFs workflow. Scans annotated genes for nested alternative ORFs.

### Use GTF input format
**Args:** `-i genes.gtf -g reference.fa -o predictions.gff3`
**Explanation:** Works with GTF format gene annotations as input.

### Set minimum ORF length
**Args:** `-i annotations.gff -g genome.fa -o output.gff -min 30`
**Explanation:** Only reports nested ORFs with at least 30 codons to filter out very short predictions.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.

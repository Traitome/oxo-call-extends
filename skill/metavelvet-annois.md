---
name: metavelvet-annois
category: utility
description: Metavelvet AnnoIS - an extra package for metavelvet for versions < 1.2.01
tags: [metavelvet-annois, utility, annotation]
author: oxo-call-community
source_url: "http://metavelvet.dna.bio.keio.ac.jp"
---

## Concepts

- **Tool Overview**: MetaVelvet AnnoIS v0.2.01 is an additional package for MetaVelvet that provides annotation functionality for metagenomic assemblies.
- **Core Function**: Provides annotation support for MetaVelvet metagenomic assemblies.
- **Gene Annotation**: Annotates genes and other genomic features in assembled sequences.
- **MetaVelvet Integration**: Works seamlessly with MetaVelvet assembler output.
- **Input/Output**: Accepts assembled contigs; outputs annotated sequences with feature information.
- **Functional Annotation**: Provides functional annotations for predicted genes.

## Pitfalls

- **Version Compatibility**: Designed for MetaVelvet versions < 1.2.01.
- **Sequence Quality**: Annotation quality depends on input sequence quality.
- **Database Completeness**: Annotation quality depends on reference database completeness.
- **False Positives**: May predict false positive genes.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Memory Requirements**: Processing large datasets may require significant memory.

## Examples

### Annotate contigs
**Args:** `metavelvet-annois -i contigs.fasta -o annotated.fasta`
**Explanation:** Annotates assembled contigs with gene predictions.

### With custom database
**Args:** `metavelvet-annois -i contigs.fasta -d custom_db/ -o annotated.fasta`
**Explanation:** Uses a custom annotation database.

### Detailed annotation
**Args:** `metavelvet-annois -i contigs.fasta -o annotated.fasta -v`
**Explanation:** Generates detailed annotations with verbose output.

### Output GFF format
**Args:** `metavelvet-annois -i contigs.fasta -o annotation.gff -f gff`
**Explanation:** Outputs annotations in GFF format.

### Batch processing
**Args:** `metavelvet-annois -i fasta/ -o annotations/`
**Explanation:** Processes multiple FASTA files in batch mode.
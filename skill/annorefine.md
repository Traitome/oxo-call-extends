---
name: annorefine
category: annotation
description: High-performance genome annotation refinement toolkit using RNA-seq evidence
tags: [annotation, refinement, rna-seq, utr, hints, augustus, genemark]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/annorefine"
---

## Concepts

- **Tool Overview**: AnnoRefine is a Rust-based toolkit for refining genome annotations using RNA-seq evidence. Generates gene prediction hints for Augustus/GeneMark and refines UTR boundaries. Version 2026.2.22.
- **Core Modules**: bam2hints (convert RNA-seq BAM to hints), utrs (refine UTR boundaries), join_hints (merge hints from multiple sources), refine (comprehensive annotation refinement).
- **Performance**: Written in Rust for high performance with memory-efficient streaming BAM processing. Supports multi-threading for large genomes (tested on multi-GB genomes).
- **Integration**: Outputs hints compatible with Augustus and GeneMark-ETP gene prediction pipelines.
- **Library Type Support**: Handles stranded RNA-seq libraries (FR, RF, F, R) for accurate intron/exon hint generation.
- **Python API**: Provides Python bindings for integration into custom workflows alongside command-line tools.
- **Novel Gene Detection**: Can detect novel genes not present in existing annotations during refinement process.

## Pitfalls

- **BAM Sorting**: Input BAM files must be coordinate-sorted. Use `samtools sort` if needed.
- **Library Strandedness**: Must correctly specify library type (--stranded RF/FR/F/R) for accurate hint generation. Incorrect specification leads to wrong intron direction hints.
- **GFF3 Format**: Input annotations must be valid GFF3 format. Malformed GFF3 causes parsing errors.
- **Memory Usage**: Large BAM files with high coverage may require substantial memory despite streaming optimization.
- **Thread Count**: Too many threads may cause memory issues on resource-constrained systems. Balance threads vs memory.

## Examples

### Convert BAM to Augustus hints
**Args:** `annorefine bam2hints --input alignments.bam --output hints.gff --stranded RF --threads 4`
**Explanation:** Converts RNA-seq BAM alignments to Augustus-compatible hints format. RF stranded library type, 4 threads for parallel processing. Use hints with `augustus --hintsfile=hints.gff`.

### Refine UTR boundaries
**Args:** `annorefine utrs --fasta genome.fa --gff3 annotations.gff3 --bam alignments.bam --output refined.gff3`
**Explanation:** Uses RNA-seq coverage evidence to extend and refine UTR boundaries in existing annotations. Outputs refined GFF3 with improved UTR annotations.

### Merge hints from multiple sources
**Args:** `annorefine join_hints --input bam_hints.gff protein_hints.gff --output merged_hints.gff`
**Explanation:** Combines hints from RNA-seq BAM and protein alignments for comprehensive gene prediction evidence. Improves Augustus/GeneMark prediction accuracy.

### Generate introns-only hints for GeneMark-ETP
**Args:** `annorefine join_hints --input bam_hints.gff protein_hints.gff --output genemark_hints.gff --introns_only`
**Explanation:** Creates intron-only hints file compatible with GeneMark-ETP pipeline. Filters other hint types for GeneMark-specific requirements.

### Comprehensive annotation refinement
**Args:** `annorefine refine --fasta genome.fa --gff3 annotations.gff3 --bam alignments.bam --output final.gff3 --enable_novel_gene_detection`
**Explanation:** Full refinement workflow: refines existing annotations, extends UTRs, and detects novel genes using RNA-seq evidence. Most comprehensive annotation improvement.

### Python API usage
**Args:** `import annorefine; result = annorefine.bam2hints(bam_file="alignments.bam", output_file="hints.gff", library_type="RF", threads=4)`
**Explanation:** Python API for integration into custom scripts. Returns result object with processing status. Useful for automated annotation pipelines.
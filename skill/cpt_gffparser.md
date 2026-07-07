---
name: cpt_gffparser
category: annotation
description: Biopython extension for reading and writing GFF3 format genome annotation files with Galaxy compatibility
tags: [cpt_gffparser, GFF3, annotation, biopython, genome-annotation, parser, galaxy]
author: oxo-call-community
source_url: "https://github.com/TAMU-CPT/CPT_GffParser"
---

## Concepts

- **Tool Overview**: CPT_GFFParser is a Biopython extension package for reading and writing GFF3 format genome annotation files, designed for Galaxy platform compatibility.
- **Core Function**: Provides `gffParse()` and `gffWrite()` functions that interface directly with Biopython SeqRecord and SeqFeature structures for seamless GFF3 file handling.
- **Algorithm**: Lightweight, memory-only solution that parses GFF3 files and converts them to Biopython-compatible SeqRecord objects with full feature hierarchy support.
- **Input**: GFF3 format files (optionally with associated SeqRecord dictionary), Biopython SeqRecord objects.
- **Output**: Parsed SeqRecord objects with hierarchical feature annotations, or GFF3 formatted output files.
- **Application**: Genome annotation processing, Galaxy tool integration, Biopython-based bioinformatics pipelines, bacterial/viral genome analysis.
- **Installation**: `pip install CPT-GFFParser` or `conda install -c bioconda cpt_gffparser` (requires Biopython >= 1.79)

## Pitfalls

- **Biopython Version**: Version 1.2+ requires Biopython >= 1.79 (older versions used UnknownSeq which was deprecated)
- **GFF3 Only**: Designed specifically for GFF3 format; GFF2 compatibility may be limited
- **Circular Features**: Better handling of circular genomes added in v1.2, ensure appropriate Biopython version
- **Galaxy Environment**: Originally designed for Galaxy's distributed permission model; may have specific assumptions about file handling
- **Parent Hierarchy**: GFF3's hierarchical feature relationships must be properly encoded with Parent qualifiers

## Examples

### Parse GFF file
**Args:** `from CPT_GFFParser import gffParse; records = gffParse(open('annotation.gff3'))`
**Explanation:** Parses a GFF3 file and returns a dictionary of SeqRecord objects keyed by organism ID.

### Parse with existing SeqRecords
**Args:** `records = gffParse(open('annotation.gff3'), seqrec_dict)`
**Explanation:** Parses GFF file and merges with existing SeqRecord dictionary, useful for adding annotations to genome sequences.

### Write SeqRecords to GFF
**Args:** `from CPT_GFFParser import gffWrite; gffWrite(seqrecords, open('output.gff3', 'w'))`
**Explanation:** Writes Biopython SeqRecord objects to GFF3 format file.

### Create SeqFeature object
**Args:** `from gffSeqFeature import gffSeqFeature; feat = gffSeqFeature(location, type, qualifiers)`
**Explanation:** Creates a GFF3-compatible SeqFeature object with location and qualifiers.

### Convert SeqRecord to GFF
**Args:** `from gffSeqFeature import convertSeqRec; convertSeqRec(seqrecord)`
**Explanation:** Converts a Biopython SeqRecord into GFF3-compatible format with proper feature hierarchy.

### Convert feature to GFF
**Args:** `from gffSeqFeature import convertSeqFeat; convertSeqFeat(seqfeature)`
**Explanation:** Converts individual SeqFeature to GFF3 format with parent-child relationships preserved.

### Parse circular genome
**Args:** `records = gffParse(open('circular.gff3'))`
**Explanation:** Handles circular genome features (plasmids, organelles) with proper feature location wrapping.

### Galaxy tool integration
**Args:** `gffWrite(output_records, output_handler)`
**Explanation:** Writing output directly to Galaxy's file handles for tool wrappers.

### Batch parse multiple organisms
**Args:** `records = gffParse(gff_handle, seqrec_dict_by_organism)`
**Explanation:** Parses GFF with multiple organisms, each organism's features keyed by ID.

---
name: gclib
category: utility
description: Genomic C++ library by Geo Pertea for handling SAM/BAM/CRAM, GFF/GTF, and FASTA genomic file formats
tags: [gclib, genomic, C++, library, SAM, BAM, CRAM, GFF, GTF, FASTA, htslib]
author: oxo-call-community
source_url: "https://github.com/gpertea/gclib"
---

## Concepts

- **Tool Overview**: gclib (Genomic C++ Library) is a source code library developed by Geo Pertea, not a standalone executable. It provides data structures and functions for parsing genomic file formats, used by bioinformatics tools like StringTie.
- **Core Function**: gclib offers C++ classes and templates for handling SAM/BAM/CRAM alignment files, GFF/GTF annotation files, and FASTA sequence files through wrappers around htslib.
- **Key Classes**: GSamReader/GSamWriter for SAM/BAM/CRAM I/O; GffReader/GffWriter for GFF/GTF parsing; GFaSeqGet/GFastaDb for FASTA sequence access; GVec for dynamic arrays; GList for linked lists; GHashMap/GIntHash for hash tables.
- **Threading Support**: GSamReader provides thread-safe access to alignment data via htslib; GffReader has limited threading capability.
- **Index Support**: SAM/BAM/CRAM files support indexing via htslib; FASTA files support .fai indexing.
- **Coordinate System**: Uses 1-based genomic coordinates for start positions, matching standard bioinformatics conventions.
- **Input/Output**: Handles genomic alignment files (SAM/BAM/CRAM), annotation files (GFF/GTF/GFF3), and sequence files (FASTA/FASTQ).
- **Installation**: This is a source code library, not an installable package. Projects link statically by including source files. Bioconda packages like stringtie include gclib automatically.

## Pitfalls

- **Not a standalone tool**: gclib is a compilation toolkit - you cannot run `gclib` as a command. It must be integrated into C++ projects via static linking.
- **Header dependencies**: When using gclib in your project, ensure all header files are in your include path. Key headers include GSam.h, Gff.h, GFaSeqGet.h, GBase.h, GStr.h, GVec.hh, GList.hh.
- **htslib dependency**: SAM/BAM/CRAM functionality requires htslib to be installed and linked. Install via `conda install -c bioconda htslib`.
- **Build system**: The provided Makefile is only for running internal tests, not for library installation. Use your project's build system to incorporate gclib sources.
- **Memory management**: GFaSeqGet loads FASTA sequences with optional .fai indexing. Without indexing, entire sequences are held in memory.
- **CIGAR parsing**: GSamRecord handles all CIGAR operations including M/=/X (matches), I/D (insertions/deletions), S/H (soft/hard clipping), and N (splice junctions).
- **Version tracking**: gclib versions (e.g., v0.12.7) should match the StringTie version being used for compatibility.

## Examples

### Understanding gclib architecture
**Args:** `GSamReader* reader = new GSamReader("alignments.bam");`
**Explanation:** gclib provides modular classes for each genomic format. GSamReader wraps htslib for alignment I/O, GffReader parses GFF/GTF into hierarchical GffObj structures, and GFaSeqGet handles FASTA access with optional indexing. Understanding this architecture helps integrate gclib into custom C++ tools.

### Using GSamReader for BAM processing
**Args:** `GSamReader* reader = new GSamReader("alignments.bam"); while(reader->next(record)) { // process record }`
**Explanation:** GSamReader provides sequential iteration through SAM/BAM/CRAM files. The next() method populates a GSamRecord object with alignment data including coordinates, CIGAR, MAPQ, and flags. Automatic format detection handles .sam, .bam, and .cram extensions.

### Parsing GFF/GTF annotations
**Args:** `GffReader gffReader("annotations.gtf"); while((gffLine=gffReader.next())) { GffObj* gene = gffReader.read(); }`
**Explanation:** GffReader constructs hierarchical GffObj representations of genes and transcripts from GTF/GFF files. The class handles both GTF format (with transcript_id/gene_id attributes) and GFF3 format (with ID/Parent hierarchical relationships). Exon structures are stored as GList<GffExon> within each GffObj.

### Extracting sequences from FASTA
**Args:** `GFaSeqGet seqGet("reference.fa"); seqGet.get subsequence("chr1", 1000000, 2000000);`
**Explanation:** GFaSeqGet provides indexed or non-indexed access to FASTA sequences. With .fai index, subsequences are extracted efficiently from disk. Without indexing, entire sequences are loaded into memory. The class handles both single-FASTA and multi-FASTA files.

### CIGAR operation handling
**Args:** `record.cigar().to_string()`
**Explanation:** GSamRecord parses CIGAR strings into structured operations. M/=/X indicate matched bases, I/D represent insertions/deletions relative to reference, S/H denote soft/hard clipping at read ends, and N represents skipped regions (splice junctions). The mapped_len field calculates total aligned length excluding soft-clipped bases.

### Integration with StringTie
**Args:** `stringtie alignments.bam -G annotations.gtf -o transcripts.gtf`
**Explanation:** StringTie uses gclib as its core library for handling all genomic file I/O. When processing RNA-seq data with StringTie, gclib handles BAM input (via GSamReader), GFF guidance annotations (via GffReader), and FASTA reference sequences (via GFaSeqGet). Understanding gclib helps troubleshoot StringTie file handling issues.

### Thread-safe BAM reading
**Args:** `GSamReader* readers[N_THREADS]; for(int i=0; i<N_THREADS; i++) readers[i] = new GSamReader(bam_path);`
**Explanation:** GSamReader supports concurrent instantiation for multi-threaded processing. Each thread creates its own reader instance pointing to the same BAM file. htslib handles thread-safe access to the underlying file handles and index structures.

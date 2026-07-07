---
name: cramtools
category: programming
description: Java-based toolkit from EBI for CRAM/BAM conversion, indexing, merging, and reference retrieval
tags: [cramtools, CRAM, BAM, EBI, Java, compression, sequence-data, SAM]
author: oxo-call-community
source_url: "http://www.ebi.ac.uk/ena/software/cram-toolkit"
---

## Concepts

- **Tool Overview**: cramtools is a Java toolkit from the European Bioinformatics Institute (EBI) for efficient compression and manipulation of sequence alignment data in CRAM format.
- **Core Function**: Provides Java implementation for CRAM/BAM conversion, indexing, merging, and reference sequence retrieval. Original Java implementation that preceded samtools CRAM support.
- **Algorithm**: Uses HTSJDK library for reading/writing BAM/CRAM files with reference-based compression.
- **Input**: BAM, CRAM, SAM, or FASTQ files; reference genome for encoding.
- **Output**: Converted BAM/CRAM files, indexes, merged files, extracted FASTQ, quality statistics.
- **Application**: CRAM file manipulation, data archival to EBI/ENA, BAM to CRAM conversion, quality control, reference retrieval for CRAM files.
- **Installation**: `conda install -c bioconda cramtools` or download JAR file directly from EBI

## Pitfalls

- **Java Requirement**: Requires Java Runtime Environment (JRE) to run; heavier than samtools-based solutions.
- **CRAM3 Format**: Older versions may not support CRAM 3.x specification; ensure compatible version.
- **Reference Access**: For CRAM decoding, reference must be available locally or via network (EBI server).
- **Memory Usage**: Java-based tools typically require more memory than native C implementations.
- **Deprecated**: Most functionality now better handled by samtools/htslib; cramtools mainly for legacy compatibility.

## Examples

### Convert CRAM to BAM
**Args:** `java -jar cramtools-3.0.jar bam -I input.cram -O output.bam -R reference.fasta`
**Explanation:** Converts CRAM file to BAM format using specified reference genome.

### Convert BAM to CRAM
**Args:** `java -jar cramtools-3.0.jar cram -I input.bam -O output.cram -R reference.fasta`
**Explanation:** Compresses BAM file to CRAM format for storage reduction.

### Index CRAM/BAM file
**Args:** `java -jar cramtools-3.0.jar index -I input.cram`
**Explanation:** Creates index file (.crai or .bai) for the alignment file.

### Merge multiple files
**Args:** `java -jar cramtools-3.0.jar merge -I input1.bam -I input2.bam -O merged.bam`
**Explanation:** Combines multiple BAM or CRAM files into a single output file.

### Dump CRAM to FASTQ
**Args:** `java -jar cramtools-3.0.jar fastq -I input.cram -O output.fastq`
**Explanation:** Extracts sequences and qualities from CRAM file as FASTQ format.

### Fix CRAM header
**Args:** `java -jar cramtools-3.0.jar fixheader -I input.cram -O fixed.cram`
**Explanation:** Repairs or modifies CRAM file header without re-writing entire file.

### Download reference sequence
**Args:** `java -jar cramtools-3.0.jar getref -I input.cram -F reference.fasta`
**Explanation:** Retrieves reference sequences required to decode CRAM file, using MD5 checksums in header.

### Quality score statistics
**Args:** `java -jar cramtools-3.0.jar qstat -I input.cram`
**Explanation:** Generates quality score distribution statistics for the alignment file.

### Display help
**Args:** `java -jar cramtools-3.0.jar -h`
**Explanation:** Shows all available commands and their options.

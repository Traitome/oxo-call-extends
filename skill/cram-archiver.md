---
name: cram-archiver
category: formatting
description: Samtools wrapper for automated CRAM conversion with checksum verification and recursive BAM file discovery
tags: [cram-archiver, CRAM, BAM, samtools, compression, archival, sequencing]
author: oxo-call-community
source_url: "https://github.com/LUMC/cram-archiver"
---

## Concepts

- **Tool Overview**: cram-archiver is a samtools wrapper for automated conversion of BAM files to CRAM format with checksum verification and recursive file discovery.
- **Core Function**: Converts BAM to CRAM using `samtools view`, verifies file integrity via checksums, generates CRAM indexes, and optionally cleans up source BAM files.
- **Algorithm**: Recursively discovers BAM files, loads reference sequences, performs CRAM conversion with parallel processing, and validates output through checksum comparison.
- **Input**: BAM files, reference genome (FASTA with index), output directory.
- **Output**: CRAM files, CRAM index files (.crai), checksum files, verification logs.
- **Application**: NGS data archival, large-scale BAM to CRAM conversion pipelines, storage optimization.
- **Installation**: `pip install cram-archiver` or `conda install -c bioconda cram-archiver`

## Pitfalls

- **Reference Requirement**: CRAM requires reference genome for decoding; must provide via `-T` flag or configure REF_PATH environment variable.
- **Checksum Mismatch**: If BAM and CRAM checksums don't match, conversion failed; check for data corruption.
- **Symbolic Links**: Recursive discovery ignores symbolic links by default.
- **Disk Space**: Requires space for both BAM and CRAM during conversion (unless --delete flag used after verification).
- **Multiple References**: If BAM files use different references, each must be available and indexed.

## Examples

### Basic BAM to CRAM conversion
**Args:** `cram-archiver -i /path/to/bams/ -o /path/to/output/`
**Explanation:** Recursively finds all BAM files and converts to CRAM in specified output directory.

### With reference genome
**Args:** `cram-archiver -i /path/to/bams/ -o /output/ -r reference.fasta`
**Explanation:** Uses specified reference genome for CRAM conversion.

### Skip checksum generation
**Args:** `cram-archiver -i /path/to/bams/ -o /output/ --no-checksum`
**Explanation:** Skips checksum generation to speed up conversion (not recommended for archival).

### Delete BAM after successful conversion
**Args:** `cram-archiver -i /path/to/bams/ -o /output/ --delete`
**Explanation:** Removes BAM file after CRAM conversion and checksum verification complete successfully.

### Set minimum file size threshold
**Args:** `cram-archiver -i /path/to/bams/ -o /output/ --min-size 1000`
**Explanation:** Only processes BAM files larger than specified byte threshold.

### Specify number of threads
**Args:** `cram-archiver -i /path/to/bams/ -o /output/ -t 8`
**Explanation:** Uses 8 threads for parallel conversion (default auto-detects CPU cores).

### Dry run (test mode)
**Args:** `cram-archiver -i /path/to/bams/ -o /output/ --dry-run`
**Explanation:** Shows what would be converted without performing actual conversion.

### Convert single file
**Args:** `cram-archiver -i single_file.bam -o /output/`
**Explanation:** Converts a single BAM file to CRAM.

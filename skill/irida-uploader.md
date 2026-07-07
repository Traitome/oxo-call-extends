---
name: irida-uploader
category: utility
description: Command-line tool for uploading NGS sequencing data to the IRIDA bioinformatics platform.
tags: [irida-uploader, NGS, sequencing data, batch upload, IRIDA]
author: oxo-call-community
source_url: "https://irida-uploader.readthedocs.io/en/latest"
---

## Concepts

- **NGS Data Upload**: irida-uploader (v0.9.5) provides command-line and GUI interfaces for uploading sequencing data to IRIDA.
- **Multi-platform Support**: Handles MiSeq, MiniSeq, NextSeq, iSeq, and generic directory formats.
- **Upload Modes**: Supports fastq sequence files, genome assemblies (FASTA), and Oxford Nanopore Fast5 files.
- **Batch Processing**: Enables uploading multiple sequencing runs simultaneously using batch mode.
- **Resume Capability**: Supports resuming interrupted uploads without retransferring already uploaded files.
- **Automation Ready**: Can be integrated with cron or task schedulers for automated data transfer.

## Pitfalls

- **Configuration Requirements**: Requires IRIDA client ID, secret, and credentials in configuration file.
- **Version Compatibility**: Uploader version must match minimum IRIDA server version requirements.
- **Network Stability**: Large uploads require stable network connections; interruptions may corrupt data.
- **File Size Limits**: IRIDA server may impose file size restrictions on uploads.
- **Sample Sheet Requirements**: Illumina runs require properly formatted SampleSheet.csv files.
- **Duplicate Detection**: Existing samples with identical names may cause upload failures.

## Examples

### Basic directory upload
**Args:** `irida-uploader -d /path/to/sequencing/run/`
**Explanation:** Uploads sequencing data from a directory using the default parser configuration.

### Upload assemblies
**Args:** `irida-uploader -d /path/to/assemblies/ --upload_mode assemblies`
**Explanation:** Uploads genome assembly FASTA files instead of sequence reads.

### Batch upload multiple runs
**Args:** `irida-uploader --batch /path/to/batch/directory/`
**Explanation:** Processes and uploads all sequencing runs contained in subdirectories.

### Force reupload of existing run
**Args:** `irida-uploader -d /path/to/run/ --force`
**Explanation:** Forces reupload even if the run was previously uploaded (ignores status file).

### Specify custom configuration
**Args:** `irida-uploader --config /path/to/config.conf -d /path/to/run/`
**Explanation:** Uses a custom configuration file instead of the default location.

### Upload Fast5 files
**Args:** `irida-uploader -d /path/to/fast5/ --upload_mode fast5`
**Explanation:** Uploads Oxford Nanopore Fast5 raw data files to IRIDA.
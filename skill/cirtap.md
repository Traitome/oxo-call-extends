---
name: cirtap
category: utility
description: CLI to handle PATRIC data from the FTP
tags: [cirtap, patric, ftp, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/MGXlab/cirtap/"
---

## Concepts

- **Tool Overview**: cirtap is a command-line interface (CLI) tool for downloading and managing data from the PATRIC (Pathosystems Resource Integration Center) FTP server.
- **Core Function**: Facilitates downloading, organizing, and processing PATRIC database data.
- **Features**: Data downloading, file organization, and metadata management from PATRIC FTP.
- **Input**: PATRIC FTP credentials and data selection parameters.
- **Output**: Downloaded data files and organized directory structure.
- **Application**: Accessing bacterial pathogen data, genome sequences, and annotations from PATRIC.
- **Installation**: Install via bioconda: `conda install -c bioconda cirtap`

## Pitfalls

- **Network Access**: Requires internet access to download from PATRIC FTP.
- **Credentials**: May require PATRIC account credentials for certain data.
- **Data Volume**: Large datasets may require significant storage space.
- **FTP Server**: Dependent on PATRIC FTP server availability.
- **File Organization**: Requires careful management of downloaded files.

## Examples

### Download genome data
**Args:** `cirtap download -t genome -o genomes/`
**Explanation:** Downloads genome data from PATRIC FTP.

### Download annotations
**Args:** `cirtap download -t annotation -o annotations/`
**Explanation:** Downloads annotation data from PATRIC FTP.

### List available datasets
**Args:** `cirtap list`
**Explanation:** Lists available datasets on PATRIC FTP.

### Display help
**Args:** `cirtap --help`
**Explanation:** Shows all available commands and options.
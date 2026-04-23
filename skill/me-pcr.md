---
name: me-pcr
category: alignment
description: Multithreaded Electronic PCR (in-silico PCR) based on NCBI e-PCR.
tags: [me-pcr, alignment]
author: oxo-call-community
source_url: "https://web.archive.org/web/20100708193215/http://genome.chop.edu/mePCR/"
---

## Concepts

- **Tool Overview**: me-pcr v1.0.6 - Multithreaded Electronic PCR (me-PCR) was developed by Kevin Murphy at Children's Hospital of Philadelphia. It is described in Murphy et al (2004) https://doi.org/10.1093/bioinformatics/btg466 and was originally available from http://genome.chop.edu/mePCR (defunct). It was based on the public domain NCBI tool e-PCR by Gregory D. Schuler, described in Schuler (1997) https://doi.org/10.1101/gr.7.5.541 which was origially availble from ftp://ncbi.nlm.nih.gov/pub/schuler/e-PCR/ (defunct). The final release of me-PCR was v1.0.6 (2008-02-18), and the author wrote that in general NCBI e-PCR should be used instead having been improved greatly over the years. The NCBI retired and withdrew the e-PCR webservice and command line tool on 2017-06-28, suggesting the online-only tool Primer-BLAST instead. However, this is not suitable for offline high throughput usage. See also Jim Kent's isPCR (aslo available in BioConda)..
- **Core Function**: Multithreaded Electronic PCR (in-silico PCR) based on NCBI e-PCR.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda me-pcr`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.

---
name: fastq-screen
category: formatting
description: "FastQ Screen allows you to screen a library of sequences in FastQ format against a set of sequence databases so you can see if the composition of the library matches with what you expect."
tags: [fastq-screen, formatting, contamination-screening, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://www.bioinformatics.babraham.ac.uk/projects/fastq_screen"
---

## Concepts

- **Tool Overview**: FastQ Screen is a tool for screening sequencing libraries against sequence databases to check for contamination or unexpected sequence composition.
- **Core Function**: Maps reads against reference databases to identify potential contaminants.
- **Input/Output**: Input: FASTQ files. Output: Report showing mapping percentages to each database.
- **Algorithm**: Uses alignment algorithms to map reads against reference databases.
- **Key Features**: Database screening, contamination detection, HTML reports, multiple database support, configurable thresholds.
- **Installation**: `conda install -c bioconda fastq-screen`

## Pitfalls

- **Database Requirements**: Requires pre-built reference databases.
- **Memory Usage**: Large databases may require significant memory.
- **Alignment Time**: Screening against multiple databases may be time-consuming.
- **False Positives**: May detect false positives from common sequences.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic screening
**Args:** `fastq-screen reads.fastq --outdir results/`
**Explanation:** Screens reads against configured databases.

### Specific databases
**Args:** `fastq-screen reads.fastq --outdir results/ --database human --database mouse`
**Explanation:** Screens against specific databases.

### Paired-end screening
**Args:** `fastq-screen reads_1.fastq reads_2.fastq --outdir results/`
**Explanation:** Screens paired-end reads.

### Custom configuration
**Args:** `fastq-screen reads.fastq --outdir results/ --conf config.conf`
**Explanation:** Uses custom configuration file.

### Generate HTML report
**Args:** `fastq-screen reads.fastq --outdir results/ --html`
**Explanation:** Generates HTML report.
---
name: bold-identification
category: annotation
description: Taxonomic assignment for sequences using the BOLD database
tags: [bold, taxonomy, identification, barcode, species]
author: oxo-call-community
source_url: "https://github.com/linzhi2013/bold_identification"
---

## Concepts

- **Tool Overview**: bold-identification assigns taxonomy to DNA sequences using the BOLD (Barcode of Life) database.
- **Core Function**: Identifies species from DNA barcodes by querying the BOLD Systems database.
- **Input**: FASTA file with query sequences (typically COI barcode region).
- **Output**: Taxonomic assignments with match statistics.
- **Database**: Uses BOLD Systems public database for species identification.
- **Installation**: Install via bioconda: `conda install -c bioconda bold-identification`

## Pitfalls

- **Network Required**: Requires internet connection to query BOLD database.
- **Barcode Region**: Best results with standard barcode regions (COI for animals).
- **Match Threshold**: Adjust similarity threshold based on identification confidence needed.
- **Rate Limiting**: Large queries may be rate-limited by BOLD servers.

## Examples

### Identify species from FASTA
**Args:** `bold_identification -i sequences.fa -o results.tsv`
**Explanation:** Identifies species for sequences in FASTA file using BOLD database.

### Set similarity threshold
**Args:** `bold_identification -i sequences.fa -t 97 -o results.tsv`
**Explanation:** Uses 97% similarity threshold for species identification.

### Specify output format
**Args:** `bold_identification -i sequences.fa -f csv -o results.csv`
**Explanation:** Outputs identification results in CSV format.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.

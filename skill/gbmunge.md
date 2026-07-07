---
name: gbmunge
category: formatting
description: Munge GenBank files into FASTA and tab-separated metadata.
tags: [gbmunge, formatting, genbank, fasta, conversion]
author: oxo-call-community
source_url: "https://github.com/sdwfrost/gbmunge"
---

## Concepts

- **Tool Overview**: gbmunge is a C-language utility that converts GenBank format files into FASTA sequence files and tab-separated metadata files. It is designed for preprocessing GenBank data for downstream bioinformatics analysis, particularly for tools that require FASTA input or structured metadata.
- **Core Function**: Extract nucleotide/protein sequences from GenBank files and generate corresponding structured metadata including sequence names, accession numbers, lengths, submission dates, and country information. The tool processes one GenBank file per run and outputs two files: a FASTA file with sequences and a tab-separated file with metadata.
- **Input Format**: GenBank flat file format (.gb, .gbk) containing annotated sequence records with ORIGIN sections containing the actual sequence data. The tool parses the LOCUS, DEFINITION, ACCESSION, VERSION, and ORIGIN lines from each record.
- **Output Formats**: (1) FASTA format with 80-character line width for sequences, header lines starting with ">" containing the primary accession number. (2) Tab-separated metadata with columns: name, accession, length, submission_date (in ISO format), country.
- **Date Reformatting**: Converts dates from GenBank format (e.g., "31-DEC-2001") to ISO 8601 standard format (e.g., "2001-12-31") for compatibility with downstream tools like BEAST that require standardized date formats.
- **Country Name Standardization**: Cleans and standardizes country names to match ISO 3166-3 codes, replacing deprecated or variant country names with current standard designations. This ensures consistency in geographic metadata for meta-analysis.
- **Installation**: Compiled C program installed via Bioconda (`conda install -c bioconda gbmunge`) or compiled from source using the provided Makefile. Requires libgencode if building from source.

## Pitfalls

- **Missing ORIGIN Section**: GenBank files without an ORIGIN section (sequence data) will produce empty FASTA output. Always verify that your GenBank file contains sequence data before processing.
- **Large NCBI Taxonomy Files**: The tool relies on NCBI-maintained mapping files (gi_taxid_nucl.dmp.gz) which are several GB in size. Ensure adequate disk space and download time when setting up the required NCBI taxonomy data.
- **Date Format Variations**: Some GenBank records use non-standard date formats that may not be properly converted. Check the output metadata file after processing to verify date conversion worked correctly.
- **Memory Usage**: When processing very large GenBank files (hundreds of MB), the tool may require significant memory. Consider splitting large files into smaller chunks for processing.
- **Compression Format**: The tool reads plain-text GenBank files. Compressed (.gz) files must be decompressed first using `gunzip` or `zcat` before processing.

## Examples

### Basic GenBank to FASTA conversion
**Args:** `-i sequences.gb -f sequences.fasta -o metadata.tsv`
**Explanation:** The fundamental gbmunge operation reads a GenBank file specified by `-i`, extracts all sequences into FASTA format output via `-f`, and generates tab-separated metadata via `-o`. The metadata file will contain one line per sequence record with name, accession, length, standardized date, and country information.

### Convert with sorted output
**Args:** `-i sequences.gb -f sequences_sorted.fasta -o metadata_sorted.tsv -s`
**Explanation:** The `-s` flag sorts the sequences alphabetically by accession number before writing to the output files. This is useful when you need consistent, reproducible output ordering for downstream processing or comparison between different runs.

### Batch process multiple files
**Args:** `for f in *.gb; do gbmunge -i "$f" -f "${f%.gb}.fasta" -o "${f%.gb}.tsv"; done`
**Explanation:** A shell loop that processes all GenBank files in the current directory. Each file is converted to its own FASTA and metadata pair with the .gb extension replaced by .fasta and .tsv respectively.

### Verify output quality
**Args:** `gbmunge -i ecoli.gb -f ecoli.fasta -o ecoli.tsv && wc -l ecoli.fasta ecoli.tsv && head -5 ecoli.tsv`
**Explanation:** After conversion, verify the output by checking line counts matches expected record counts, and inspect the first few lines of the metadata file to ensure dates were properly reformatted and country names standardized.

### Prepare data for BEAST analysis
**Args:** `gbmunge -i viral_sequences.gb -f viral.fasta -o viral_metadata.tsv && awk -F'\t' 'NR>1 {print $1,$3,$4}' viral_metadata.tsv > beast_dates.tsv`
**Explanation:** gbmunge is commonly used to prepare sequence data for BEAST (Bayesian Evolutionary Analysis Sampling Trees), which requires dates in ISO format. The metadata output can be extracted to create the date file needed for tip-dating analysis.

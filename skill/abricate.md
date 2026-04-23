---
name: abricate
category: annotation
description: Mass screening of contigs for antimicrobial resistance or virulence genes.
tags: [abricate, annotation, antimicrobial-resistance, virulence, amr, bacteria]
author: oxo-call-community
source_url: "https://github.com/tseemann/abricate"
---

## Concepts

- **Tool Overview**: Screens bacterial genome assemblies (contigs) for antimicrobial resistance (AMR) and virulence genes using sequence alignment against multiple databases. Version 1.4.0.
- **Core Function**: Takes assembled contigs (FASTA/GenBank) as input and identifies AMR/virulence genes by aligning against built-in databases using BLAST+.
- **Input/Output**: Input is assembled contigs in FASTA, GenBank, or compressed formats (.gz, .bz2). Output is a tab-delimited report with gene matches, coverage, identity, and resistance profiles.
- **Installation**: Install via bioconda: `conda install -c bioconda abricate`
- **Platform Support**: Linux (x86_64), macOS (x86_64), and platform-independent
- **Bundled Databases**: NCBI, CARD, ARG-ANNOT, ResFinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF, VFDB, Victors, BacMet2
- **Two Commands**: `abricate` (main screening) and `abricate-get_db` (database update)
- **Dependency**: Requires BLAST+ >= 2.7 and any2fasta

## Pitfalls

- **Contigs Only**: Only accepts assembled contigs, NOT raw FASTQ reads. Assemble first with SPAdes, Unicycler, etc.
- **No Point Mutation Detection**: ABRicate only detects acquired resistance genes via sequence alignment. It does NOT detect point mutations conferring resistance (use ARIBA or AMRFinderPlus for that).
- **Database Setup Required**: Run `abricate --setupdb` after installation to build BLAST databases from the sequence files.
- **Default Database**: The default database is `ncbi`. Use `--db` to specify a different database. Different databases may give different results.
- **Minimum Identity/Coverage**: Default thresholds may miss distant homologs. Adjust `--minidentity` and `--mincoverage` if needed.
- **Multiple Databases Recommended**: Run with multiple databases and combine results for comprehensive screening.

## Examples

### Display help and check installation
**Args:** `--help`
**Explanation:** Shows all available command-line options and subcommands.

### Check installation and list databases
**Args:** `--check`
**Explanation:** Verifies that all dependencies (BLAST+, any2fasta) are correctly installed and databases are set up.

### List available databases
**Args:** `--list`
**Explanation:** Lists all bundled databases available for screening. Use this to see which databases are installed and their versions.

### Screen a single assembly for AMR genes
**Args:** `assembly.fasta`
**Explanation:** Screens the assembly file against the default (ncbi) database. Output is a tab-delimited report of all detected AMR genes with coverage, identity, and resistance profiles.

### Screen with a specific database
**Args:** `--db card --quiet assembly.fasta`
**Explanation:** Screens against the CARD database in quiet mode (less verbose output). CARD provides curated AMR gene references with resistance mechanisms.

### Screen multiple files using a file list
**Args:** `--fofn assembly_list.txt`
**Explanation:** Screens all assemblies listed in the file-of-filenames (FOFN). Each line in the file should be a path to an assembly file.

### Combine results into a summary matrix
**Args:** `--summary sample1.tab sample2.tab sample3.tab`
**Explanation:** Merges individual screening reports into a gene presence/absence matrix. Each row is a gene, each column is a sample. Useful for comparing AMR profiles across isolates.

### Update a database to latest version
**Args:** `--db ncbi --force`  *(for abricate-get_db)*
**Explanation:** Forces download and rebuild of the NCBI AMR database to the latest version. Use `abricate-get_db` command.

### Build/setup all databases
**Args:** `--setupdb`
**Explanation:** Builds BLAST databases from the bundled sequence files. Must be run after installation or after adding custom databases.

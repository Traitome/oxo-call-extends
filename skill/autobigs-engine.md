---
name: autobigs-engine
category: programming
description: autoBIGS Engine - Core library for rapid MLST profile fetching from sequences
tags: [autobigs-engine, mlst, sequence-typing, pathogen-identification, library]
author: oxo-call-community
source_url: "https://github.com/Syph-and-VPD-Lab/autoBIGS.engine"
---

## Concepts

- **Tool Overview**: autoBIGS Engine is the core library powering MLST (Multi-Locus Sequence Typing) profile fetching from bacterial genome sequences. Version 0.14.2.
- **Core Function**: Provides the computational engine for identifying MLST alleles and sequence types from genome sequences for various bacterial pathogens.
- **MLST Database Integration**: Interfaces with MLST databases to match allele sequences and determine sequence types (ST).
- **Algorithm Efficiency**: Optimized for rapid allele matching and ST determination in large-scale typing workflows.
- **Multiple Pathogen Support**: Supports MLST schemes for various bacterial pathogens including Neisseria, Salmonella, E. coli, Staphylococcus, and more.
- **Input/Output**: Accepts genome sequences in FASTA format, outputs MLST profiles with allele calls and ST assignments.
- **Installation**: `conda install -c bioconda autobigs-engine` or install from GitHub.

## Pitfalls

- **Database Updates**: MLST databases are regularly updated. Ensure database is current for accurate typing results.
- **Novel Alleles**: Novel alleles not present in the database will result in unknown sequence type calls.
- **Assembly Quality**: Poor quality assemblies may produce missing or incorrect allele calls.
- **Scheme Selection**: Must select appropriate MLST scheme for the target organism. Wrong scheme produces meaningless results.
- **Ambiguous Matches**: Some sequences may match multiple alleles equally well, requiring manual review.
- **Memory Requirements**: Processing large genome collections may require significant memory resources.

## Examples

### Display help
**Args:** `autobigs-engine --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic MLST typing
**Args:** `autobigs-engine --input genome.fasta --scheme neisseria --output results.txt`
**Explanation:** Performs MLST typing using Neisseria scheme and outputs results to text file.

### Process multiple genomes
**Args:** `autobigs-engine --input-dir genomes/ --scheme salmonella --output batch_results.tsv`
**Explanation:** Processes all FASTA files in directory with Salmonella MLST scheme.

### Update MLST database
**Args:** `autobigs-engine --update-database`
**Explanation:** Updates local MLST database to latest version from public repositories.

### Verbose output
**Args:** `autobigs-engine --input genome.fasta --scheme ecoli --verbose --output detailed.txt`
**Explanation:** Provides detailed output including individual allele sequences and confidence scores.

### Custom database path
**Args:** `autobigs-engine --input genome.fasta --scheme staphylococcus --db-path /custom/db/ --output results.txt`
**Explanation:** Uses custom MLST database path instead of default location.

### Quality filtering
**Args:** `autobigs-engine --input genome.fasta --scheme enterococcus --min-coverage 5 --output filtered_results.txt`
**Explanation:** Filters results requiring minimum 5x coverage for allele calls.

### JSON output format
**Args:** `autobigs-engine --input genome.fasta --scheme campylobacter --format json --output results.json`
**Explanation:** Outputs MLST results in JSON format for programmatic processing.

### Batch processing with parallel execution
**Args:** `autobigs-engine --input-dir genomes/ --scheme pseudomonas --threads 8 --output batch_results.tsv`
**Explanation:** Processes multiple genomes using 8 parallel threads for faster analysis.
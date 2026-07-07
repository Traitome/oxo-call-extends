---
name: ngmaster
category: typing
description: NG-MAST and NG-STAR sequence typing for Neisseria gonorrhoeae.
tags: [ngmaster, typing, gonorrhoeae, ng-master, ng-star]
author: oxo-call-community
source_url: "https://github.com/MDU-PHL/ngmaster"
---

## Concepts

- **Tool Overview**: NGMASTER performs in silico multi-antigen sequence typing for N. gonorrhoeae.
- **Core Function**: Determines NG-MAST and NG-STAR types from genome sequences.
- **Algorithm**: Compares sequences against reference databases using BLAST.
- **Input Format**: Accepts FASTA files with genome sequences.
- **Output**: Produces typing results with allele numbers and types.
- **Use Case**: Epidemiological surveillance, outbreak tracking, and antimicrobial resistance monitoring.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Database Updates**: Requires up-to-date reference databases.
- **Sequence Quality**: Poor quality sequences affect typing accuracy.
- **Database Access**: Requires internet for database updates.
- **Memory Usage**: Large genomes require memory.
- **Ambiguous Results**: May produce ambiguous type calls.

## Examples

### Display help
**Args:** `ngmaster --help`
**Explanation:** Shows available options and usage instructions.

### Type genome
**Args:** `ngmaster -i genome.fasta -o results.txt`
**Explanation:** Determines NG-MAST and NG-STAR types.

### Output JSON
**Args:** `ngmaster -i genome.fasta --json -o results.json`
**Explanation:** Outputs results in JSON format.

### Update database
**Args:** `ngmaster --update`
**Explanation:** Updates reference databases.

### Verbose mode
**Args:** `ngmaster -i genome.fasta -v -o results.txt`
**Explanation:** Runs with verbose output.

### Force typing
**Args:** `ngmaster -i genome.fasta -f -o results.txt`
**Explanation:** Forces typing even with partial matches.

### Multiple files
**Args:** `ngmaster -i genome1.fasta genome2.fasta -o results.txt`
**Explanation:** Processes multiple genome files.
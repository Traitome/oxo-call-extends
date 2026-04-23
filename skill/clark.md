---
name: clark
category: metagenomics
description: Fast and accurate k-mer based sequence classification for metagenomics
tags: [clark, metagenomics, classification, k-mer, taxonomy, microbiome]
author: oxo-call-community
source_url: "https://github.com/rouni001/CLARK"
---

## Concepts

- **Tool Overview**: CLARK (CLAssifier based on Reduced K-mers) is a fast and accurate sequence classifier for metagenomic and genomic data using discriminative k-mers.
- **Core Function**: Classifies DNA sequences (reads or contigs) to their most likely source organism by matching discriminative k-mers against a reference database.
- **Input/Output**: Input: FASTQ/FASTA files. Output: Classification report with taxonomic assignments and confidence scores.
- **Database Creation**: Requires building a reference database from NCBI genomes. Use `CLARKSCripts` for database setup.
- **K-mer Approach**: Uses discriminative k-mers (unique to each taxon) for fast and memory-efficient classification.
- **Confidence Score**: Provides confidence scores for each classification based on k-mer matches.

## Pitfalls

- **Database Required**: Must build or download a reference database before classification. Database creation can take hours and requires significant disk space.
- **Memory Usage**: Database must fit in RAM. Human genome database requires ~100GB RAM. Use `--light` mode for reduced memory.
- **K-mer Length**: Default k=31 works well for most applications. Shorter k-mers increase sensitivity but reduce specificity.
- **Classification Level**: Can classify at species, genus, or custom taxonomic levels. Default is species-level.
- **Paired-End Data**: For paired-end reads, provide both files separately with `-R` and `-R2` flags.
- **Output Format**: Multiple output formats available. Use `--summary` for concise report or `--detail` for per-read assignments.

## Examples

### Classify single-end reads
**Args:** `-R reads.fq -D /path/to/database -O results.txt`
**Explanation:** Classifies single-end reads against the reference database, outputs results to results.txt.

### Classify paired-end reads
**Args:** `-R reads_R1.fq -R2 reads_R2.fq -D /path/to/database -O results.txt`
**Explanation:** Classifies paired-end reads, considering both mates for improved accuracy.

### Build reference database
**Args:** `CLARKSCripts/setDB.sh -D /path/to/database --standard`
**Explanation:** Creates a standard reference database from NCBI bacterial and viral genomes.

### Build custom database from FASTA
**Args:** `CLARKSCripts/setDB.sh -D /path/to/database -F genomes/*.fna -T taxonomy.txt`
**Explanation:** Creates a custom database from user-provided genome FASTA files with taxonomy information.

### Classify with summary report
**Args:** `-R reads.fq -D /path/to/database --summary`
**Explanation:** Outputs a concise summary report with taxon counts and percentages instead of per-read assignments.

### Classify with detailed output
**Args:** `-R reads.fq -D /path/to/database --detail`
**Explanation:** Outputs detailed per-read classification including confidence scores and matched k-mer counts.

### Light mode for reduced memory
**Args:** `-R reads.fq -D /path/to/database --light`
**Explanation:** Uses reduced database loading for systems with limited RAM, trades some accuracy for memory efficiency.

### Classify at genus level
**Args:** `-R reads.fq -D /path/to/database --taxonomic_level genus`
**Explanation:** Classifies reads at genus level instead of species, useful for broader taxonomic profiling.

### Output in CAMI format
**Args:** `-R reads.fq -D /path/to/database --camill`
**Explanation:** Outputs results in CAMI (Critical Assessment of Metagenome Interpretation) format for benchmarking.

### Filter low-confidence classifications
**Args:** `-R reads.fq -D /path/to/database --confidence 0.5`
**Explanation:** Only reports classifications with confidence score >= 0.5, reducing false positives.

---
name: blast
category: alignment
description: BLAST+ finds regions of local similarity between sequences by comparing nucleotide or protein sequences to sequence databases
tags: [blast, alignment, sequence-search, database-search, ncbi]
author: oxo-call-community
source_url: "https://blast.ncbi.nlm.nih.gov/doc/blast-help/"
---

## Concepts

- **Tool Overview**: BLAST+ (Basic Local Alignment Search Tool) is a suite of command-line tools for sequence similarity searching, finding regions of local similarity between sequences.
- **Core Programs**: blastn (nucleotide vs nucleotide), blastp (protein vs protein), blastx (translated nucleotide vs protein), tblastn (protein vs translated nucleotide), tblastx (translated nucleotide vs translated nucleotide)
- **Database Building**: Use `makeblastdb` to create BLAST databases from FASTA files before searching
- **Output Formats**: Tabular (-outfmt 6/7), XML, ASN.1, and plain text formats available
- **E-value Threshold**: Statistical significance measure; lower values indicate more significant matches
- **Installation**: Install via bioconda: `conda install -c bioconda blast`

## Pitfalls

- **Database Path**: Always specify full path to database; BLAST looks in current directory by default
- **Large Databases**: For large databases, use `-num_threads` for parallel processing
- **Memory Usage**: blastn with large databases can be memory-intensive; consider using megablast for intraspecies comparisons
- **Query Format**: Ensure query sequences are valid FASTA format without special characters in headers
- **Output Parsing**: Tabular format (-outfmt 6) is recommended for downstream processing

## Examples

### Create a BLAST database from FASTA
**Args:** `makeblastdb -in genome.fa -dbtype nucl -out genome_db`
**Explanation:** Creates a nucleotide BLAST database named 'genome_db' from genome.fa for subsequent searches.

### Basic nucleotide BLAST search
**Args:** `blastn -query sequences.fa -db genome_db -out results.txt -evalue 1e-5`
**Explanation:** Searches sequences against the genome database with e-value threshold of 1e-5.

### Protein BLAST search
**Args:** `blastp -query proteins.fa -db nr -out results.txt -evalue 1e-10 -max_target_seqs 10`
**Explanation:** Searches protein sequences against nr database, returning top 10 hits per query.

### Translated BLAST search
**Args:** `blastx -query dna_sequences.fa -db protein_db -out results.txt -evalue 1e-3 -outfmt 6`
**Explanation:** Translates DNA sequences in 6 frames and searches against protein database, outputting tabular format.

### BLAST with custom output format
**Args:** `blastn -query seq.fa -db genome_db -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore" -out results.tsv`
**Explanation:** Custom tabular output with specific columns for downstream analysis.

### Parallel BLAST search
**Args:** `blastn -query large_query.fa -db genome_db -num_threads 8 -out results.txt`
**Explanation:** Uses 8 threads for faster searching of large query files.

### Build protein database
**Args:** `makeblastdb -in proteins.fa -dbtype prot -out protein_db -parse_seqids`
**Explanation:** Creates a protein BLAST database with sequence IDs parsed from FASTA headers.

### Megablast for highly similar sequences
**Args:** `blastn -query reads.fa -db genome_db -task megablast -out results.txt -perc_identity 95`
**Explanation:** Uses megablast algorithm optimized for highly similar sequences (>95% identity).

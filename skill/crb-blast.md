---
name: crb-blast
category: utility
description: Conditional Reciprocal Best BLAST for high-confidence ortholog assignment between transcriptomes and reference proteins
tags: [crb-blast, BLAST, ortholog, reciprocal-best-blast, transcriptome-annotation, gene-annotation, orthology, ruby]
author: oxo-call-community
source_url: "https://github.com/cboursnell/crb-blast"
---

## Concepts

- **Tool Overview**: crb-blast (v0.6.9) - Conditional Reciprocal Best BLAST - a novel method for high-confidence ortholog assignment between sequence sets.
- **Core Function**: Finds orthologs by performing reciprocal best BLAST hits with learned e-value cutoffs. The key innovation is learning an appropriate e-value cutoff for each pairwise alignment based on the overall relatedness of the two datasets being compared, rather than using a single global cutoff.
- **Algorithm**: (1) Performs BLAST alignment of query->target and target->query. (2) Identifies reciprocal best hits where the best match for query in query->target is also the best hit in reverse alignment. (3) Fits a function to the distribution of alignment e-values over sequence lengths to determine per-sequence e-value cutoffs. (4) Applies these learned cutoffs to identify high-confidence ortholog pairs.
- **Input**: Query FASTA (nucleotide transcripts), Target FASTA (nucleotide or protein sequences).
- **Output**: Tab-separated file with columns: query, target, id (percent identity), alnlen, evalue, bitscore, qstart..qend, tstart..tend, qlen, tlen.
- **Application**: Ortholog assignment for de-novo transcriptome annotation, cross-species gene mapping, genome annotation validation, phylogenomic analysis.
- **Installation**: `gem install crb-blast` (requires Ruby v2.0+ and NCBI BLAST+ in PATH)

## Pitfalls

- **Ruby Dependency**: Requires Ruby v2.0 or later. If Ruby is not installed, use RVM: `curl -sSL https://get.rvm.io | bash -s stable --ruby`
- **BLAST+ Requirement**: NCBI BLAST+ must be installed and in PATH. Download from https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/
- **Sequence Type Matching**: Query should be nucleotide sequences (transcripts), Target can be nucleotide or protein. Using protein targets generally gives better results.
- **E-value Learning**: The algorithm learns e-value cutoffs from the data itself - sufficient sequence diversity is needed for proper fitting.
- **Computational Cost**: Full reciprocal BLAST is expensive. Use `--split` option for large files to parallelize across multiple BLAST jobs.
- **Threading**: Use `--threads` to parallelize BLAST searches. Default is 1 thread.

## Examples

### Display help message
**Args:** `-l`
**Explanation:** Show all available command-line options including --query, --target, --evalue, --threads, --output, and --split.

### Basic ortholog finding
**Args:** `--query assembly.fa --target reference_proteins.fa --output annotation.tsv`
**Explanation:** Run CRB-BLAST to find orthologs between assembled transcripts (assembly.fa) and a reference protein database (reference_proteins.fa). Output results to annotation.tsv.

### Multi-threaded execution
**Args:** `--query transcripts.fa --target proteins.fa --threads 8 --output orthologs.tsv`
**Explanation:** Run with 8 threads for faster BLAST searches. Increase thread count based on available CPU cores and database size.

### Using E-value cutoff
**Args:** `--query assembly.fa --target proteins.fa --evalue 1e-10 --output annotation.tsv`
**Explanation:** Set a stricter e-value cutoff of 1e-10 (default is 1e-5). More stringent filtering reduces false positives but may miss distant orthologs.

### Split large files for parallel processing
**Args:** `--query large_transcripts.fa --target large_proteins.fa --split --threads 16 --output results.tsv`
**Explanation:** Split large FASTA files into chunks and run multiple BLAST jobs in parallel, then combine results. Essential for large-scale datasets to reduce runtime.

### Using as Ruby library
**Args:** `blaster = CRB_Blast.new('query.fa', 'target.fa'); blaster.run(1e-5, 4, true)`
**Explanation:** Use CRB-BLAST as a library in Ruby code. Initialize with query and target files, then run with e-value 1e-5, 4 threads, and verbose output enabled.

### Step-by-step library usage
**Args:** `blaster = CRB_Blast.new('query.fa', 'target.fa'); blaster.makedb; blaster.run_blast(1e-5, 6, true); blaster.load_outputs; blaster.find_reciprocals; blaster.find_secondaries`
**Explanation:** Execute CRB-BLAST in individual steps: create BLAST database, run BLAST searches with 6 threads, load results, find reciprocal best hits, find secondary hits.

### Cross-species transcriptome annotation
**Args:** `--query plant_transcripts.fa --target plant_proteins.fa --threads 12 --output plant_orthologs.tsv`
**Explanation:** Annotate a de-novo assembled plant transcriptome by finding orthologous proteins from a reference plant protein database. Useful for functional annotation of novel transcriptomes.

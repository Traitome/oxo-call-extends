---
name: hpcblast
category: hpc
description: A wrapper for NCBI-BLAST+ suite which provides a simple and efficient method to accelerate the blast search on HPC clusters
tags: [hpcblast, blast, parallel, hpc, sun_grid_engine]
author: oxo-call-community
source_url: "https://github.com/yodeng/hpc-blast"
---

## Concepts

- **Parallel BLAST Execution**: Wrapper for NCBI-BLAST+ that splits queries and runs in parallel
- **Query Splitting**: Automatically divides input sequence files into smaller chunks for parallel processing
- **HPC Environment Support**: Native support for Sun Grid Engine (SGE) and other cluster managers
- **Localhost Mode**: Can also run on a single machine for testing and small-scale analyses
- **Transparent Wrapper**: Simply prepend `hpc-blast` to standard BLAST commands
- **Load Balancing**: Distributes workload across available compute nodes for optimal resource utilization

## Pitfalls

- **Cluster Configuration**: Requires proper HPC cluster configuration and job scheduling setup
- **Memory Coordination**: Large databases may require memory coordination across nodes
- **Output Merging**: Requires proper merging of results from parallel jobs
- **Database Availability**: BLAST database must be accessible from all compute nodes
- **Job Queue Delays**: Cluster queue times can affect overall execution time
- **Input Size**: Small query sets may not benefit from parallelization overhead

## Examples

### Basic parallel BLASTN
**Args:** `hpc-blast blastn -query input.fasta -db ref_db -out results.txt`
**Explanation:** Runs BLASTN in parallel by prepending hpc-blast to standard BLAST command.

### With specific number of chunks
**Args:** `hpc-blast -c 16 blastn -query input.fasta -db ref_db -out results.txt`
**Explanation:** Splits the query into 16 chunks for parallel processing across cluster nodes.

### Localhost mode for testing
**Args:** `hpc-blast -l blastp -query proteins.fasta -db uniprot -out blast_results.txt`
**Explanation:** Runs parallel BLASTP on localhost without submitting to cluster scheduler.

### SGE cluster submission
**Args:** `hpc-blast -sge blastx -query transcripts.fasta -db nr -out results.txt`
**Explanation:** Submits parallel BLASTX jobs to Sun Grid Engine cluster.

### Custom chunk size
**Args:** `hpc-blast -cs 1000 blastn -query large_input.fasta -db ref_db -out results.txt`
**Explanation:** Sets custom chunk size of 1000 sequences per parallel job.
---
name: rop
category: utility
description: Read Origin Protocol (ROP) — discovers the genomic source of every read in a sequencing library, including reads from repeat regions, recombinant BCR/TCR loci, and microbial communities, via a k-mer-based voting scheme.
tags: ["rop", "read-origin", "repeat", "bcr", "tcr", "microbiome", "k-mer"]
author: oxo-call-community
source_url: "https://github.com/smangul1/rop"
---

## Concepts

- **Tool Overview**: ROP (v1.1.2, Mangul / USC) is a computational protocol for discovering the genomic source of every read in a sequencing library. It is specifically designed to handle reads that other mappers discard: reads from repetitive regions, reads from recombinant BCR/TCR loci (which do not match a single V/D/J segment in the reference), and reads from microbial communities.
- **Core Function**: Takes a set of sequencing reads (FASTQ) and a reference (or references — genome + microbiome + BCR/TCR loci) and reports, for each read, its likely source(s) with a confidence score. The output is a per-read TSV that can be summarized into a per-sample or per-source count matrix.
- **Algorithm**: A k-mer-based voting scheme: (1) build a k-mer index of all references; (2) for each read, count the k-mers per reference; (3) assign the read to the reference with the most k-mers (breaking ties by edit distance). Reads with no clear winner are flagged as "ambiguous" or "novel". The default k is 25.
- **Input Format**: A FASTQ file (single or paired) and a FASTA reference (single or multi-FASTA, e.g., concatenated genome + microbiome + BCR/TCR references). The reference is typically the union of all expected sources. BCR/TCR references must be V/D/J segment databases (e.g., IMGT).
- **Output Format**: A TSV with one row per read: `read_id, source_ref, source_position, num_kmers, confidence, ambiguous`. The `ambiguous` column is `TRUE` for reads with no clear winner. Optional `-o` for a per-sample summary.
- **Use Case**: Estimating the fraction of reads from a host vs. a microbiome in a metagenomic dataset, quantifying BCR/TCR clonal expansion in a scRNA-Seq dataset (reads that don't match the reference V(D)J are often chimeric), recovering reads from repetitive regions that a standard mapper discards, and QC-ing a sequencing library for cross-contamination.

## Pitfalls

- **CRITICAL — The reference must be a UNION of all expected sources**: A reference that omits a source produces reads assigned to "ambiguous" (e.g., a metagenomic read from an unsequenced bacterium). Pre-build the reference with `cat host.fa microbiome.fa bcr_ref.fa > combined_ref.fa`.
- **CRITICAL — The k-mer index is built ONCE per reference and is sensitive to k-mer size**: The default k=25 is good for genomes but loses signal for short repeats. For BCR/TCR CDR3 analysis, use k=15; for microbial reads, use k=21.
- **The voting scheme is not probabilistic**: ROP uses a simple majority-vote; a read with 10 k-mers in source A and 9 in source B is assigned to A, with confidence = 10/19. For Bayesian source assignment, use `Kraken2` or `mash` instead.
- **Tied votes are broken arbitrarily**: Reads with the same number of k-mers in two sources are assigned to the first source in the reference order. The reference order matters; re-order or use a tie-breaker (e.g., `-t unique`) for better behavior.
- **No chimera detection**: ROP assigns each read to a single source. Chimeric reads (e.g., a BCR read spanning V and J segments from different alleles) are mis-assigned. For chimera detection, use `IGBLAST` or `MiXCR`.
- **Memory scales with reference size**: A 10 Gbp reference uses ~10 GB of RAM. For very large references, use a chunked reference or pre-compute the k-mer index with `jellyfish`.

## Examples

### Basic read-origin assignment
**Args:** `rop -i reads.fastq -r reference.fa -o origins.tsv`
**Explanation:** `-i` is the input FASTQ, `-r` is the reference FASTA, `-o` is the output TSV. The output has one row per read (`read_id, source_ref, source_position, num_kmers, confidence, ambiguous`).

### Paired-end reads
**Args:** `rop -i reads_1.fastq -I reads_2.fastq -r reference.fa -o origins.tsv`
**Explanation:** `-I` is the second mate of paired-end reads. ROP processes both mates independently and writes two rows per pair (or one row per pair with `-p paired`).

### Build a union reference (host + microbiome + BCR/TCR)
**Args:** `cat human.fa microbiome.fa bcr_vdj.fa > combined.fa && rop -i reads.fastq -r combined.fa -o origins.tsv`
**Explanation:** Composite: build a combined reference FASTA and pass to ROP. The output has per-read source assignments across all three classes. Useful for analyzing a 10x Genomics 5' scRNA-Seq dataset with BCR enrichment.

### Specify k-mer size
**Args:** `rop -i reads.fastq -r reference.fa -k 15 -o origins.tsv`
**Explanation:** `-k 15` reduces the k-mer size to 15, suitable for short CDR3 regions in BCR/TCR analysis. For typical genomes, keep the default 25.

### Use a pre-built jellyfish k-mer index
**Args:** `jellyfish count -m 25 -s 1G -t 8 -o ref_kmer.jf reference.fa && rop --load-jf ref_kmer.jf -i reads.fastq -o origins.tsv`
**Explanation:** `--load-jf` loads a pre-built Jellyfish k-mer index, avoiding a re-count for each ROP run. Useful for iterating on a large reference.

### Filter to high-confidence assignments
**Args:** `rop -i reads.fastq -r reference.fa -o origins.tsv && awk -F'\t' '$5 > 0.95' origins.tsv > high_conf.tsv`
**Explanation:** Composite: run ROP, then filter to reads with confidence > 0.95. The `confidence` column is the fraction of the read's k-mers that support the assigned source.

### Summarize per-source counts
**Args:** `rop -i reads.fastq -r reference.fa -o origins.tsv --summary per_source.tsv`
**Explanation:** `--summary` writes a per-source count matrix (`source<TAB>num_reads<TAB>num_high_confidence_reads`). Useful for a quick QC of the library composition.

---
name: rnalien
category: utility
description: Unsupervised pipeline that builds a covariance model (CM) for an RNA family starting from a single input sequence, using BLAST, RNAz, LocARNA, and Infernal.
tags: ["rnalien", "rna-family", "covariance-model", "infernal", "rna-blast", "rna-secondary-structure"]
author: oxo-call-community
source_url: "http://rna.tbi.univie.ac.at/rnalien/tool"
---

## Concepts

- **Tool Overview**: RNAlien (v1.8.0, Vienna TBI) is an unsupervised pipeline for building a covariance model (CM) of an RNA family starting from a single representative sequence. It integrates BLAST, RNAz (for structural-conservation filtering), LocARNA (for sequence-structure alignment), and Infernal's `cmbuild` to produce a ready-to-use CM in a fully automated fashion.
- **Core Function**: Given one query sequence and a sequence database (e.g., a bacterial genome collection or a transcriptomic contig set), RNAlien finds homologous sequences, filters for structural conservation, aligns them, and emits a CM that can be used with `cmsearch` to find additional family members. This automates what is usually weeks of manual work.
- **Algorithm**: Four-stage pipeline: (1) BLAST (`blastn` or `psiblast`) is used to find candidate homologs in a user-supplied database; (2) candidate sequences are filtered by `RNAz` to retain only those that show significant structural conservation relative to the query; (3) the filtered set is aligned with `LocARNA` (sequence-structure alignment) to produce a Stockholm-format alignment; (4) `cmbuild` (Infernal) converts the alignment into a CM. Optionally, a `cmcalibrate` step is run to fit the CM's E-value statistics.
- **Input Format**: A single query sequence in FASTA format plus a sequence database to search (multi-FASTA of candidate homologs, e.g., RefSeq bacterial proteins translated to nucleotides via `transeq --table 11`, or a set of bacterial genomes concatenated into a single FASTA). A BLAST database built from the same FASTA is required.
- **Output Format**: A directory containing: the BLAST hits (raw and filtered), the LocARNA alignment in Stockholm format, the inferred secondary structure in dot-bracket notation, the final `.cm` file (Infernal covariance model), and a summary log. The `.cm` is ready to use with `cmsearch`.
- **Use Case**: Building a custom RNA family model for an experimentally validated ncRNA (e.g., a putative small regulatory RNA in a new bacterial species), creating a profile to scan a large metagenomic database for that family's members, and rebuilding Rfam-style models for poorly annotated clades.

## Pitfalls

- **CRITICAL — `rnalien` is a wrapper; the underlying tools must be installed**: BLAST+, ViennaRNA (RNAfold/RNAz), LocARNA, and Infernal must all be on PATH; the Bioconda recipe `rnalien` pulls in most of them but LocARNA sometimes needs a separate `conda install -c bioconda locarna`. Verify with `RNAz --version` and `cmbuild -h` before running a large database scan.
- **CRITICAL — Input sequence must be a real RNA (not a gene)**: RNAlien assumes the input is a mature, structural ncRNA. Giving it a coding sequence (CDS) or a genomic window larger than a few hundred nucleotides will produce a CM that does not match anything meaningful, or that matches spurious conserved stems. Trim to the mature RNA boundaries first.
- **The BLAST E-value threshold determines sensitivity vs precision**: The default E-value (1e-3) is permissive; for divergent families use 1e-2 and for very conserved ones (tRNA) use 1e-10. The downstream `RNAz` filter is the second line of defense, so a permissive BLAST is acceptable.
- **`RNAz` requires at least 3 aligned sequences to score structural conservation**: If the input family has only 1 or 2 close homologs, RNAlien will emit a CM from the LocARNA alignment directly, skipping the `RNAz` step. Such CMs are not statistically calibrated and should be `cmcalibrate`d manually with `cmcalibrate --mpi <cm_file>`.
- **Memory can grow with database size**: For a 50 GB RefSeq nucleotide database, RNAlien needs ≥ 16 GB of RAM and ~2 hours of wall time. For very large databases, split with `seqkit split` and run RNAlien on each chunk in parallel via a Snakemake/Nextflow pipeline.
- **The LocARNA alignment may be missing columns in divergent families**: Very divergent families (e.g., RNase P, tmRNA) have alignments where LocARNA cannot confidently place all columns; the resulting CM will have a lot of insert states and may produce false-positive `cmsearch` hits. Always validate the resulting CM with `cmsearch --tblout hits.tbl <cm> test.fa` on a known positive control sequence.

## Examples

### Basic RNAlien run
**Args:** `rnalien -q query.fa -d candidates.fa -o alien_run/`
**Explanation:** `-q` is the single query FASTA, `-d` is the candidate-sequence database, `-o` is the output directory. The script will build a temporary BLAST database, run the pipeline, and place the final CM in `alien_run/final.cm`.

### Use a precomputed BLAST database
**Args:** `makeblastdb -in candidates.fa -dbtype nucl -out cand_db && rnalien -q query.fa -db cand_db -o alien_run/`
**Explanation:** Building the BLAST DB explicitly with `makeblastdb` is faster for repeated runs and lets you reuse the same database across multiple RNAlien queries (one per family of interest). `-db` accepts the database path/prefix.

### Tighten the BLAST E-value threshold
**Args:** `rnalien -q query.fa -d candidates.fa -o alien_run/ -e 1e-10`
**Explanation:** `-e 1e-10` (also `--evalue`) tightens the BLAST E-value cutoff to 1e-10, retaining only close homologs. Recommended for conserved families (tRNA, rRNA, snoRNA) where the goal is a high-precision CM, not a divergent one.

### Skip the LocARNA step (use BLAST-derived alignment)
**Args:** `rnalien -q query.fa -d candidates.fa -o alien_run/ --skip-locarna`
**Explanation:** `--skip-locarna` falls back to a plain multiple alignment (via MAFFT) of the BLAST hits, skipping the sequence-structure-aware LocARNA step. Faster, but the resulting CM has lower structural discrimination; only use this for very short or very conserved RNAs.

### Calibrate the resulting CM for E-value accuracy
**Args:** `cmcalibrate alien_run/final.cm`
**Explanation:** After RNAlien finishes, `cmcalibrate` fits the CM's E-value distribution by sampling random sequence space. Required for `cmsearch` to return accurate E-values; runs in O(hours) on large CMs but is the difference between a CM that "looks right" and one that is quantitative.

### Search a metagenome with the built CM
**Args:** `cmsearch --tblout hits.tbl -E 1e-5 alien_run/final.cm metagenome.fa > cmsearch.out`
**Explanation:** Standard Infernal usage: `-E 1e-5` filters hits to E-value ≤ 1e-5; `--tblout` writes a tabular summary. This is the standard follow-up to RNAlien for scanning large metagenomic contigs.

### Run RNAlien on multiple families in a loop
**Args:** `for q in queries/*.fa; do name=$(basename "$q" .fa); rnalien -q "$q" -d candidates.fa -o "alien_runs/$name/"; done`
**Explanation:** Shell snippet to process many query sequences in series; one RNAlien run per query, with parallelization handled by an outer `xargs -P` or GNU parallel if desired. Each family produces its own CM in `alien_runs/<name>/`.

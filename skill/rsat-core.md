---
name: rsat-core
category: utility
description: "RSAT (Regulatory Sequence Analysis Tools) core — a suite of ~50 command-line programs for analyzing cis-regulatory elements in non-coding sequences: motif discovery, scanning, clustering, quality assessment, comparative genomics, and regulatory variation analysis."
tags: ["rsat", "rsat-core", "regulatory-sequence-analysis", "motif-discovery", "chip-seq", "transcription-factor", "non-coding", "promoter-analysis"]
author: oxo-call-community
source_url: "https://rsat.eu/"
---
## Concepts

- **Tool Overview**: RSAT-core (Regulatory Sequence Analysis Tools, v2025.04.04, van Helden et al.) is a suite of ~50 command-line programs for analyzing cis-regulatory elements in non-coding sequences. It supports motif discovery (including genome-wide data sets like ChIP-seq), transcription-factor binding motif analysis (quality, comparisons, clustering), comparative genomics, and the analysis of regulatory variations (rSNPs, indels). Available via conda (bioconda), Docker, Apptainer, and as a web server at https://rsat.eu/.
- **Core Function**: RSAT provides individual programs for each task. The most-used programs include: `retrieve-seq` (fetch upstream/downstream sequences of genes), `oligo-analysis` (count words and detect over-represented oligonucleotides), `dyad-analysis` (detect spaced word pairs), `dna-pattern` (match a single pattern or a set of patterns), `matrix-scan` (scan sequences with a PSSM), `matrix-clustering` (cluster PSSMs), `convert-matrix` (convert between matrix formats), `consensus` (derive a consensus from aligned instances), `patser` (scan with a PSSM, returns p-values), `peak-motifs` (complete ChIP-seq motif discovery pipeline), and `snp-sites` (extract variation in regulatory regions).
- **Algorithm**: Each program implements a specific algorithm. `oligo-analysis` uses a Markov-chain background model (default 1st order). `matrix-scan` uses a PSSM with a user-specified background model (Bernoulli or Markov). `peak-motifs` is a complete pipeline that calls several RSAT programs in series: sequence retrieval, word counting, motif discovery, motif comparison, motif enrichment, and motif-to-PSSM conversion.
- **Input Format**: Programs accept FASTA, tab-delimited gene lists, BED, GFF, GTF, custom RSAT formats, and matrix formats (TRANSFAC, MEME, JASPAR). Several programs require an organism-specific genome and annotation; RSAT provides pre-built annotations for >110 organisms.
- **Output Format**: Each program writes its own output: tab-delimited tables, GFF, BED, MEME motifs, TRANSFAC matrices, HTML, or PDF. The `peak-motifs` pipeline writes a comprehensive HTML report.
- **Use Case**: ChIP-seq motif discovery (canonical use case for `peak-motifs`), promoter analysis of a set of co-regulated genes, comparing motifs across multiple ChIP-seq experiments, scanning a genome for matches to a PSSM, detecting over- or under-represented words in a set of sequences, and clustering a collection of PSSMs from different sources.

## Pitfalls

- **CRITICAL — The RSAT environment must be configured before use**: After `conda install rsat-core`, run `rsat-config` (or set `$RSAT` and `$PATH` manually) to point to the installed RSAT directory. Without configuration, most programs fail with "RSAT not configured".
- **CRITICAL — The package does NOT include genome sequences nor DNA motif collections**: Download the organism-specific data via `rsat-download-data` or from the RSAT website. The motif collections (JASPAR, etc.) and the genome sequences must be downloaded separately.
- **CRITICAL — `peak-motifs` requires a ChIP-seq peak file (BED) and the matching genome**: The peak file is typically from MACS2 or another peak caller; the genome is the organism-specific FASTA. Without both, the pipeline aborts.
- **`oligo-analysis` word counts are sensitive to the background model**: A 0th-order (Bernoulli) background model is the default; a 1st-order Markov model is more accurate for vertebrate genomes. Select with `-markov` (e.g., `-markov 1`).
- **`matrix-scan` can be slow on large genomes**: A PSSM of length 20 on a 3 Gb genome takes ~10 minutes. Use a smaller PSSM (length 6–10) or restrict to a subset of chromosomes with `-seq`.
- **`peak-motifs` is a COMPLETE pipeline, not a single tool**: It runs ~10 RSAT programs in series. The full pipeline takes 30–60 minutes for a typical ChIP-seq dataset. Use `rsat-launch` to run it.
- **The web interface is the recommended entry point for new users**: https://rsat.eu/ provides a UI for most programs. The command-line interface is for power users and pipeline integration.
- **`dyad-analysis` is computationally expensive on long words**: A word length of 6 produces 4^6 = 4096 dyad combinations; length 8 produces 65,536. Use a length of 4–6 for most promoter analyses.

## Examples

### Retrieve upstream sequences of a gene list
**Args:** `retrieve-seq -org Saccharomyces_cerevisiae -gene list.txt -up 1000 -down 0 -type upstream -out upstream_seqs.fa`
**Explanation:** `-org` selects the organism, `-gene` is the gene list, `-up` and `-down` define the upstream/downstream range, `-type upstream` fetches only the upstream region, `-out` is the output FASTA. Requires the organism to be installed via `rsat-download-data`.

### Count over-represented words in upstream sequences
**Args:** `oligo-analysis -i upstream_seqs.fa -l 6 -markov 1 -sort -out oligo_results.tab`
**Explanation:** `-i` is the input FASTA, `-l 6` is the word length, `-markov 1` uses a 1st-order background model, `-sort` sorts by significance, `-out` is the output table. Returns a ranked list of over-represented 6-mers.

### Detect spaced word pairs (dyads)
**Args:** `dyad-analysis -i upstream_seqs.fa -l 3 -sp 5-50 -markov 1 -sort -out dyad_results.tab`
**Explanation:** `-l 3` is the word length, `-sp 5-50` is the spacing range between the two words. Detects over-represented spaced word pairs, a common motif in eukaryotic promoters.

### Scan a genome with a PSSM
**Args:** `matrix-scan -m jaspar.pfm -i genome.fa -bg bg_markov1.tab -out matrix_scan.gff -format gff`
**Explanation:** `-m` is the PSSM (TRANSFAC or MEME format), `-i` is the genome FASTA, `-bg` is the background model (1st-order Markov), `-out` is the output GFF. Each PSSM hit is a GFF record.

### Run the ChIP-seq motif discovery pipeline
**Args:** `rsat-launch peak-motifs -v 1 -i peaks.bed -t atac -org Homo_sapiens -mask repeats -out peak_motifs_report/`
**Explanation:** `-v 1` is verbose, `-i` is the ChIP-seq peak BED, `-t atac` is the peak type (alternatives: `narrow`, `broad`), `-org` is the organism, `-mask repeats` masks repetitive regions, `-out` is the output directory. The full pipeline takes 30–60 minutes and writes an HTML report.

### Cluster a collection of PSSMs
**Args:** `matrix-clustering -hierarchy -i matrices.tf -out matrix_tree.png -format png`
**Explanation:** `-hierarchy` is the hierarchical clustering method, `-i` is the input matrix collection (TRANSFAC format), `-out` is the output tree. Useful for comparing motifs from different sources.

### Compare two PSSMs
**Args:** `compare-matrices -m1 maxtf.pfm -m2 tfsiiia.pfm -out compare.tab`
**Explanation:** `compare-matrices` computes a similarity score (Pearson correlation, Sandelin-Wasserman, or Kullback-Leibler) between two PSSMs. Returns a single score and a per-column alignment.

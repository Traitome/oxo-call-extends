---
name: rnabob
category: utility
description: fast RNA secondary structure motif search tool using descriptor-based pattern matching
tags: ["rnabob", "rna", "motif-search", "secondary-structure", "utility"]
author: oxo-call-community
source_url: "https://github.com/bioconda/bioconda-recipes/tree/master/recipes/rnabob"
---

## Concepts

- **Tool Overview**: RNAbob (unpublished, S.R. Eddy) is a fast RNA secondary structure motif searcher that scans sequence databases for RNAs capable of adopting a user-defined secondary structure. It is the predecessor to `rnamotif` and `rnabob` focuses on speed and a compact descriptor language.
- **Core Function**: Matches a structural "descriptor" (a small pattern language for stems, loops, bulges, mismatches) against FASTA-formatted sequences, optionally applying scoring rules based on nearest-neighbor thermodynamic parameters.
- **Algorithm**: Uses descriptor-based pattern matching with a backtracking engine; large descriptor sets can be preprocessed with `rmprune` (from the `rnamotif` suite) to remove equivalent sub-descriptors and speed up the search.
- **Input Format**: Two required inputs — a FASTA-formatted sequence file (the database to be searched) and a descriptor file (a small text file that defines the structural motif). Common companion tools: `rmprune` to reduce descriptor redundancy, `rmfmt` to format hits, `rm2ct` to convert to CT format.
- **Output Format**: Text report written to stdout (or a redirected file) with one block per hit listing the sequence ID, hit start–end positions, the descriptor instance that matched, and (optionally) a score. Default score is 0; include scoring rules in the descriptor to enable non-trivial scores.
- **Use Case**: Discovery of structural motifs (tRNA, hairpins, GNRA tetraloops, kink-turns) in genome-scale RNA sequence databases such as bacterial or organellar genomes, or large transcriptomic contigs.

## Pitfalls

- **CRITICAL — Unstranded descriptor assumption**: A descriptor such as `s5` means a stem of length 5; RNAbob does **not** automatically search the reverse complement. To find motifs on both strands you must pre-reverse-complement the input or run RNAbob twice and merge results.
- **CRITICAL — Output goes to stdout**: By default the full hit report is printed to stdout; if you forget to redirect (`rnabob descr input.fa > hits.txt`) the program can appear to "hang" in a shell. Always use `> hits.txt 2> err.log` to separate diagnostics from hits.
- **Score is zero by default**: A hit with `score = 0` is not "low quality" — it just means no `s` (score) rules were defined. Don't filter results by score unless you have authored a scoring section in the descriptor.
- **No FASTA index required, but sequence length matters**: RNAbob loads the entire FASTA into memory and is single-threaded; multi-GB metagenome files can be slow. Pre-splitting the FASTA by contig with `seqkit split` is often the easiest speed-up.
- **Descriptor syntax is unforgiving**: A single unclosed parenthesis or missing `:` delimiter will silently match nothing. Always test a small known-positive sequence first (`rnabob descr known_pos.fa`) and confirm at least one hit before scaling up.
- **Version 2.2.1 is the last bioconda release**: No further updates are planned upstream; for new features (better scoring, more flexible mismatches) use `rnamotif` from the same authors instead.

## Examples

### Basic motif search
**Args:** `rnabob hairpin.descr sequences.fa > hits.txt`
**Explanation:** `hairpin.descr` is a descriptor that defines a hairpin of stem-length 5 with a 4-nt loop; `sequences.fa` is the FASTA database to scan; the `> hits.txt` redirect captures the hit report (stdout) into a file.

### Search both strands by reverse-complementing
**Args:** `rnabob hairpin.descr seq_rc.fa >> hits.txt && cat hits.txt | sort -u > hits.uniq.txt`
**Explanation:** `seq_rc.fa` is the reverse-complement of the input (e.g., produced by `seqkit seq -r -p -t dna`); appending (`>>`) concatenates the strand-flipped results; `sort -u` deduplicates identical hits because reverse-complement searches can recover palindromic motifs twice.

### Search with a known-positive control
**Args:** `rnabob trna.descr positive.fa`
**Explanation:** Always test a small known-positive FASTA first; the absence of any hit indicates a syntax error in the descriptor or a mis-specified stem length.

### Pre-prune a large descriptor set
**Args:** `rmprune large_set.descr pruned.descr && rnabob pruned.descr sequences.fa > hits.txt`
**Explanation:** `rmprune` (shipped with the `rnamotif` bioconda package, not `rnabob` directly) collapses equivalent descriptors to reduce search time; useful when the descriptor set has many overlapping stem/loop definitions.

### Convert hits to CT (dot-bracket-like) format
**Args:** `rnabob trna.descr seq.fa > hits.rmfmt && rm2ct hits.rmfmt > hits.ct`
**Explanation:** `rm2ct` (also from the `rnamotif` package) parses RNAbob's output and produces a `connect` table (CT) file suitable for downstream secondary-structure visualization with `VARNA` or `RNAplot`.

### Show descriptor help
**Args:** `rnabob --help`
**Explanation:** Prints the full list of command-line flags (`-descr`, `-xdescr`, `-Idir` for descriptor include directories, etc.) and a one-line description of each; useful when adapting an old descriptor to a new search.

### Score-ranked motif search
**Args:** `rnabob -s scoring.descr trna_with_score.descr seq.fa | sort -k7,7nr | head`
**Explanation:** When scoring rules (`s` lines) are embedded in the descriptor, RNAbob emits a numeric score per hit; piping through `sort -k7,7nr` ranks by descending score and `head` keeps only the top hits.

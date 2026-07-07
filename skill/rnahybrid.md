---
name: rnahybrid
category: utility
description: Find the minimum free-energy (MFE) hybridization between a long RNA target and a short RNA query; the canonical tool for miRNA target prediction in plants and the seed-matched miRNA-mRNA duplex model.
tags: ["rnahybrid", "mirna", "target-prediction", "mfe", "duplex", "utr"]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/rnahybrid"
---

## Concepts

- **Tool Overview**: RNAhybrid (v2.1.2, Bielefeld / Marcus et al. 2004) is a tool for computing the minimum free-energy (MFE) hybridization between a long target RNA and a short query RNA. It implements the classic miRNA-mRNA seed-match model with the MFE derived from the nearest-neighbor thermodynamic parameters of RNAcofold. It is the de-facto miRNA target predictor for plant studies and is also used to scan viral genomes for miRNA-like regulators.
- **Core Function**: Takes two FASTA inputs — a long target (e.g., 3' UTR) and a short query (e.g., mature miRNA, 18–25 nt) — and reports the energetically best hybridization(s) of the query to the target. The energy model forbids internal loops in the query (the "no bulge" constraint), making it ideal for short, stiff queries like miRNAs.
- **Algorithm**: O(target_length × query_length) dynamic programming on a restricted energy model (ViennaRNA energy parameters, no query-side bulges). An empirical p-value is reported for each hit, based on a precomputed distribution of MFE values for random query/target pairs with matching dinucleotide composition.
- **Input Format**: Two FASTA files: `-t targets.fa` (long sequences, e.g., 3' UTRs) and `-q queries.fa` (short sequences, e.g., mature miRNAs). Multi-FASTA inputs are supported; each query is tested against every target. Sequence names are echoed in the output for downstream parsing.
- **Output Format**: Plain-text report with one block per hit containing: query name, target name, target position, hybridization alignment, MFE in kcal/mol, and p-value. The output is line-based and easily parsed with `awk`/`grep`; alternative tabular outputs exist via `--tsv`.
- **Use Case**: miRNA target prediction in plants (where seed matching alone is insufficient and MFE adds specificity), viral genome scans for host miRNA binding sites, siRNA off-target prediction in RNAi design, and validation of experimentally identified miRNA-mRNA pairs.

## Pitfalls

- **CRITICAL — Query and target FASTA roles are NOT symmetric**: `-q` is the SHORT sequence (miRNA), `-t` is the LONG sequence (mRNA). Swapping them does not crash but gives nonsensical MFE values (long-query with a long target is computationally tractable but energetically wrong). Double-check with `awk '/^>/{print}' queries.fa | wc -l` and confirm the queries are short.
- **CRITICAL — No seed constraint by default**: RNAhybrid reports the MFE duplex regardless of seed complementarity. miRNA predictions should be filtered to retain only hits with a strong seed (positions 2–8 of the miRNA paired to the target). Pipe through `awk '$0 ~ /^>/ {hdr=$0; next} {print hdr"\t"$0}'` and then a seed filter.
- **Energy cutoff is in negative kcal/mol**: `-e -25` is a strong cutoff (highly stable); `-e -15` is permissive. Choose based on the length of the query (longer miRNAs naturally have lower MFE).
- **`-p 0.05` does not filter by default — it sets the p-value display threshold**: Output is sorted by p-value, and the top `-n` hits are kept (set by `-n`, default 100). Combine `-e` and `-p` for stricter filtering, but the canonical workflow is to filter on MFE first and p-value second.
- **No G-U wobble penalties differ from ViennaRNA**: RNAhybrid uses a slightly older energy parameter set; MFE values may differ by ±0.5 kcal/mol from RNAfold/RNAcofold. This is rarely a problem in practice but matters when comparing RNAhybrid scores to RNAfold/RNAcofold scores in the same publication.
- **Viral/structured targets need `--noLP` and `--noLonelyPairs`**: A long target with strong internal structure (e.g., a viral 5' UTR) can hide seed sites in base-paired regions; passing `--noLP` opens up those positions and may reveal biologically relevant sites.

## Examples

### Basic miRNA target prediction
**Args:** `RNAhybrid -t mRNA.fa -q miRNA.fa -e -25 -p 10 > results.txt`
**Explanation:** `-t mRNA.fa` is the target mRNA (or UTR) FASTA, `-q miRNA.fa` is the miRNA FASTA, `-e -25` sets an MFE cutoff of -25 kcal/mol, `-p 10` displays the top 10 hits. Output `results.txt` lists each hit with its alignment, MFE, and p-value.

### Filter by p-value
**Args:** `RNAhybrid -t mRNA.fa -q miRNA.fa -e -20 -p 0.05 > significant_hits.txt`
**Explanation:** `-p 0.05` displays only hits with empirical p-value ≤ 0.05; combines with `-e -20` for a moderate-stringency filter. Suitable for first-pass plant miRNA target scans.

### Restrict hits to a single perfect seed
**Args:** `RNAhybrid -t mRNA.fa -q miRNA.fa -e -20 -s 3utr_human -u 6 -a 8 -m 2000 -p 100 > seed_matches.txt`
**Explanation:** `-u 6 -a 8` defines a 6-nt perfect match starting at position 8 of the miRNA; `-m 2000` is the maximum target length considered. Useful when validating predicted miRNA-mRNA pairs against a strict canonical seed model.

### Force target on the plus strand
**Args:** `RNAhybrid -t mRNA.fa -q miRNA.fa -e -20 --tsv > plus_strand.tsv`
**Explanation:** `--tsv` outputs the results in a tab-separated table (query, target, position, energy, p-value) instead of the default pretty-printed alignment blocks. Easy to ingest into R or pandas.

### Search very long viral genomes
**Args:** `RNAhybrid -t sars_cov_2_genome.fa -q human_mirna.fa -e -25 -p 5 --noLP > viral_hits.txt`
**Explanation:** `--noLP` disables lonely-pair penalties (relevant for highly structured viral RNA), `-p 5` keeps the top 5 hits per query. Use this pattern for screening viral genomes for host miRNA binding sites.

### Process many target FASTA files
**Args:** `for t in 3utrs/*.fa; do RNAhybrid -t "$t" -q mirna.fa -e -20 -p 1; done > all_hits.txt`
**Explanation:** Simple shell loop that calls RNAhybrid once per target FASTA file and concatenates the results; this is faster than concatenating the targets into a single multi-FASTA because the output is per-file and easier to debug.

### miRNA-mRNA validation with constraint on seed
**Args:** `RNAhybrid -t validated_targets.fa -q mir-21.fa -e -20 -c > mir21_hits.txt`
**Explanation:** `-c` enables constraints on the alignment (e.g., forcing perfect Watson-Crick at positions 2–7 of the miRNA, the canonical seed). Use this when validating experimentally supported miRNA-target pairs from CLASH or AGO-CLIP data.

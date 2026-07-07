---
name: rnacode
category: utility
description: Scan a multiple sequence alignment for evolutionary signatures of protein-coding regions (synonymous/conservative mutations, reading-frame conservation) without species-specific models.
tags: ["rnacode", "coding-potential", "msa", "reading-frame", "synonymous-mutations"]
author: oxo-call-community
source_url: "https://viennarna.github.io/RNAcode"
---

## Concepts

- **Tool Overview**: RNAcode (v0.3.1, part of the ViennaRNA package family) scans a multiple sequence alignment (MSA) for regions whose evolutionary signature is consistent with protein coding. Unlike CPC, CPAT, or Pfam-based methods, RNAcode does not depend on species-specific training data and does not use machine learning; it works on raw evolutionary signals.
- **Core Function**: Detects reading-frame conservation and synonymous-vs-replacement substitution biases along a nucleotide alignment. The output is a list of candidate coding regions with p-values, suitable for ncRNA vs mRNA discrimination in transcriptomic assemblies.
- **Algorithm**: For every reading frame in every column of the input alignment, RNAcode evaluates (a) whether substitutions are mostly synonymous given the implied amino acid, (b) whether the reading frame is preserved across most sequences, and (c) whether the substitution pattern resembles a protein-like amino-acid substitution matrix. These scores are combined and compared against a randomized background to produce p-values.
- **Input Format**: A multiple sequence alignment in ClustalW (`.aln`) or FASTA-aligned (`.fa`, `.fasta`) format. At least 3 sequences are required; the more the better (≥10 recommended). The alignment must be a true MSA — sequences of the same length with gaps in corresponding positions — not a multi-FASTA of unaligned sequences.
- **Output Format**: Plain-text table written to stdout, with one row per reported region: start, end, frame, p-value, score, and a brief description. Suitable for direct piping into `awk` / `grep` for filtering. A machine-readable `-o` JSON output exists in newer ViennaRNA versions.
- **Use Case**: Identifying protein-coding exons inside long non-coding RNA candidates, validating de novo transcript annotations (e.g., from StringTie), or confirming that a putative ORF in a viral genome is real. RNAcode is one of the few tools that can detect short ORFs (<100 aa) in poorly annotated species.

## Pitfalls

- **CRITICAL — Input must be a real multiple alignment, not a multi-FASTA**: If sequences are unaligned (different lengths, no gap columns), RNAcode either crashes or produces nonsense p-values. Always run `MAFFT`, `Clustal Omega`, or `MUSCLE` first and use the aligned output.
- **CRITICAL — At least 3 sequences required, ≥ 10 strongly recommended**: With 3 sequences the p-value estimates are extremely noisy; the manual explicitly states that anything below 5 sequences is unreliable. For statistical power, use 10+ sequences.
- **Reading-frame inference is not free**: If the input alignment contains a frameshift (lengths that are not multiples of 3 in a coding region), RNAcode will report multiple low-scoring frames. Pre-screen with `cdhit` or remove clear pseudogenes from the input.
- **No strand information used**: RNAcode scans the plus strand only by default. To check the reverse complement, build the alignment on `seqkit seq -r -p` reverse-complemented sequences.
- **Cannot distinguish coding from conserved ncRNA structure**: A region that is highly conserved but not coding (e.g., a ribosomal RNA helix) may score as a false positive. Combine with `RNAz` or `Infernal` cmsearch results to filter structural conservation.
- **Output columns are space-separated, not tab-separated**: Direct piping into CSV parsers can fail. Convert with `column -t` or `tr ' ' '\t'` before downstream processing.

## Examples

### Basic coding-potential scan
**Args:** `RNAcode alignment.aln > coding_regions.txt`
**Explanation:** Reads the ClustalW or aligned FASTA file `alignment.aln`, scans all six reading frames, and writes a space-separated table of significant coding regions to `coding_regions.txt`. Default parameters (--cutoff 1e-5) are appropriate for eukaryotic alignments of 5+ sequences.

### Filter output by p-value
**Args:** `RNAcode --cutoff 0.01 alignment.aln > significant_coding.txt`
**Explanation:** `--cutoff 0.01` raises the p-value threshold from the strict 1e-5 default to 0.01, increasing recall. Recommended when the input has fewer than 10 sequences (where 1e-5 is too conservative) or when validating borderline ORFs.

### Restrict to a specific reading frame
**Args:** `RNAcode --frame 1 alignment.aln > frame1_hits.txt`
**Explanation:** `--frame 1` (+1 frame) limits the scan to a single reading frame; useful when the expected coding frame is known (e.g., from a UniProt homolog) and you want to test that frame specifically. Frames are 1-based: 1, 2, 3 for plus-strand, 4, 5, 6 for minus-strand.

### Disable the GC-content randomization
**Args:** `RNAcode --gc-content none alignment.aln > no_gc.txt`
**Explanation:** `--gc-content none` skips the GC-matched random background; the default behavior builds randomized alignments with the same GC content as the input. Use this flag when the input species has extreme GC bias (e.g., Mycobacterium) that confuses the default background model.

### Run on a FASTA-aligned input
**Args:** `RNAcode aligned.fa --gt-alignment 0.9 > high_identity.txt`
**Explanation:** `--gt-alignment 0.9` requires at least 90% of sequences to be present in any given column before it contributes to the score; reduces noise from alignments with many partial sequences (e.g., ESTs). The flag accepts any value in [0, 1].

### JSON output for downstream pipelines
**Args:** `RNAcode alignment.aln --format json > coding.json`
**Explanation:** `--format json` (ViennaRNA ≥ 2.6) writes a structured JSON document instead of the space-separated table, convenient for ingestion by Snakemake/Nextflow parsers. Each hit includes start, end, frame, score, p-value, and the underlying synonymous/replacement counts.

### Combine with a structural scan
**Args:** `( RNAcode alignment.aln | awk '$5 < 0.01 {print $0}'; RNAz --both-strands alignment.aln | awk '/^$/{} END{print "RNAz done"}' ) > combined.txt`
**Explanation:** Composite snippet: RNAcode hits with p-value < 0.01 are concatenated with an RNAz scan; the difference in output (coding regions vs structurally conserved regions) makes it easy to spot conflicts — a region that is both coding AND structurally conserved is a strong candidate for a structured mRNA element.

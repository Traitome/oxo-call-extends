---
name: rnabridge-align
category: alignment
description: bridge paired-end RNA-seq alignments into full fragment alignments (BAM in / BAM out)
tags: ["rnabridge-align", "rna-seq", "alignment", "splicing", "bridge"]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/rnabridge-align"
---

## Concepts

- **Tool Overview**: rnabridge-align (Shao-group, v1.0.1) constructs the alignment of an entire RNA-seq fragment given the alignments of its two paired-end mate reads. The output BAM contains the bridged fragment CIGAR (not just the two mate CIGARs), which improves downstream splice-aware quantification and visualization.
- **Core Function**: Given a coordinate-sorted BAM of paired-end RNA-seq alignments (TopHat2/STAR/HISAT2), it walks the splice graph for each fragment and emits a single consensus CIGAR + MD string representing the whole fragment, propagating splice junctions across the mate boundary.
- **Algorithm**: Dynamic programming over a splicing graph; candidates are ranked by a "bottleneck weight" (min_bridging_score) and the top-K (`--dp_solution_size`) candidate paths are kept. Splice junctions are propagated between mates, so a junction whose evidence is split across the two mates still appears in the bridged CIGAR.
- **Input/Output**: Input is a sorted BAM (`samtools sort` first). Output is a BAM with bridged alignments; the program does **not** require an indexed reference, but supplying a reference transcriptome GTF (`-r`) improves accuracy by giving the bridge a prior on known isoforms.
- **Library Type**: `--library_type` accepts `unstranded`, `first`, or `second` (mapping to Illumina's `fr-unstranded` / `fr-firststrand` / `fr-secondstrand`). If the input BAM was produced by STAR with `--outSAMstrandField intronMotif`, the program can infer it from the `XS` tag; use `--preview` to inspect the inference without running the full bridge.
- **Use Case**: Recovering splice junctions in RNA-seq libraries with long fragments (≥400 bp) or stranded protocols where conventional spliced aligners can underreport junctions that span the two mates; prerequisite for tools like `rMATS` and `MISO` when junction chaining is required.

## Pitfalls

- **CRITICAL — Input BAM MUST be sorted by coordinate**: rnabridge-align uses mate-coordinate lookups; an unsorted BAM will produce silently wrong bridges or out-of-order errors. Run `samtools sort -o input.sorted.bam input.bam` first.
- **CRITICAL — `--library_type` should be set explicitly**: When the input lacks the `XS` strand tag, the default `empty` value produces `unstranded` results that are wrong for dUTP (Illumina TruSeq stranded) libraries. Use `--preview` first; if `library_type` reads `unknown`, set it explicitly.
- **Reference GTF is optional but recommended**: Without `-r`, bridging is purely de-novo on the splice graph; with `-r reference.gtf`, known isoforms are scored higher. For novel-transcript discovery leave `-r` off; for well-annotated genomes (human/mouse/fly) always provide it.
- **`--min_bridging_score` defaults to 0.5**: Lower values accept noisier bridges (more junctions, more false positives); raise to 0.7+ for high-coverage data, lower to 0.3 for low-input libraries. The right value is dataset-specific — re-run with `--preview` and inspect the score histogram.
- **Memory and runtime scale with CIGAR length**: Reads whose mates together generate a CIGAR longer than `--max_num_cigar` (default 1000) are skipped; very long fragment libraries (e.g., 10x Genomics linked-reads) may need this raised.
- **Build dependencies (Boost + htslib ≥ 1.5)**: The source build requires Boost (headers only) and htslib compiled with `--disable-bz2 --disable-lzma --disable-gcs --disable-s3`; on most conda installs the bioconda package is the safer path because it bundles the right htslib.

## Examples

### Basic bridge
**Args:** `rnabridge-align -i aligned.sorted.bam -o bridged.bam`
**Explanation:** Reads the coordinate-sorted input BAM and writes a bridged BAM with one consensus CIGAR per fragment; library type is auto-inferred from the `XS` tag if present.

### Bridge with reference transcriptome
**Args:** `rnabridge-align -i aligned.sorted.bam -r gencode.v44.annotation.gtf -o bridged.bam`
**Explanation:** Provides a GTF of known isoforms so the bridge prefers junction chains matching annotated transcripts; strongly recommended for human/mouse and other well-annotated genomes.

### Preview the inferred library type
**Args:** `rnabridge-align --preview -i aligned.sorted.bam`
**Explanation:** Prints the inferred `library_type` and the fragment-length range observed in the input and exits without writing output; a quick sanity check before a full run.

### Set library type explicitly (stranded TruSeq)
**Args:** `rnabridge-align --library_type second -i aligned.sorted.bam -o bridged.bam`
**Explanation:** Forces `fr-secondstrand` (Illumina TruSeq stranded dUTP); required when the input BAM was produced by an aligner that does not emit the `XS` tag.

### Tighten bridging for high-coverage data
**Args:** `rnabridge-align --min_bridging_score 0.7 --dp_solution_size 5 -i in.bam -o out.bam`
**Explanation:** Raises the bottleneck-weight threshold to 0.7 to suppress marginal junctions, and caps the candidate path count at 5 to speed up the DP; useful on deeply sequenced libraries.

### Loosen bridging for low-input data
**Args:** `rnabridge-align --min_bridging_score 0.3 -i in.bam -o out.bam`
**Explanation:** Lowers the threshold to 0.3 to recover weak junctions; appropriate for low-coverage or degraded-RNA libraries, at the cost of more false-positive bridges.

### Show full parameter table
**Args:** `rnabridge-align --help`
**Explanation:** Lists every tunable (`--min_bridging_score`, `--dp_solution_size`, `--dp_stack_size`, `--max_clustring_flank`, `--flank_tiny_length`, `--flank_tiny_ratio`, `--min_splice_boundary_hits`, `--max_num_cigar`) with its default and one-line meaning.

### Sort input first (required precondition)
**Args:** `samtools sort -@ 4 -o aligned.sorted.bam aligned.bam && rnabridge-align -i aligned.sorted.bam -o bridged.bam`
**Explanation:** Always pre-sort; the `-@ 4` parallelizes the sort across 4 threads; without this, the bridge silently produces wrong results or aborts with a coordinate-order error.

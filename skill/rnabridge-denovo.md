---
name: rnabridge-denovo
category: assembly
description: reconstruct RNA-seq fragment sequences from paired-end reads via de Bruijn graph bridging
tags: ["rnabridge-denovo", "rna-seq", "assembly", "de-bruijn", "bridge"]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/rnabridge-denovo"
---

## Concepts

- **Tool Overview**: rnabridge-denovo (Shao-group, v1.0.1) is the *sequence* counterpart to rnabridge-align: given two paired-end FASTQ files, it returns the full fragment sequences in FASTA format by bridging the gap between the two reads over a de Bruijn graph (built with the Bifrost library).
- **Core Function**: Takes paired-end reads whose fragment length is greater than 2× read length (i.e., there is a "gap" of unsequenced bases between mate 1 and mate 2) and assembles the intervening sequence by finding a path through a colored de Bruijn graph.
- **Algorithm**: Builds a Bifrost-compacted de Bruijn graph of the input reads, then for each pair enumerates paths whose 5' end is anchored at the 3' end of read 1 and whose 3' end is anchored at the 5' end of read 2, emitting one FASTA record per bridged fragment.
- **Input/Output**: Positional args are required: `R1.fq R2.fq output.fa`. Reads must be paired and in the same order (use `seqkit pair` or `trimmomatic` to ensure consistent pairing after quality trimming). Output is multi-FASTA, one record per bridged fragment.
- **Build Dependency**: The C++ source depends on Bifrost (https://github.com/pmelsted/bifrost) for the colored de Bruijn graph. Bifrost must be installed first and its include/lib directories exported via `C_INCLUDE_PATH`, `CPLUS_INCLUDE_PATH`, `LD_LIBRARY_PATH`, `LIBRARY_PATH`, and `PATH`.
- **Use Case**: Recovering full transcript fragments for downstream ORF prediction, novel-isoform assembly, or as input to long-read polishing when short-read coverage is uneven. Sister tool `rnabridge-align` is preferred when a reference genome is available; `rnabridge-denovo` is preferred for *de novo* transcriptome assembly of organisms without a high-quality reference.

## Pitfalls

- **CRITICAL — Read pairing must be preserved**: Both FASTQs must list mates in identical order. After trimming with Trimmomatic or fastp, run `repair.sh` (from BBMap) or `seqkit pair` to restore the order, otherwise the bridge will emit nonsense concatenations.
- **CRITICAL — Fragment length must exceed 2× read length**: If `fragment_length ≤ 2 × read_length`, the two reads already overlap and there is nothing to bridge. Such pairs are silently skipped; pre-filtering with `bbduk.sh` or checking the Bioanalyzer fragment-size distribution avoids wasted CPU.
- **Bifrost must be installed first, with environment variables set**: A common failure mode is compiling rnabridge-denovo without exporting `LD_LIBRARY_PATH` to point at Bifrost's `lib/`; the binary builds but crashes at runtime with "cannot find libBifrost.so".
- **No reference required, but no reference means no error correction against truth**: Bridges are consensus paths through the graph; highly expressed transcripts will be bridged correctly, but low-coverage or repetitive regions may produce chimeric or truncated fragments.
- **Memory scales with k-mer diversity, not read count**: A 1 Gbp metagenome with a small k (e.g., 31) can use >50 GB of RAM; tune `-k` in the Bifrost build or downsample reads with `seqkit sample` for memory-constrained machines.
- **Output FASTA can be large and unsorted**: There is no `--sort-by-length` or similar; downstream tools (e.g., `cd-hit-est`) usually want length-sorted inputs, so pipe through `awk '/^>/{name=$0; next} {print name"\t"$0}' bridges.fa | sort -t$'\t' -k2,2nr | awk '{print $1; print $2}' > bridges.sorted.fa`.

## Examples

### Basic bridge of paired-end reads
**Args:** `rnabridge-denovo reads_1.fq reads_2.fq bridges.fa`
**Explanation:** Positional arguments: read-1 FASTQ, read-2 FASTQ, output FASTA. Each record in `bridges.fa` is one reconstructed fragment; fragment IDs encode the originating read pair.

### Bridge with prior read-repair
**Args:** `repair.sh in1.fq in2.fq fixed1.fq fixed2.fq && rnabridge-denovo fixed1.fq fixed2.fq bridges.fa`
**Explanation:** `repair.sh` (BBMap) re-synchronizes the two FASTQs after trimming by dropping or singleton-fixing unpaired reads; without this step, downstream `rnabridge-denovo` emits spurious bridges for mis-paired reads.

### Verify the k-mer graph builds (Bifrost prerequisite)
**Args:** `export LD_LIBRARY_PATH=/opt/bifrost/lib:$LD_LIBRARY_PATH && rnabridge-denovo r1.fq r2.fq out.fa`
**Explanation:** Explicitly export `LD_LIBRARY_PATH` to point at the Bifrost install; without it, the program crashes with a `libBifrost` loader error even if the binary itself was linked successfully.

### Count bridged fragments
**Args:** `grep -c '^>' bridges.fa`
**Explanation:** Quick check that bridges were emitted (a non-zero count); zero bridges usually means the fragment length is shorter than 2× read length, or the two FASTQs are not in the same order.

### De-duplicate identical bridges
**Args:** `seqkit rmdup bridges.fa -o bridges.uniq.fa`
**Explanation:** Many fragments will produce identical or near-identical bridges (especially for highly expressed transcripts); collapsing duplicates shrinks the file and speeds up downstream ORF prediction.

### Pipe into a length-sorted FASTA for downstream tools
**Args:** `awk '/^>/{h=$0; next} {print h"\t"$0}' bridges.fa | sort -t$'\t' -k2,2nr | cut -f1,2 | tr '\t' '\n' > bridges.sorted.fa`
**Explanation:** Re-orders the FASTA so the longest record is first, the format expected by `cd-hit-est` and most transcriptome assemblers; `awk`/`sort`/`cut`/`tr` together transform the two-line FASTA into a sortable stream and back.

### Check Bifrost availability before running
**Args:** `ldd $(which rnabridge-denovo) | grep -i bifrost`
**Explanation:** Verifies that the dynamic linker can resolve `libBifrost.so`; a missing entry here predicts a runtime crash and is faster to diagnose than a failed run on a real dataset.

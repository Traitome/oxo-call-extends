---
name: rosella
category: metagenomics
description: Metagenomic binning pipeline and algorithm that uses UMAP for dimensionality reduction of contig k-mer composition and HDBSCAN for clustering, producing high-quality MAGs from short-read assemblies.
tags: ["rosella", "metagenomics", "binning", "umap", "hdbscan", "mag", "mag-assembly"]
author: oxo-call-community
source_url: "https://github.com/rhysnewell/rosella.git"
---

## Concepts

- **Tool Overview**: Rosella (v0.5.7, Rhys Newell) is a metagenomic binning algorithm and pipeline that uses UMAP (Uniform Manifold Approximation and Projection) for dimensionality reduction of contig k-mer composition and HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) for clustering. It produces high-quality metagenome-assembled genomes (MAGs) from short-read assemblies.
- **Core Function**: Takes a metagenomic assembly (contigs in FASTA) and the reads used to generate it, and produces a set of MAG bins (FASTA files, one per bin) and a QC report. Rosella is competitive with or outperforms MetaBAT2, MaxBin2, and VAMB on the CAMI II benchmarks.
- **Algorithm**: (1) Compute per-contig k-mer composition (typically k=4 or k=6, with optional coverage from read mapping); (2) Apply UMAP to reduce the k-mer × coverage matrix to 2D; (3) Cluster the 2D embedding with HDBSCAN; (4) Refine the bins by removing outliers, splitting chimeras, and re-clustering; (5) Score bins with CheckM and report the high-quality MAGs (completeness > 90%, contamination < 5%).
- **Input Format**: A contigs FASTA (output of an assembler like MEGAHIT, metaSPAdes, or IDBA-UD) and the corresponding read files (BAM from mapping reads back to contigs, or the raw FASTQ). Coverage is auto-computed via read mapping; pass `--bam` to skip the mapping step.
- **Output Format**: A directory of per-bin FASTAs (`bins/bin.*.fa`), a TSV summary (`bins.tsv`) with per-bin completeness/contamination (from CheckM), a UMAP embedding plot (`umap.pdf`), and a refined-bin set (`refined_bins/`). The standard `bins.tsv` is usable as input to `dRep` for dereplication.
- **Use Case**: The standard binning step in a metagenomic study (e.g., a soil or human gut microbiome), producing MAGs for downstream functional or taxonomic analysis, recovering low-abundance organisms that other binners miss, and integrating with `dRep` for a non-redundant MAG catalog.

## Pitfalls

- **CRITICAL — Coverage is required for good binning**: Rosella's UMAP embedding uses k-mer composition AND coverage. Without coverage (i.e., if you pass a contigs FASTA without the corresponding reads), the binning is poor. Pass the BAM file or the raw FASTQ so Rosella can compute coverage via `coverM` or `minimap2`.
- **CRITICAL — The assembly must be reasonable**: Rosella does NOT assemble — it bins an existing assembly. A fragmented assembly (e.g., N50 < 1 kbp) produces fragmented bins. Use MEGAHIT with `--min-contig-len 1000` or metaSPAdes with `--subassemblies`.
- **The UMAP hyperparameters are not auto-tuned**: The default `n_neighbors=15`, `min_dist=0.1` works for most microbiomes, but for unusual communities (very high or very low diversity), manual tuning is needed. Use `--umap-n-neighbors 30` for higher-diversity samples.
- **HDBSCAN's `min_cluster_size` affects bin count**: The default is 5 contigs; smaller values produce more bins (some may be noise), larger values produce fewer bins (some may be merged). Use `--min-cluster-size 10` for cleaner bins on large assemblies.
- **The refinement step can over-split**: Rosella's "split" step (refining a bin into multiple sub-bins) is aggressive. For high-quality MAGs, use `--no-split` to skip the split and rely on HDBSCAN's natural cluster boundaries.
- **Memory scales with contig count**: A 1 M-contig assembly needs ~30 GB RAM for the UMAP step. For very large assemblies, pre-filter with `--min-contig-len 2500` to reduce the contig count.

## Examples

### Basic Rosella run
**Args:** `rosella bin -c contigs.fa -r reads_1.fastq.gz -r reads_2.fastq.gz -o bins/`
**Explanation:** `-c` is the contigs FASTA, `-r` is the (paired) read files, `-o` is the output directory. Produces `bins/bin.*.fa`, `bins/bins.tsv`, and `bins/umap.pdf`. Rosella auto-computes coverage via read mapping.

### Use a pre-computed BAM
**Args:** `minimap2 -ax sr contigs.fa reads_1.fastq.gz reads_2.fastq.gz | samtools sort -o contigs.bam && samtools index contigs.bam && rosella bin -c contigs.fa --bam contigs.bam -o bins/`
**Explanation:** Composite: pre-map reads to contigs with `minimap2`, then pass the BAM to Rosella via `--bam`. Skips Rosella's internal mapping step; useful for large datasets where the mapping is slow.

### Adjust UMAP neighbors for high-diversity samples
**Args:** `rosella bin -c contigs.fa -r reads_1.fastq.gz -r reads_2.fastq.gz -o bins/ --umap-n-neighbors 30`
**Explanation:** `--umap-n-neighbors 30` increases the UMAP neighborhood size from 15 to 30, which is better for high-diversity samples (e.g., soil microbiomes with thousands of species). Slower than the default.

### Increase the minimum cluster size
**Args:** `rosella bin -c contigs.fa -r reads_1.fastq.gz -r reads_2.fastq.gz -o bins/ --min-cluster-size 10`
**Explanation:** `--min-cluster-size 10` requires HDBSCAN to find clusters of at least 10 contigs. Reduces the number of noise bins; useful for high-quality MAG production.

### Skip the split step
**Args:** `rosella bin -c contigs.fa -r reads_1.fastq.gz -r reads_2.fastq.gz -o bins/ --no-split`
**Explanation:** `--no-split` disables Rosella's "split" refinement step. The output bins are the raw HDBSCAN clusters. Useful when the split step over-fragments bins.

### Dereplicate with dRep
**Args:** `rosella bin -c contigs.fa -r reads_1.fastq.gz -r reads_2.fastq.gz -o bins/ && dRep dereplicate bins/ -o dereplicated_bins/ -g bins/*.fa`
**Explanation:** Composite: bin with Rosella, then dereplicate with `dRep` to produce a non-redundant MAG catalog. The output `dereplicated_bins/` contains one MAG per species cluster.

### Pre-filter short contigs
**Args:** `seqkit seq -m 2500 contigs.fa > contigs_filtered.fa && rosella bin -c contigs_filtered.fa -r reads_1.fastq.gz -r reads_2.fastq.gz -o bins/`
**Explanation:** Composite: pre-filter the assembly to contigs ≥ 2500 bp, then bin. Reduces memory usage and produces cleaner bins for very large assemblies.

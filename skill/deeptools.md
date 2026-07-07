---
name: deeptools
category: qc
description: deepTools - Suite for normalisation, analysis, and visualisation of deep-sequencing data (BAM/bigWig/BED).
tags: [deeptools, qc, visualization, coverage, normalization, chip-seq, atac-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/deeptools/deepTools"
---

## Concepts

- **Tool Overview**: deepTools (v3.5.x) is a Python suite of ~30 command-line utilities built on `pyBigWig`/`pysam` for analysing and visualising high-throughput sequencing data. Tools share a consistent `-b/--bam`, `-o/--outFileName`, `--binSize`, `--region` interface and support multi-core via `-p/--numberOfProcessors`.
- **Tool Categories**:
  - **Coverage tracks**: `bamCoverage` (BAM → bigWig/bedGraph), `bamCompare` (two BAMs → ratio bigWig), `bigwigCompare`, `multiBigwigSummary`.
  - **QC**: `plotFingerprint` (ChIP/ATAC enrichment), `plotCoverage` (cumulative coverage), `bamPEFragmentSize` (insert-size distribution), `estimateReadFiltering` (count reads removed by SAM flags), `computeGCBias` / `correctGCBias`.
  - **Matrix & plots**: `computeMatrix` (build coverage matrix over intervals) → `plotHeatmap`, `plotProfile`; `multiBamSummary` → `plotCorrelation`, `plotPCA`.
  - **Filtering**: `alignmentSieve` (filter reads by SAM flags / mapping quality / region).
- **Normalisation Methods** (used by `bamCoverage`/`bamCompare` via `--normalizeUsing`):
  - `RPKM` = reads per kilobase per million mapped (default; bin value = `(reads in bin) / (bin size kb × total mapped reads M)`).
  - `CPM` = counts per million mapped (no length normalisation).
  - `BPM` = bins per million mapped, analogous to TPM for RNA-seq.
  - `RPGC` = 1× depth; requires `--normalizeUsing RPGC --effectiveGenomeSize EGS` (so coverage = reads / (EGS × total reads)).
  - `None` = raw read counts per bin (default for some tools).
- **`computeMatrix` Modes**:
  - `scale-regions` — rescale all input regions to the same length (`-m scale-regions`).
  - `reference-point` — anchor on TSS/TES/centre and probe a fixed window (`-m reference-point --referencePoint TSS|TES|center`).
- **Input**: BAM/CRAM (sorted + indexed), bigWig, or BED/GTF intervals. CRAM needs `--reference`.
- **Output**: bigWig/bedGraph (coverage), `.npz` (matrices), `.tab` (raw tables), PNG/PDF/SVG (plots).
- **Installation**: `conda install -c bioconda deeptools` (also requires `pyBigWig`, `matplotlib`, `numpy`, `pysam`).
- **Use Case**: ChIP-seq/ATAC-seq signal profiling around promoters; sample QC via PCA/correlation; coverage track generation for IGV; GC-bias diagnostics; insert-size QC.

## Pitfalls

- **BAM/CRAM must be sorted and indexed**. deepTools requires a `.bai`/`.csi` for random-access; an unindexed file silently produces empty/wrong output. Run `samtools index aln.bam` first.
- **`--normalizeUsing RPGC` needs `--effectiveGenomeSize`**. Using RPGC without `--effectiveGenomeSize` is an error; the value must match your reference (e.g. 2.9 Gb for hg38 autosomes, 3.1 Gb for hg38 incl. chrY). Mismatched EGS produces comparably scaled but absolutely wrong coverage values.
- **`--binSize 50` (default) may be too coarse**. For promoter-scale features use `--binSize 10` or smaller; for whole-genome visualisation use `--binSize 100`–500 to keep file sizes manageable. Larger bins average out local features.
- **`--extendReads` is required for single-end ChIP-seq**. Without extension, only the read's 5' end is counted, drastically underestimating fragment coverage. Use `--extendReads <insert_size>` (e.g. 200) or `--extendReads` (auto from paired-end) for SE data. For PE data, extension is implicit.
- **`computeMatrix scale-regions` distorts length heterogeneity**. Rescaling intervals of very different lengths to a fixed width can hide length-dependent effects; use `reference-point` mode or split intervals into length buckets before plotting.
- **Heatmap colour scale defaults are auto-scaled per matrix**. To compare samples, fix `--zMin`/`--zMax` to identical values; otherwise one sample's outliers dominate the colour range.
- **`--region CHR:START:END` is 1-based, not 0-based**. deepTools follows UCSC convention (1-based, inclusive). Mixing with BED (0-based, half-open) silently off-by-ones your intervals.
- **`--blackListFileName` only excludes reads, not regions**. The blacklist removes reads overlapping blacklist intervals; if you want to *display* regions excluding blacklist, use `--region` instead.
- **CRAM requires a reference**. Without `--reference ref.fa`, CRAM decoding fails on `pyBigWig`/`pysam` 0.22+. Always pass the FASTA used to encode the CRAM.
- **`plotHeatmap` consumes a lot of RAM for big matrices**. A `computeMatrix` output with 100k regions × 1000 bins × 6 samples exceeds 5 GB RAM during plotting. Use `--regionsLabel` to downsample or split by chromosome.
- **`plotFingerprint --ignoreDuplicates` matters**. By default duplicates are counted; for ChIP-seq QC this inflates apparent enrichment. Always pass `--ignoreDuplicates` (and pre-mark duplicates with `picard MarkDuplicates`).
- **`-p` defaults to `max(1, n_cpu/2)`**. On busy nodes this can starve other jobs; pin explicitly with `-p 4` or similar.

## Examples

### Generate an RPKM-normalised bigWig coverage track
**Args:** `bamCoverage -b sample.bam -o sample.rpkm.bw --binSize 10 --normalizeUsing RPKM -p 8`
**Explanation:** `-b` is the input BAM (must be sorted + indexed); `--binSize 10` produces 10-bp bins; `--normalizeUsing RPKM` (default) divides each bin's read count by (bin_size_kb × total_mapped_M); `-p 8` uses 8 cores. Output `sample.rpkm.bw` can be loaded into IGV.

### Generate a 1× (RPGC) coverage track with effective genome size
**Args:** `bamCoverage -b sample.bam -o sample.1x.bw --normalizeUsing RPGC --effectiveGenomeSize 2913022398 --binSize 50 -of bigwig`
**Explanation:** `--normalizeUsing RPGC` produces 1× depth (reads per base per genome copy); `--effectiveGenomeSize 2913022398` is hg38 autosomes (sum of chr1–22 + X); `--binSize 50` averages 50-bp windows; `-of bigwig` (default) outputs bigWig.

### Compare two BAMs as a log2 ratio (ChIP/input)
**Args:** `bamCompare -b1 chip.bam -b2 input.bam -o chip_over_input.log2ratio.bw --binSize 50 --scaleFactorsMethod readCount --operation log2 --normalizeUsing RPKM`
**Explanation:** `-b1` is treatment, `-b2` is control; `--operation log2` computes `log2(chip/input)` per bin; `--scaleFactorsMethod readCount` normalises by total reads; output `chip_over_input.log2ratio.bw` is the standard ChIP-seq enrichment track.

### Extend single-end reads to fragment length
**Args:** `bamCoverage -b se.bam -o se.bw --extendReads 200 --binSize 10 --normalizeUsing CPM`
**Explanation:** `--extendReads 200` extends each SE read to 200 bp (estimated fragment size) so the coverage reflects the full fragment rather than just the 5' end; `--normalizeUsing CPM` divides by total mapped reads in millions.

### Compute a coverage matrix around TSS for plotting
**Args:** `computeMatrix reference-point -S signal.bw -R promoters.bed -o matrix.gz --referencePoint TSS -a 2000 -b 2000 --binSize 10 --sortRegions keep`
**Explanation:** `-S` is the bigWig(s) (space-separated for multiple samples); `-R promoters.bed` defines intervals (BED 0-based); `--referencePoint TSS` anchors at each interval's start; `-a 2000 -b 2000` define ±2 kb windows; `--binSize 10` produces 400 bins per region; `--sortRegions keep` preserves BED order.

### Plot a heatmap of ChIP-seq signal at promoters
**Args:** `plotHeatmap -m matrix.gz -out heatmap.png --colorMap RdBu_r --zMin 0 --zMax 50 --missingDataColor 0 --dpi 200`
**Explanation:** `-m` is the `computeMatrix` output; `--colorMap RdBu_r` selects the diverging palette; `--zMin 0 --zMax 50` fixes the colour scale (essential for cross-sample comparisons); `--missingDataColor 0` paints NaN bins as black; `--dpi 200` produces publication-quality output.

### Plot the average profile with confidence interval
**Args:** `plotProfile -m matrix.gz -out profile.png --plotType lines --yMin 0 --yMax 50 --regionsLabel SampleA SampleB SampleC --numPlotsPerRow 3`
**Explanation:** `--plotType lines` produces line plots (alternatives: `heatmap`, `overlapped_lines`); `--yMin/--yMax` fix the y-axis; `--regionsLabel` names each sample in the legend (matches the order of `-S` in `computeMatrix`); `--numPlotsPerRow 3` lays out sub-plots.

### Run QC across multiple BAMs and plot correlation/PCA
**Args:** `multiBamSummary bins --bamfiles *.bam -o bins.npz --binSize 10000 -p 8 --outRawCounts counts.tab && plotCorrelation -s bins.npz -o corr.png --corMethod spearman --plotType heatmap && plotPCA -s bins.npz -o pca.png --plotTitle "Sample PCA"`
**Explanation:** `multiBamSummary bins --binSize 10000` computes per-10 kb-bin read counts per BAM; `--outRawCounts counts.tab` exports raw counts (for downstream R/Python); `plotCorrelation --corMethod spearman` produces a Spearman heatmap; `plotPCA` projects samples into 2-D for QC clustering.

### ChIP-seq fingerprint QC
**Args:** `plotFingerprint -b chip.bam input.bam -o fingerprint.png --ignoreDuplicates --labels ChIP Input --plotFileFormat png`
**Explanation:** `plotFingerprint` ranks bins by coverage and plots the cumulative fraction; `--ignoreDuplicates` removes duplicate reads (essential for fair comparison); `--labels` names the curves. A good ChIP-seq shows a pronounced "shoulder" while the input rises diagonally.

### Insert-size distribution for paired-end BAM
**Args:** `bamPEFragmentSize -b sample.bam -o fragsize.png --hist`
**Explanation:** `bamPEFragmentSize --hist` produces a histogram of paired-end fragment sizes; the modal size indicates library type (e.g. ~150 bp for ATAC, ~300 bp for ChIP). Also reports mean, median, and std.

### Filter reads by SAM flags and write a new BAM
**Args:** `alignmentSieve -b sample.bam -o filtered.bam --filterMetrics metrics.txt --samFlagExclude 256 --samFlagInclude 2 --minMappingQuality 20 --ignoreDuplicates -p 8`
**Explanation:** `--samFlagExclude 256` excludes secondary alignments; `--samFlagInclude 2` requires properly-paired; `--minMappingQuality 20` drops low-MAPQ reads; `--ignoreDuplicates` removes duplicates; `--filterMetrics metrics.txt` logs counts per filter. Output BAM is coordinate-sorted and indexed.

### Diagnose and correct GC bias
**Args:** `computeGCBias -b sample.bam --effectiveGenomeSize 2913022398 -g hg38.fa --GCbiasFrequenciesFile gc_freq.txt -o gc_bias.png -p 8 && correctGCBias -b sample.bam --effectiveGenomeSize 2913022398 -g hg38.fa --GCbiasFrequenciesFile gc_freq.txt -o sample.gc.bw`
**Explanation:** `computeGCBias` models read density as a function of GC content and writes `gc_freq.txt`; `correctGCBias` uses that file to reweight reads, producing a corrected bigWig. Required for whole-genome sequencing where GC content varies between regions.

---
name: hmftools-teal
category: expression
description: Characterises telomeres in tumor and normal samples from WGS data, measuring telomere content and estimating telomeric length.
tags: [hmftools-teal, telomere, WGS, WGS-analysis, cancer, bioinformatics, aging]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/teal/README.md"
---

## Concepts

- **Tool Overview**: TEAL (v1.3.6) measures telomere content and estimates telomeric length from whole-genome sequencing (WGS) BAM input. It can be run in germline-only, tumor-only, or tumor-normal paired mode. When provided with tumor-normal pairs, TEAL also calls somatic telomeric rearrangements—breakends linking non-telomeric genomic regions to telomeric content.

- **Telomeric Fragment Extraction**: TEAL extracts all genomic fragments where at least one read contains two or more adjacent canonical telomeric repeats (TTAGGG in vertebrates), including supplementary and duplicate reads. This produces a Telomere BAM typically 10,000x smaller than the original BAM, containing only candidate telomeric fragments.

- **Telomeric Annotation Pipeline**: Each extracted read is annotated for: (1) PolyG tail identification (sequencing artifacts that may mimic telomeric content), (2) canonical G-orientation (TTAGGG) and C-orientation (TAACCC) telomeric repeat counts, (3) non-canonical telomeric repeat counts in the determined orientation. Reads are classified as 'C-rich' or 'G-rich' based on their dominant telomeric content.

- **Telomere Length Estimation**: TEAL calculates average telomere length using the formula: MeanTelomereLength = TotalTelomericReads × (1-duplicatePercent) × MeanReadLength / (MeanReadDepth × GCBiasAdj × 46). The 46 constant represents the number of telomeres in one copy of the human genome (2 per chromosome). The GC bias adjustment accounts for GC content effects on sequencing coverage.

- **Somatic Telomeric Rearrangement Detection**: In paired tumor-normal mode, TEAL identifies reads with soft-clipping at telomeric boundaries and counts split read and discordant pair support for each candidate rearrangement. Blacklisted genomic regions (49kb total) are excluded due to recurrent artifact alignment. Rearrangements require minimum thresholds: 3+ split reads, 20+ telomeric base pairs in soft clip, and 50+ base anchor length.

- **Purity and Ploidy Adjustment**: For tumor samples, TEAL uses PURPLE-derived purity and ploidy estimates to separate tumor-specific telomeric content from germline contribution. The tumor telomere length is derived from the mixed measurement using the formula that accounts for stromal admixture.

## Pitfalls

- **Java 17+ Requirement**: TEAL requires Java 17 or higher to run. Older Java versions will cause startup failures. Verify your Java installation with `java -version` before running TEAL.

- **WGS Metrics File Dependency**: TEAL requires WGS metrics files (from Picard CollectWgsMetrics) for both tumor and reference samples. These contain essential statistics like mean read depth, GC bias, and duplicate proportions. Without these files in paired mode, TEAL will fail.

- **Reference Genome Version Mismatch**: Input BAM files must use the same genome build (GRCh37/V37 or GRCh38/V38) as specified by ref_genome_version. Mixing builds causes incorrect telomere coordinate assignment and unreliable length estimates.

- **Low Coverage Samples**: Samples with mean read depth below 20x may produce unreliable telomere length estimates due to insufficient telomeric read counts. Consider whether the data quality is sufficient for your research question.

- **CRAM File Reference Requirement**: When using CRAM input files, you must provide the reference genome FASTA path via the ref_genome parameter. CRAM files are reference-compressed and cannot be decoded without the original reference sequence.

- **High GC Bias Samples**: Samples with extreme GC bias (GC50Bias < 0.6 or > 1.1) have less reliable length estimates due to coverage distortions. The GC bias adjustment table may not adequately correct for very extreme bias values.

## Examples

### Run TEAL with HMF pipeline outputs (tumor-normal paired)
**Args:** `java -Xmx16G -cp teal.jar com.hartwig.hmftools.teal.TealPipelineApp -reference COLO829R -reference_bam COLO829R.bam -tumor COLO829T -tumor_bam COLO829T.bam -purple /path/to/COLO829/purple -cobalt /path/to/COLO829/cobalt -reference_wgs_metrics COLO829R_WGSMetrics.txt -tumor_wgs_metrics COLO829T_WGSMetrics.txt -output_dir /path/to/COLO829/teal -threads 28`
**Explanation:** Standard HMF pipeline mode using pre-computed PURPLE and COBALT outputs. Requires WGS metrics files from Picard. Produces telomere length estimates and somatic rearrangement calls for the COLO829 reference sample pair.

### Germline-only mode with HMF pipeline files
**Args:** `java -Xmx16G -cp teal.jar com.hartwig.hmftools.teal.TealPipelineApp -reference sample1 -reference_bam sample1.bam -cobalt /path/to/sample1/cobalt -reference_wgs_metrics sample1_WGSMetrics.txt -output_dir ./teal_germline/ -threads 16`
**Explanation:** Analyzes a single germline sample using COBALT normalization and WGS metrics. Produces baseline telomere length for normal tissue without tumor comparison.

### Paired tumor-normal mode standalone
**Args:** `java -Xmx16G -cp teal.jar com.hartwig.hmftools.teal.TealApplication -reference tumor1R -reference_bam tumor1R.bam -tumor tumor1T -tumor_bam tumor1T.bam -reference_duplicate_proportion 0.2284 -reference_gc50_read_depth 21.4 -reference_mean_read_depth 27.1 -tumor_purity 0.6 -tumor_ploidy 1.98 -tumor_duplicate_proportion 0.2766 -tumor_gc50_read_depth 55.5 -tumor_mean_read_depth 57.5 -output_dir ./teal/ -threads 28`
**Explanation:** Standalone mode without HMF pipeline dependencies. All parameters must be explicitly provided including duplicate proportions, GC depths, and tumor purity/ploidy from external sources.

### Germline-only mode standalone
**Args:** `java -Xmx16G -cp teal.jar com.hartwig.hmftools.teal.TealApplication -reference sample1 -reference_bam sample1.bam -reference_duplicate_proportion 0.15 -reference_gc50_read_depth 30.0 -reference_mean_read_depth 35.0 -output_dir ./teal_germline/ -threads 8`
**Explanation:** Minimal germline-only analysis in standalone mode. Only requires basic metrics from WGS analysis. Suitable for population studies of telomere length in normal samples.

### Process with GRCh38 reference
**Args:** `java -Xmx16G -cp teal.jar com.hartwig.hmftools.teal.TealPipelineApp -reference sample1 -reference_bam sample1.bam -tumor sample1T -tumor_bam sample1T.bam -ref_genome_version V38 -purple ./purple -cobalt ./cobalt -reference_wgs_metrics sample1_WGSMetrics.txt -tumor_wgs_metrics sample1T_WGSMetrics.txt -output_dir ./teal/`
**Explanation:** Runs TEAL on GRCh38-aligned data by specifying V38 genome version. Ensure all input files (BAM, PURPLE, COBALT) were generated from GRCh38-aligned inputs for consistent coordinates.

### Enable multi-threading for large cohorts
**Args:** `java -Xmx32G -cp teal.jar com.hartwig.hmftools.teal.TealPipelineApp -reference sample1 -reference_bam sample1.bam -tumor sample1T -tumor_bam sample1T.bam -purple ./purple -cobalt ./cobalt -reference_wgs_metrics sample1_WGSMetrics.txt -tumor_wgs_metrics sample1T_WGSMetrics.txt -output_dir ./teal/ -threads 32`
**Explanation:** Uses 32 threads for parallel processing of large WGS files. Higher thread counts reduce wall-clock time for large cohorts but require more RAM. The -Xmx32G ensures sufficient heap memory for parallel operations.

### Collect WGS metrics for TEAL input
**Args:** `java -jar picard.jar CollectWgsMetrics I=tumor.bam O=tumor_wgs_metrics.txt R=reference.fasta LEVEL=SAMPLE`
**Explanation:** Picard command to generate the WGS metrics file required by TEAL. Must be run on both tumor and reference BAMs before TEAL execution. The SAMPLE level collects metrics for the entire BAM file.

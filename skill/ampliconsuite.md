---
name: ampliconsuite
category: variant-calling
description: End-to-end pipeline for focal amplification analysis (ecDNA, BFB) from WGS data using AmpliconArchitect
tags: [focal-amplification, ecdna, bfb, wgs, structural-variant, pipeline, ampliconarchitect]
author: oxo-call-community
source_url: "https://github.com/AmpliconSuite/AmpliconSuite-pipeline"
---

## Concepts

- **Tool Overview**: AmpliconSuite-pipeline is an end-to-end wrapper for analyzing focal copy number amplifications (ecDNA, BFB cycles) from paired-end whole-genome sequencing data. Integrates alignment, CNV calling, AmpliconArchitect, and AmpliconClassifier. Version 1.5.2.
- **Supported Genomes**: hg19, GRCh37, GRCh38 (hg38), mm10 (GRCm38), and GRCh38_viral for oncoviral analysis.
- **Workflow Stages**: Can start from FASTQ, BAM, or pre-computed CNV calls. Handles alignment (BWA), CNV detection (CNVkit/control-freec), seed detection, AA execution, and classification.
- **Flexible Entry Points**: Can begin at any intermediate stage using `--bam`, `--cnv_bed`, or `--completed_AA_runs` options.
- **Container Support**: Available as Docker and Singularity containers for reproducible analysis environments.
- **Repository Integration**: Optional upload to AmpliconRepository.org for community data sharing.
- **Mosek License**: Requires Mosek optimization license (free for academic use) for AmpliconArchitect operations.

## Pitfalls

- **Mosek License**: Must obtain and install Mosek license file in `$HOME/mosek/` directory. Pipeline will fail without valid license.
- **Thread Count**: Recommended 12+ threads for efficient parallel processing. Lower thread counts significantly increase runtime.
- **Coverage Requirements**: WGS coverage of 30x+ recommended for reliable focal amplification detection. Lower coverage may miss events.
- **Memory Requirements**: Large genomes and high coverage datasets require substantial RAM (32GB+ recommended).
- **Tumor Purity**: Low tumor purity (<30%) may cause false negatives. Use `--purity` to specify estimated purity for better CNV calling.
- **CNV Calling Method**: Default CNVkit segmentation may not suit all sample types. Try `--cnvkit_segmentation hmm-tumor` for heterogeneous tumors.

## Examples

### Analyze from FASTQ files
**Args:** `AmpliconSuite-pipeline.py -s sample1 -t 12 --fastqs R1.fq.gz R2.fq.gz --ref GRCh38 --run_AA --run_AC`
**Explanation:** Full pipeline from raw FASTQ: aligns with BWA, calls CNVs, runs AmpliconArchitect, and classifies amplifications. Most common workflow.

### Analyze from BAM file
**Args:** `AmpliconSuite-pipeline.py -s sample1 -t 12 --bam aligned.bam --ref GRCh38 --run_AA --run_AC`
**Explanation:** Starts from pre-aligned BAM file. Skips alignment step, proceeds with CNV calling, AA, and classification.

### Use custom CNV calls
**Args:** `AmpliconSuite-pipeline.py -s sample1 -t 8 --bam aligned.bam --cnv_bed custom_cnvs.bed --ref GRCh38 --run_AA`
**Explanation:** Uses user-provided CNV calls instead of automatic CNV detection. Useful when high-quality CNV data is already available.

### Re-classify existing AA results
**Args:** `AmpliconSuite-pipeline.py -s collection1 -t 4 --completed_AA_runs AA_output_dir/ --ref GRCh38 --run_AC`
**Explanation:** Re-runs classification on previously generated AmpliconArchitect outputs. Useful for trying different classification parameters.

### Analyze oncoviral samples
**Args:** `AmpliconSuite-pipeline.py -s viral_sample -t 12 --fastqs R1.fq.gz R2.fq.gz --ref GRCh38_viral --cnsize_min 10000 --run_AA`
**Explanation:** Uses GRCh38_viral reference for oncoviral integration analysis. Lower CN size threshold (10kb) detects smaller viral amplicons.

### Specify tumor purity and ploidy
**Args:** `AmpliconSuite-pipeline.py -s tumor1 -t 12 --bam tumor.bam --ref GRCh38 --purity 0.7 --ploidy 2.5 --run_AA`
**Explanation:** Provides tumor purity (70%) and ploidy (2.5n) estimates for improved CNV calling accuracy. Critical for heterogeneous samples.

### Adjust CNV detection sensitivity
**Args:** `AmpliconSuite-pipeline.py -s sample1 -t 12 --bam aligned.bam --ref GRCh38 --cngain 3.5 --cnsize_min 30000 --run_AA`
**Explanation:** Lowers CN gain threshold to 3.5 (default 4.5) and minimum size to 30kb. More sensitive detection of smaller/lower-level amplifications.

### Run with external SV calls
**Args:** `AmpliconSuite-pipeline.py -s sample1 -t 12 --bam aligned.bam --ref GRCh38 --sv_vcf external_svs.vcf --run_AA`
**Explanation:** Incorporates external structural variant calls (e.g., from Manta, Delly) to improve AA analysis. Recommended when high-quality SV data available.

### Download reference data
**Args:** `AmpliconSuite-pipeline.py --download_repo GRCh38`
**Explanation:** Downloads required reference genome annotation data for GRCh38. Must run once before analysis with each reference genome.

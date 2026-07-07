---
name: rnalyze
category: expression
description: "Comprehensive Snakemake/Nextflow pipeline for bulk and single-cell RNA-Seq analysis: QC, alignment, quantification, and differential expression."
tags: ["rnalyze", "rna-seq", "pipeline", "snakemake", "differential-expression", "sleuth", "star"]
author: oxo-call-community
source_url: "https://github.com/MohamedElsisii/rnalyze#readme"
---
## Concepts

- **Tool Overview**: RNAlyze (v1.0.1, MohamedElsisii) is a one-stop pipeline that runs a complete bulk or single-cell RNA-Seq analysis: FastQC/MultiQC for QC, STAR/HISAT2 for alignment, Salmon/kallisto for transcript-level quantification, and Sleuth/DESeq2 for differential expression. The pipeline is implemented as a Snakemake workflow with a `config.yaml` parameter file.
- **Core Function**: Takes a samplesheet (sample, condition, fastq_1, fastq_2) and a reference, and produces gene/transcript expression matrices, QC reports (HTML/PDF), and a differential expression table with MA plot and volcano plot. The main entry point is `snakemake -s RNAlyze.smk --configfile config.yaml --cores N`.
- **Algorithm**: Modular pipeline composed of independent rules; each rule is a Snakefile block that can be disabled, replaced, or extended. Default tools per stage: FastQC + MultiQC (QC), STAR (alignment), Salmon (quantification), tximport (gene-level aggregation), DESeq2 (differential expression). All parameters are exposed through the config file.
- **Input Format**: A `samples.tsv` (tab-separated: sample_id, condition, fastq_1, fastq_2) and a `config.yaml` with paths to the reference FASTA, GTF, and Salmon index. FASTQ files must be paired-end (the pipeline does not yet support single-end cleanly) and may be gzipped.
- **Output Format**: A results directory with sub-folders per stage (`qc/`, `aligned/`, `quant/`, `de/`). The final deliverables are `results/de/differential_expression.tsv` (DE results), `results/qc/multiqc_report.html` (QC report), and `results/quant/salmon.merged.gene_counts.tsv` (gene-level count matrix).
- **Use Case**: Bulk RNA-Seq differential expression analysis for a few dozen samples, time-course RNA-Seq (the pipeline supports continuous covariates via Sleuth), and small-scale single-cell RNA-Seq (the scRNA branch uses `kb-python` instead of STAR/Salmon).

## Pitfalls

- **CRITICAL — Conda environments must be activated per rule**: The Snakefile declares conda envs per rule; the user's base environment does NOT need STAR or Salmon pre-installed, but `snakemake --use-conda` (or `--conda-prefix`) must be set or the rules will fail with "command not found". The default invocation pattern is `snakemake --use-conda --cores 16`.
- **CRITICAL — Reference FASTA and GTF must be version-matched**: The Salmon index built from one Ensembl release will produce a `transcript-to-gene` map that mismatches the gene IDs in a different Ensembl release. Always re-build the Salmon index from the same FASTA/GTF pair.
- **Paired-end FASTQs must be sorted identically**: If sample R1/R2 FASTQ reads are not in the same order (e.g., after trimming with `fastp` and `--trim_poly_g`), STAR's `--readFilesIn` will misalign. Run `seqkit pair` or use `bbmap's repair.sh` to restore ordering.
- **Differential expression requires at least 2 replicates per condition**: A design with N=1 will be reported by DESeq2 as a warning and most p-values will be NaN. The pipeline does not block this; you must check the design yourself.
- **Single-cell mode requires `kb-python` and a kallisto + bustools index**: Running the scRNA branch on a bulk-aligned reference will silently produce an empty count matrix. The scRNA path is enabled with `mode: scrna` in the config.
- **Snakemake version compatibility**: The Snakefile targets Snakemake 7.x; running with Snakemake 8+ (which changed the conda solver defaults) requires `--conda-frontend mamba` to avoid hangs in the solver.

## Examples

### Run with the default config
**Args:** `snakemake -s RNAlyze.smk --configfile config.yaml --use-conda --cores 16 -p`
**Explanation:** `-s` selects the Snakefile, `--configfile` provides the per-project configuration, `--use-conda` enables per-rule conda environments, `--cores 16` sets parallelism, `-p` prints each command. This is the canonical bulk RNA-Seq invocation.

### Dry-run to see the DAG
**Args:** `snakemake -s RNAlyze.smk --configfile config.yaml --use-conda --cores 16 -n`
**Explanation:** `-n` (dry-run) prints the rule graph and the commands that WOULD be executed without actually running them. Run this first on a new samplesheet to verify the workflow is sensible (correct rules triggered, no orphan files).

### Resume from a failed run
**Args:** `snakemake -s RNAlyze.smk --configfile config.yaml --use-conda --cores 16 --rerun-triggers mtime`
**Explanation:** `--rerun-triggers mtime` forces re-evaluation of input mtimes; combined with Snakemake's automatic skip of up-to-date rules, this lets you resume a failed run without redoing successful stages. Useful when a single rule crashed (e.g., STAR ran out of memory).

### Run on a Slurm cluster
**Args:** `snakemake -s RNAlyze.smk --configfile config.yaml --use-conda --cluster "sbatch -A my_account -p core -n {threads} --mem {resources.mem_mb}M" --jobs 50`
**Explanation:** `--cluster` defines a per-job sbatch template; `--jobs 50` allows up to 50 concurrent jobs. The standard pattern for HPC deployments. Add `--cluster-status` if you want a status script to handle failed/cancelled jobs.

### Force rebuild of a specific stage
**Args:** `snakemake -s RNAlyze.smk --configfile config.yaml --use-conda --cores 16 --force quant/salmon.merged.gene_counts.tsv`
**Explanation:** Targets a specific output file; the upstream rules are re-run only as needed, but rules downstream of the target are skipped. Useful when you want to rebuild the Salmon aggregation but keep the alignment.

### Run single-cell branch
**Args:** `snakemake -s RNAlyze.smk --configfile config_scrna.yaml --use-conda --cores 16`
**Explanation:** A second config file (`config_scrna.yaml`) enables the scRNA mode (`mode: scrna`), which uses `kb-python` (kallisto + bustools) instead of STAR/Salmon. Reference must be a pre-built `kb-python` index specified under `kb_index:` in the config.

---
name: nextflow
category: hpc
description: A reactive workflow framework and language for composing parallelized, scalable, and reproducible computational pipelines using the POSIX filesystem.
tags: [nextflow, workflow, pipeline, hpc, cluster, containers, dsl2, groovy]
author: oxo-call-community
source_url: "https://www.nextflow.io/docs/latest/index.html"
---

## Concepts

- **Tool Overview**: Nextflow is a workflow management system that enables scalable and reproducible scientific workflows using software containers. It supports local execution, HPC clusters (SLURM, SGE, PBS), and cloud platforms (AWS Batch, Google Cloud, Azure). Version 24.04.
- **DSL2 Syntax**: Nextflow uses DSL2 (Domain Specific Language 2) by default. Workflows are defined with `workflow {}`, processes with `process {}`, and modules can be imported with `include {}`. DSL2 enables modular, reusable pipeline components.
- **Channels and Processes**: Data flows between processes via channels. Processes define input/output channels and a `script:` block with shell commands. Channels can be created from files, values, or programmatically.
- **Execution Profiles**: Profiles defined in `nextflow.config` select execution environments. Common profiles: `standard` (local), `docker` (Docker containers), `singularity` (HPC), `slurm` (SLURM scheduler). Activate with `-profile slurm,singularity`.
- **nf-core Pipelines**: nf-core (https://nf-co.re/) provides community-maintained Nextflow pipelines for common analyses (RNA-seq: nf-core/rnaseq; WGS: nf-core/sarek; WES: nf-core/sarek; scRNA-seq: nf-core/scrnaseq). Download with `nf-core download`.
- **Resume Feature**: Nextflow caches all process outputs in a `work/` directory. Use `-resume` to restart a failed pipeline from the last successful step, dramatically reducing compute costs.
- **Tower Integration**: Nextflow Tower (Seqera Platform) provides a web interface to monitor and manage pipeline runs: `nextflow run pipeline.nf -with-tower`.
- **Installation**: `conda install -c bioconda nextflow`

## Pitfalls

- **CRITICAL - Java Version**: Nextflow requires Java 11 or later. Check with `java -version`. Some HPC environments have old Java versions; set `JAVA_HOME` to a compatible version.
- **work/ Directory Size**: The `work/` directory stores all intermediate files and can become very large (hundreds of GB). Delete with `nextflow clean -f` after pipeline completion. Use `publishDir` to copy final outputs.
- **Config File Location**: `nextflow.config` in the current directory or `~/.nextflow/config` is automatically loaded. Scope your config properly (`process`, `executor`, `docker`, etc.) to avoid unintended settings.
- **DSL1 vs DSL2**: Older pipelines use DSL1 syntax. DSL1 is deprecated in Nextflow 22+. Check pipeline documentation for the required Nextflow version.
- **Container Versions**: Always pin container versions in profiles (e.g., `container = 'biocontainers/samtools:1.15.1'`). `latest` tags change unpredictably and break reproducibility.
- **HPC Memory Limits**: Process `memory` directives must respect HPC queue limits. Use `errorStrategy 'retry'` with `maxRetries 2` and double memory on retry to handle occasional memory failures.

## Examples

### Run a Nextflow pipeline with a profile
**Args:** `run nf-core/rnaseq -profile docker --input samplesheet.csv --genome GRCh38 --outdir results/ -resume`
**Explanation:** Runs the nf-core/rnaseq pipeline using Docker containers. `--input` is a CSV samplesheet; `--genome GRCh38` uses iGenomes reference; `-resume` resumes from cache if re-run. Replace `docker` with `singularity` for HPC.

### Run with SLURM executor
**Args:** `run main.nf -profile slurm -c custom.config --outdir results/ -resume`
**Explanation:** Submits pipeline jobs to SLURM. The `slurm` profile must be defined in `nextflow.config` with `process.executor = 'slurm'`. `-c custom.config` adds additional configuration on top of the profile.

### Check pipeline status and resume
**Args:** `log`
**Explanation:** Shows history of all pipeline runs with run names, dates, status, and work directories. Use the run name with `-resume <run_name>` to resume a specific previous run.

### Pull the latest version of a pipeline
**Args:** `pull nf-core/sarek`
**Explanation:** Downloads or updates the nf-core/sarek pipeline from GitHub. Use `-revision 3.2.3` to pin a specific version. Pulled pipelines are cached in `~/.nextflow/assets/`.

### Run with custom params file
**Args:** `run nf-core/rnaseq -profile singularity -params-file params.yaml --outdir results/ -resume`
**Explanation:** `params.yaml` contains pipeline parameters in YAML format (e.g., `genome: GRCh38`, `aligner: star_salmon`). Separating params into a file improves reproducibility and version control.

### Test a pipeline with minimal test data
**Args:** `run nf-core/rnaseq -profile test,docker --outdir test_results/`
**Explanation:** All nf-core pipelines include a `test` profile that downloads minimal test data automatically. Use this to verify the pipeline works in your environment before running on real data.

### Clean up work directory
**Args:** `clean -f -before 2024-01-01`
**Explanation:** Removes cached work directories for runs completed before the specified date. `-f` forces deletion without confirmation. Reclaims disk space while preserving results published with `publishDir`.

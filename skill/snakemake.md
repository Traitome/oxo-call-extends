---
name: snakemake
category: hpc
description: A Python-based workflow management system for creating reproducible and scalable data analyses with support for cluster/cloud execution and software environments.
tags: [snakemake, workflow, pipeline, hpc, python, conda, bioinformatics]
author: oxo-call-community
source_url: "https://snakemake.readthedocs.io/"
---

## Concepts

- **Tool Overview**: Snakemake is a Python-based workflow system using a Makefile-like syntax. Workflows are defined in a `Snakefile` using `rule` blocks. Snakemake automatically determines which rules to run based on requested outputs and available inputs. Version 8.x.
- **Rule-Based Execution**: Each `rule` has `input:`, `output:`, and `shell:`/`run:`/`script:` sections. Snakemake builds a DAG (Directed Acyclic Graph) from these dependencies and executes rules in the correct order, skipping already-completed steps.
- **Wildcards**: Curly braces in input/output paths are wildcards: `rule bwa: input: "{sample}.fastq", output: "{sample}.bam"`. Snakemake infers wildcard values from requested output filenames.
- **Conda Integration**: Each rule can specify its own conda environment: `conda: "envs/bwa.yaml"`. Snakemake creates and activates environments automatically. Use `--use-conda` flag to enable this.
- **Cluster Execution**: Submit rules to SLURM with `--executor slurm` (Snakemake 8+) or `--cluster "sbatch ..."` (legacy). Resource directives (`threads:`, `resources: mem_mb=8000`) map to cluster job parameters.
- **Config Files**: Load configuration with `configfile: "config.yaml"` in the Snakefile. Access values as `config["key"]`. Allows parameterizing workflows without editing the Snakefile.
- **Checkpoints**: `checkpoint` rules create dynamic branches in the DAG based on rule outputs. Useful for workflows where the number of outputs (e.g., assembled contigs) is not known in advance.
- **Installation**: `conda install -c bioconda snakemake`

## Pitfalls

- **CRITICAL - Output Before Input**: Snakemake works backwards from the requested output to determine what rules to run. Always specify the desired output with `snakemake output_file` or define `rule all: input: [list of final outputs]`. Running `snakemake` without arguments only runs the first rule.
- **Dry-Run Before Running**: Always use `-n` (dry-run) first to verify the rule execution plan before submitting to a cluster. `snakemake -n --forceall` shows all rules that would be executed.
- **Thread Count vs Jobs**: `-j N` sets maximum parallel jobs (rules) when running locally, or maximum simultaneous cluster jobs. Within each rule, `threads:` sets CPU count. Both must be set for HPC use.
- **Conda Env Creation Time**: `--use-conda` creates conda environments on first run, which can take significant time. Use `--conda-create-envs-only` to pre-create environments before submitting to a cluster.
- **Locked Workflows**: Snakemake locks the working directory while running. If a run fails ungracefully, remove the `.snakemake/locks/` directory before re-running: `snakemake --unlock`.
- **Missing Output Files**: If a rule produces output files only sometimes (e.g., filtering steps), use `ancient()`, `temp()`, or `touch()` wrappers, or declare outputs as optional with `expand(..., allow_missing=True)`.

## Examples

### Dry-run to preview execution plan
**Args:** `-n --forceall -j 8`
**Explanation:** `-n` dry-run; `--forceall` shows all rules including those with existing outputs; `-j 8` maximum 8 parallel jobs. ALWAYS run this before actual execution to verify the DAG is correct.

### Run workflow locally with conda environments
**Args:** `--use-conda -j 16 --conda-prefix /path/to/conda/envs/`
**Explanation:** `-j 16` allows up to 16 parallel jobs; `--use-conda` activates per-rule conda environments; `--conda-prefix` centralizes env storage to avoid re-creating them per project.

### Submit to SLURM cluster (Snakemake 8+)
**Args:** `--executor slurm --jobs 100 --use-conda --default-resources slurm_account=myproject mem_mb=8000 runtime=120`
**Explanation:** Snakemake 8 uses plugin executors. `--executor slurm` submits each rule as a SLURM job; `--jobs 100` max 100 simultaneous jobs; `--default-resources` sets default SLURM account, memory, and runtime.

### Force re-run of specific rule
**Args:** `-R align_reads -j 8`
**Explanation:** `-R rule_name` forces re-execution of the specified rule and all downstream rules that depend on its output. Use when you've updated a rule's code and want to reprocess.

### Generate workflow DAG visualization
**Args:** `--dag | dot -Tpdf > workflow_dag.pdf`
**Explanation:** Outputs a DOT-format graph of the workflow DAG (Directed Acyclic Graph). Pipe to Graphviz's `dot` to generate a PDF visualization. Use `--rulegraph` for a simplified rule-level graph without sample-specific nodes.

### Run with a config file override
**Args:** `--config genome=hg38 samples=samples_new.tsv -j 8 --use-conda`
**Explanation:** Override or add config values at runtime without modifying the Snakefile. `config["genome"]` will be `"hg38"` in the Snakefile. Useful for running the same workflow on different datasets.

### Unlock a stalled workflow
**Args:** `--unlock`
**Explanation:** Removes Snakemake's working directory lock left by a crashed run. The lock file is in `.snakemake/locks/`. Run `--unlock` before re-starting an interrupted pipeline.

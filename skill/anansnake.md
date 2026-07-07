---
name: anansnake
category: workflow
description: Automated ANANSE analysis with seq2science & snakemake!
tags: [anansnake, workflow, snakemake, ANANSE, seq2science, GRN]
author: oxo-call-community
source_url: "https://github.com/vanheeringen-lab/anansnake"
---

## Concepts

- **Tool Overview**: Anansnake is a Snakemake workflow that automates long-running ANANSE analyses. It links seq2science output to ANANSE with sample tables and configuration files.
- **Core Function**: Automates the ANANSE workflow (binding prediction, network inference, influence analysis) using Snakemake for parallel execution and reproducibility.
- **Seq2Science Integration**: Works seamlessly with seq2science input/output, using the same RNA-seq and ATAC-seq samples.tsv files.
- **Workflow Management**: Leverages Snakemake's dependency management and parallel execution capabilities for efficient GRN modeling.
- **Multi-sample Support**: Handles multiple samples and cell types in a single workflow run.
- **Installation**: Available via Bioconda (`conda install -c bioconda anansnake`). Requires seq2science (1.2.1.*).

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires specific sample table format compatible with seq2science.
- **Seq2Science Dependency**: Must have seq2science installed and configured properly.
- **ANANSE Requirements**: Requires ANANSE dependencies including motif databases.
- **Resource Requirements**: Long-running analyses require sufficient computational resources.
- **Configuration Complexity**: Proper configuration file setup is essential for successful workflow execution.

## Examples

### Display help
**Args:** `anansnake --help`
**Explanation:** Shows available options and usage information.

### Initialize workflow
**Args:** `anansnake init --output-dir my_analysis/`
**Explanation:** Initializes a new Anansnake workflow directory with template files.

### Run workflow with default settings
**Args:** `anansnake run --input samples.tsv --config config.yaml --output results/`
**Explanation:** Runs the automated ANANSE workflow using sample table and configuration file.

### Run with parallel jobs
**Args:** `anansnake run --input samples.tsv --config config.yaml -j 8`
**Explanation:** Runs workflow with 8 parallel jobs for faster execution.

### Dry run to check workflow
**Args:** `anansnake run --input samples.tsv --config config.yaml --dryrun`
**Explanation:** Performs a dry run to preview the workflow without actual execution.

### Specify genome
**Args:** `anansnake run --input samples.tsv --config config.yaml --genome hg38`
**Explanation:** Specifies the genome build for the analysis (e.g., hg38 for human).

### Use custom motif database
**Args:** `anansnake run --input samples.tsv --config config.yaml --motifs JASPAR2022.pwm`
**Explanation:** Uses a custom motif database for TF binding prediction.

### Restart from specific step
**Args:** `anansnake run --input samples.tsv --config config.yaml --restart-from binding`
**Explanation:** Restarts workflow from a specific step (binding, network, or influence).

### Generate workflow graph
**Args:** `anansnake run --input samples.tsv --config config.yaml --dag | dot -Tpng > workflow.png`
**Explanation:** Generates a visual representation of the workflow dependency graph.
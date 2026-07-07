---
name: croo
category: utility
description: Cromwell output organizer for organizing and visualizing pipeline outputs with file tables, task graphs, and UCSC browser tracks
tags: [croo, cromwell, WDL, pipeline, ENCODE, output-organization, workflow, metadata]
author: oxo-call-community
source_url: "https://github.com/ENCODE-DCC/croo"
---

## Concepts

- **Tool Overview**: croo (v0.6.0) - Cromwell Output Organizer - a Python package for organizing outputs from Cromwell workflow executions into a structured directory layout.
- **Core Function**: Parses Cromwell's metadata.json output files and organizes raw pipeline outputs into an organized directory structure with copies or soft links to each output file, as defined by an output definition JSON file. Also generates HTML reports with file tables, task graphs, and UCSC Genome Browser track links.
- **Algorithm**: (1) Reads metadata.json from Cromwell execution. (2) Parses output definition JSON to understand expected output structure. (3) Creates organized directory hierarchy. (4) Copies or soft-links output files to appropriate locations. (5) Generates HTML report with interactive visualizations.
- **Input**: Cromwell metadata.json file (local or remote URI like gs://, s3://), output definition JSON file (defines expected outputs and naming).
- **Output**: Organized output directory with files, HTML report with file tables and task graphs, optional UCSC browser track links.
- **Application**: ENCODE uniform processing pipelines, bioinformatics workflow output management, cloud storage output organization.
- **Installation**: `pip install croo` or `conda install -c bioconda croo`

## Pitfalls

- **Metadata Required**: Requires metadata.json from Cromwell - won't work with other workflow engines.
- **Output Definition JSON**: Must have correct output definition JSON matching your pipeline's outputs.
- **Remote File Access**: When using remote URIs (gs://, s3://), ensure proper cloud credentials are configured.
- **Soft-link vs Copy**: Default uses soft-links for local-to-local transfers. Use `--method copy` to force copying.
- **Python 3.6+**: Requires Python 3.6 or higher version.
- **ENCODE Pipelines**: Primarily designed for ENCODE DCC pipelines - may need custom output definition for other pipelines.

## Examples

### Basic local organization
**Args:** `croo metadata.json --out-def-json pipeline.out_def.json --out-dir output/`
**Explanation:** Organize outputs from a local Cromwell metadata.json file using the output definition JSON.

### Remote Google Cloud storage
**Args:** `croo gs://bucket/path/metadata.json --out-def-json s3://other/bucket/out_def.json --out-dir gs://final/output/`
**Explanation:** Read metadata from Google Cloud and output definition from S3, write organized outputs to Google Cloud.

### Generate HTML report with UCSC tracks
**Args:** `croo metadata.json --out-def-json out_def.json --out-dir output/ --ucsc-genome-db hg38`
**Explanation:** Create HTML report with clickable UCSC Genome Browser tracks for the specified genome assembly.

### Force copy instead of soft-link
**Args:** `croo metadata.json --out-def-json out_def.json --out-dir output/ --method copy`
**Explanation:** Force copying files instead of creating soft-links, useful when sharing outputs.

### List output files only
**Args:** `croo metadata.json --out-def-json out_def.json --dry-run`
**Explanation:** Preview what files would be organized without actually creating the output structure.

### Specify custom task graph output
**Args:** `croo metadata.json --out-def-json out_def.json --out-dir output/ --task-graph my_tasks.pdf`
**Explanation:** Generate a PDF visualization of the workflow task dependency graph.

### Multi-sample batch processing
**Args:** `for i in sample_*/metadata.json; do croo $i --out-def-json out_def.json --out-dir ${i%/}/output/; done`
**Explanation:** Process multiple Cromwell outputs in batch using a shell loop.

### Install ENCODE pipeline output definitions
**Args:** `croo --setup-encode-pipeline`
**Explanation:** Download and install standard ENCODE pipeline output definition JSON files.

### Check version
**Args:** `croo --version`
**Explanation:** Display installed croo version.

### Show help
**Args:** `croo --help`
**Explanation:** Show all available command-line options.

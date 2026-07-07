---
name: crimson
category: formatting
description: Convert bioinformatics tool outputs (FastQC, samtools, Picard, STAR, VEP) to JSON or YAML format
tags: [crimson, JSON, YAML, format-converter, FastQC, samtools, Picard, STAR, VEP, bioinformatics, pipeline]
author: oxo-call-community
source_url: "https://github.com/bow/crimson"
---

## Concepts

- **Tool Overview**: crimson v1.1.1 - A converter that transforms non-standard bioinformatics tool outputs into structured JSON or YAML format for easier parsing and integration into pipelines.
- **Core Function**: Parses output files from common bioinformatics tools and converts them to machine-readable JSON or YAML. Supports both command-line execution and Python library import.
- **Algorithm**: Reads tool-specific output formats, extracts relevant metrics and data fields, structures them according to tool-specific schemas, outputs in requested format (JSON/YAML).
- **Input**: Output files from supported bioinformatics tools (FastQC, FusionCatcher, samtools flagstat, Picard metrics, STAR log, STAR-Fusion, VEP plain text).
- **Output**: JSON or YAML file containing structured, parsed data from the original tool output.
- **Application**: Data pipeline integration, automated parsing of QC metrics, standardized data extraction for dashboards, reproducible workflow outputs.
- **Installation**: `pip install crimson` or `conda install -c bioconda crimson`

## Pitfalls

- **Supported Tools Limited**: Only supports specific tools: FastQC, FusionCatcher, samtools flagstat, Picard metrics, STAR log, STAR-Fusion, VEP plain text. Not a universal converter.
- **Version Compatibility**: Tool-specific parsers may break with different tool versions that change output formats.
- **File Path Required**: Must provide actual file path - cannot read from stdin.
- **Python 3.8+**: Requires Python >= 3.8 and < 4.0
- **Output Format**: Default output is JSON. Use `-y` flag for YAML output.
- **Docker Registry**: For Docker, use `docker pull ghcr.io/bow/crimson` (GitHub registry, not quay.io for latest versions).

## Examples

### Convert FastQC output to JSON
**Args:** `crimson fastqc /path/to/sample_fastqc.txt`
**Explanation:** Parse FastQC output file and output structured JSON to stdout. Extracts all QC metrics (adapter content, sequence quality, GC content, etc.).

### Convert to YAML format
**Args:** `crimson fastqc -y /path/to/sample_fastqc.txt`
**Explanation:** Use YAML output format instead of JSON using the -y flag.

### Write output to file
**Args:** `crimson fastqc -o results.json /path/to/sample_fastqc.txt`
**Explanation:** Write output directly to a file instead of stdout using the -o flag.

### Convert samtools flagstat
**Args:** `crimson flagstat /path/to/alignment.flagstat`
**Explanation:** Parse samtools flagstat output and convert to JSON/YAML with read counts, mapping percentages, and proper pairs information.

### Convert Picard metrics
**Args:** `crimson picard /path/to/picard.metrics`
**Explanation:** Parse Picard metrics files (alignment summary, insert size, RNA-seq metrics, etc.) into structured format.

### Convert STAR log file
**Args:** `crimson star /path/to/Log.final.out`
**Explanation:** Parse STAR aligner log file to extract alignment rates, splice junction counts, and other mapping statistics.

### Convert VEP output
**Args:** `crimson vep /path/to/vep_output.txt`
**Explanation:** Parse Variant Effect Predictor plain text output into structured format with consequence types and allele frequencies.

### Use as Python library
**Args:** `from crimson import fastqc; result = fastqc("/path/to/fastqc.txt")`
**Explanation:** Import and use parser functions directly in Python scripts for programmatic access to parsed data.

### Convert FusionCatcher output
**Args:** `crimson fusioncatcher /path/to/fusions.txt`
**Explanation:** Parse FusionCatcher fusion gene detection output to extract fusion events with breakpoints and spanning reads.

### Convert STAR-Fusion hits
**Args:** `crimson star-fusion /path/to/hits.tsv`
**Explanation:** Parse STAR-Fusion hits table output into structured JSON with fusion junction reads and peptide evidence.

### Multiple outputs in pipeline
**Args:** `crimson fastqc R1_fastqc.txt > qc.json && crimson fastqc R2_fastqc.txt >> qc.json`
**Explanation:** Chain multiple conversions for downstream processing. In bash, append to same JSON array or process separately.

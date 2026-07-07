---
name: abromics_galaxy_json_extractor
category: utility
description: Tool to convert Galaxy AMR output to abromics project format.
tags: [abromics_galaxy_json_extractor, utility, amr, galaxy, format-conversion, surveillance]
author: oxo-call-community
source_url: "https://gitlab.com/ifb-elixirfr/abromics/abromics-galaxy-json-extractor"
---

## Concepts

- **Tool Overview**: Converts Galaxy AMR analysis output (JSON format) to the Abromics project format for integration with the Abromics surveillance platform. Version 0.8.3.6.
- **Core Function**: Extracts and reformats antimicrobial resistance analysis results from Galaxy workflows into Abromics-compatible project files.
- **Supported Input Tools**: Abricate, Bakta, Bandage, Bracken, Fastp, Integronfinder2, ISEScan, Kraken2, Plasmidfinder, Quast, Recentrifuge, Refseqmasher, Shovill, Staramr, and tabular files.
- **Input/Output**: Input is Galaxy AMR output from supported tools; output is Abromics project JSON format.
- **Installation**: Install via bioconda: `conda install -c bioconda abromics_galaxy_json_extractor`
- **Platform Support**: Platform-independent (noarch)
- **Galaxy Integration**: Designed to bridge Galaxy workflow outputs with the Abromics surveillance platform.
- **Dependencies**: Requires Biopython, NumPy, and Pandas.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Format**: Requires specific tool output formats. Refer to documentation for supported versions.
- **Galaxy Version**: Galaxy tool versions may affect output structure. Ensure compatibility with supported versions.
- **Optional Files**: Some tools support optional files (e.g., protein.faa, annotation.gff3) for enhanced output.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Convert Abricate output to Abromics format
**Args:** `-i abricate_output.tsv -o abromics_project.json --tool abricate`
**Explanation:** Converts Abricate AMR analysis output to Abromics project format for platform integration.

### Convert Bakta output with optional files
**Args:** `-i bakta_output.json -o output.json --tool bakta --faa protein.faa --fna nucleotide.fna --gff annotation.gff3`
**Explanation:** Converts Bakta annotation output with optional sequence files for comprehensive AMR analysis.

### Convert with metadata
**Args:** `-i input.tsv -o output.json --tool staramr --sample-name sample1 --project-name project1`
**Explanation:** Converts output with additional metadata (sample and project names) for better organization in the Abromics platform.

### Convert Shovill assembly output
**Args:** `-i contigs.fasta -o output.json --tool shovill --bam alignment.bam --gfa contigs.gfa`
**Explanation:** Converts Shovill assembly output with optional BAM and GFA files for assembly quality assessment.
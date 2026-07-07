---
name: gnk_fastasort
category: programming
description: gnk_fastasort generates GenomeNote-ordered TSV files from genome assemblies, part of the Sanger Tree of Life genome processing pipeline.
tags: [gnk_fastasort, programming, fasta, sanger-tol, genome-annotation, nextflow]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/gnk_fastasort"
---

## Concepts

- **GenomeNote Output**: gnk_fastasort is part of the sanger-tol Genome Afterparty suite that generates standardized outputs for genome assemblies. It creates ordered TSV files that organize genome sequence information according to karyotypic conventions.

- **Integration with Tree of Life Pipelines**: This tool is designed to work within the nf-core based Nextflow pipelines developed by the Sanger Tree of Life project. It processes outputs from genome assembly workflows to produce publication-ready annotation files.

- **Sequence Ordering Standards**: The tool follows GAP (Genome Afterparty) conventions for organizing sequence data, ensuring consistency across different genome projects and compatibility with other Tree of Life analysis tools.

- **Input Requirements**: gnk_fastasort processes FASTA files from genome assemblies. The input FASTA should contain assembled contigs/scaffolds with appropriate headers containing assembly metadata.

- **Output Format**: Generates TSV files with columns for sequence identifiers, lengths, and ordering information. The output follows standard Genome Note conventions used by the Tree of Life project.

## Pitfalls

- **Pipeline Integration**: gnk_fastasort is primarily designed as a module within larger Nextflow pipelines, not as a standalone command-line tool. Direct usage may require understanding of the pipeline framework.

- **Input FASTA Quality**: The quality of output depends heavily on input FASTA quality. Poorly assembled or unannotated genomes may produce less useful ordering information.

- **Naming Convention Requirements**: Input sequences should follow standard naming conventions with meaningful headers that can be parsed for metadata. Non-standard headers may be accepted but could produce less informative outputs.

- **Dependency on Other GAP Tools**: This tool is part of an interconnected suite. Some outputs may require inputs from other GAP components like genomenote or sequencecomposition.

- **Version Compatibility**: Ensure compatibility between gnk_fastasort and other GAP pipeline components when used in custom workflows, as file formats may change between versions.

## Examples

### View tool help and parameters
**Args:** `--help`
**Explanation:** As a Nextflow module, gnk_fastasort parameters are typically accessed through the main pipeline. Run this command to see if standalone usage is supported in your installation.

### Process assembly FASTA within a pipeline
**Args:** `nextflow run sanger-tol/genomenote --input samplesheet.csv --assembly GCA_922984935.2`
**Explanation:** In practice, gnk_fastasort functionality is invoked through the genomenote pipeline. This command runs the full Genome Note generation pipeline which includes sequence sorting as one of its steps.

### Check available sanger-tol pipelines
**Args:** `nextflow pull sanger-tol/genomenote`
**Explanation:** Before running GAP pipelines, ensure you have the latest version pulled. This command fetches the most recent pipeline definition from the nf-core registry.

### Run with custom genome note template
**Args:** `nextflow run sanger-tol/genomenote --input samplesheet.csv --note_template template.docx`
**Explanation:** The genomenote pipeline (which includes gnk_fastasort functionality) supports custom templates for generating Genome Notes. This allows you to customize the output format while using standardized ordering.

### Configure for different output directory
**Args:** `nextflow run sanger-tol/genomenote --input samplesheet.csv --outdir /custom/output/path`
**Explanation:** Override the default output directory for all pipeline results including any gnk_fastasort-generated files. Use absolute paths for cloud storage compatibility.

### List all GAP pipeline tools
**Args:** `nextflow run sanger-tol/sequencecomposition --help`
**Explanation:** To explore other GAP tools that work with gnk_fastasort outputs, run help on related pipelines like sequencecomposition, readmapping, or blobtoolkit.

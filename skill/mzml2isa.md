---
name: mzml2isa
category: formatting
description: mzml2isa - Convert mzML files to ISA-tab format
tags: [mzml2isa, formatting, mzml, isa-tab, metabolomics, metadata]
author: oxo-call-community
source_url: "https://github.com/ISA-tools/mzml2isa"
---

## Concepts

- **Tool Overview**: mzml2isa v1.1.1 is a parsing tool that extracts metadata from mzML mass spectrometry files and generates ISA-tab format files. It automates the creation of standardized metadata files required for metabolomics repositories.
- **Core Function**: Reads mzML files (the standard XML format for raw MS data) and automatically extracts acquisition parameters, sample information, and instrument settings to populate ISA-tab metadata templates.
- **ISA-tab Format**: ISA-tab is a framework for describing experimental metadata in a tab-delimited format. It consists of three files: studies, assays, and protocols, enabling reproducible and shareable experiment descriptions.
- **Input Format**: Accepts individual mzML files or directories containing multiple mzML files. Files should be valid mzML format from LC-MS or GC-MS experiments.
- **Output**: Generates ISA-tab files (i_investigation.txt, s_*.txt, and a_*.txt) that can be submitted to metabolomics repositories like MetaboLights or Metabolomics Workbench.
- **Use Case**: Metabolomics data submission to public repositories, ensuring metadata compliance, reproducible metabolomics studies, and data sharing standardization.

## Pitfalls

- **mzML Validity**: Only processes valid mzML files. Corrupted or non-standard mzML files cause parsing errors.
- **Missing Metadata**: If mzML files lack required metadata fields, ISA-tab entries will have empty fields. Complete metadata in original acquisition is essential.
- **File Naming**: Output file names derive from input mzML names. Inconsistent naming conventions may cause issues in downstream processing.
- **Encoding Issues**: Special characters in metadata may cause encoding problems. Use UTF-8 encoding consistently.
- **ISA Configuration**: Some ISA-tab fields require manual completion (e.g., sample characteristics). mzml2isa extracts what's available but not all fields are auto-fillable.
- **Version Compatibility**: ISA-tab specification has evolved. Ensure compatibility with target repository's version requirements.

## Examples

### Basic conversion
**Args:** `-i mzml_dir -o isa_output`
**Explanation:** Standard conversion. Takes directory of mzML files and generates ISA-tab files in output directory.

### Convert single file
**Args:** `-i sample.mzML -o output_dir`
**Explanation:** Converts a single mzML file to ISA-tab format.

### Specify study identifier
**Args:** `-i mzml_files/ -o isa_dir -s my_study`
**Explanation:** Sets a custom study identifier used as prefix in output ISA files.

### Verbose output
**Args:** `-i data/ -o results/ -v`
**Explanation:** Enables verbose logging showing parsing progress and any warnings about missing metadata.

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

---
name: nmrml2isa
category: utility
description: nmrml2isa converts nmrML files to ISA-Tab format for metadata standardization.
tags: [nmrml2isa, utility, nmr, isa-tab]
author: oxo-call-community
source_url: "http://github.com/ISA-tools/nmrml2isa"
---

## Concepts

- **Tool Overview**: nmrml2isa converts NMR metadata from nmrML format to ISA-Tab.
- **Core Function**: Standardizes NMR data metadata for interoperability.
- **Algorithm**: Parses nmrML XML structure and maps to ISA-Tab format.
- **Input Format**: Accepts nmrML XML files.
- **Output**: Produces ISA-Tab files (investigation, study, assay).
- **Use Case**: Metadata standardization, data sharing, and repository submission.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **File Compatibility**: Requires valid nmrML files.
- **Metadata Completeness**: Depends on input metadata quality.
- **Dependency**: Requires Python and related libraries.
- **Documentation**: Limited documentation.
- **Output Validation**: Requires ISA-Tab validation.

## Examples

### Display help
**Args:** `nmrml2isa --help`
**Explanation:** Shows available options and usage instructions.

### Basic conversion
**Args:** `nmrml2isa -i data.nmrML -o isa_output/`
**Explanation:** Converts nmrML to ISA-Tab format.

### Multiple files
**Args:** `nmrml2isa -d nmrml_files/ -o isa_output/`
**Explanation:** Processes multiple nmrML files.

### Investigation title
**Args:** `nmrml2isa -i data.nmrML -o isa_output/ -t "NMR Study"`
**Explanation:** Sets investigation title.

### Author info
**Args:** `nmrml2isa -i data.nmrML -o isa_output/ -a "John Doe"`
**Explanation:** Sets author information.

### Verbose mode
**Args:** `nmrml2isa -i data.nmrML -o isa_output/ -v`
**Explanation:** Runs with verbose output.

### Validate output
**Args:** `nmrml2isa -i data.nmrML -o isa_output/ --validate`
**Explanation:** Validates ISA-Tab output.
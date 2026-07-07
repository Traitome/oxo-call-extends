---
name: beast2-xml
category: programming
description: beast2-xml - Generate BEAST2 XML configuration files
tags: [beast2-xml, programming, BEAST2, XML, configuration]
author: oxo-call-community
source_url: "https://github.com/acorg/beast2-xml"
---

## Concepts

- **Tool Overview**: beast2-xml (v1.5.2) is a command line script and Python class for generating BEAST2 XML configuration files, simplifying the setup of Bayesian phylogenetic analyses.
- **Core Function**: Automates generation of BEAST2 XML input files from sequence alignments and parameter specifications.
- **XML Generation**: Creates properly formatted XML files for BEAST2 MCMC analyses.
- **Template System**: Supports customizable templates for different analysis types.
- **Python API**: Provides Python class for programmatic XML generation.
- **Input/Output**: Accepts FASTA alignments and parameter files; outputs BEAST2 XML.
- **Installation**: `conda install -c bioconda beast2-xml`.

## Pitfalls

- **BEAST2 Compatibility**: Generated XML must be compatible with target BEAST2 version.
- **Model Specification**: Requires careful specification of evolutionary models and priors.
- **Template Customization**: Custom templates require understanding of BEAST2 XML schema.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Generate XML from FASTA
**Args:** `beast2-xml -i alignment.fasta -o analysis.xml`
**Explanation:** Generates BEAST2 XML file from sequence alignment.

### Specify model
**Args:** `beast2-xml -i alignment.fasta -o analysis.xml -m GTR`
**Explanation:** Uses GTR substitution model in generated XML.

### Set chain length
**Args:** `beast2-xml -i alignment.fasta -o analysis.xml -l 10000000`
**Explanation:** Sets MCMC chain length to 10 million iterations.

### Add calibration point
**Args:** `beast2-xml -i alignment.fasta -o analysis.xml -c "node1:10.0"`
**Explanation:** Adds calibration point for divergence time estimation.

### Use strict clock
**Args:** `beast2-xml -i alignment.fasta -o analysis.xml -clock strict`
**Explanation:** Uses strict molecular clock model.

### Specify output frequency
**Args:** `beast2-xml -i alignment.fasta -o analysis.xml -sf 1000`
**Explanation:** Sets sampling frequency to every 1000 iterations.

### Display help
**Args:** `beast2-xml --help`
**Explanation:** Shows all available command-line options and usage information.
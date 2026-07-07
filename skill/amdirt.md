---
name: amdirt
category: metagenomics
description: AncientMetagenomeDir Toolkit for exploring and downloading ancient metagenomic data
tags: [amdirt, metagenomics, ancient-dna, metadata, SPAAM, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/SPAAM-community/amdirt"
---

## Concepts

- **Tool Overview**: AMDirT (AncientMetagenomeDir Toolkit) is a Python toolkit for interacting with the AncientMetagenomeDir metadata repository of ancient metagenomic samples and ancient microbial genomes.
- **Core Function**: Enables exploration and downloading of sequencing data for ancient microbial and environmental (meta)genomes, automatic generation of input samplesheets for bioinformatic pipelines, and validation of AncientMetagenomeDir submissions.
- **Input/Output**: Inputs: AncientMetagenomeDir TSV tables (samples, libraries); Outputs: filtered tables, pipeline samplesheets (nf-core/eager, shotgun-metagenomics), download scripts, citation BibTeX files.
- **Installation**: Available via PyPI (`pip install amdirt`) or Bioconda (`conda create -n amdirt -c bioconda amdirt`).
- **Features**: Graphical (Streamlit) and command-line interfaces, support for host-associated and environmental metagenomes, automatic citation retrieval, and validation of metadata submissions.

## Pitfalls

- **Metadata Format**: Input tables must match AncientMetagenomeDir format exactly; only rows can be removed, not columns.
- **Internet Connection**: Requires network access for downloading metadata and sequence data from repositories.
- **Citation Availability**: Some publications may lack citation information in cross-ref databases; manual verification recommended.
- **Output Validation**: Always review generated samplesheets before running pipelines to ensure accuracy.
- **Directory Structure**: Ensure output directories exist before running commands.

## Examples

### Launch graphical viewer
**Args:** `AMDirT viewer`
**Explanation:** Launches the Streamlit-based graphical interface for exploring and filtering ancient metagenome data.

### Convert metadata to pipeline samplesheet
**Args:** `AMDirT convert filtered_samples.tsv ancientmetagenome-hostassociated -o samplesheets/ --eager`
**Explanation:** Converts filtered samples table to nf-core/eager pipeline input format.

### Convert with libraries table
**Args:** `AMDirT convert --libraries filtered_libraries.tsv filtered_samples.tsv ancientmetagenome-hostassociated -o samplesheets/ --eager`
**Explanation:** Uses both filtered samples and libraries tables for more precise pipeline configuration.

### Generate download script
**Args:** `AMDirT convert filtered_samples.tsv ancientmetagenome-hostassociated -o output/ --download`
**Explanation:** Creates a shell script for downloading sequence data from SRA/ENA.

### Validate metadata submission
**Args:** `AMDirT validate submission.tsv ancientmetagenome-hostassociated`
**Explanation:** Validates a submission against AncientMetagenomeDir format requirements.

### Generate citation BibTeX
**Args:** `AMDirT convert filtered_samples.tsv ancientmetagenome-hostassociated -o output/ --citation`
**Explanation:** Downloads citation information and generates BibTeX file for selected samples.
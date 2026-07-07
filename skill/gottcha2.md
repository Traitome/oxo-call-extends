---
name: gottcha2
category: bioinformatics
description: GOTTCHA2 is a metagenomic taxonomic classification tool that identifies the genomic origin of sequencing reads using unique clade-specific markers.
tags: [gottcha2, metagenomics, taxonomic-classification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/poeli/GOTTCHA2"
---

## Concepts

- **Taxonomic Classification**: GOTTCHA2 classifies metagenomic sequencing reads to their taxonomic origins using unique clade-specific markers.

- **Marker-based Identification**: Uses clade-specific marker genes to identify organisms at different taxonomic levels (species, genus, family).

- **Database Construction**: Builds custom databases of marker genes from reference genomes for accurate classification.

- **Read Mapping**: Maps sequencing reads to marker databases using alignment-based approaches.

- **Abundance Estimation**: Estimates relative abundance of different taxa in metagenomic samples.

- **Quality Control**: Provides metrics for assessing classification quality and confidence.

## Pitfalls

- **Database Coverage**: Classification accuracy depends on database coverage. Ensure your target organisms are represented in the marker database.

- **Read Length**: Short reads may not contain enough information for accurate classification. Use longer reads when possible.

- **Marker Specificity**: Some markers may not be truly clade-specific. Validate marker specificity for your research question.

- **Computational Resources**: Building large databases or processing many samples may require significant resources.

- **False Positives**: Low-quality reads or contaminants can produce false positive classifications. Preprocess reads carefully.

## Examples

### Build marker database
**Args:** `gottcha2 build -i reference_genomes/ -o marker_db/`
**Explanation:** Builds a marker database from reference genome sequences.

### Classify reads
**Args:** `gottcha2 classify -i reads.fastq -d marker_db/ -o results.txt`
**Explanation:** Classifies metagenomic reads using the marker database.

### Estimate abundance
**Args:** `gottcha2 abundance -i results.txt -o abundance.txt`
**Explanation:** Estimates relative abundance of taxa from classification results.

### Custom marker selection
**Args:** `gottcha2 build -i genomes/ -m custom_markers.txt -o custom_db/`
**Explanation:** Builds a database using custom marker genes specified in a file.

### Filter low-confidence hits
**Args:** `gottcha2 classify -i reads.fastq -d marker_db/ -c 0.9 -o filtered.txt`
**Explanation:** Only keeps classifications with confidence scores above 0.9.

### Batch processing
**Args:** `gottcha2 classify -d samples/ -d marker_db/ -o results/`
**Explanation:** Processes multiple sample files in a directory.

### Generate report
**Args:** `gottcha2 report -i results.txt -o report.html`
**Explanation:** Generates an HTML report with classification statistics and visualizations.
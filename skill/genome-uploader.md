---
name: genome-uploader
category: data-submission
description: genome-uploader - Python script to upload bins and MAGs in FASTA format to ENA (European Nucleotide Archive).
tags: [genome-uploader, data-submission, ENA, FASTA]
author: oxo-call-community
source_url: "https://github.com/EBI-Metagenomics/genome_uploader"
---

## Concepts
- **Data Submission**: Submits genomic data to ENA.
- **MAG Upload**: Uploads metagenome-assembled genomes.
- **FASTA Handling**: Handles FASTA format sequences.
- **Metadata Management**: Manages submission metadata.
- **Batch Upload**: Supports batch upload of multiple sequences.

## Pitfalls
- **Network Dependency**: Requires network access for submission.
- **Authentication**: Requires proper ENA authentication.
- **Data Format**: Requires correct FASTA format.
- **Metadata Completeness**: Requires complete metadata.
- **Submission Limits**: May hit ENA submission limits.

## Examples
### Upload genome to ENA
**Args:** `genome-uploader -i genome.fasta -m metadata.json -o submission.log`
**Explanation:** Uploads genome sequence to ENA.

### Batch upload
**Args:** `genome-uploader -i ./genomes/ -m metadata.json -o submission.log`
**Explanation:** Uploads multiple genomes in batch.

### Validate submission
**Args:** `genome-uploader -i genome.fasta -m metadata.json --validate`
**Explanation:** Validates submission before upload.

### Upload MAGs
**Args:** `genome-uploader -i ./mags/ -m mag_metadata.json -o submission.log`
**Explanation:** Uploads metagenome-assembled genomes.

### Dry run
**Args:** `genome-uploader -i genome.fasta -m metadata.json --dry-run`
**Explanation:** Performs dry run without actual submission.
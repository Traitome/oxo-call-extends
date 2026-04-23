---
name: blobtoolkit
category: qc
description: Interactive quality assessment of genome assemblies with blobplot visualization
tags: [blobtoolkit, qc, genome-assembly, blobplot, contamination]
author: oxo-call-community
source_url: "https://github.com/genomehubs/blobtoolkit"
---

## Concepts

- **Tool Overview**: BlobToolKit is an interactive quality assessment tool for genome assemblies with web-based visualization.
- **Core Function**: Generates interactive blobplots to identify contamination and assembly issues.
- **Components**: blobtools (command-line), blobtoolkit-viewer (web interface), blobtoolkit-pipeline (automation).
- **Input Types**: Assembly FASTA, BAM files, BLAST/Diamond results, BUSCO results.
- **Output**: Interactive web visualizations, filtered assemblies, quality reports.
- **Installation**: Install via bioconda: `conda install -c bioconda blobtoolkit`

## Pitfalls

- **Database Setup**: Requires NCBI taxonomy database and node.js for viewer.
- **Memory Usage**: Large assemblies with many hits require significant memory.
- **Browser Compatibility**: Viewer works best in Chrome or Firefox.
- **Data Preparation**: All input files must use consistent sequence identifiers.
- **Port Binding**: Default viewer port may need adjustment if already in use.

## Examples

### Create BlobDir dataset
**Args:** `blobtools create --fasta assembly.fa --taxdump taxdump/ --out BlobDir`
**Explanation:** Creates BlobDir dataset from assembly with taxonomy database.

### Add coverage data
**Args:** `blobtools add --BlobDir BlobDir --bam coverage.bam`
**Explanation:** Adds BAM coverage information to existing BlobDir.

### Add BLAST hits
**Args:** `blobtools add --BlobDir BlobDir --blast blast_hits.tsv`
**Explanation:** Adds BLAST taxonomy results to BlobDir dataset.

### Launch interactive viewer
**Args:** `blobtools host BlobDir`
**Explanation:** Starts web server for interactive blobplot visualization.

### Filter assembly by taxonomy
**Args:** `blobtools filter --BlobDir BlobDir --taxon 9606 --output filtered_assembly`
**Explanation:** Filters assembly to keep only sequences assigned to specified taxon.

### Generate static images
**Args:** `blobtools view --BlobDir BlobDir --format png --out blobplot.png`
**Explanation:** Creates static blobplot image for publication.

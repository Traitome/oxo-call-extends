---
name: blobtools
category: qc
description: Modular command-line solution for visualisation, quality control and taxonomic partitioning of genome datasets
tags: [blobtools, qc, genome-assembly, contamination, taxonomic]
author: oxo-call-community
source_url: "https://github.com/DRL/blobtools"
---

## Concepts

- **Tool Overview**: BlobTools is a modular tool for visualisation, quality control and taxonomic partitioning of genome assemblies.
- **Core Function**: Identifies contamination and taxonomic composition in genome assemblies using coverage and BLAST results.
- **Input Types**: Assembly FASTA, BAM files (coverage), BLAST/Diamond results (taxonomy).
- **Output**: Blob plots showing taxonomic composition and coverage distribution.
- **Taxonomic Assignment**: Uses NCBI taxonomy database for species identification.
- **Installation**: Install via bioconda: `conda install -c bioconda blobtools`

## Pitfalls

- **Database Required**: NCBI taxonomy database must be downloaded and accessible.
- **Memory Usage**: Large assemblies with many BLAST hits require significant memory.
- **BAM Sorting**: BAM files should be sorted and indexed before use.
- **Taxonomy Updates**: Ensure taxonomy database is current for accurate classification.
- **Output Interpretation**: Blob plots require understanding of coverage vs GC-content distributions.

## Examples

### Create blobplot
**Args:** `blobtools create -i assembly.fa -b aligned.bam -t blast_hits.tsv -o blobplot`
**Explanation:** Creates blobplot from assembly, BAM coverage, and BLAST taxonomy results.

### View blobplot
**Args:** `blobtools view -i blobplot.blobDB -o blobplot.png`
**Explanation:** Generates blobplot image from BlobDB file.

### Create with multiple coverage files
**Args:** `blobtools create -i assembly.fa -b cov1.bam cov2.bam -t taxonomy.tsv -o multi_cov`
**Explanation:** Uses multiple BAM files for coverage information from different libraries.

### Filter by taxonomy
**Args:** `blobtools filter -i blobplot.blobDB --taxon 9606 -o human_only`
**Explanation:** Filters to keep only sequences assigned to human (taxid 9606).

### Export statistics
**Args:** `blobtools stats -i blobplot.blobDB -o stats.txt`
**Explanation:** Outputs assembly statistics with taxonomic breakdown.

### Create taxonomy file from BLAST
**Args:** `blobtools taxify -f blast_hits.tsv -s 2 -t 1 -o taxonomy.tsv`
**Explanation:** Converts BLAST output to BlobTools taxonomy format.

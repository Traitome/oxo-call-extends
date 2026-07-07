---
name: agouti
category: expression
description: Annotation of Genomic and Transcriptomic Intervals - flexible tool for annotating coordinates using GTF/GFF features
tags: [agouti, annotation, gtf, gff, genomic-intervals, transcriptomic-intervals]
author: oxo-call-community
source_url: "https://github.com/zywicki-lab/agouti"
---

## Concepts

- **Tool Overview**: AGouTI (Annotation of Genomic and Transcriptomic Intervals) is a universal tool for flexible annotation of any genomic or transcriptomic coordinates using known genomic features from GTF/GFF files.
- **Core Function**: Annotates genomic or transcriptomic intervals with overlapping features like genes, transcripts, exons, UTRs, CDSs, and provides information about closest genes for intergenic regions.
- **Two-Step Process**: First creates an SQLite database from GTF/GFF annotation, then annotates intervals using the database.
- **Coordinate Systems**: Works with both genomic coordinates (chromosome positions) and transcriptomic coordinates (positions within transcripts).
- **Input/Output**: Input: BED files or custom column-based text files (TSV, CSV). Output: Annotated intervals with selected features and attributes.
- **Installation**: Install via pip: `pip install AGouTI` or bioconda: `conda install -c bioconda agouti`
- **Citation**: Kosiński, J.G., & Żywicki, M. (2023). AGouTI–Flexible Annotation of Genomic and Transcriptomic Intervals. PLoS Comput Biol, 19(10), e1011527.

## Pitfalls

- **Python Version**: Requires Python >= 3.7 (Python >= 3.10 for full compatibility with BED input).
- **Database Creation**: Must create database before annotation - this step can be time-consuming for large GTF files.
- **Feature Names**: All feature names and attributes are automatically converted to lowercase in the database.
- **Intergenic Regions**: Intervals without gene/transcript overlap are marked as "intergenic" with information about closest genes.
- **Multiple Annotations**: A single region may have multiple overlapping annotations - ensure output format handles this.

## Examples

### Display help information
**Args:** `agouti --help`
**Explanation:** Shows available modules and general options.

### Create database from GTF
**Args:** `agouti create_db --gtf annotation.gtf --output annotation.db`
**Explanation:** Creates SQLite database from GTF annotation file for efficient querying.

### Create database from GFF3
**Args:** `agouti create_db --gff annotation.gff3 --output annotation.db`
**Explanation:** Creates database from GFF3 format annotation file.

### Annotate BED file
**Args:** `agouti annotate --db annotation.db --input intervals.bed --output annotated.bed`
**Explanation:** Annotates genomic intervals in BED format using the annotation database.

### Annotate custom TSV file
**Args:** `agouti annotate --db annotation.db --input data.tsv --chr-col 1 --start-col 2 --end-col 3 --output annotated.tsv`
**Explanation:** Annotates custom TSV file by specifying column numbers for chromosome, start, and end positions.

### Select specific features
**Args:** `agouti annotate --db annotation.db --input intervals.bed --features gene,exon,cds --output annotated.bed`
**Explanation:** Annotates only with gene, exon, and CDS features from the annotation.

### Select specific attributes
**Args:** `agouti annotate --db annotation.db --input intervals.bed --attributes gene_id,gene_name,transcript_id --output annotated.bed`
**Explanation:** Includes only specified attributes in the annotation output.

### Transcriptomic mode
**Args:** `agouti annotate --db annotation.db --input transcript_positions.bed --mode transcriptomic --output annotated.bed`
**Explanation:** Annotates transcriptomic coordinates (positions within transcripts) rather than genomic coordinates.

### De novo intragenic assignment
**Args:** `agouti annotate --db annotation.db --input intervals.bed --intragenic 5prime,middle,3prime --output annotated.bed`
**Explanation:** Assigns intragenic regions de novo as 5' part, middle, or 3' part of transcripts.

### Include closest genes for intergenic
**Args:** `agouti annotate --db annotation.db --input intervals.bed --closest-genes 3 --output annotated.bed`
**Explanation:** For intergenic intervals, includes information about 3 closest genes upstream and downstream.

### Custom output separator
**Args:** `agouti annotate --db annotation.db --input intervals.bed --output annotated.tsv --separator "\t"`
**Explanation:** Uses tab separator for output file instead of default comma.
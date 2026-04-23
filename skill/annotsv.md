---
name: annotsv
category: variant-calling
description: Annotation and ranking of structural variations with ACMG-based pathogenicity scoring
tags: [structural-variant, annotation, ranking, acmg, sv, cnv, pathogenicity]
author: oxo-call-community
source_url: "https://github.com/lgmgeo/AnnotSV"
---

## Concepts

- **Tool Overview**: AnnotSV annotates and ranks structural variations (SVs) from human genomes with comprehensive functional annotations and ACMG-based pathogenicity classification. Version 3.5.8.
- **ACMG Scoring**: Implements ACMG guidelines for SV pathogenicity assessment (1-5 ranking). Rapid identification of potentially pathogenic SVs for clinical prioritization.
- **Annotation Sources**: Integrates multiple databases: gene annotations, regulatory elements, disease databases (ClinVar, DGV), population frequencies, and functional predictions.
- **Supported Genomes**: Primarily human (hg19/GRCh37, GRCh38), also supports mouse genome (mm10/GRCm38) since version 2.2.
- **Input Formats**: Accepts BED format SV files with customizable SV type column specification (--svtBEDcol).
- **Output Format**: Generates annotated TSV with comprehensive annotations, ranking scores, and pathogenicity classifications.
- **Filtering Options**: Supports filtering by SV type, size, frequency, and annotation criteria for focused analysis.

## Pitfalls

- **Environment Variable**: Must set ANNOTSV environment variable pointing to installation directory. Required for database access.
- **Database Installation**: Requires separate installation of human and mouse annotation databases via `make install-human-annotation` and `make install-mouse-annotation`.
- **BED Format**: Input BED must be properly formatted. Column containing SV type must be specified correctly with --svtBEDcol.
- **Memory Usage**: Large SV files with many annotations require substantial memory. Consider splitting large files.
- **Database Updates**: Annotation databases should be updated periodically for latest ClinVar and other database entries.
- **Mouse Support**: Mouse annotation requires separate database installation and configuration. Default is human-only.

## Examples

### Basic SV annotation
**Args:** `AnnotSV -SVinputFile variants.bed -outputFile annotated.tsv -svtBEDcol 4`
**Explanation:** Standard annotation: input BED file with SV type in column 4. Outputs comprehensive annotations including genes affected, frequencies, and ACMG ranking.

### Annotate with custom output directory
**Args:** `AnnotSV -SVinputFile variants.bed -outputFile /results/annotated.tsv -svtBEDcol 5 -genomeBuild GRCh38`
**Explanation:** Specifies output directory and GRCh38 genome build. SV type in column 5. Use appropriate build matching input coordinates.

### Filter for rare variants
**Args:** `AnnotSV -SVinputFile variants.bed -outputFile rare.tsv -svtBEDcol 4 -minFreq 0.01`
**Explanation:** Filters variants with population frequency >1% (DGV/gnomAD). Focuses on potentially pathogenic rare SVs. Useful for clinical analysis.

### Annotate specific SV types only
**Args:** `AnnotSV -SVinputFile variants.bed -outputFile deletions.tsv -svtBEDcol 4 -svt "DEL"`
**Explanation:** Annotates only deletion variants. Useful for focused analysis of specific SV types. Supported types: DEL, DUP, INV, INS, BND, CNV.

### Mouse genome annotation
**Args:** `AnnotSV -SVinputFile mouse_vars.bed -outputFile mouse_annotated.tsv -svtBEDcol 4 -genomeBuild mm10`
**Explanation:** Annotates mouse SVs using mm10 genome build. Requires mouse annotation database installed separately.

### Large SV file processing
**Args:** `AnnotSV -SVinputFile large_file.bed -outputFile large_annotated.tsv -svtBEDcol 4 -max_sv_size 1000000`
**Explanation:** Processes large SV file with size limit of 1Mb. Very large SVs (>1Mb) may be filtered or cause memory issues. Adjust threshold based on dataset.

### Test installation
**Args:** `cd $ANNOTSV/share/doc/AnnotSV/Example/; AnnotSV -SVinputFile test.bed -outputFile ./test.tsv -svtBEDcol 4`
**Explanation:** Runs test example from installation directory to verify proper setup. Should produce annotated TSV with expected output format.

### Install annotation databases
**Args:** `cd /path/to/AnnotSV; make PREFIX=. install-human-annotation; make PREFIX=. install-mouse-annotation`
**Explanation:** Installs required annotation databases for human and mouse genomes. Must run after initial installation before using AnnotSV.
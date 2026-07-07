---
name: tbl2asn-forever
category: utility
description: NCBI tool for automating creation of GenBank sequence submission files from feature tables and FASTA sequences.
tags: [tbl2asn, genbank, submission, ncbi, annotation, sequence, fasta, feature-table]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2"
---

## Concepts

- **Tool Overview**: tbl2asn-forever (v25.7.2f) - Command-line tool that automates the creation of sequence records for GenBank submission. Converts feature tables and FASTA sequences into ASN.1 format (.sqn) files ready for submission.
- **Core Function**: Takes three input file types: template file (.sbt) with submitter info, FASTA sequence file (.fsa), and optional feature table (.tbl) for annotation. Outputs .sqn file for GenBank submission.
- **Input Files**: Required: template (.sbt) + FASTA (.fsa). Optional: feature table (.tbl), quality scores (.qvl), source table (.src).
- **Output**: Generates .sqn files (ASN.1 format) for GenBank submission, plus optional .val (validation), .gbf (flatfile), and .error files.
- **Installation**: `conda install -c bioconda tbl2asn-forever` or download from NCBI FTP
- **Key Use Case**: Required tool for bulk genome/sequence submission to GenBank with or without annotation.

## Pitfalls

- **Template File Required**: Without a valid .sbt template file containing submitter information, tbl2asn cannot generate submissions.
- **File Naming**: All related files (FASTA, feature table, source table) must share the same name prefix. Example: `sequence.fsa` + `sequence.tbl` + `sequence.sbt`.
- **Directory Processing**: tbl2asn processes ALL .fsa files in a directory. Use separate directories for different submissions or use `-i` for single file.
- **Gap Handling**: Use `-a` flag to specify gap handling: `r10u` (10+ Ns are gaps, 100 Ns unknown length) or `r10k` (10+ Ns gaps, 100 Ns known length).
- **Validation**: Always use `-V` flag to validate submissions before sending to GenBank. Common: `-V vb` for validation + GenBank flatfile generation.
- ** organism Qualifier**: Use `-j "[organism=Species name] [strain=Strain name]"` to add source organism information to all sequences.

## Examples

### Basic submission generation
**Args:** `tbl2asn-forever -p ./submissions -t template.sbt -j "[organism=Escherichia coli] [strain=MG1655]"`
**Explanation:** Process all .fsa files in directory with organism information added via command line.

### With gap handling
**Args:** `tbl2asn-forever -p ./submissions -t template.sbt -a r10u`
**Explanation:** Specify that runs of 10+ Ns represent assembly gaps and 100 Ns represent unknown length gaps.

### Generate with validation
**Args:** `tbl2asn-forever -p ./submissions -t template.sbt -V vb`
**Explanation:** Generate .sqn file and .gbf GenBank flatfile while running validation. Outputs errorlog.val for review.

### Single file processing
**Args:** `tbl2asn-forever -i chromosome1.fsa -t template.sbt -o chromosome1.sqn`
**Explanation:** Process only the specified FASTA file instead of all files in directory.

### With genome-specific processing
**Args:** `tbl2asn-forever -p ./genome -t template.sbt -M n`
**Explanation:** Use `-M n` for normal genome processing. Use `-M b` for big genomes or `-M t` for TSA (Transcriptome Shotgun Assembly).

### Add comments
**Args:** `tbl2asn-forever -p ./submissions -t template.sbt -y "Contigs larger than 2kb included" -V vb`
**Explanation:** Add a comment to each submission and run full validation.

### Discrepancy report
**Args:** `tbl2asn-forever -p ./submissions -t template.sbt -Z discrepancy_report.txt -V v`
**Explanation:** Generate discrepancy report to identify inconsistencies in the submission using `-Z`.

### Output to specific directory
**Args:** `tbl2asn-forever -p ./submissions -r ./output -t template.sbt`
**Explanation:** Use `-r` to specify output directory for .sqn files instead of overwriting in source directory.

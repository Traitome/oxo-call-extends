---
name: tbl2asn
category: utility
description: NCBI tool for automating creation of GenBank sequence submission files from feature tables and FASTA sequences.
tags: [tbl2asn, genbank, submission, ncbi, annotation, sequence, fasta, feature-table]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2"
---

## Concepts

- **Tool Overview**: tbl2asn (v25.7) - Command-line program that automates the creation of sequence records for submission to GenBank. Converts feature tables and FASTA sequences into ASN.1 format (.sqn) files ready for submission.
- **Core Function**: Takes template file (.sbt), FASTA sequence file (.fsa), and optional feature table (.tbl) for annotation. Outputs .sqn file for GenBank submission.
- **Input Files**: Required: template (.sbt) with submitter info + FASTA (.fsa). Optional: feature table (.tbl), quality scores (.qvl), source table (.src).
- **Output**: Generates .sqn files (ASN.1 format) for GenBank submission, plus optional .val (validation), .gbf (flatfile), and discrepancy reports.
- **Installation**: `conda install -c bioconda tbl2asn` or download from NCBI anonymous FTP
- **Note**: tbl2asn-forever is the actively maintained fork - use that for new installations.

## Pitfalls

- **Template File Required**: The .sbt template file containing submitter/block information is required for all submissions.
- **File Prefix Matching**: Paired files (.fsa, .tbl, .sbt) must share the same filename prefix in the same directory.
- **Batch Processing**: Without `-i` flag, processes ALL .fsa files in the specified directory - use separate directories for different projects.
- **Validation Essential**: Always run validation with `-V v` or `-V vb` before submission to catch errors early.
- **Organism Information**: Use `-j` flag to specify organism and strain: `-j "[organism=Bacteroides thetaiota] [strain=HG3]"`
- **Gap Specification**: Use `-a` to specify gap handling: `r10u` (10+ Ns = gaps), `r10k` (10+ Ns = gaps, 100 Ns = known length gaps).

## Examples

### Basic usage
**Args:** `tbl2asn -p ./submissions -t template.sbt`
**Explanation:** Process all .fsa files in directory using template file for submitter information.

### With organism info
**Args:** `tbl2asn -p ./submissions -t template.sbt -j "[organism=Salmonella enterica] [strain=LT2]"`
**Explanation:** Add organism and strain source qualifiers to all sequences in the submission.

### Generate validation files
**Args:** `tbl2asn -p ./submissions -t template.sbt -V vb`
**Explanation:** Create GenBank flatfile (.gbf) and run validation, generating .val and errorlog.val files.

### Single file
**Args:** `tbl2asn -i genome.fsa -t template.sbt -o genome.sqn`
**Explanation:** Process only the specified file, outputting to explicit output filename.

### Gap handling for assemblies
**Args:** `tbl2asn -p ./assembly -t template.sbt -a r10u`
**Explanation:** Handle assembly gaps where 10+ Ns represent gaps and 100 Ns represent unknown length gaps.

### With comment
**Args:** `tbl2asn -p ./submissions -t template.sbt -y "Assembled using SPAdes v3.15" -V v`
**Explanation:** Add comment to submission records and run validation without flatfile generation.

### Discrepancy report
**Args:** `tbl2asn -p ./submissions -t template.sbt -Z report.txt`
**Explanation:** Generate discrepancy report identifying inconsistencies in the sequence annotation records.

### Output redirection
**Args:** `tbl2asn -p ./submissions -r ./output -t template.sbt`
**Explanation:** Use `-r` to write output files to specified directory rather than overwriting source files.

### CDS ORF finding
**Args:** `tbl2asn -p ./submissions -t template.sbt -k c`
**Explanation:** Use `-k c` to annotate longest ORF if no .tbl file provided. Product name will be 'unknown' unless in FASTA defline.

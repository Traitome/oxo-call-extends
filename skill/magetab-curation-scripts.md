---
name: magetab-curation-scripts
category: expression
description: Perl-based scripts for ArrayExpress and Expression Atlas curation of MAGE-TAB files
tags: [magetab-curation-scripts, expression, MAGE-TAB, ArrayExpress]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/perl-curation-scripts"
---

## Concepts

- **Tool Overview**: magetab-curation-scripts v1.1.0 - Perl-based scripts for validating and processing MAGE-TAB formatted experiments for ArrayExpress and Expression Atlas.
- **Core Function**: Validates MAGE-TAB files, checks data integrity, and prepares submissions for public repositories.
- **Input/Output**: Input: MAGE-TAB files (IDF, SDRF, ADF); Output: Validation reports, processed files, submission-ready data.
- **Installation**: `conda install -c bioconda magetab-curation-scripts`
- **MAGE-TAB Format**: Standard format for microarray and sequencing data annotation.
- **ArrayExpress Integration**: Prepares data for submission to EBI's ArrayExpress database.

## Pitfalls

- **File Format**: Incorrect MAGE-TAB format causes validation errors.
- **Ontology Terms**: Missing or incorrect ontology terms fail validation.
- **File References**: Broken file references cause processing failures.
- **Perl Dependencies**: Missing Perl modules prevent script execution.
- **Data Consistency**: Inconsistent metadata between IDF and SDRF files.
- **Array Design**: Incorrect array design annotations affect data interpretation.

## Examples

### Validate MAGE-TAB files
**Args:** `validate-magetab.pl -i idf.txt -s sdrf.txt`
**Explanation:** Validates MAGE-TAB IDF and SDRF files.

### Check experiment
**Args:** `check-experiment.pl -i idf.txt -s sdrf.txt -a adf.txt`
**Explanation:** Performs comprehensive experiment validation.

### Generate report
**Args:** `validate-magetab.pl -i idf.txt -s sdrf.txt -o report.html`
**Explanation:** Generates HTML validation report.

### Convert to submission format
**Args:** `prepare-submission.pl -i idf.txt -s sdrf.txt -o submission_dir`
**Explanation:** Prepares files for ArrayExpress submission.

### Check array design
**Args:** `check-array-design.pl -a adf.txt`
**Explanation:** Validates array design file.

### Validate ontology terms
**Args:** `validate-ontology.pl -s sdrf.txt -t EFO`
**Explanation:** Validates ontology terms against EFO ontology.
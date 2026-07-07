---
name: mage-tab-merger
category: utility
description: Utility scripts to merge SDRFs, condensed SDRFs and IDFs (MAGE-Tab) for meta-analysis and other purposes.
tags: [mage-tab-merger, utility, MAGE-Tab, meta-analysis]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/mage-tab-merger"
---

## Concepts

- **Tool Overview**: mage-tab-merger v0.0.4 - Utility scripts to merge SDRFs (Sample and Data Relationship Format), condensed SDRFs, and IDFs (Investigation Description Format) from MAGE-Tab format for meta-analysis.
- **Core Function**: Merges multiple MAGE-Tab files to enable meta-analysis across experiments.
- **Input/Output**: Input: Multiple MAGE-Tab files (IDF, SDRF); Output: Merged MAGE-Tab files.
- **Installation**: `conda install -c bioconda mage-tab-merger`
- **MAGE-Tab Format**: Standard format for microarray and sequencing data annotation.
- **Meta-analysis Support**: Enables combining data from multiple experiments for integrated analysis.

## Pitfalls

- **File Format**: Incorrect MAGE-Tab format causes merge failures.
- **Ontology Consistency**: Inconsistent ontology terms across files require manual resolution.
- **Sample Conflicts**: Duplicate sample names across files may cause conflicts.
- **Header Compatibility**: Different column headers require careful mapping.
- **Data Integrity**: Missing or corrupted files can break the merge process.
- **Version Compatibility**: Older MAGE-Tab formats may not be fully supported.

## Examples

### Merge SDRF files
**Args:** `merge-sdrf.py -i sdrf1.txt sdrf2.txt -o merged_sdrf.txt`
**Explanation:** Merges multiple SDRF files into a single file.

### Merge IDF files
**Args:** `merge-idf.py -i idf1.txt idf2.txt -o merged_idf.txt`
**Explanation:** Merges multiple IDF files into a single file.

### Merge with condensed SDRF
**Args:** `merge-sdrf.py -i sdrf1.txt sdrf2.txt --condensed condensed_sdrf.txt -o merged.txt`
**Explanation:** Merges SDRFs with condensed SDRF file.

### Check compatibility
**Args:** `check-compatibility.py -i sdrf1.txt sdrf2.txt`
**Explanation:** Checks if SDRF files are compatible for merging.

### Verbose mode
**Args:** `merge-sdrf.py -i sdrf1.txt sdrf2.txt -o merged.txt -v`
**Explanation:** Provides detailed logging during merge.

### With sample mapping
**Args:** `merge-sdrf.py -i sdrf1.txt sdrf2.txt -m mapping.txt -o merged.txt`
**Explanation:** Uses custom sample mapping file.
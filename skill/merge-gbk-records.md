---
name: merge-gbk-records
category: utility
description: Merge multiple GenBank records into a single record with customizable spacer sequences.
tags: [merge-gbk-records, genbank, sequence-manipulation]
author: oxo-call-community
source_url: "http://github.com/kblin/merge-gbk-records"
---

## Concepts

- **Tool Overview**: merge-gbk-records combines multiple GenBank records.
- **Core Function**: Merges GenBank records into single record.
- **Spacer Sequence**: Adds customizable spacer between sequences.
- **Multi-file Support**: Handles multiple files or multi-record files.
- **Sequence Concatenation**: Concatenates sequences in order.
- **Installation**: `conda install -c bioconda merge-gbk-records`

## Pitfalls

- **Input Format**: Requires valid GenBank format.
- **Sequence Order**: Order depends on input file order.
- **Spacer Selection**: Spacer type affects downstream analysis.
- **File Size**: May produce large output files.
- **Annotation Preservation**: Annotations may be lost.
- **Memory Requirements**: High memory for large records.

## Examples

### Merge GenBank records
**Args:** `merge-gbk-records -i record1.gbk record2.gbk -o merged.gbk`
**Explanation:** Merges multiple GenBank records.

### With spacer
**Args:** `merge-gbk-records -i records.gbk -s 100 -o merged.gbk`
**Explanation:** Adds 100bp spacer between records.

### All-N spacer
**Args:** `merge-gbk-records -i records.gbk -n -o merged.gbk`
**Explanation:** Uses all-N spacer sequence.

### Stop codon spacer
**Args:** `merge-gbk-records -i records.gbk -p -o merged.gbk`
**Explanation:** Uses stop codon spacer.

### Help documentation
**Args:** `merge-gbk-records --help`
**Explanation:** Displays available options.

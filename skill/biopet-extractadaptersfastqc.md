---
name: biopet-extractadaptersfastqc
category: qc
description: Extract adapter sequences found by FastQC
tags: [fastqc, adapter-detection, qc]
author: oxo-call-community
source_url: "https://github.com/biopet/extractadaptersfastqc"
---

## Concepts
- **Tool Overview**: ExtractAdaptersFastqc reads FastQC reports and extracts adapter sequences that were detected, for use in downstream adapter trimming.
- **Adapter Extraction**: Parses FastQC output to identify detected adapter sequences.
- **Output Formats**: Can output adapter sequences as plain text or FASTA format.
- **Applications**: Automated adapter detection, QC pipeline integration, trimming parameter generation.

## Pitfalls
- **FastQC Requirement**: Requires FastQC report as input.
- **Detection Limits**: Only extracts adapters that FastQC successfully detected.

## Examples
### Extract adapters from FastQC report
**Args:** `java -jar ExtractAdaptersFastqc.jar -I fastqc_report/ -o adapters.fa --format fasta`
**Explanation:** Extracts detected adapter sequences in FASTA format.

### Output as plain text
**Args:** `java -jar ExtractAdaptersFastqc.jar -I fastqc_report/ -o adapters.txt`
**Explanation:** Outputs adapter sequences as newline-separated text.

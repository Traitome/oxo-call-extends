---
name: sierra-local
category: annotation
description: sierra-local - HIV drug resistance prediction tool
tags: ["sierra-local", "annotation", "HIV", "drug-resistance"]
author: oxo-call-community
source_url: "https://github.com/PoonLab/sierra-local"
---

## Concepts

- **Tool Overview**: sierra-local (v0.4.4) predicts HIV drug resistance from sequences.
- **Core Function**: Generates drug resistance predictions for HIV-1 sequences.
- **Algorithm**: Uses Stanford HIVdb rules for resistance interpretation.
- **Input/Output**: Accepts FASTA sequences and produces resistance reports.
- **HIV Analysis**: Specialized for HIV drug resistance testing.
- **Applications**: Clinical HIV management, antiretroviral therapy selection.

## Pitfalls

- **Sequence Quality**: Requires high-quality sequence data.
- **Subtype Specificity**: Optimized for HIV-1, may not work for other subtypes.
- **Database Updates**: Requires regular database updates for new resistance mutations.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.
- **Reference Sequence**: Requires proper reference alignment.

## Examples

### Predict drug resistance
**Args:** `sierra-local -i hiv_sequences.fasta -o resistance_results.json`
**Explanation:** `-i` input FASTA; `-o` output JSON results.

### Output CSV format
**Args:** `sierra-local -i hiv_sequences.fasta -f csv -o resistance_results.csv`
**Explanation:** `-f csv` CSV output format.

### With reference
**Args:** `sierra-local -i hiv_sequences.fasta -r hxb2.fasta -o results.json`
**Explanation:** `-r` reference sequence.

### Help command
**Args:** `sierra-local --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sierra-local --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sierra-local -v -i hiv_sequences.fasta -o results.json`
**Explanation:** `-v` verbose output.

### Batch processing
**Args:** `sierra-local -b sequences_list.txt -o results/`
**Explanation:** `-b` batch file with multiple sequences.

---
name: m-party
category: alignment
description: Mining Protein dAtasets foR Targeted EnzYmes - identifies plastic degrading enzymes.
tags: [m-party, alignment, sequence, enzymes]
author: oxo-call-community
source_url: "https://github.com/ozefreitas/M-PARTY"
---

## Concepts

- **Tool Overview**: M-PARTY v0.2.2 identifies plastic-degrading enzymes from protein sequences.
- **Core Function**: Searches for enzymes with potential plastic degradation activity.
- **HMM-based**: Uses Hidden Markov Models for structural annotation.
- **HMMER Integration**: Relies on hmmsearch from HMMER for sequence analysis.
- **Plastic Degradation**: Specialized for polyethylene (PE) degrading enzymes.
- **Input/Output**: Accepts FASTA sequences; outputs enzyme predictions.

## Pitfalls

- **Plastic-specific**: Designed for plastic-degrading enzyme identification.
- **Memory Requirements**: Memory usage depends on sequence count.
- **Parameter Tuning**: May require parameter adjustment for HMM search.
- **Data Quality**: Results depend on sequence quality.
- **HMM Database**: Requires pre-trained HMM database.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Search for plastic-degrading enzymes
**Args:** `m-party -i sequences.fasta -o results/`
**Explanation:** Identifies potential plastic-degrading enzymes.

### With custom HMM database
**Args:** `m-party -i sequences.fasta -d custom_hmm/ -o results/`
**Explanation:** Uses custom HMM database for search.

### Verbose output
**Args:** `m-party -i sequences.fasta -v -o results/`
**Explanation:** Shows detailed analysis results.

### Batch processing
**Args:** `m-party -i fasta/ -o results/`
**Explanation:** Processes multiple sequence files.

### Generate report
**Args:** `m-party -i sequences.fasta -r report.html -o results/`
**Explanation:** Generates analysis report.
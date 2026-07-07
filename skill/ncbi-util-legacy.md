---
name: ncbi-util-legacy
category: utility
description: NCBI legacy utilities provide deprecated but still useful bioinformatics tools from NCBI.
tags: [ncbi-util-legacy, utility, ncbi, legacy, toolkit]
author: oxo-call-community
source_url: "ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/"
---

## Concepts

- **Tool Overview**: NCBI utility legacy tools provide older NCBI bioinformatics utilities that are still in use.
- **Core Function**: Offers various bioinformatics utilities including sequence formatting, alignment, and analysis tools.
- **Algorithm**: Implements classic NCBI algorithms for sequence processing and analysis.
- **Input Format**: Accepts standard bioinformatics formats (FASTA, GenBank, EMBL).
- **Output**: Produces processed sequences, alignments, and analysis results.
- **Use Case**: Legacy pipeline support, backward compatibility, and specialized sequence analysis.

## Pitfalls

- **Deprecated Tools**: Many tools have been superseded by newer alternatives.
- **Limited Support**: May not receive updates or bug fixes.
- **Version Compatibility**: Options may vary between versions.
- **Documentation**: Older tools may have limited documentation.
- **Performance**: May be slower than modern alternatives.
- **Security**: Legacy code may have security vulnerabilities.

## Examples

### Display help
**Args:** `ncbi-tools --help`
**Explanation:** Shows available options and usage instructions.

### Sequence formatting
**Args:** `seqformat -i input.fasta -o output.fasta -f fasta`
**Explanation:** Formats sequence file into FASTA format.

### Reverse complement
**Args:** `seqrev -i input.fasta -o reverse.fasta`
**Explanation:** Generates reverse complement of sequences.

### Sequence statistics
**Args:** `seqstat -i input.fasta -o stats.txt`
**Explanation:** Calculates sequence statistics.

### Translate DNA to protein
**Args:** `seqtranslate -i dna.fasta -o protein.faa`
**Explanation:** Translates nucleotide sequences to amino acids.

### FASTA to GenBank conversion
**Args:** `seqconvert -i input.fasta -f genbank -o output.gb`
**Explanation:** Converts FASTA to GenBank format.
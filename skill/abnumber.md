---
name: abnumber
category: utility
description: AbNumber - Convenience Python APIs for antibody numbering and alignment using ANARCI
tags: [abnumber, utility, antibody, numbering, anarci, cdr, immunoinformatics]
author: oxo-call-community
source_url: "https://github.com/prihoda/AbNumber"
---

## Concepts

- **Tool Overview**: AbNumber provides convenience Python APIs for antibody numbering and alignment using ANARCI. Version 0.4.4.
- **Core Function**: Numbers antibody sequences using various numbering schemes (Kabat, Chothia, IMGT, Martin, AHo) and identifies CDR regions.
- **Input/Output**: Input is antibody sequence (FASTA or direct sequence); output is numbered sequence with CDR annotations.
- **Installation**: Install via bioconda: `conda install -c bioconda abnumber` or via pip: `pip install abnumber`
- **Platform Support**: Platform-independent (Python library)
- **ANARCI Backend**: Uses ANARCI for accurate antibody sequence numbering and region identification.
- **Chain Object**: Central data structure for representing antibody chains with methods for accessing CDRs, FRs, and numbered positions.

## Pitfalls

- **Python Library**: AbNumber is primarily a Python library/API, not a standalone command-line tool.
- **Sequence Type**: Only works on antibody sequences. Non-antibody sequences will produce errors or empty results.
- **Numbering Scheme**: Different numbering schemes (Kabat, Chothia, IMGT, Martin, AHo) may give different CDR boundaries.
- **ANARCI Dependency**: Requires ANARCI to be installed for numbering functionality.

## Examples

### Basic usage in Python script
**Args:** `from abnumber import Chain; chain = Chain('EVQLQQSGAEVVRSGASVKLSCTASGFNIKDYYIHWVKQRPEKGLEWIGWIDPEIGDTEYVPKFQGKATMTADTSSNTAYLQLSSLTSEDTAVYYCNAGHDYDRGRFPYWGQGTLVTVSA', 'H')`
**Explanation:** Create a Chain object from an antibody heavy chain sequence.

### Get numbered sequence with IMGT scheme
**Args:** `chain.numbered_sequence`
**Explanation:** Returns the sequence with IMGT numbering positions.

### Get CDR sequences
**Args:** `chain.cdr1_seq, chain.cdr2_seq, chain.cdr3_seq`
**Explanation:** Access CDR1, CDR2, and CDR3 sequences.

### Switch numbering scheme to Kabat
**Args:** `chain.to_scheme('kabat')`
**Explanation:** Convert the chain to use Kabat numbering scheme.

### Access chain regions
**Args:** `chain.regions`
**Explanation:** Returns a dictionary with all regions (FR1, CDR1, FR2, CDR2, FR3, CDR3, FR4).

### Load from FASTA file
**Args:** `from abnumber import Chain; chain = Chain.from_fasta('antibody.fasta')`
**Explanation:** Load an antibody sequence from a FASTA file.
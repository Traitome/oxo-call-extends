---
name: abnumber
category: utility
description: AbNumber - Antibody numbering using ANARCI
tags: [abnumber, utility, antibody, numbering, anarci]
author: oxo-call-community
source_url: "https://github.com/prihoda/AbNumber"
---

## Concepts

- **Tool Overview**: Antibody numbering tool using ANARCI for sequence annotation and CDR identification. Version 0.4.4.
- **Core Function**: Numbers antibody sequences using various numbering schemes (Kabat, Chothia, IMGT, etc.) and identifies CDR regions.
- **Input/Output**: Input is antibody sequence (FASTA); output is numbered sequence with CDR annotations.
- **Installation**: Install via bioconda: `conda install -c bioconda abnumber`
- **Platform Support**: Platform-independent (noarch)
- **ANARCI Backend**: Uses ANARCI for accurate antibody sequence numbering and region identification.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Sequence Type**: Only works on antibody sequences. Non-antibody sequences will produce errors or empty results.
- **Numbering Scheme**: Different numbering schemes (Kabat, Chothia, IMGT) may give different CDR boundaries.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available numbering schemes and options.

### Number antibody sequence with default scheme
**Args:** `antibody.fasta`
**Explanation:** Numbers the antibody sequence using the default numbering scheme and outputs CDR positions.

### Use IMGT numbering scheme
**Args:** `--scheme imgt antibody.fasta`
**Explanation:** Numbers the antibody sequence using the IMGT numbering scheme, which is standard for immunoinformatics.

### Output numbered sequence to file
**Args:** `--scheme chothia -i antibody.fasta -o numbered.txt`
**Explanation:** Uses Chothia numbering scheme and writes the numbered sequence with CDR annotations to the output file.

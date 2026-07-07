---
name: gigatyper
category: mlst
description: gigatyper - Run all available MLST schemes for species against genome assemblies.
tags: [gigatyper, mlst, assembly, species-identification]
author: oxo-call-community
source_url: "https://github.com/rpetit3/gigatyper"
---

## Concepts
- **MLST Analysis**: Performs multi-locus sequence typing.
- **Species Identification**: Identifies species.
- **Assembly Analysis**: Analyzes genome assemblies.
- **Scheme Detection**: Detects MLST schemes.
- **Database Coverage**: Supports multiple species.

## Pitfalls
- **Assembly Quality**: Requires good assembly.
- **Scheme Availability**: Limited by available schemes.
- **Database Updates**: Requires updated databases.
- **Novel Alleles**: May not detect novel alleles.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Run MLST
**Args:** `gigatyper run -i assembly.fasta -o results.txt`
**Explanation:** Runs MLST analysis.

### Specify species
**Args:** `gigatyper run -i assembly.fasta -s "Staphylococcus aureus" -o results.txt`
**Explanation:** Specifies species.

### Update database
**Args:** `gigatyper update`
**Explanation:** Updates MLST database.

### List schemes
**Args:** `gigatyper list`
**Explanation:** Lists available MLST schemes.

### Generate report
**Args:** `gigatyper run -i assembly.fasta -r -o report.html`
**Explanation:** Generates MLST report.
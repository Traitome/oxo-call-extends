---
name: sampei
category: proteomics
description: SAMPEI - Peptide identification with undefined modifications
tags: ["sampei", "proteomics", "mass spectrometry", "peptide identification", "modifications"]
author: oxo-call-community
source_url: "https://github.com/FenyoLab/SAMPEI"
---

## Concepts

- **Tool Overview**: SAMPEI (v0.0.9) is a mass spectrometry-based peptide identification tool that leverages high-quality query spectra to identify peptides with undefined modifications (mass shifts).
- **Core Function**: Identifies peptides from MS/MS spectra by comparing against high-quality query spectra, enabling detection of unknown modifications.
- **Algorithm**: Uses spectral similarity matching to identify peptide sequences and their modifications without prior knowledge of modification types.
- **Input Format**: Mass spectrometry data (mzML, mzXML), protein database (FASTA), query spectra.
- **Output Format**: Identified peptides with modifications, confidence scores, spectral matches.
- **Use Case**: Proteomics analysis, post-translational modification discovery, biomarker identification.

## Pitfalls

- **Spectrum quality**: Requires high-quality MS/MS spectra for accurate identification.
- **Database size**: Large protein databases increase search time.
- **Modification detection**: May miss modifications with very large mass shifts.
- **Computational resources**: Large datasets require significant memory and CPU.
- **False positives**: May identify spurious matches in complex samples.
- **Parameter tuning**: Search parameters may require adjustment for optimal results.

## Examples

### Basic peptide search
**Args:** `sampei -i spectra.mzML -d proteins.fasta -o results.txt`
**Explanation:** `-i` input spectra; `-d` protein database; `-o` results.

### With query spectra
**Args:** `sampei -i spectra.mzML -d proteins.fasta -q query_spectra.mzML -o results.txt`
**Explanation:** `-q` high-quality query spectra for comparison.

### Mass tolerance
**Args:** `sampei -i spectra.mzML -d proteins.fasta -o results.txt -t 0.5`
**Explanation:** `-t` mass tolerance in Da (default: 0.5).

### Maximum modifications
**Args:** `sampei -i spectra.mzML -d proteins.fasta -o results.txt -m 3`
**Explanation:** `-m` maximum number of modifications per peptide.

### Output XML
**Args:** `sampei -i spectra.mzML -d proteins.fasta -o results.xml --format xml`
**Explanation:** `--format xml` outputs results in XML format.

### Verbose mode
**Args:** `sampei -i spectra.mzML -d proteins.fasta -o results.txt -v`
**Explanation:** `-v` verbose output with detailed information.

### Decoy database
**Args:** `sampei -i spectra.mzML -d proteins.fasta -o results.txt --decoy`
**Explanation:** `--decoy` generates decoy database for FDR estimation.
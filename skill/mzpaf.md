---
name: mzpaf
category: formatting
description: mzPAF - HUPO-PSI Peptide peak annotation format library
tags: [mzpaf, formatting, peptide, peak-annotation, hupo-psi, proteomics]
author: oxo-call-community
source_url: "https://github.com/HUPO-PSI/mzPAF"
---

## Concepts

- **Tool Overview**: mzPAF v0.2.0b0 is the HUPO-PSI (Human Proteome Organization - Proteomics Standards Initiative) standard library for peptide peak annotation format. It provides tools for reading, writing, and validating peptide fragmentation spectra annotations.
- **Core Function**: Implements the mzPAF format specification for representing peptide fragmentation data including peak lists, fragment ion annotations, charge states, and neutral losses.
- **Format Specification**: mzPAF (mass spectrometry Peak Annotation Format) standardizes how peptide fragment peaks and their annotations are stored, enabling interoperability between proteomics tools and databases.
- **Input Format**: Accepts mzPAF format files containing annotated fragment ion spectra. Can also import from other proteomics formats with conversion.
- **Output**: Produces validated mzPAF files with properly annotated peaks and associated metadata including peptide sequence, charge, and fragmentation method.
- **Use Case**: Proteomics analysis pipelines, peptide identification validation, fragmentation pattern analysis, and standardized spectrum annotation sharing.

## Pitfalls

- **Beta Version**: This is a beta release (v0.2.0b0). API and format may change before stable release.
- **Format Validation**: Not all proteomics tools produce fully compliant mzPAF files. Validation before sharing is recommended.
- **Fragment Ion Types**: Different fragmentation methods (CID, HCD, ETD) have different ion types. Ensure correct ion annotation conventions.
- **Peak Intensity**: Intensity values should be properly normalized for cross-sample comparisons.
- **Metadata Completeness**: Minimum required metadata fields must be present for valid mzPAF files.
- **Compatibility**: Check tool compatibility before converting between mzPAF and other formats.

## Examples

### Validate mzPAF file
**Args:** `-i spectrum.mzpaf --validate`
**Explanation:** Validates that the mzPAF file conforms to the HUPO-PSI specification.

### Convert to mzPAF from MGF
**Args:** `-i spectrum.mgf -o converted.mzpaf`
**Explanation:** Converts from MGF (Mascot Generic Format) to mzPAF format.

### Display format information
**Args:** `--info`
**Explanation:** Shows details about mzPAF format specification and requirements.

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage instructions.

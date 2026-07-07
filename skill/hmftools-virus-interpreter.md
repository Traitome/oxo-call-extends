---
name: hmftools-virus-interpreter
category: variant-calling
description: Post-processes VIRUSBreakend summary results by adding annotation, interpretation, and filtering for oncoviral reporting.
tags: [hmftools-virus-interpreter, virus, viral-integration, oncovirus, HPV, EBV, VIRUSBreakend, cancer, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/virus-interpreter/README.md"
---

## Concepts

- **Tool Overview**: Virus Interpreter (v1.7.2) is a post-processing tool for VIRUSBreakend output that adds taxonomic annotation, clinical interpretation, and reporting filters for oncoviral detection. It takes the VIRUSBreakend summary file and produces an annotated TSV report identifying clinically relevant viral integrations in tumor samples.

- **Taxonomic Annotation**: Virus Interpreter resolves the reference taxid for each detected virus by looking up the NCBI taxonomy database to find the matching virus name. This ensures consistent virus naming across samples and batches, handling cases where VIRUSBreakend may report multiple related taxids for the same viral species.

- **Clinical Interpretation Framework**: The tool maps detected viruses to clinical categories defined in the reporting database: HPV, EBV, MCV (Merkel cell polyomavirus), HBV (Hepatitis B), and HHV-8 (Kaposi's sarcoma-associated herpesvirus). Within the Hartwig pipeline, all clinically relevant HPV species are mapped to "HPV" for simplified clinical reporting.

- **Reporting Criteria for Viruses**: A virus is flagged as reported (potentially a driver) if: (1) QC status is not LOW_VIRAL_COVERAGE, (2) species is in the reporting database, (3) at least 1 integration site is detected. For EBV, additional requirements include >90% viral genome coverage and coverage higher than expected clonal mean. For viruses without integration sites, reportability requires >90% coverage and QC status that is not FAIL_CONTAMINATION or FAIL_NO_TUMOR.

- **Driver Likelihood Annotation**: Viruses in the reporting database receive a driver likelihood annotation (HIGH/LOW) based on clinical evidence. Viruses that don't meet reporting criteria receive UNKNOWN. Viruses not in the reporting database are annotated with UNKNOWN as their clinical significance cannot be assessed.

- **Integration Site Detection**: VIRUSBreakend (and consequently Virus Interpreter) detects viral integration events by identifying reads that span both viral and human genomic sequences. These discordant read pairs and split reads indicate where the virus has integrated into the host genome, which is critical for assessing oncogenic potential.

## Pitfalls

- **VIRUSBreakend Dependency**: Virus Interpreter requires output from VIRUSBreakend. Without running VIRUSBreakend first, Virus Interpreter has no input. Ensure VIRUSBreakend completes successfully and produces a valid summary file before running Virus Interpreter.

- **NCBI Taxonomy Database Access**: Virus Interpreter performs taxonomic lookups to resolve virus names. If the taxonomy database is outdated or inaccessible, annotation may fail or produce incorrect virus names. Ensure network access to NCBI for database queries.

- **Low Viral Coverage Samples**: Samples with insufficient viral sequencing depth may produce unreliable results. If QC status is LOW_VIRAL_COVERAGE, the virus will not be reported regardless of integration detection. Consider re-sequencing or enrichment for viral targets if clinical suspicion is high.

- **Reference Database Limitations**: The reporting database defines which viruses are considered clinically relevant. Viruses not in the database (e.g., novel viruses or less common pathogens) will not receive driver likelihood annotations. Custom database files may be needed for research applications.

- **Sample Quality Issues**: Contaminated samples or samples with insufficient tumor content (FAIL_CONTAMINATION or FAIL_NO_TUMOR QC) may have unreliable viral detection results. Always check sample QC metrics before interpreting viral findings.

- **Genome Build Consistency**: VIRUSBreakend and Virus Interpreter should be run with the same genome reference build (GRCh37 or GRCh38). Mixing builds causes coordinate mismatches between viral and human sequence alignments.

## Examples

### Run Virus Interpreter with VIRUSBreakend output
**Args:** `virus-interpreter -sample tumor1 -virus_breakend_dir ./virusbreakend/ -output_dir ./virus_interpreter/`
**Explanation:** Standard Virus Interpreter run using VIRUSBreakend output directory. The tool reads the summary file and produces annotated output with clinical interpretations for all detected viruses.

### Specify custom reporting database
**Args:** `virus-interpreter -sample tumor1 -virus_breakend_dir ./virusbreakend/ -reporting_db custom_virus_reporting.tsv -output_dir ./virus_interpreter/`
**Explanation:** Uses a custom reporting database instead of the default HMF database. Custom databases can add or remove viruses from clinical consideration for research or specific cohort studies.

### Enable blacklisting for specific viruses
**Args:** `virus-interpreter -sample tumor1 -virus_breakend_dir ./virusbreakend/ -blacklist HIV -output_dir ./virus_interpreter/`
**Explanation:** Blacklists HIV from reporting. HIV is often detected as a passenger virus in immunocompromised patients but is not typically a driver in cancer analysis. Blacklisting prevents it from appearing in clinical reports.

### Process with GRCh38 reference
**Args:** `virus-interpreter -sample tumor1 -virus_breakend_dir ./virusbreakend_grch38/ -ref_genome_version V38 -output_dir ./virus_interpreter/`
**Explanation:** Runs Virus Interpreter on GRCh38-aligned VIRUSBreakend output. Ensure all VIRUSBreakend files were generated with GRCh38 reference for consistent coordinates.

### Generate annotated output TSV
**Args:** `virus-interpreter -sample tumor1 -virus_breakend_dir ./virusbreakend/ -output_dir ./virus_interpreter/ && cat ./virus_interpreter/virus.annotated.tsv`
**Explanation:** Runs Virus Interpreter and displays the annotated output file. The output contains one line per detected virus with fields including taxid, name, qcStatus, integrations, interpretation, percentageCovered, meanCoverage, driverLikelihood, and reported status.

### Filter for high-confidence viral findings
**Args:** `grep -E "reported.*true|driverLikelihood.*HIGH" ./virus_interpreter/virus.annotated.tsv | head -20`
**Explanation:** Filters the annotated output for high-confidence viral findings. Shows only viruses marked as reported or with HIGH driver likelihood for clinical review.

### Interpret sample as HPV positive or negative
**Args:** `awk -F'\t' '$1 ~ /taxid/ || $4 == "HPV"' ./virus_interpreter/virus.annotated.tsv`
**Explanation:** Extracts HPV-specific results from the annotated output. If any HPV taxid is present and reported, the sample is considered HPV positive for clinical decision support.

---
name: annosine2
category: annotation
description: AnnoSINE_v2 - De novo SINE annotation tool for plant and animal genomes
tags: [sine, transposable-element, annotation, repeat, plant, animal]
author: oxo-call-community
source_url: "https://github.com/liaoherui/AnnoSINE_v2"
---

## Concepts

- **Tool Overview**: AnnoSINE_v2 annotates Short Interspersed Nuclear Elements (SINEs) in plant and animal genomes using homology-based, structure-based, or hybrid methods. Version 2.0.9.
- **SINE Detection**: Identifies SINE transposable elements by detecting characteristic features: tRNA-derived regions, RNA polymerase III promoters, target site duplications (TSDs).
- **Three Modes**: Mode 1 (homology-based), Mode 2 (structure-based), Mode 3 (hybrid combining both approaches). Mode 3 recommended for comprehensive annotation.
- **Animal Support**: v2 adds animal pHMMs for SINE detection in animal genomes (v1 was plant-focused). Can use both plant and animal models simultaneously.
- **HMM/BLAST Search**: Uses HMMER for profile HMM searches and BLAST for sequence similarity. Adjustable E-value thresholds for sensitivity control.
- **Copy Number Filtering**: Filters candidates based on minimum copy number (--copy_number default 20) to avoid false positives from unique sequences.
- **RepeatMasker Integration**: Automatically runs RepeatMasker on full genome using non-redundant SINE library for final annotation.

## Pitfalls

- **IRF Path**: IRF (Inverted Repeat Finder) executable must be in PATH or specified with --irf_path. Required for structure-based detection.
- **Memory Requirements**: Large genomes require substantial memory for BLAST searches. Use --num_alignments to limit memory usage.
- **Runtime**: Full annotation can take hours for large genomes. Use --automatically_continue to resume interrupted runs.
- **E-value Thresholds**: Default E-values (1e-10) may be too stringent for divergent SINEs. Relax with -e 0.01 for broader detection.
- **Copy Number Threshold**: Default --copy_number 20 may miss low-copy SINE families. Lower threshold (--copy_number 10) for sensitive detection but increases false positives.
- **Temporary Files**: Large temporary files created in /tmp. Use --temp_dir to specify alternative location with more space.

## Examples

### Hybrid mode annotation (recommended)
**Args:** `AnnoSINE_v2 3 genome.fa output.gff --threads 36`
**Explanation:** Mode 3 hybrid method combining homology and structure-based detection. Most comprehensive for unknown SINE families. 36 threads for parallel processing.

### Homology-based annotation
**Args:** `AnnoSINE_v2 1 genome.fa output.gff --hmmer_evalue 1e-5 --blast_evalue 1e-5 --threads 24`
**Explanation:** Mode 1 homology-based detection only. Relaxed E-values (1e-5) for detecting divergent SINEs. Faster than hybrid mode but may miss novel SINEs.

### Structure-based annotation
**Args:** `AnnoSINE_v2 2 genome.fa output.gff --copy_number 15 --threads 16`
**Explanation:** Mode 2 structure-based detection using IRF to find inverted repeats. Lower copy threshold (15) for sensitive detection. Good for genomes with poorly characterized SINEs.

### Animal genome annotation
**Args:** `AnnoSINE_v2 3 animal_genome.fa output.gff --animal 1 --threads 32`
**Explanation:** Uses animal-specific pHMMs (--animal 1) for SINE detection in animal genomes. Essential for non-plant genomes as v1 plant models miss animal SINEs.

### Combined plant and animal models
**Args:** `AnnoSINE_v2 3 mixed_genome.fa output.gff --animal 2 --threads 40`
**Explanation:** Uses both plant and animal pHMMs (--animal 2) simultaneously. Useful for genomes with diverse SINE families or unknown origin.

### Sensitive detection for divergent SINEs
**Args:** `AnnoSINE_v2 3 genome.fa output.gff -e 0.01 -minc 1 -s 150 --threads 24`
**Explanation:** Very relaxed parameters: E-value 0.01, minimum copy number 1, max shift 150bp. Maximum sensitivity for highly divergent or rare SINEs. Use cautiously.

### Resume interrupted run
**Args:** `AnnoSINE_v2 3 genome.fa output.gff --automatically_continue 1 --threads 36`
**Explanation:** Resumes from last completed step if previous run was interrupted. Saves time for long-running annotations on large genomes.

### Generate visualization figures
**Args:** `AnnoSINE_v2 3 genome.fa output.gff --figure y --threads 24`
**Explanation:** Outputs MSA alignment figures and copy number distribution plots. Useful for visual inspection of SINE families and quality assessment.
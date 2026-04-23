---
name: arriba
category: variant-calling
description: Arriba - Fast and accurate gene fusion detection from RNA-Seq data based on STAR chimeric alignments
tags: [gene-fusion, rna-seq, cancer, transcriptomics, chimeric-reads]
author: oxo-call-community
source_url: "https://github.com/suhrig/arriba"
---

## Concepts

- **Tool Overview**: Arriba detects gene fusions from RNA-Seq data using chimeric alignments from STAR aligner. Winner of DREAM SMC-RNA Challenge for fusion detection accuracy. Version 2.5.1.
- **Speed**: Post-alignment runtime typically ~2 minutes. Ultrafast processing suitable for clinical research settings requiring rapid results.
- **STAR Integration**: Uses STAR's chimeric alignment output. Requires STAR with --chimOutType WithinBAM for proper fusion detection.
- **Clinical Focus**: Designed for clinical research with emphasis on sensitivity and short runtimes. Suitable for cancer research and precision oncology.
- **Filtering**: Built-in filters remove false positives from read-through transcripts, mapping artifacts, and common false positives.
- **Annotation**: Annotates fusions with known oncogenic fusions, functional predictions, and recurrence in cancer databases.
- **Visualization**: Generates fusion visualization plots showing breakpoints and supporting reads. Useful for validation and reporting.

## Pitfalls

- **STAR Parameters**: Requires specific STAR parameters (--chimOutType WithinBAM SoftClip). Incorrect STAR settings prevent fusion detection.
- **Reference Genome**: Must use same reference genome for STAR alignment and Arriba annotation. Mismatched references cause incorrect fusion annotation.
- **Expression Level**: Low expression of fusion transcripts reduces detection sensitivity. Ensure adequate RNA-seq depth (≥50M reads for cancer samples).
- **Known False Positives**: Some genes prone to false fusion calls due to genomic proximity or sequence similarity. Review Arriba's blacklist filters.
- **Complex Fusions**: Complex multi-gene fusions or fusions with large intronic regions may be missed or incorrectly reported.
- **Annotation Database**: Requires annotation file matching reference genome version. Outdated annotations miss novel or recently characterized fusions.

## Examples

### Basic fusion detection
**Args:** `arriba -x aligned.bam -o fusions.tsv -a annotations.gtf -g reference.fa`
**Explanation:** Detects fusions from STAR-aligned BAM file. Outputs fusion list with annotations. Requires STAR alignment with chimeric output enabled.

### Run with STAR alignment
**Args:** `STAR --chimOutType WithinBAM SoftClip --chimSegmentMin 12 --runThreadN 8 --genomeDir genome/ --readFilesIn R1.fq.gz R2.fq.gz --outFileNamePrefix star_; arriba -x star_Aligned.out.bam -o fusions.tsv -a annotations.gtf -g reference.fa`
**Explanation:** Complete workflow: STAR alignment with chimeric detection, then Arriba fusion calling. STAR parameters required for proper chimeric output.

### Generate fusion visualization
**Args:** `arriba -x aligned.bam -o fusions.tsv -a annotations.gtf -g reference.fa -p fusion_plots.pdf`
**Explanation:** Creates PDF visualization of detected fusions. Shows breakpoint positions, supporting reads, and gene structures. Useful for manual validation.

### Filter for known oncogenic fusions
**Args:** `arriba -x aligned.bam -o oncogenic.tsv -a annotations.gtf -g reference.fa --knownFusions known_fusions.txt`
**Explanation:** Uses custom known fusion list to prioritize or filter results. Focus on clinically relevant fusions. Useful for targeted cancer analysis.

### Adjust sensitivity thresholds
**Args:** `arriba -x aligned.bam -o fusions.tsv -a annotations.gtf -g reference.fa --minimumSupport 3 --minimumMappingQuality 20`
**Explanation:** Requires minimum 3 supporting reads and mapping quality ≥20. Stricter thresholds reduce false positives but may miss low-frequency fusions.

### Report all fusions including low-confidence
**Args:** `arriba -x aligned.bam -o all_fusions.tsv -a annotations.gtf -g reference.fa --reportAllFusions`
**Explanation:** Reports all candidate fusions including low-confidence calls. Useful for exploratory analysis when sensitivity is critical.

### Use blacklist to filter false positives
**Args:** `arriba -x aligned.bam -o filtered.tsv -a annotations.gtf -g reference.fa --blacklist blacklist.txt`
**Explanation:** Applies blacklist of known false positive gene pairs. Removes common artifacts from read-through transcripts and mapping errors. Recommended for clinical analysis.
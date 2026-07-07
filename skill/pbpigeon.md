---
name: pbpigeon
category: qc
description: pbpigeon provides PacBio transcript analysis toolkit.
tags: [pbpigeon, qc, pacbio, transcript, iso-seq]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pigeon"
---

## Concepts

- **Tool Overview**: pbpigeon analyzes PacBio transcripts.
- **Core Function**: Processes Iso-Seq transcript data.
- **Algorithm**: Uses transcript classification and filtering.
- **Input Format**: Accepts Iso-Seq alignments.
- **Output**: Produces classified transcripts.
- **Use Case**: Transcriptomics, gene annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Classification Accuracy**: May have classification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pigeon --help`
**Explanation:** Shows available options and usage instructions.

### Classify transcripts
**Args:** `pigeon classify -i alignments.bam -o classified.gff`
**Explanation:** Classifies transcripts from alignments.

### Filter transcripts
**Args:** `pigeon filter -i classified.gff -o filtered.gff`
**Explanation:** Filters classified transcripts.

### Verbose mode
**Args:** `pigeon -v classify -i alignments.bam -o classified.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pigeon -t 4 classify -i alignments.bam -o classified.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pigeon classify -i alignments.bam -o classified.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `pigeon report -i classified.gff -o report.html`
**Explanation:** Generates HTML report.
---
name: pbfusion
category: qc
description: pbfusion detects fusion genes from PacBio Iso-Seq data.
tags: [pbfusion, qc, fusion-gene, iso-seq]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbfusion"
---

## Concepts

- **Tool Overview**: pbfusion detects gene fusions.
- **Core Function**: Identifies fusion transcripts from Iso-Seq data.
- **Algorithm**: Uses alignment-based fusion detection.
- **Input Format**: Accepts Iso-Seq alignments.
- **Output**: Produces fusion gene calls.
- **Use Case**: Cancer genomics, transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **False Positives**: May produce false positive calls.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbfusion --help`
**Explanation:** Shows available options and usage instructions.

### Detect fusions
**Args:** `pbfusion -i alignments.bam -o fusions.txt`
**Explanation:** Detects fusion genes from alignments.

### With annotation
**Args:** `pbfusion -i alignments.bam -a annotations.gtf -o fusions.txt`
**Explanation:** Uses gene annotations for detection.

### Verbose mode
**Args:** `pbfusion -v -i alignments.bam -o fusions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbfusion -t 4 -i alignments.bam -o fusions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbfusion -i alignments.bam -o fusions.bed --bed`
**Explanation:** Outputs in BED format.

### Filter fusions
**Args:** `pbfusion -i alignments.bam -o fusions.txt --min-support 5`
**Explanation:** Filters by minimum support reads.
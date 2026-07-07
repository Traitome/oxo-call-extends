---
name: fqgrep
category: formatting
description: Search a pair of fastq files for reads that match a given ref or alt sequence.
tags: [fqgrep, FASTQ, sequence search, variant calling]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/fqgrep"
---

## Concepts
- **FASTQ Sequence Search**: Searches FASTQ files for specific sequences.
- **Reference/Alternative Matching**: Identifies reads matching reference or alternative alleles.
- **Paired-End Support**: Works with paired-end read data.
- **Variant Detection**: Useful for targeted variant detection.
- **Quality Filtering**: Filters reads based on quality scores.

## Pitfalls
- **Sequence Specificity**: Requires exact or near-exact sequence matches.
- **Read Length**: May miss variants in reads shorter than the search sequence.
- **Ambiguity Handling**: Does not handle ambiguous bases well.
- **Performance**: Slower on very large FASTQ files.
- **Output Volume**: May generate large output files for high-frequency variants.

## Examples
### Search for reference allele
**Args:** `fqgrep --ref ATCG --alt TAGC -1 reads_R1.fastq -2 reads_R2.fastq -o matched.fastq`
**Explanation:** Searches for reads matching either reference or alternative sequence.

### Search with quality filter
**Args:** `fqgrep --ref ATCG --alt TAGC -1 reads_R1.fastq -2 reads_R2.fastq -o matched.fastq -q 30`
**Explanation:** Filters reads with minimum quality score of 30.

### Single-end search
**Args:** `fqgrep --ref ATCG -1 reads.fastq -o matched.fastq`
**Explanation:** Searches single-end reads for the reference sequence.

### Output unmapped reads
**Args:** `fqgrep --ref ATCG --alt TAGC -1 reads_R1.fastq -2 reads_R2.fastq -o matched.fastq --unmatched unmatched.fastq`
**Explanation:** Outputs both matched and unmatched reads.

### Allow mismatches
**Args:** `fqgrep --ref ATCG --alt TAGC -1 reads_R1.fastq -2 reads_R2.fastq -o matched.fastq -m 2`
**Explanation:** Allows up to 2 mismatches in the search sequence.
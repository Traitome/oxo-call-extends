---
name: bioawk
category: utility
description: BWK awk modified for biological data processing
tags: [awk, bioinformatics, text-processing, sequence]
author: oxo-call-community
source_url: "https://github.com/lh3/bioawk"
---

## Concepts
- **Tool Overview**: bioawk is an extension of BWK awk modified for biological data processing. It adds built-in parsing for common bioinformatics formats (FASTA, FASTQ, BED, GFF, VCF, SAM).
- **Format Support**: Automatically parses FASTA/FASTQ (name, seq, qual, comment), BED, GFF, VCF, and SAM records into awk fields.
- **Built-in Functions**: Provides bioinformatics-specific functions like reverse complement, GC content calculation, and sequence length.
- **Streaming**: Processes bioinformatics files in streaming mode, ideal for large datasets.

## Pitfalls
- **Field Semantics**: Field meanings differ by format (e.g., $1 is chromosome in BED, but ID in FASTA).
- **Not a Replacement**: bioawk complements but doesn't replace specialized tools for complex operations.

## Examples
### Count sequences in FASTA
**Args:** `bioawk -c fastx 'END{print NR}' sequences.fa`
**Explanation:** Counts the number of sequences in a FASTA file.

### Calculate GC content
**Args:** `bioawk -c fastx '{print $name, gc($seq)}' input.fa`
**Explanation:** Prints sequence name and GC content for each FASTA record.

### Extract sequences by length
**Args:** `bioawk -c fastx 'length($seq)>1000{print ">"$name"\n"$seq}' input.fa`
**Explanation:** Filters FASTA sequences longer than 1000bp.

### Reverse complement
**Args:** `bioawk -c fastx '{print ">"$name"\n"revcomp($seq)}' input.fa`
**Explanation:** Outputs reverse complement of each sequence.

### Extract specific BED columns
**Args:** `bioawk -c bed '{print $chrom, $start, $end, $name}' regions.bed`
**Explanation:** Prints selected columns from a BED file.

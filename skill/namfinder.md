---
name: namfinder
category: alignment
description: NAMfinder - Find Non-overlapping Approximate Matches using strobemers
tags: [namfinder, alignment, strobemers, approximate-matching, sequence]
author: oxo-call-community
source_url: "https://github.com/ksahlin/namfinder"
---

## Concepts

- **Tool Overview**: NAMfinder v0.1.3 (Non-overlapping Approximate Match Finder) identifies approximate sequence matches between query and reference sequences using strobemer technology for efficient seeding.
- **Core Function**: Finds non-overlapping approximate matches (NAMs) between query sequences and a reference, enabling fast similarity search without the overhead of full dynamic programming alignment.
- **Algorithm**: Uses strobemers (heterogeneous k-mers with灵活的 positions) as seeds for alignment. These allow faster and more sensitive approximate matching compared to traditional fixed-position k-mers.
- **Input Format**: Accepts query sequences in FASTA/FASTQ format and a reference genome in FASTA format. Both can be gzipped.
- **Output**: Produces tabular output (TSV/CSV) containing match coordinates, alignment coordinates, similarity scores, and match length for each NAM found.
- **Use Case**: Fast sequence similarity search, genome skimming for species identification, quickly finding approximate matches in large reference databases, and seed generation for further alignment.

## Pitfalls

- **Seed Sensitivity**: Low sensitivity settings may miss divergent matches. High sensitivity increases computational cost.
- **Match Overlap**: The "non-overlapping" constraint means overlapping matches are merged or reported separately depending on settings.
- **Reference Size**: Very large references increase memory usage. Indexing may take significant time for large genomes.
- **Strobemer Parameters**: Default strobemer parameters work for many cases but may need tuning for specific similarity requirements.
- **Quality Scores**: FASTQ quality scores are not considered in matching, only sequence content.
- **Short Queries**: Very short query sequences may not contain sufficient strobemer seeds for reliable matching.

## Examples

### Basic NAM finding
**Args:** `-q query.fasta -r reference.fasta -o nams.tsv`
**Explanation:** Standard NAM finding workflow. Searches query sequences against reference and outputs matches.

### Adjust identity threshold
**Args:** `-q sample.fa -r ref.fa -o results.tsv -id 0.85`
**Explanation:** Only reports matches with at least 85% sequence identity.

### Set minimum match length
**Args:** `-q input.fasta -r genome.fa -o matches.tsv -ml 100`
**Explanation:** Filters out matches shorter than 100bp to focus on substantial alignments.

### Use multiple threads
**Args:** `-q queries.fa -r reference.fa -o output.tsv -t 8`
**Explanation:** Uses 8 threads to accelerate processing on multi-core systems.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.

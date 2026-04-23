---
name: ampliconsplitter
category: assembly
description: Split highly similar collapsed amplicons to recover all amplicons from long-read sequencing
tags: [amplicon, splitting, long-read, nanopore, haplotype, assembly]
author: oxo-call-community
source_url: "https://github.com/RolandFaure/AmpliconSplitter"
---

## Concepts

- **Tool Overview**: AmpliconSplitter separates highly similar amplicons that were incorrectly collapsed into a single consensus sequence (~95-96% similarity threshold). Version 1.9.22.
- **Long-Read Focused**: Designed for ONT and other long-read technologies where amplicons may be merged during assembly due to high similarity.
- **Haplotype Recovery**: Recovers distinct haplotypes/amplicons from collapsed assemblies by leveraging read-level variation information.
- **Core Workflow**: Takes reference amplicon(s) and long reads, performs local reassembly with variation-aware splitting, outputs separated amplicons.
- **Polishing Options**: Supports racon (fast) or medaka (more accurate but slower) for polishing separated sequences.
- **SNP Rescue**: Can automatically recognize SNPs shared by specific proportion of reads as real variants rather than errors.
- **Memory Management**: Offers low-memory mode for resource-constrained environments at the cost of speed.

## Pitfalls

- **Compiler Version**: Requires gcc >= 11.2.0 for compilation. Older compilers cause build failures.
- **Dependency Paths**: If minimap2, racon, medaka, or samtools are not in PATH, must specify with `--path_to_*` options.
- **Read Quality**: Low-quality long reads may cause splitting failures. Use `--min-read-quality` to filter poor quality reads.
- **Memory Usage**: Default mode uses significant memory for large datasets. Enable `--low-memory` if needed.
- **Polisher Choice**: Medaka is more accurate but much slower than racon. Choose based on accuracy requirements vs time constraints.
- **Similarity Limit**: Works best for amplicons around 95-96% similarity. Very high similarity (>98%) may not split well.

## Examples

### Basic amplicon splitting
**Args:** `python ampliconsplitter.py -f reads.fastq -r collapsed_amplicons.fa -o output_dir/`
**Explanation:** Standard usage: splits collapsed amplicons using long reads. Outputs separated amplicons to output_dir/ampliconsplitter_final_amplicons.fa.

### Use medaka for higher accuracy
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ -p medaka -t 8`
**Explanation:** Uses medaka polisher (more accurate) with 8 threads. Slower but produces higher-quality separated sequences. Recommended for final analysis.

### Filter low-quality reads
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ -q 10`
**Explanation:** Filters reads with average quality below Q10 before processing. Improves results for noisy long-read data.

### Enable SNP rescue for known variants
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ -u 0.25`
**Explanation:** Automatically treats SNPs shared by >=25% of reads as real variants. Useful when true variants are known to exist at moderate frequency.

### Resume interrupted run
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ --resume`
**Explanation:** Resumes from a previously interrupted run. Useful for long-running analyses that were stopped.

### Low memory mode
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ -l -t 4`
**Explanation:** Enables low-memory mode with 4 threads. Trades speed for reduced memory footprint. Essential for memory-limited systems.

### Specify custom tool paths
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ --path_to_minimap2 /usr/local/bin/minimap2 --path_to_racon /opt/racon/bin/racon`
**Explanation:** Specifies custom paths for dependencies not in system PATH. Required when tools are installed in non-standard locations.

### Debug mode for troubleshooting
**Args:** `python ampliconsplitter.py -f reads.fastq -r amplicons.fa -o output/ -d --no_clean`
**Explanation:** Enables debug mode and keeps temporary files for inspection. Useful for diagnosing splitting failures or unexpected results.

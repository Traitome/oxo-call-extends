---
name: lace
category: assembly
description: Builds SuperTranscripts - linear representations of transcriptome data
tags: [lace, assembly, SuperTranscript, transcriptome, long-read, RNA-seq]
author: oxo-call-community
source_url: "https://github.com/Oshlack/Lace"
---

## Concepts

- **SuperTranscript**: Creates linear representation of alternative splicing
- **Transcriptome Assembly**: Assembles transcriptome from RNA-seq data
- **Alternative Splicing**: Handles alternatively spliced transcripts
- **Graph-based**: Builds splice graphs from read alignments
- **Linear Representation**: Converts graphs to linear sequences
- **Long-read Support**: Works with both short and long reads

## Pitfalls

- **Input Quality**: Requires high-quality alignment files
- **Gene Annotation**: Benefits from existing gene annotations
- **Alternative Splicing**: Complex splicing may not resolve fully
- **Computational Resources**: Large transcriptomes need significant memory
- **Parameter Tuning**: May need optimization for different data types
- **Isoform Resolution**: Difficult to resolve all isoforms accurately

## Examples

### Assemble SuperTranscript
**Args:** `lace_runner.py config.cfg`
**Explanation:** Runs LACE assembly with configuration file.

### Specify output directory
**Args:** `lace_runner.py config.cfg -o output/`
**Explanation:** Specifies output directory for results.

### Use annotation guide
**Args:** `lace_runner.py config.cfg -a annotation.gtf`
**Explanation:** Uses annotation to guide assembly.

### Set minimum coverage
**Args:** `lace_runner.py config.cfg --min-cov 5`
**Explanation:** Sets minimum coverage threshold of 5.

### Export splice graph
**Args:** `lace_runner.py config.cfg --export-graph`
**Explanation:** Exports splice graph visualizations.

### Paired-end mode
**Args:** `lace_runner.py config_pe.cfg`
**Explanation:** Processes paired-end sequencing data.
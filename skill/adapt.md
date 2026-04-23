---
name: adapt
category: utility
description: Activity-informed design tool for nucleic acid diagnostics, optimized for CRISPR-Cas13a detection systems
tags: [diagnostics, crispr, primer-design, cas13a, viral-detection, guide-design]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/adapt"
---

## Concepts

- **Tool Overview**: ADAPT (Activity-informed Design with All-inclusive Patrolling of Targets) designs nucleic acid diagnostics for viruses, particularly suited for Cas13a-based detection systems like SHERLOCK.
- **Core Function**: Designs optimal primer pairs and guide RNA sequences for viral detection by maximizing predicted activity and coverage across viral diversity.
- **Input/Output**: Input: FASTA sequences or NCBI taxonomy IDs. Output: TSV files with primer sequences, guide sequences, and predicted activity scores.
- **Machine Learning**: Uses trained models to predict Cas13a guide activity, enabling optimization for detection sensitivity.
- **Installation**: Install via bioconda: `conda install -c bioconda adapt`

## Pitfalls

- **Python Version**: Requires Python 3.8 with specific dependency versions (NumPy <1.19.0, TensorFlow 2.3.2).
- **MAFFT Required**: Multiple sequence alignment requires MAFFT - ensure it's installed and in PATH.
- **Memory Intensive**: Processing large viral genome sets requires significant memory for alignment and optimization.
- **Model Selection**: Use `--predict-cas13a-activity-model` for Cas13a systems; custom models available for other platforms.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available search types, input formats, and all command line options.

### Design guides with sliding window approach
**Args:** `sliding-window fasta viral_sequences.fasta -o probes.tsv --obj minimize-guides -w 200 -gl 28 -gm 1 -gp 0.95`
**Explanation:** Designs 28nt guides in 200nt sliding windows, allowing 1 mismatch, covering 95% of sequences without activity prediction.

### Design complete targets with Cas13a model
**Args:** `complete-targets auto-from-args 64320 None guides.tsv --obj maximize-activity -gl 28 -pl 30 --predict-cas13a-activity-model --best-n-targets 5`
**Explanation:** Designs primers and guides for Zika virus (taxid 64320) using Cas13a activity prediction, outputs top 5 designs.

### Design with specificity filtering
**Args:** `complete-targets fasta sequences.fasta -o design.tsv --specific-against-fastas human.fasta bacteria.fasta --id-m 4`
**Explanation:** Designs probes specific to viral sequences, avoiding cross-reactivity with human and bacterial genomes (4 mismatches allowed for specificity).

### Design with custom coverage requirements
**Args:** `complete-targets fasta viral.fasta -o design.tsv -pp 0.98 -pm 0 -gp 0.99 -gm 1`
**Explanation:** Designs with strict coverage: primers cover 98% diversity (0 mismatches), guides cover 99% (1 mismatch allowed).

### Process multiple viruses from file
**Args:** `complete-targets auto-from-file virus_list.tsv output_dir/ --obj maximize-activity --predict-cas13a-activity-model`
**Explanation:** Batch processes multiple viruses listed in TSV file, creating separate output directories for each.

### Design with sampling for large datasets
**Args:** `complete-targets auto-from-args 11137 None guides.tsv --sample-seqs 100 --cluster-threshold 0.15 --predict-cas13a-activity-model`
**Explanation:** Designs for influenza A (taxid 11137) using 100 sampled sequences and clustering to handle diversity.

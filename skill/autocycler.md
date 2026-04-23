---
name: autocycler
category: assembly
description: Autocycler - Tool for generating consensus long-read assemblies for bacterial genomes
tags: [bacterial-genomics, long-read-assembly, consensus-assembly, nanopore, pacbio]
author: oxo-call-community
source_url: "https://github.com/rrwick/Autocycler"
---

## Concepts

- **Tool Overview**: Autocycler generates high-quality consensus assemblies for bacterial genomes by combining multiple alternative assemblies from the same long-read dataset. It is the successor to Trycycler and designed for automated, large-scale processing.

- **Consensus Approach**: Works by compressing input assemblies into a compact De Bruijn graph, clustering similar sequences, trimming overlaps, and resolving ambiguities to produce a final consensus assembly.

- **Assembly Requirements**: Requires multiple complete (or nearly complete) assemblies of the same genome from different assemblers or different read subsets. Works best when most input assemblies are circular/complete.

- **Automated Pipeline**: Designed for full automation without manual intervention, making it suitable for processing hundreds or thousands of bacterial genomes.

- **Problem Resolution**: Addresses common assembly issues including circularization failures, missing small plasmids, false positive contigs, fragmentation, and medium-to-large scale indel errors.

- **Quality Improvement**: Produces more accurate assemblies than any single assembler by leveraging the consensus of multiple independent assembly attempts.

- **Long-Read Focus**: Specifically designed for long-read technologies (Oxford Nanopore, PacBio HiFi) where complete bacterial genomes are achievable.

## Pitfalls

- **Complete Assembly Requirement**: Autocycler works best when most input assemblies are complete. If unable to obtain complete assemblies due to long repeats, results may be suboptimal.

- **Input Diversity**: Requires multiple different assemblies (different assemblers or read subsets). Using identical or very similar assemblies provides no benefit.

- **Repeat Limitations**: Cannot resolve repeats longer than the read length, which is the fundamental limitation preventing complete assemblies.

- **Computational Resources**: Processing multiple assemblies and building De Bruijn graphs requires significant memory for large genomes or plasmids.

- **Plasmid Detection**: Small plasmids may be missed if they don't appear in most input assemblies. Ensure adequate coverage and assembly of small circular elements.

- **Species Suitability**: Designed primarily for bacterial genomes. Not suitable for eukaryotic genomes with complex repeat structures.

- **Assembly Order**: The order and naming of input assemblies can affect clustering and consensus building. Use consistent naming conventions.

## Examples

### Subsample reads for multiple assemblies
**Args:** `autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --count 10 --seed 42`
**Explanation:** Creates 10 subsampled read sets from input long reads, each with different random seed, to generate diverse assemblies.

### Compress input assemblies
**Args:** `autocycler compress --assembly assembly_1.fasta --assembly assembly_2.fasta --assembly assembly_3.fasta --out_dir compressed --threads 8`
**Explanation:** Compresses multiple input assemblies into a compact De Bruijn graph representation for downstream processing.

### Cluster similar sequences
**Args:** `autocycler cluster --input compressed --out_dir clustered --min_identity 95.0`
**Explanation:** Clusters similar sequences from compressed assemblies using 95% identity threshold to group homologous regions.

### Trim overlapping regions
**Args:** `autocycler trim --input clustered --out_dir trimmed`
**Explanation:** Trims overlapping regions between clustered sequences to prepare for consensus building.

### Resolve ambiguities
**Args:** `autocycler resolve --input trimmed --out_dir resolved --min_coverage 3`
**Explanation:** Resolves ambiguous regions by selecting the most supported path, requiring minimum 3 supporting assemblies.

### Combine into final consensus
**Args:** `autocycler combine --input resolved --out_dir final_assembly --min_length 1000`
**Explanation:** Combines resolved sequences into final consensus assembly, filtering out contigs shorter than 1000bp.

### Full pipeline with default parameters
**Args:** `autocycler subsample --reads reads.fastq.gz --out_dir step1 --count 8 && for i in step1/*.fastq.gz; do flye --nano-raw $i --out-dir asm_$(basename $i .fastq.gz) --genome-size 5m --threads 8; done && autocycler compress --assembly asm_*/assembly.fasta --out_dir step2 && autocycler cluster --input step2 --out_dir step3 && autocycler trim --input step3 --out_dir step4 && autocycler resolve --input step4 --out_dir step5 && autocycler combine --input step5 --out_dir final`
**Explanation:** Complete workflow: subsample reads, assemble each subset with Flye, then run through all Autocycler steps to produce consensus assembly.

### Generate dot plot for visualization
**Args:** `autocycler dotplot --assembly1 assembly_1.fasta --assembly2 assembly_2.fasta --output comparison.png`
**Explanation:** Creates dot plot comparing two assemblies to visualize structural differences and similarities.

### Clean intermediate files
**Args:** `autocycler clean --directory working_dir --keep_final`
**Explanation:** Removes intermediate files from working directory while preserving final output files to save disk space.

### Convert GFA to FASTA
**Args:** `autocycler gfa2fasta --input assembly.gfa --output assembly.fasta`
**Explanation:** Converts GFA format assembly graph to FASTA format for downstream analysis or submission to databases.

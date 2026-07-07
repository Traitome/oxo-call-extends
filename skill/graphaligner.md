---
name: graphaligner
category: bioinformatics
description: GraphAligner aligns long sequencing reads to assembly graphs, enabling accurate mapping of reads to complex genomic structures.
tags: [graphaligner, long-reads, assembly-graph, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/maickrau/GraphAligner"
---

## Concepts

- **Sequence-to-Graph Alignment**: GraphAligner aligns long sequencing reads directly to assembly graphs rather than linear references.

- **Graph Representation**: Uses assembly graphs to represent complex genomic structures including repeats and structural variants.

- **Long Read Support**: Optimized for long-read sequencing technologies like Oxford Nanopore and PacBio.

- **Gap Handling**: Handles gaps and structural variations in the graph during alignment.

- **Quality-aware Alignment**: Incorporates base quality scores into the alignment process.

- **Output Formats**: Supports various output formats including GAF (Graph Alignment Format) and SAM/BAM.

## Pitfalls

- **Graph Complexity**: Very complex assembly graphs can increase alignment time and memory usage.

- **Read Quality**: Low-quality reads may produce incorrect alignments. Preprocess reads carefully.

- **Graph Construction**: Results depend on the quality of the input assembly graph. Poorly constructed graphs will affect alignment.

- **Memory Requirements**: Aligning many reads to large graphs may require significant memory.

- **Parameter Tuning**: Adjust parameters based on read length, error rate, and graph complexity.

## Examples

### Align reads to graph
**Args:** `graphaligner -g assembly.gfa -r reads.fastq -o alignments.gaf`
**Explanation:** Aligns long reads to an assembly graph in GFA format.

### Output SAM format
**Args:** `graphaligner -g assembly.gfa -r reads.fastq -f sam -o alignments.sam`
**Explanation:** Outputs alignments in SAM format instead of GAF.

### Adjust alignment sensitivity
**Args:** `graphaligner -g assembly.gfa -r reads.fastq -s high -o alignments.gaf`
**Explanation:** Sets high sensitivity mode for more accurate but slower alignment.

### Filter low-quality alignments
**Args:** `graphaligner -g assembly.gfa -r reads.fastq -q 20 -o alignments.gaf`
**Explanation:** Only keeps alignments with quality score >= 20.

### Parallel processing
**Args:** `graphaligner -g assembly.gfa -r reads.fastq -t 8 -o alignments.gaf`
**Explanation:** Uses 8 threads for parallel alignment.

### Generate alignment statistics
**Args:** `graphaligner stats -i alignments.gaf -o stats.txt`
**Explanation:** Generates statistics about the alignments.

### Visualize alignments
**Args:** `graphaligner visualize -g assembly.gfa -a alignments.gaf -o visualization.png`
**Explanation:** Creates a visualization of reads aligned to the graph.
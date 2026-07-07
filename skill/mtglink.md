---
name: mtglink
category: assembly
description: MTG-link is a local assembly tool for linked-read data
tags: [mtglink, assembly, linked-reads, barcode, loci-assembly]
author: oxo-call-community
source_url: "https://github.com/anne-gcd/MTG-Link"
---

## Concepts

- **Tool Overview**: MTG-link v2.4.1 is a local assembly tool designed for linked-read sequencing technologies.
- **Core Function**: Assembles specific genomic loci using barcode information from linked-reads.
- **Input Requirements**: Requires linked-reads, target flanking sequences in GFA format, and indexed BAM file.
- **Output**: Produces assembled target sequences in FASTA format and assembly graph files.
- **Barcode Utilization**: Uses barcodes to subsample reads from flanking regions for improved assembly.
- **Applications**: Gap-filling, structural variant characterization, and alternative allele reconstruction.

## Pitfalls

- **Input Format**: Requires specific GFA format with segment elements (S lines) and gap elements (G lines).
- **BAM Indexing**: Input BAM file must be coordinate-sorted and indexed.
- **Barcode Quality**: Assemblies depend on barcode calling quality from the linked-read technology.
- **Memory Requirements**: Large target regions may require significant computational resources.
- **Dependency on External Tools**: Requires mindthegap, mummer, and other dependencies.
- **Species Specificity**: Optimized for regions with moderate complexity; highly repetitive regions may fail.

## Examples

### Basic local assembly
**Args:** `mtglink -i input.gaf -j links.txt -o output_dir`
**Explanation:** Assembles target loci using linked-read alignments and barcode information.

### Specify flanking sequences
**Args:** `mtglink -i alignments.bam -f flanking.gfa -o assembly_results`
**Explanation:** Uses pre-defined flanking sequences in GFA format for targeted assembly.

### Set minimum barcode count
**Args:** `mtglink -i input.bam -j barcodes.txt -o results --min-bc 10`
**Explanation:** Requires minimum barcode count threshold for read inclusion.

### Display help
**Args:** `mtglink --help`
**Explanation:** Shows all available options and usage information.

### Output assembly graph
**Args:** `mtglink -i aln.bam -j links.txt -o out --graph`
**Explanation:** Also outputs the assembly graph for downstream analysis.

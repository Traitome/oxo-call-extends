---
name: arcs
category: assembly
description: ARCS - Scaffold genome assemblies using linked reads (10x Genomics) or long reads (ONT/PacBio)
tags: [scaffolding, linked-reads, long-reads, 10x, assembly, genome]
author: oxo-call-community
source_url: "https://github.com/BirolLab/arcs"
---

## Concepts

- **Tool Overview**: ARCS (Assembly Recovery by Linked-read and long-read Scaffolding) scaffolds genome assembly drafts using linked reads (10x Genomics Chromium) or long reads (ONT/PacBio). Version 1.2.8.
- **Linked-Read Mode**: Uses barcode information from 10x Genomics linked reads to connect contigs. Barcodes from same DNA molecule link contigs from same genomic region.
- **Long-Read Mode**: Segments long reads and assigns synthetic barcodes to create pseudo-linked reads. Uses these for scaffolding without actual linked-read data.
- **Two Modes**: `arcs-linked` for 10x linked reads, `arcs-long` for ONT/PacBio long reads. Both use same underlying scaffolding algorithm.
- **Input Requirements**: Draft assembly (FASTA), aligned reads (BAM), and barcode information (linked-read mode) or long reads (long-read mode).
- **Output**: Scaffolded assembly with improved contiguity. Reports scaffold statistics and contig connections.
- **Integration**: Works with LINKS for additional scaffolding. Can be combined with other scaffolding tools for multi-stage improvement.

## Pitfalls

- **Barcode Coverage**: Low barcode coverage reduces scaffolding accuracy. Ensure adequate linked-read depth (>50x recommended).
- **Contig Length**: Short contigs (<1kb) may not scaffold well. Consider filtering very short contigs before scaffolding.
- **Misassembly Risk**: Incorrect barcode links can create misassemblies. Validate scaffolds with additional evidence (e.g., Hi-C, genetic maps).
- **Long-Read Quality**: Poor quality long reads reduce pseudo-linked read accuracy. Filter low-quality reads before scaffolding.
- **Memory Usage**: Large genomes with many contigs require substantial memory. Monitor memory for >10k contigs.
- **Chimeric Contigs**: Chimeric input contigs cause incorrect scaffolding. QC assembly before scaffolding.

## Examples

### Scaffold with 10x linked reads
**Args:** `arcs-linked -c assembly.fa -b linked_reads.bam -a barcodes.txt -o scaffolded.fa`
**Explanation:** Basic linked-read scaffolding. Uses barcode information to connect contigs. Outputs scaffolded assembly and connection statistics.

### Scaffold with long reads (ONT)
**Args:** `arcs-long -c assembly.fa -l ont_reads.fastq -o scaffolded.fa`
**Explanation:** Long-read scaffolding mode. Segments ONT reads to create pseudo-linked reads for scaffolding. Useful when linked-read data unavailable.

### Specify minimum barcode links
**Args:** `arcs-linked -c assembly.fa -b reads.bam -a barcodes.txt -o scaffolded.fa -l 5`
**Explanation:** Requires minimum 5 shared barcodes to scaffold contigs. Higher threshold increases confidence but may miss valid connections.

### Adjust contig length threshold
**Args:** `arcs-linked -c assembly.fa -b reads.bam -a barcodes.txt -o scaffolded.fa -s 2000`
**Explanation:** Only scaffolds contigs ≥2000bp. Filters short contigs that may produce unreliable links. Improves scaffold quality.

### PacBio HiFi long-read scaffolding
**Args:** `arcs-long -c assembly.fa -l hifi_reads.fastq -o scaffolded.fa -q 20`
**Explanation:** Uses high-quality PacBio HiFi reads (Q20). Higher quality threshold for pseudo-linked read creation. More accurate scaffolding.

### Multi-threaded processing
**Args:** `arcs-linked -c assembly.fa -b reads.bam -a barcodes.txt -o scaffolded.fa -t 16`
**Explanation:** Uses 16 threads for parallel processing. Significantly speeds up scaffolding for large genomes with many contigs.

### Generate detailed connection report
**Args:** `arcs-linked -c assembly.fa -b reads.bam -a barcodes.txt -o scaffolded.fa -r connections.txt`
**Explanation:** Outputs detailed report of all contig connections including barcode counts and confidence scores. Useful for manual validation.
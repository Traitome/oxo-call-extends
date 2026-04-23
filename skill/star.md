---
name: star
category: alignment
description: Spliced Transcripts Alignment to a Reference (STAR) — an ultrafast RNA-seq splice-aware aligner with support for fusion detection, long reads, and single-cell data.
tags: [star, alignment, rna-seq, splice-aware, fusion, single-cell, fastq, bam]
author: oxo-call-community
source_url: "https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf"
---

## Concepts

- **Tool Overview**: STAR (Spliced Transcripts Alignment to a Reference) is the gold-standard RNA-seq aligner, optimized for speed and accuracy for both bulk and single-cell RNA-seq. Version 2.7.11b.
- **CRITICAL - Long Options as Mode Selectors**: STAR does not use traditional subcommands. All operations are controlled by long options like `--runMode genomeGenerate` (index), `--runMode alignReads` (default alignment), `--runMode inputAlignmentsFromBAM` (re-alignment from BAM). The mode is set by `--runMode`, not by a positional subcommand.
- **Two-Step Workflow**: (1) Generate genome index with `--runMode genomeGenerate`; (2) Align reads with default `--runMode alignReads`. The genome index is large (~30 GB for human) and computed once.
- **Memory Requirements**: STAR loads the entire genome index into RAM. The human genome requires ~30 GB RAM. Use `--genomeSAindexNbases 11` for small genomes (<1 Gb) to avoid over-indexing.
- **Output Files**: STAR produces `Aligned.sortedByCoord.out.bam` (if `--outSAMtype BAM SortedByCoordinate`), `Log.final.out` (alignment summary), `SJ.out.tab` (splice junctions), and `Log.out`. The `--outFileNamePrefix` parameter sets a common prefix for all output files.
- **Two-Pass Alignment**: For better splice junction detection, use two-pass mode (`--twopassMode Basic`). First pass discovers splice junctions; second pass uses them for improved alignment. Essential for novel splice site detection.
- **Single-Cell Support**: STAR supports STARsolo for 10x Chromium, Drop-seq, and other droplet-based scRNA-seq with `--soloType Droplet --soloCBwhitelist`.
- **Installation**: `conda install -c bioconda star`

## Pitfalls

- **CRITICAL - No Subcommands**: STAR uses `--runMode` flags, not subcommands. `STAR genomeGenerate` is WRONG; `STAR --runMode genomeGenerate` is correct. The binary may be named `STAR` (uppercase), not `star`.
- **Genome Directory**: `--genomeDir` must point to a directory containing the STAR index, not to individual files. The index must be generated with the same STAR version being used.
- **genomeSAindexNbases for Small Genomes**: For genomes <1 Gb, set `--genomeSAindexNbases` to `min(14, log2(GenomeLength)/2 - 1)`. Failing to do this causes errors or poor memory usage.
- **BAM Output Not Sorted by Default**: Default output is `Aligned.out.sam` (unsorted SAM). Use `--outSAMtype BAM SortedByCoordinate` for a sorted BAM directly. Alternatively, pipe to samtools.
- **runThreadN For Both Steps**: Set `--runThreadN` for both genome generation and alignment steps. They are separate invocations and each needs threading specified.

## Examples

### Generate genome index
**Args:** `--runMode genomeGenerate --genomeDir star_genome_index/ --genomeFastaFiles reference.fa --sjdbGTFfile annotation.gtf --runThreadN 8 --sjdbOverhang 149`
**Explanation:** Builds STAR genome index. `--sjdbOverhang` should be read_length - 1 (e.g., 149 for 150 bp reads). Index is stored in `star_genome_index/` directory. Creates ~30 GB of files for human genome.

### Align paired-end RNA-seq reads
**Args:** `--runMode alignReads --genomeDir star_genome_index/ --readFilesIn R1.fastq.gz R2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix sample_ --runThreadN 8 --outSAMattributes NH HI AS NM MD`
**Explanation:** `--readFilesCommand zcat` to decompress gzipped inputs; `--outSAMtype BAM SortedByCoordinate` outputs sorted BAM directly; `--outFileNamePrefix sample_` prefixes all output files. Standard attributes NH/HI/AS/NM/MD needed by downstream tools.

### Two-pass alignment for better splice junction detection
**Args:** `--runMode alignReads --genomeDir star_genome_index/ --readFilesIn R1.fastq.gz R2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix sample_ --runThreadN 8 --twopassMode Basic`
**Explanation:** `--twopassMode Basic` enables 2-pass mode: STAR performs a first alignment pass to collect splice junctions, then rebuilds the index and re-aligns. Improves detection of novel junctions. Requires 2× the time but significantly improves accuracy.

### Align with gene counts (for bulk RNA-seq quantification)
**Args:** `--runMode alignReads --genomeDir star_genome_index/ --readFilesIn R1.fastq.gz R2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix sample_ --runThreadN 8 --quantMode GeneCounts --sjdbGTFfile annotation.gtf`
**Explanation:** `--quantMode GeneCounts` generates `ReadsPerGene.out.tab` with per-gene read counts (equivalent to HTSeq output). Columns 2-4 represent unstranded, forward-stranded, and reverse-stranded counts.

### Generate genome index for small genome
**Args:** `--runMode genomeGenerate --genomeDir small_genome_index/ --genomeFastaFiles small_ref.fa --sjdbGTFfile annotation.gtf --genomeSAindexNbases 11 --runThreadN 4`
**Explanation:** `--genomeSAindexNbases 11` adjusts SA index size for small genomes (<1 Gb). Use the formula min(14, floor(log2(genomeLength)/2 - 1)) to calculate the correct value.

### STARsolo for 10x Chromium single-cell RNA-seq
**Args:** `--runMode alignReads --genomeDir star_genome_index/ --readFilesIn cDNA_R2.fastq.gz Barcode_R1.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix sc_sample_ --soloType CB_UMI_Simple --soloCBwhitelist 3M-february-2018.txt --soloCBstart 1 --soloCBlen 16 --soloUMIstart 17 --soloUMIlen 12 --runThreadN 8`
**Explanation:** STARsolo mode for 10x Chromium v3 scRNA-seq. Note R2 (cDNA) comes first, R1 (barcode+UMI) second. `--soloCBwhitelist` is the 10x cell barcode whitelist. UMI starts at position 17 in R1 for v3 chemistry.

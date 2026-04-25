---
name: hisat2
category: alignment
description: A fast and sensitive alignment program for mapping next-generation sequencing reads to a population of human genomes and other genomes, supporting splice-aware alignment for RNA-seq.
tags: [hisat2, alignment, rna-seq, splice-aware, fastq, bam, genome]
author: oxo-call-community
source_url: "https://daehwankimlab.github.io/hisat2/manual/"
---

## Concepts

- **Tool Overview**: HISAT2 is a fast, memory-efficient splice-aware aligner for mapping reads to a reference genome, designed primarily for RNA-seq. It uses a graph-based index (GBM) that encodes both genomic sequence and known splice sites. Version 2.2.1.
- **Index Building**: Before alignment, build a genome index with `hisat2-build`. Pre-built indexes for common genomes (human, mouse, etc.) are available for download from the HISAT2 website. Use `hisat2-inspect` to verify index contents.
- **Splice-Aware Alignment**: HISAT2 is designed for RNA-seq: it discovers novel splice junctions and aligns reads spanning introns. For DNA alignment (WGS/WES/ChIP-seq), HISAT2 works but Bowtie2 or BWA-MEM may be more appropriate.
- **Output Format**: Default output is SAM to stdout. Always pipe to `samtools sort -o output.bam` and then `samtools index`. Use `--no-unal` to suppress unaligned reads from SAM output to reduce file size.
- **Known Splice Sites**: Provide known splice sites with `--known-splicesite-infile` (generated from a GTF by `hisat2_extract_splice_sites.py`) to improve alignment sensitivity for annotated transcripts.
- **Strandedness**: For strand-specific RNA-seq libraries, specify `--rna-strandness RF` (dUTP/reverse-stranded) or `--rna-strandness FR` (forward-stranded). Check library strandedness with RSeQC's `infer_experiment.py` if unsure.
- **Installation**: `conda install -c bioconda hisat2`

## Pitfalls

- **CRITICAL - Index Prefix Not File**: `-x genome_index` refers to the index prefix, not a file. If your index files are `genome.1.ht2`, `genome.2.ht2`, etc., the prefix is `genome`, not `genome.1.ht2`.
- **RAM Requirements**: HISAT2 requires ~8 GB RAM for the human genome index. Ensure sufficient memory before running on large genomes.
- **Strandedness Errors**: Using the wrong `--rna-strandness` setting will cause downstream tools (featureCounts, HTSeq) to miscount reads. Always verify library strandedness.
- **Novel vs Known Splice Sites**: Without a known splice site file, HISAT2 discovers splice sites de novo. Providing annotated splice sites significantly improves alignment of reads at annotated exon junctions.
- **Multiple Mappers**: By default, HISAT2 reports the best alignment per read. Use `-k N` to report up to N alignments per read or `--all` for all alignments. Downstream tools like StringTie prefer primary alignments.

## Examples

### Build a genome index
**Args:** `hisat2-build -p 8 reference.fa genome_index`
**Explanation:** Builds HISAT2 index from reference FASTA using 8 threads. Creates files `genome_index.1.ht2` through `genome_index.8.ht2`. Run only once per genome. Pre-built indexes are available for hg38, mm10, etc.

### Align paired-end RNA-seq reads
**Args:** `-x genome_index -1 R1.fastq.gz -2 R2.fastq.gz -p 8 --dta | samtools sort -@ 4 -o aligned.bam && samtools index aligned.bam`
**Explanation:** `-x` index prefix; `-1`/`-2` paired-end inputs; `-p 8` threads; `--dta` (downstream transcriptome assembly) adds XS strand tags required by StringTie/Cufflinks. Pipe directly to samtools sort+index.

### Align with known splice sites for better accuracy
**Args:** `-x genome_index -1 R1.fastq.gz -2 R2.fastq.gz -p 8 --known-splicesite-infile known_splicesites.txt --dta | samtools sort -@ 4 -o aligned.bam`
**Explanation:** Provides annotated splice sites to improve alignment of reads at known exon junctions. Generate `known_splicesites.txt` with: `hisat2_extract_splice_sites.py annotation.gtf > known_splicesites.txt`.

### Align strand-specific (reverse-stranded dUTP) library
**Args:** `-x genome_index -1 R1.fastq.gz -2 R2.fastq.gz -p 8 --rna-strandness RF --dta | samtools sort -@ 4 -o aligned_stranded.bam`
**Explanation:** `--rna-strandness RF` for reverse-stranded (dUTP/TruSeq Stranded) libraries. Use `FR` for forward-stranded libraries. This information is preserved in the BAM and used by featureCounts/HTSeq.

### Align single-end reads
**Args:** `-x genome_index -U reads.fastq.gz -p 8 --no-unal | samtools sort -@ 4 -o aligned.bam`
**Explanation:** `-U` for single-end (unpaired) reads; `--no-unal` suppresses unaligned reads from output, reducing BAM file size. Pipe to samtools for immediate sorting.

### Align with summary statistics saved to file
**Args:** `-x genome_index -1 R1.fastq.gz -2 R2.fastq.gz -p 8 --dta --summary-file alignment_summary.txt | samtools sort -@ 4 -o aligned.bam`
**Explanation:** `--summary-file` saves the alignment rate summary (total reads, aligned concordantly, discordantly, etc.) to a file for MultiQC parsing. Without this flag, summary prints to stderr only.

### Extract splice site statistics from GTF
**Args:** `hisat2_extract_splice_sites.py annotation.gtf > known_splicesites.txt && hisat2_extract_exons.py annotation.gtf > exons.txt`
**Explanation:** Helper scripts to prepare splice site and exon files from a GTF annotation. These files can be used with `--known-splicesite-infile` and `--novel-splicesite-outfile` to improve and annotate alignments.

---
name: cufflinks
category: expression
description: Cufflinks assembles transcripts, estimates abundances, and tests for differential expression from RNA-Seq alignments
tags: [cufflinks, expression, RNA-seq, transcriptome, assembly, FPKM, differential-expression]
author: oxo-call-community
source_url: "http://cole-trapnell-lab.github.io/cufflinks/"
---

## Concepts

- **Tool Overview**: Cufflinks (v2.2.1) assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples.
- **Core Function**: Takes aligned RNA-Seq reads (SAM/BAM), assembles them into parsimonious set of transcripts, and estimates relative abundances based on read support.
- **Input/Output**: Input: aligned SAM/BAM files from TopHat or other aligners. Output: transcripts.gtf, genes.fpkm_tracking, isoforms.fpkm_tracking in output directory
- **RABT Assembly**: Reference Annotation Based Transcript assembly uses known transcripts to guide assembly while discovering novel transcripts and isoforms
- **Library Types**: Supports ff-firststrand, ff-secondstrand, ff-unstranded, fr-firststrand, fr-secondstrand, fr-unstranded (default)
- **Bias Correction**: Can correct for fragment bias using reference genome FASTA to improve FPKM accuracy
- **Installation**: `conda install -c bioconda cufflinks`

## Pitfalls

- **Compatible Hits**: For accurate quantification, use `--compatible-hits-norm` to count only fragments compatible with reference transcripts
- **Multi-reads**: Use `-u/--multi-read-correct` to properly weight reads mapping to multiple genomic locations
- **Fragment Length**: Cufflinks learns fragment length from BAM headers for paired-end data; manual specification via `-m` is deprecated
- **GTF Format**: Output GTF uses a specific format with transcript_id, gene_id, and fpkm attributes
- **Memory**: Large genomes with many alignments require significant memory

## Examples

### Reference-guided assembly with known transcripts
**Args:** `-G annotation.gtf -p 8 -o cufflinks_output accepted_hits.bam`
**Explanation:** Use `-G` to strictly quantify against reference transcripts. Output includes FPKM values for each known transcript.

### De novo transcriptome assembly
**Args:** `-o cufflinks_output accepted_hits.bam`
**Explanation:** Assemble novel transcripts without guide annotation. Cufflinks will predict transcripts from the data alone.

### Reference-guided with bias correction
**Args:** `-g reference.gtf -b genome.fa -u -p 8 -o cufflinks_output accepted_hits.bam`
**Explanation:** Use `-b` for bias correction with genome FASTA, and `-u` for multi-read correction to improve accuracy.

### Assembly with mask file
**Args:** `-M mask.gtf -G annotation.gtf -p 8 -o cufflinks_output accepted_hits.bam`
**Explanation:** Use `-M` to ignore reads from rRNA or mitochondrial transcripts during assembly.

### Upper quartile normalization
**Args:** `-G annotation.gtf --library-norm-method quartile -p 8 -o cufflinks_output accepted_hits.bam`
**Explanation:** Use quartile normalization for better robustness with low-abundance genes.

### Filter low-abundance transcripts
**Args:** `-G annotation.gtf -F 0.05 -j 0.1 -p 8 -o cufflinks_output accepted_hits.bam`
**Explanation:** Use `-F` to suppress transcripts below 5% of major isoform abundance, `-j` to filter intronic reads.

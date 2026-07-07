---
name: aptardi
category: rna-analysis
description: aptardi - Alternative Polyadenylation Transcriptome Analysis from RNA sequencing and DNA sequencing Information
tags: [aptardi, polyadenylation, RNA-Seq, alternative-polyadenylation, APA, machine-learning]
author: oxo-call-community
source_url: "https://github.com/luskry/aptardi"
---

## Concepts

- **Tool Overview**: aptardi (v1.4) - A machine learning tool that predicts polyadenylation (polyA) sites from RNA-Seq data combined with DNA sequence information.
- **Core Function**: Identifies 3' ends of transcripts by integrating RNA-Seq data and genome sequence using machine learning. Evaluates 3' terminal exons of input transcripts and annotates 3' ends accordingly.
- **Alternative Polyadenylation (APA)**: A post-transcriptional regulatory mechanism where different polyA sites are used, generating transcript isoforms with different 3' UTRs.
- **Key Features**:
  - Combines both RNA-Seq expression data and DNA sequence information
  - Uses machine learning to predict expressed polyadenylation sites
  - Outputs updated transcript annotations in GTF/GFF format
  - Focuses on 3' terminal exons rather than intron junctions
- **Input**: 
  - Transcriptome annotation (GTF/GFF format)
  - Sorted BAM file of aligned RNA-Seq reads
  - Genome FASTA file
- **Output**: Updated GTF/GFF file with refined 3' ends
- **Applications**: 
  - Transcriptome refinement and annotation
  - Alternative polyadenylation analysis
  - Gene expression studies
- **Installation**: `conda create -n aptardi_env -c conda-forge -c bioconda aptardi`

## Pitfalls

- **External Dependencies**: Requires SAMtools and BEDtools (bioconda versions may cause conflicts)
- **Model Files**: Requires pre-trained model (model.hdf5) and scale file (scale.pk)
- **BAM File Requirements**: BAM file must be sorted
- **Input Format**: Transcript file must be in GTF/GFF format (designed for StringTie output)
- **Environment Conflicts**: Bioconda samtools and bedtools packages may prevent aptardi from working

## Examples

### Basic usage with pre-built model
**Args:** `aptardi --o /output/dir --f genome.fasta --r transcripts.gtf --b alignments.bam --n model.hdf5 --t scale.pk`
**Explanation:** Predict polyA sites using pre-trained machine learning model.

### Pipeline mode with StringTie output
**Args:** `stringtie alignments.bam | aptardi --o /output/dir --f genome.fasta --r - --b alignments.bam --n model.hdf5 --t scale.pk`
**Explanation:** Pipe StringTie output directly to aptardi for transcript refinement.

### Building custom model
**Args:** `aptardi --o /output/dir --f genome.fasta --r transcripts.gtf --b alignments.bam --m train --train_data training_set.txt`
**Explanation:** Train a custom machine learning model for polyA prediction.

### Help documentation
**Args:** `aptardi --help`
**Explanation:** Shows available options and parameters.

### Check version
**Args:** `aptardi --version`
**Explanation:** Displays installed version.
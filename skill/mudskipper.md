---
name: mudskipper
category: alignment
description: mudskipper is a tool for converting genomic BAM/SAM files to transcriptomic BAM/RAD files.
tags: [mudskipper, alignment, RNA-seq, transcriptome, BAM-conversion]
author: oxo-call-community
source_url: "https://github.com/OceanGenomics/mudskipper"
---

## Concepts

- **Tool Overview**: mudskipper v0.1.0 converts genome-coordinate alignments to transcript-coordinate alignments.
- **Core Function**: Translates alignment targets and coordinates from genomic to transcriptomic coordinates.
- **Input**: Accepts genome-aligned BAM/SAM files with spliced alignments.
- **Output**: Produces transcriptome-coordinate BAM files for use with Salmon.
- **Purpose**: Enables alignment-based RNA-seq quantification without re-mapping reads.
- **Integration**: Works with Salmon for transcript quantification in alignment-based mode.

## Pitfalls

- **Input Requirements**: Only accepts short RNA-seq read alignments; not tested for long reads.
- **Splicing**: Requires spliced alignments in input BAM/SAM.
- **Annotation Match**: BAM targets must match annotation file targets.
- **Alignment Quality**: Results depend on quality of initial genome alignment.
- **Format Compatibility**: Output is compatible with Salmon alignment-based mode only.
- **Coordinate System**: Converts genomic coordinates to transcriptomic; assumes correct annotation.

## Examples

### Bulk RNA-seq conversion
**Args:** `mudskipper bulk -a annotations.gtf -o transcripts.bam genome_alignments.bam`
**Explanation:** Converts genome BAM to transcriptome BAM using annotation GTF.

### Specify output format
**Args:** `mudskipper bulk -a ref.gtf -o out.bam -f bam in.bam`
**Explanation:** Specifies output format as BAM.

### Salmon quantification
**Args:** `salmon quant -a transcripts.bam -o quant_out/ -r`
**Explanation:** Quantifies transcripts using converted alignment file.

### Display help
**Args:** `mudskipper --help`
**Explanation:** Shows usage and available options.

### Validate input
**Args:** `mudskipper validate -a annotation.gtf -i input.bam`
**Explanation:** Validates input BAM and annotation compatibility.

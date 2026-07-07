---
name: mvirs
category: metagenomics
description: mVIRs - Localisation of inducible prophages using NGS data
tags: [mvirs, metagenomics, prophage, localization, ngs, phage, bacteria]
author: oxo-call-community
source_url: "https://github.com/SushiLab/mVIRs"
---

## Concepts

- **Tool Overview**: mVIRs v1.1.1 is a command-line tool that localizes and extracts genome sequences of inducible prophages in bacterial host genomes using paired-end DNA sequencing data. The approach relies on identifying DNA segments predicted to exist in a circularized or concatenated form upon induction.
- **Core Function**: Identifies and localizes inducible prophages within bacterial genomes by analyzing the orientation and apparent insert size of paired-end reads aligned to a reference genome, and locates exact genomic coordinates by partially aligned reads (clipped alignments).
- **Algorithm**: Detects outward-oriented paired-end reads (OPRs) with unusually large insert sizes as primary prophage indicators. Clipped alignments provide precise start/end positions. Results can be classified using tools like VirSorter2, VirFinder, VIBRANT, or Prophage Hunter.
- **Input Format**: Requires paired-end Illumina sequencing data (FASTA/FASTQ), a reference bacterial genome (FASTA), and dependencies including BWA for alignment and samtools for BAM processing.
- **Output**: Outputs predicted prophage locations as genomic coordinates and extracted prophage sequences as FASTA files. Reports both OPR regions (indicative of potential prophages) and precise clipped alignment coordinates.
- **Use Case**: Microbiome research, phage-bacteria interaction studies, gut microbial strain analysis, and prophage ecology in environmental or clinical samples.

## Pitfalls

- **Reference Quality**: mVIRs requires a high-quality reference genome. Poor quality references with gaps or misassemblies will produce unreliable prophage predictions.
- **Read Depth**: Low sequencing depth may miss prophages or produce false negatives. Sufficient coverage of the bacterial genome is essential.
- **Insert Size Assumption**: The tool assumes a known and consistent insert size library. Variable insert sizes across the library may affect OPR detection accuracy.
- **Clipped Alignment Sensitivity**: Clipped alignments are precise but may miss part of the prophage due to ambiguous alignments or strict criteria. Combine with OPR detection for comprehensive results.
- **Database Dependencies**: Requires external tools (BWA, samtools) to be installed and in PATH. Ensure correct versions (BWA ≥0.7.17, samtools ≥1.9).
- **Version Differences**: Version 1.1.0+ includes clipped read information for precise detection. Earlier versions may lack this feature.

## Examples

### Basic prophage detection
**Args:** `-i input.bam -o prophage_locations.tsv -r reference.fasta`
**Explanation:** Runs mVIRs with a BAM file aligned to the reference genome. Outputs predicted prophage locations and sequences.

### Output prophage sequences as FASTA
**Args:** `-i alignment.bam -r genome.fasta -o results/ --fasta`
**Explanation:** Extracts and outputs identified prophage sequences as a FASTA file for downstream analysis.

### Specify OPR threshold
**Args:** `-i reads.bam -r ref.fasta -o output.tsv -t 500`
**Explanation:** Sets the insert size threshold for outward-oriented paired reads to 500bp. OPRs larger than this indicate potential prophage regions.

### Run with custom prefix for output files
**Args:** `-i sample.bam -r bacterial_ref.fasta -o mvirs_results/ -p sample_prophage`
**Explanation:** Outputs results with a custom prefix for organized file naming in large studies.

### Display help and version
**Args:** `-h` or `--version`
**Explanation:** Shows available command-line options and version information (v1.1.1).

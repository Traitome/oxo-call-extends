---
name: ismapper
category: alignment
description: A mapping-based tool for identification of the site and orientation of IS insertions in bacterial genomes using paired-end reads.
tags: [ismapper, alignment, IS, insertion sequence, bacterial genomics]
author: oxo-call-community
source_url: "https://github.com/jhawkey/IS_mapper/"
---

## Concepts

- **IS Insertion Detection**: ismapper identifies insertion sequence (IS) elements and precisely maps their insertion sites in bacterial genomes using paired-end sequencing reads.
- **Orientation Analysis**: Determines the directionality of IS insertions relative to the reference genome, providing strand-specific information.
- **Split Read Mapping**: Utilizes split-read alignment strategies to detect breakpoints where IS elements have inserted into the host genome.
- **Copy Number Estimation**: Quantifies the number of IS copies present in a genome, aiding in strain classification and evolutionary studies.
- **Reference-guided Analysis**: Requires a reference genome to identify IS insertion sites by comparing mapped reads against known IS element sequences.
- **Output Annotation**: Generates GFF3-formatted output files for visualization in genome browsers and downstream analysis pipelines.

## Pitfalls

- **Reference Genome Quality**: Poorly assembled reference genomes can lead to incorrect insertion site calls or missed insertions.
- **Read Depth Variation**: Low sequencing coverage in certain genomic regions may result in false-negative IS detection.
- **IS Element Diversity**: Highly divergent IS elements not present in the reference database may be missed.
- **Repeat Regions**: Regions with high sequence similarity to IS elements can produce false-positive calls.
- **Paired-end Fragment Size**: Insertions larger than the sequencing library fragment size may not be properly detected.
- **IS Family Specificity**: The tool is optimized for specific IS families; performance may vary across different IS types.

## Examples

### Basic IS mapping
**Args:** `ismapper --reference ref.fasta --reads sample_R1.fastq sample_R2.fastq --output results/`
**Explanation:** Maps paired-end reads to identify IS insertion sites relative to the reference genome.

### Specify IS database
**Args:** `ismapper -r ref.fasta -1 R1.fq -2 R2.fq -o output/ --is-database is_elements.fasta`
**Explanation:** Uses a custom IS element database for detection instead of the built-in database.

### Single-end mode
**Args:** `ismapper --single-end --reference ref.fasta --reads single_end.fastq --output se_results/`
**Explanation:** Processes single-end sequencing data for IS detection.

### Generate visualization
**Args:** `ismapper -r ref.fasta -1 R1.fastq -2 R2.fastq -o results/ --visualize`
**Explanation:** Produces graphical representations of IS insertion sites alongside standard output.

### Filter by quality
**Args:** `ismapper -r ref.fasta -1 R1.fastq -2 R2.fastq -o results/ --min-quality 30`
**Explanation:** Filters reads based on Phred quality score before analysis.

### Batch processing
**Args:** `ismapper --batch input_list.txt --reference ref.fasta --output batch_results/`
**Explanation:** Processes multiple samples specified in a batch input file.
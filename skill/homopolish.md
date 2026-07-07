---
name: homopolish
category: polishing
description: Homopolish is a high-quality Nanopore-only genome polisher that uses homologous sequences to correct systematic errors in long-read sequencing data.
tags: [homopolish, nanopore, genome-polishing, long-read, sequencing-error-correction]
author: oxo-call-community
source_url: "https://github.com/ythuang0522/homopolish"
---

## Concepts

- **Tool Overview**: Homopolish (v0.4.2) is a genome polishing tool specifically designed for Oxford Nanopore sequencing data. It uses homologous sequence alignment to correct systematic errors, particularly homopolymer-length errors common in Nanopore reads.

- **Error Correction Strategy**: Homopolish builds a model trained on homologous sequences to identify and correct systematic errors in Nanopore reads. This approach outperforms traditional polishers like Medaka on many datasets.

- **Standalone Operation**: Unlike hybrid polishers that require short reads, Homopolish works exclusively with Nanopore long reads, making it ideal for projects where only long-read data is available.

- **Combination with Other Tools**: For optimal results, Homopolish can be combined with other polishers like Medaka or HELEN. When used in sequence, genome quality can exceed Q50 on R9.4 flow cells.

- **Supported Organisms**: Effective on bacteria, viruses, fungi, and metagenomic datasets, making it versatile for various genomic applications.

- **Iterative Polishing**: Supports multiple rounds of polishing to progressively improve genome accuracy through successive error correction.

## Pitfalls

- **Computational Resources**: Polishing large genomes requires significant computational resources. Consider parallel processing for large datasets.

- **Read Quality**: Poor-quality reads may limit polishing effectiveness. Pre-filter low-quality reads before polishing.

- **Memory Usage**: Memory requirements increase with genome size. Monitor memory usage for large eukaryotic genomes.

- **Time Consumption**: Multiple polishing rounds can be time-consuming. Balance between polishing rounds and desired accuracy.

- **Basecaller Compatibility**: Results may vary depending on the basecaller used (e.g., Guppy vs. Bonito). Use consistent basecalling for reproducibility.

- **Reference Dependence**: The polishing quality depends on the quality of the initial assembly. Poor initial assemblies limit improvement potential.

## Examples

### Run basic Homopolish polishing
**Args:** `homopolish polish -i assembly.fasta -r reads.fastq -o polished_assembly.fasta`
**Explanation:** Polishes an assembly using Nanopore reads. Corrects systematic errors including homopolymer-length errors.

### Perform multiple polishing rounds
**Args:** `homopolish polish -i assembly.fasta -r reads.fastq -o polished.fasta -rounds 3`
**Explanation:** Runs three rounds of polishing for progressively higher accuracy. Each round refines the assembly further.

### Use with Medaka combination
**Args:** `medaka_consensus -i reads.fastq -d assembly.fasta -o medaka_out && homopolish polish -i medaka_out/consensus.fasta -r reads.fastq -o final_assembly.fasta`
**Explanation:** First runs Medaka, then uses Homopolish for final polishing. This combination often achieves Q50+ quality.

### Specify output directory
**Args:** `homopolish polish -i assembly.fasta -r reads.fastq -o polished.fasta -w work_dir/`
**Explanation:** Uses specified working directory for temporary files, useful for managing large polishing jobs.

### Polish with quality filtering
**Args:** `homopolish polish -i assembly.fasta -r reads.fastq -o polished.fasta -q 10`
**Explanation:** Filters reads with quality score below 10 before polishing, improving efficiency and accuracy.

### Generate polishing statistics
**Args:** `homopolish polish -i assembly.fasta -r reads.fastq -o polished.fasta -stats stats.txt`
**Explanation:** Outputs detailed statistics about the polishing process including error correction rates.

### Run on metagenomic data
**Args:** `homopolish polish -i metagenome_assembly.fasta -r metagenome_reads.fastq -o polished_metagenome.fasta`
**Explanation:** Polishes metagenomic assemblies, handling mixed microbial sequences effectively.
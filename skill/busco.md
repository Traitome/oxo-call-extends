---
name: busco
category: qc
description: Assessment of genome assembly and annotation completeness using Universal Single Copy Orthologs
tags: [busco, qc, completeness, genome, ortholog]
author: oxo-call-community
source_url: "https://busco.ezlab.org"
---

## Concepts

- **Tool Overview**: BUSCO assesses genome assembly and annotation completeness using evolutionarily informed expectations of gene content.
- **Core Function**: Searches for near-universal single-copy orthologs to evaluate completeness.
- **Databases**: Lineage-specific datasets from OrthoDB (bacteria, eukaryota, etc.).
- **Input**: Genome FASTA, protein FASTA, or transcript FASTA.
- **Output**: Completeness scores (complete, fragmented, missing) and sequence files.
- **Modes**: Genome, proteins, transcriptome assessment modes.
- **Installation**: Install via bioconda: `conda install -c bioconda busco`

## Pitfalls

- **Lineage Selection**: Choose appropriate lineage dataset for accurate assessment.
- **Database Download**: First run downloads lineage datasets automatically.
- **Memory Usage**: Large genomes require significant memory.
- **Augustus Required**: Eukaryotic mode requires AUGUSTUS for gene prediction.
- **Auto-lineage**: Use --auto-lineage for automatic lineage selection.

## Examples

### Assess genome completeness
**Args:** `busco -i genome.fa -l bacteria -o genome_busco -m genome`
**Explanation:** Assesses bacterial genome completeness using bacteria lineage dataset.

### Assess eukaryotic genome
**Args:** `busco -i genome.fa -l eukaryota_odb10 -o euk_busco -m genome`
**Explanation:** Assesses eukaryotic genome using eukaryota ortholog dataset.

### Assess protein set
**Args:** `busco -i proteins.fa -l metazoa_odb10 -o protein_busco -m protein`
**Explanation:** Assesses protein annotation completeness using metazoa dataset.

### Auto-lineage detection
**Args:** `busco -i genome.fa --auto-lineage -o auto_busco -m genome`
**Explanation:** Automatically selects the most appropriate lineage dataset.

### Multi-threaded run
**Args:** `busco -i genome.fa -l bacteria -c 16 -o busco_out -m genome`
**Explanation:** Uses 16 threads for faster BUSCO analysis.

### Use Augustus species
**Args:** `busco -i genome.fa -l insecta_odb10 --augustus_species fly -o insect_busco -m genome`
**Explanation:** Uses Drosophila AUGUSTUS parameters for insect genome assessment.

---
name: aliceasm
category: assembly
description: Fast and haplotype-aware assembler for PacBio HiFi reads producing phased assemblies
tags: [assembly, hifi, nanopore, haplotype, phasing, pacbio]
author: oxo-call-community
source_url: "https://github.com/RolandFaure/alice-asm"
---

## Concepts

- **Tool Overview**: Alice is an efficient HiFi genome assembler that produces haplotype-separated assemblies, particularly suited for heterozygous and polyploid genomes.
- **Core Function**: Assembles PacBio HiFi reads into phased haplotype-resolved assemblies, separating homologous chromosomes.
- **Input/Output**: Input: PacBio HiFi FASTQ. Output: Haplotype-resolved assembly FASTA files.
- **Speed**: An order of magnitude faster than other HiFi assemblers while maintaining high quality.
- **Installation**: Install via bioconda: `conda install -c bioconda aliceasm`

## Pitfalls

- **HiFi Data Required**: Designed for HiFi/CCS reads - may not work well with CLR or other data types.
- **Coverage Requirements**: Requires sufficient HiFi coverage (typically 15-30x) for good haplotype separation.
- **Heterozygosity Level**: Works best with moderate heterozygosity; very low heterozygosity may not separate haplotypes well.
- **Memory Usage**: Large genomes require substantial memory - allocate based on genome size.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows assembly options and parameters.

### Basic HiFi assembly
**Args:** `assemble -i hifi_reads.fastq -o assembly/`
**Explanation:** Assembles HiFi reads into haplotype-resolved assembly.

### Specify expected ploidy
**Args:** `assemble -i hifi.fastq --ploidy 4 -o tetraploid_asm/`
**Explanation:** Assembles tetraploid genome with 4 expected haplotypes.

### Set minimum contig length
**Args:** `assemble -i hifi.fastq -l 10000 -o assembly/`
**Explanation:** Filters out contigs shorter than 10kb from output.

### Assembly with coverage cutoff
**Args:** `assemble -i hifi.fastq --min-coverage 20 -o assembly/`
**Explanation:** Uses minimum 20x coverage threshold for contig inclusion.

### Output separate haplotypes
**Args:** `assemble -i hifi.fastq --separate-haplotypes -o assembly/`
**Explanation:** Outputs each haplotype as separate FASTA file.

### Multi-threaded assembly
**Args:** `assemble -i hifi.fastq -t 32 -o assembly/`
**Explanation:** Uses 32 threads for faster assembly.

### Assembly with polishing
**Args:** `assemble -i hifi.fastq --polish -o assembly/`
**Explanation:** Performs additional polishing steps on assembled contigs.

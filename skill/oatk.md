---
name: oatk
category: assembly
description: Oatk is an organelle genome assembly toolkit for chloroplast and mitochondrial genomes.
tags: [oatk, assembly, organelle-genome, chloroplast, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/c-zhou/oatk"
---

## Concepts

- **Tool Overview**: Oatk assembles organelle genomes from sequencing data.
- **Core Function**: Assembles chloroplast and mitochondrial genomes.
- **Algorithm**: Uses reference-guided and de novo assembly approaches.
- **Input Format**: Accepts FASTQ reads and optional reference sequences.
- **Output**: Produces assembled organelle genome sequences.
- **Use Case**: Organelle genome assembly, phylogenomics, and evolutionary studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Quality**: Results depend on reference sequence quality.
- **Contamination**: May include nuclear DNA sequences.
- **Memory Usage**: Large datasets require memory.
- **Assembly Completeness**: May not assemble complete circular genomes.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `oatk --help`
**Explanation:** Shows available options and usage instructions.

### Assemble organelle genome
**Args:** `oatk assemble -i reads.fastq -o organelle.fasta`
**Explanation:** Assembles organelle genome from reads.

### With reference
**Args:** `oatk assemble -i reads.fastq -r reference.fasta -o organelle.fasta`
**Explanation:** Uses reference-guided assembly.

### Chloroplast only
**Args:** `oatk assemble -i reads.fastq -o chloroplast.fasta --chloroplast`
**Explanation:** Assembles only chloroplast genome.

### Mitochondrial only
**Args:** `oatk assemble -i reads.fastq -o mitochondrial.fasta --mitochondrial`
**Explanation:** Assembles only mitochondrial genome.

### Circularize
**Args:** `oatk circularize -i organelle.fasta -o circular.fasta`
**Explanation:** Circularizes assembled genome.

### Annotate
**Args:** `oatk annotate -i organelle.fasta -o annotation.gff`
**Explanation:** Annotates organelle genome.

### Verbose mode
**Args:** `oatk assemble -i reads.fastq -o organelle.fasta -v`
**Explanation:** Runs with verbose output.
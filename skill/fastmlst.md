---
name: fastmlst
category: utility
description: "A Fast Multilocus Sequence Typing scan against PubMLST typing schemes."
tags: [fastmlst, utility, MLST, bacterial-typing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/EnzoAndree/FastMLST"
---

## Concepts

- **Tool Overview**: FastMLST is a tool for performing rapid Multilocus Sequence Typing (MLST) analysis against PubMLST typing schemes.
- **Core Function**: Identifies MLST types by comparing sequences against known typing schemes.
- **Input/Output**: Input: Genome sequences (FASTA), contigs. Output: MLST type, allele profiles.
- **Algorithm**: Uses sequence comparison against MLST databases for type identification.
- **Key Features**: Fast MLST typing, PubMLST integration, multiple species support, batch processing, detailed reporting.
- **Installation**: `conda install -c bioconda fastmlst`

## Pitfalls

- **Database Updates**: Requires up-to-date MLST database.
- **Genome Quality**: Requires high-quality genome sequences.
- **Memory Usage**: Large datasets may require significant memory.
- **Species Support**: Limited to supported species in PubMLST.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic MLST typing
**Args:** `fastmlst -i genome.fasta -o mlst_result.txt`
**Explanation:** Identifies MLST type for genome.

### Specify species
**Args:** `fastmlst -i genome.fasta -o mlst_result.txt -s Escherichia_coli`
**Explanation:** Specifies target species for typing.

### Batch processing
**Args:** `fastmlst -i genomes/ -o results/ --batch`
**Explanation:** Processes multiple genomes in batch mode.

### Update database
**Args:** `fastmlst --update`
**Explanation:** Updates MLST database.

### Verbose output
**Args:** `fastmlst -i genome.fasta -o mlst_result.txt -v`
**Explanation:** Generates verbose output with additional details.
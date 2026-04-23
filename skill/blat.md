---
name: blat
category: alignment
description: Fast sequence alignment tool for mRNA/DNA and cross-species protein alignments
tags: [blat, alignment, ucsc, sequence-mapping]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/goldenpath/help/blatSpec.html"
---

## Concepts

- **Tool Overview**: BLAT (BLAST-Like Alignment Tool) is a fast sequence alignment tool developed by UCSC, optimized for finding sequences of 95%+ similarity.
- **Core Function**: Rapidly aligns mRNA/DNA sequences and performs cross-species protein alignments.
- **Input Types**: Accepts FASTA (.fa), NIB (.nib), or 2BIT (.2bit) files as database or query.
- **Output Format**: PSL (Pattern Space Layout) format by default; supports multiple output formats.
- **Speed Optimization**: Use `-ooc=11.ooc` file to speed up alignment by ~40x.
- **Installation**: Install via bioconda: `conda install -c bioconda blat`

## Pitfalls

- **High Similarity Requirement**: BLAT is optimized for high-similarity alignments (>90% identity); use BLAST for more divergent sequences.
- **Memory Usage**: Large genomes require significant memory; use 2BIT format for efficiency.
- **Output Parsing**: PSL format has specific column order; be careful when parsing results.
- **Strand Direction**: Specify `-q=rna` for RNA sequences to properly handle splice sites.
- **Intron Size**: Default max intron is 750kb; adjust with `-maxIntron` for large genomes.

## Examples

### Basic DNA alignment
**Args:** `genome.2bit query.fa -ooc=11.ooc output.psl`
**Explanation:** Aligns query sequences against genome using overused 11-mer file for 40x speedup.

### mRNA to genome alignment
**Args:** `genome.fa mrna.fa -q=rna -ooc=11.ooc -fine output.psl`
**Explanation:** Aligns mRNA sequences with fine-tuned search for small initial/terminal exons.

### Protein alignment
**Args:** `-t=prot -q=prot protein_db.fa query_proteins.fa output.psl`
**Explanation:** Performs protein-to-protein alignment with appropriate type settings.

### Cross-species DNA alignment
**Args:** `-q=dnax -t=dnax genome.fa query.fa output.psl`
**Explanation:** Translates query and target in multiple frames for cross-species DNA alignment.

### Fast remapping mode
**Args:** `genome.fa reads.fa -fastMap -ooc=11.ooc output.psl`
**Explanation:** Fast DNA/DNA remapping without intron handling, for high-identity alignments.

### Custom output format
**Args:** `genome.fa query.fa -out=blast8 output.txt`
**Explanation:** Outputs in blast8 tabular format for compatibility with downstream tools.

### Adjust minimum identity
**Args:** `genome.fa query.fa -minIdentity=95 -minScore=50 output.psl`
**Explanation:** Sets minimum identity to 95% and minimum score to 50 for stringent filtering.

### Generate overused tile file
**Args:** `genome.fa query.fa -makeOoc=11.ooc output.psl`
**Explanation:** Creates overused 11-mer file for future faster alignments against this genome.

---
name: biopython
category: programming
description: Freely available tools for computational molecular biology
tags: [python, bioinformatics, sequence-analysis, parsing]
author: oxo-call-community
source_url: "http://www.biopython.org/"
---

## Concepts
- **Tool Overview**: Biopython is the most widely used Python library for computational molecular biology. It provides tools for biological computation including sequence analysis, structure parsing, database access, and phylogenetics.
- **Core Modules**: SeqIO (sequence I/O), AlignIO (alignment I/O), PDB (structure parsing), Entrez (NCBI access), Phylo (phylogenetics), BioSQL (database interface).
- **Sequence Operations**: Translation, transcription, reverse complement, motif searching, ORF finding.
- **Applications**: Sequence analysis, structural biology, population genetics, bioinformatics pipeline development.

## Pitfalls
- **Performance**: Pure Python implementation may be slow for large datasets; consider specialized tools for heavy computation.
- **Version Compatibility**: API changes between major versions may break existing code.

## Examples
### Parse FASTA file
**Args:** `python -c "from Bio import SeqIO; [print(r.id, len(r)) for r in SeqIO.parse('seqs.fa', 'fasta')]"`
**Explanation:** Parses FASTA file and prints sequence IDs and lengths.

### Translate DNA to protein
**Args:** `python -c "from Bio.Seq import Seq; print(Seq('ATGGCC').translate())"`
**Explanation:** Translates a DNA sequence to protein.

### Search NCBI
**Args:** `python -c "from Bio import Entrez; Entrez.email='x@x.com'; print(Entrez.esearch(db='nucleotide', term='BRCA1').read())"`
**Explanation:** Searches NCBI nucleotide database for BRCA1.

---
name: bioruby
category: programming
description: Ruby library for bioinformatics with sequence analysis and database access
tags: [bioruby, ruby, programming, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/bioruby/bioruby"
---

## Concepts

- **Tool Overview**: BioRuby is a Ruby library providing integrated access to bioinformatics services and tools.
- **Core Function**: Sequence analysis, database access, and file format parsing in Ruby.
- **Features**: FASTA/GenBank parsing, BLAST integration, sequence alignment, and phylogenetics.
- **Modules**: Sequence, alignment, database, and phylogenetics modules.
- **Installation**: Install via bioconda: `conda install -c bioconda bioruby`

## Pitfalls

- **Ruby Required**: Requires Ruby runtime environment.
- **Gem Dependencies**: Some features require additional Ruby gems.
- **Performance**: Slower than compiled tools for large-scale analysis.
- **Documentation**: Some modules have limited documentation.

## Examples

### Parse FASTA file
**Args:** `ruby -e "require 'bio'; Bio::FlatFile.open(Bio::FastaFormat, 'seqs.fa').each {|s| puts s.definition}"`
**Explanation:** Reads and prints definitions from a FASTA file using BioRuby.

### Reverse complement sequence
**Args:** `ruby -e "require 'bio'; puts Bio::Sequence::NA.new('ATCG').reverse_complement"`
**Explanation:** Computes reverse complement of a DNA sequence.

### Calculate GC content
**Args:** `ruby -e "require 'bio'; puts Bio::Sequence::NA.new('ATCGATCG').gc_percent"`
**Explanation:** Calculates GC percentage of a DNA sequence.

### Translate DNA to protein
**Args:** `ruby -e "require 'bio'; puts Bio::Sequence::NA.new('ATGAAATTT').translate"`
**Explanation:** Translates DNA sequence to protein using standard genetic code.

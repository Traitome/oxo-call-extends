---
name: ruby
category: programming
description: Ruby is a dynamic, reflective, object-oriented, general-purpose programming language.
tags: ["ruby", "programming", "language", "scripting"]
author: oxo-call-community
source_url: "https://www.ruby-lang.org"
---

## Concepts

- **Tool Overview**: Ruby (v2.2.3+) is a dynamic, object-oriented programming language known for its elegant syntax and readability. It is widely used for web development, scripting, and bioinformatics tool development.
- **Core Function**: Provides a complete programming environment with built-in support for text processing, regular expressions, and object-oriented design. Extensible through gems (Ruby packages).
- **Language Features**: Dynamic typing, automatic memory management, metaprogramming capabilities, and a rich standard library.
- **Bioinformatics Use**: Used for developing bioinformatics tools, parsing sequence data, building pipelines, and rapid prototyping.
- **Package Ecosystem**: RubyGems package manager with bioinformatics-specific gems like bio-ruby, bioruby, and ruby-dna-tools.
- **Use Case**: Scripting bioinformatics workflows, developing web applications for genomic data, text processing of sequence files.

## Pitfalls

- **Performance**: Generally slower than compiled languages for computationally intensive tasks.
- **Memory usage**: Higher memory footprint compared to some other scripting languages.
- **Threading limitations**: Global interpreter lock (GIL) limits true parallelism in MRI Ruby.
- **Version compatibility**: Different Ruby versions may have breaking changes.
- **Dependency management**: Gem version conflicts can be challenging.
- **Windows compatibility**: Some gems may not work properly on Windows.

## Examples

### Run Ruby script
**Args:** `ruby my_script.rb`
**Explanation:** Executes a Ruby script file.

### Start interactive Ruby shell
**Args:** `irb`
**Explanation:** Launches the interactive Ruby interpreter for testing code snippets.

### Check Ruby version
**Args:** `ruby --version`
**Explanation:** Displays the installed Ruby version.

### Install a gem
**Args:** `gem install bio`
**Explanation:** Installs the bio-ruby gem for bioinformatics functionality.

### List installed gems
**Args:** `gem list`
**Explanation:** Lists all installed Ruby gems.

### Create a simple sequence parser
**Args:** `ruby -e "File.open('seq.fasta').each { |line| puts line if line =~ /^>/ }"`
**Explanation:** Extracts sequence headers from a FASTA file.

### Use Ruby with pipes
**Args:** `cat input.fastq | ruby -ne 'puts $_.chomp if $. % 4 == 2'`
**Explanation:** Extracts sequence lines from a FASTQ file using Ruby one-liner.

---
name: peek-bio
category: utility
description: peek-bio provides instant file previews for genomics data.
tags: [peek-bio, utility, preview, genomics]
author: oxo-call-community
source_url: "https://github.com/pwilson97/peek-bio"
---

## Concepts

- **Tool Overview**: peek-bio previews genomics files.
- **Core Function**: Provides instant file previews.
- **Algorithm**: Uses file format detection.
- **Input Format**: Accepts various genomics files.
- **Output**: Produces file previews.
- **Use Case**: File inspection, data exploration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **File Format**: Requires proper file format.
- **Preview Quality**: Preview may be truncated.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peek-bio --help`
**Explanation:** Shows available options and usage instructions.

### Preview file
**Args:** `peek-bio -i file.bam -o preview.txt`
**Explanation:** Preview BAM file contents.

### Preview VCF
**Args:** `peek-bio -i file.vcf -o preview.txt`
**Explanation:** Preview VCF file contents.

### Verbose mode
**Args:** `peek-bio -v -i file.bam -o preview.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peek-bio -t 4 -i file.bam -o preview.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peek-bio -i file.bam -o preview.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peek-bio -i file.bam -o preview.txt --report report.html`
**Explanation:** Generates HTML report.
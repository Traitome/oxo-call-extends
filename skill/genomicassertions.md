---
name: genomicassertions
category: testing
description: genomicassertions - A package to test common files in genomics (.vcf.gz, .bam).
tags: [genomicassertions, testing, BAM, VCF, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dakl/genomicassertions"
---

## Concepts
- **File Validation**: Validates genomic file formats.
- **Testing Framework**: Provides testing utilities for genomics.
- **BAM Testing**: Tests BAM file integrity.
- **VCF Testing**: Tests VCF file integrity.
- **Quality Control**: Performs quality control checks.

## Pitfalls
- **File Format**: Requires correct input formats.
- **Memory Usage**: Large files require significant memory.
- **Dependency Management**: Requires correct dependencies.
- **Version Compatibility**: Options may vary between versions.
- **Test Coverage**: Requires comprehensive test coverage.

## Examples
### Test BAM file
**Args:** `python -c "from genomicassertions import BAMAssertions; BAMAssertions().assert_bam('reads.bam')"`
**Explanation:** Validates BAM file integrity.

### Test VCF file
**Args:** `python -c "from genomicassertions import VCFAssertions; VCFAssertions().assert_vcf('variants.vcf.gz')"`
**Explanation:** Validates VCF file integrity.

### Run all tests
**Args:** `python -m pytest test_genomic.py -v`
**Explanation:** Runs genomic tests with pytest.

### Batch testing
**Args:** `genomicassertions batch -i ./files/ -o test_results.txt`
**Explanation:** Tests multiple genomic files.

### Generate report
**Args:** `genomicassertions report -i ./files/ -o report.html`
**Explanation:** Generates testing report.
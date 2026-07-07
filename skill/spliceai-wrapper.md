---
name: spliceai-wrapper
category: variant-calling
description: SpliceAI Wrapper - Caching wrapper for Illumina SpliceAI
tags: [spliceai-wrapper, variant-calling, splicing, caching, wrapper]
author: oxo-call-community
source_url: "https://github.com/bihealth/spliceai-wrapper"
---

## Concepts

- **Tool Overview**: spliceai-wrapper (v0.1.0) - A caching wrapper for SpliceAI
- **Core Function**: Provides caching functionality for SpliceAI predictions
- **Input/Output**: Accepts SpliceAI inputs; outputs cached predictions
- **Algorithm**: Caching layer for SpliceAI
- **Installation**: `conda install -c bioconda spliceai-wrapper`
- **Key Features**: Caching, SpliceAI integration, performance optimization

## Pitfalls

- **Input Requirements**: Requires properly formatted SpliceAI inputs
- **Cache Management**: Cache size affects performance
- **Cache Invalidation**: Invalid cache may produce incorrect results
- **Memory Usage**: Large caches require significant memory
- **Output Format**: Output format depends on configuration
- **Cache Accuracy**: Cache accuracy depends on invalidation strategy

## Examples

### Display help
**Args:** `spliceai-wrapper --help`
**Explanation:** Shows available options and usage information.

### Basic splice prediction with caching
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta`
**Explanation:** Predict splice variants with caching.

### With cache directory
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta --cache-dir cache/`
**Explanation:** Set cache directory for predictions.

### Clear cache
**Args:** `spliceai-wrapper --clear-cache`
**Explanation:** Clear prediction cache.

### With cache size limit
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta --cache-size 10GB`
**Explanation:** Set cache size limit.

### Output detailed results
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta --detailed`
**Explanation:** Output detailed prediction information.

### Output cache statistics
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta --cache-stats`
**Explanation:** Output cache statistics.

### Output statistics
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta --stats`
**Explanation:** Output prediction statistics.

### Generate report
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta --report`
**Explanation:** Generate prediction report.

### With threads
**Args:** `spliceai-wrapper -I input.vcf -O output.vcf -R reference.fasta -p 8`
**Explanation:** Use multiple threads for prediction.
---
name: sword
category: sequence-analysis
description: Highly efficient protein database search tool for sequence similarity analysis.
tags: [sword, protein-search, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rvaser/sword"
---

## Concepts

- **Tool Overview**: sword (v1.0.4) is an efficient protein database search tool.
- **Core Function**: Searches protein sequences against databases.
- **Algorithm**: Uses advanced indexing and parallel computing for fast searches.
- **Input/Output**: Input: Query sequence, protein database; Output: Similarity hits.
- **Applications**: Protein homology search, sequence analysis, annotation.
- **Installation**: `conda install -c bioconda sword` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large databases require significant memory.
- **Performance**: Depends on database size and query complexity.
- **Parameter Tuning**: Incorrect parameters affect search results.
- **Database Format**: Requires specific database format.
- **Sequence Quality**: Poor quality sequences affect results.
- **Scalability**: Very large databases may be challenging.

## Examples

### Display help
**Args:** `sword --help`
**Explanation:** Shows available options and usage information.

### Basic database search
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt`
**Explanation:** Search query against protein database.

### With E-value threshold
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt -e 1e-5`
**Explanation:** Use E-value threshold of 1e-5.

### Verbose mode
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt --stats`
**Explanation:** Generate statistics about search.

### Batch processing
**Args:** `for q in queries/*.fasta; do sword -i $q -d db.fasta -o results/${q%.fasta}.txt; done`
**Explanation:** Search multiple queries against database.

### Filter by score
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt -s 100`
**Explanation:** Filter by minimum alignment score.

### Include all hits
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt --all`
**Explanation:** Output all hits.

### Generate report
**Args:** `sword -i query.fasta -d database.fasta -o hits.txt --report`
**Explanation:** Generate comprehensive search report.

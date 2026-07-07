---
name: metagraph
category: alignment
description: Ultra Scalable Framework for DNA Search, Alignment, Assembly.
tags: [metagraph, alignment, dna-search, assembly]
author: oxo-call-community
source_url: "https://github.com/ratschlab/metagraph"
---

## Concepts

- **Tool Overview**: MetaGraph v0.5.1 is an ultra-scalable framework for DNA sequence search, alignment, and assembly that can handle petabase-scale datasets.
- **Core Function**: Provides compressed indexing and efficient querying of very large biological sequence collections.
- **Compressed Indexing**: Produces compressed indexes that can represent several petabases of input data efficiently.
- **Scalable Search**: Enables fast sequence search across massive sequence collections.
- **Input/Output**: Accepts FASTA/Q sequence files; outputs search results, alignments, and assembly graphs.
- **Multi-purpose**: Supports multiple operations including indexing, search, alignment, and assembly.

## Pitfalls

- **Memory Requirements**: Building indexes for large datasets may require significant memory.
- **Index Building Time**: Creating compressed indexes for large datasets can be time-consuming.
- **Query Performance**: Query performance may vary depending on index size and query complexity.
- **Storage Requirements**: Index files can be large and require substantial storage space.
- **Parameter Tuning**: May require parameter adjustment for optimal performance.
- **Learning Curve**: Complex tool with many options that may require time to master.

## Examples

### Build compressed index
**Args:** `metagraph build -i sequences.fasta -o index.mg`
**Explanation:** Builds a compressed index from input sequences.

### Query index
**Args:** `metagraph query -i index.mg -q queries.fasta -o results.txt`
**Explanation:** Queries the index with input query sequences.

### Build assembly graph
**Args:** `metagraph assemble -i reads.fastq -o assembly.gfa`
**Explanation:** Assembles reads into an assembly graph.

### Index statistics
**Args:** `metagraph stats -i index.mg -o stats.txt`
**Explanation:** Generates statistics about the compressed index.

### Merge indexes
**Args:** `metagraph merge -i index1.mg index2.mg -o merged.mg`
**Explanation:** Merges multiple indexes into a single index.
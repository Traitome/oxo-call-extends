---
name: psortem
category: hpc
description: psortem performs parallel external merge sort for large datasets.
tags: [psortem, hpc, parallel-processing, sorting]
author: oxo-call-community
source_url: "https://github.com/tseemann/psortem"
---

## Concepts

- **Tool Overview**: psortem sorts large datasets.
- **Core Function**: Parallel merge sort.
- **Algorithm**: Uses external merge sort.
- **Input Format**: Accepts text files.
- **Output**: Produces sorted output.
- **Use Case**: Large data sorting.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Disk Space**: Requires temporary space.
- **Runtime**: Sorting may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psortem --help`
**Explanation:** Shows available options and usage instructions.

### Sort file
**Args:** `psortem -i unsorted.txt -o sorted.txt`
**Explanation:** Performs parallel merge sort.

### With parameters
**Args:** `psortem -i unsorted.txt -p params.txt -o sorted.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psortem -v -i unsorted.txt -o sorted.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psortem -t 4 -i unsorted.txt -o sorted.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Memory limit
**Args:** `psortem -m 10G -i unsorted.txt -o sorted.txt`
**Explanation:** Limits memory usage to 10GB.

### Generate report
**Args:** `psortem -i unsorted.txt -o sorted.txt --report report.html`
**Explanation:** Generates HTML report.
---
name: tqdm
category: utility
description: tqdm - Fast, extensible progress bar for Python and CLI.
tags: [tqdm, progress-bar, python, cli, utility]
author: oxo-call-community
source_url: "https://github.com/tqdm/tqdm"
---

## Concepts

- **Tool Overview**: tqdm - A fast and extensible progress bar library for Python and command-line applications.
- **Core Function**: Provides visual progress tracking for iterative processes and loops.
- **Input**: Iterable objects, command-line pipelines.
- **Output**: Progress bar display, completion statistics.
- **Installation**: `pip install tqdm`
- **Use Case**: Progress tracking, long-running tasks, data processing pipelines.

## Pitfalls

- **Overhead**: Very small iterations may have noticeable overhead.
- **Output**: Progress bar may interfere with other output streams.

## Examples

### Python usage
**Args:** `from tqdm import tqdm; for i in tqdm(range(1000)): process(i)`
**Explanation:** Add progress bar to Python loop.

### CLI usage
**Args:** `find . -name "*.txt" | tqdm | wc -l`
**Explanation:** Add progress bar to shell pipeline.

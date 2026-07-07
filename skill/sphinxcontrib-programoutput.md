---
name: sphinxcontrib-programoutput
category: documentation
description: Sphinx ProgramOutput - Extension to include program output in documentation
tags: [sphinxcontrib-programoutput, documentation, sphinx, program-output, code-execution]
author: oxo-call-community
source_url: "http://sphinxcontrib-programoutput.readthedocs.org/"
---

## Concepts

- **Tool Overview**: sphinxcontrib-programoutput (v0.8) - A Sphinx documentation extension
- **Core Function**: Includes program output in Sphinx documentation
- **Input/Output**: Accepts program commands; outputs documentation with results
- **Algorithm**: Automatic program execution and output capture
- **Installation**: `conda install -c bioconda sphinxcontrib-programoutput`
- **Key Features**: Program output, code execution, Sphinx integration

## Pitfalls

- **Input Requirements**: Requires properly configured program commands
- **Program Availability**: Program must be available for execution
- **Execution Time**: Long-running programs may delay documentation build
- **Memory Usage**: Large outputs require significant memory
- **Output Format**: Output format depends on configuration
- **Execution Safety**: Unsafe commands may affect system

## Examples

### Display help
**Args:** `python -c "import sphinxcontrib.programoutput; help(sphinxcontrib.programoutput)"`
**Explanation:** Shows module documentation.

### Basic program output
**Args:** `.. code-block:: bash :caption: Example output :class: example-output $ echo "Hello, World!" Hello, World!`
**Explanation:** Include program output in documentation.

### With command execution
**Args:** `.. program-output:: echo "Hello, World!" :caption: Example output`
**Explanation:** Execute command and include output.

### With error handling
**Args:** `.. program-output:: ls /nonexistent :caption: Error example :ellipsis: 3`
**Explanation:** Handle command errors.

### With output truncation
**Args:** `.. program-output:: cat large_file.txt :caption: Truncated output :maxlines: 10`
**Explanation:** Truncate long output.

### With output highlighting
**Args:** `.. program-output:: python -c "print('Hello')" :caption: Python output :language: python`
**Explanation:** Highlight output syntax.

### Output detailed results
**Args:** `.. program-output:: command :caption: Detailed output :detail: full`
**Explanation:** Output detailed program information.

### Output statistics
**Args:** `.. program-output:: command :caption: Output statistics :stats: true`
**Explanation:** Output execution statistics.

### Generate report
**Args:** `.. program-output:: command :caption: Execution report :report: true`
**Explanation:** Generate execution report.
---
name: sphinx-argparse
category: documentation
description: Sphinx Argparse - Auto-documentation for argparse commands
tags: [sphinx-argparse, documentation, sphinx, argparse, auto-documentation]
author: oxo-call-community
source_url: "https://github.com/ashb/sphinx-argparse"
---

## Concepts

- **Tool Overview**: sphinx-argparse (v0.1.15) - A Sphinx documentation extension
- **Core Function**: Automatically documents argparse commands and options
- **Input/Output**: Accepts argparse parsers; outputs documentation
- **Algorithm**: Automatic documentation generation
- **Installation**: `conda install -c bioconda sphinx-argparse`
- **Key Features**: Auto-documentation, argparse integration, Sphinx extension

## Pitfalls

- **Input Requirements**: Requires properly configured argparse parsers
- **Parser Structure**: Parser structure affects documentation quality
- **Sphinx Configuration**: Sphinx configuration affects output format
- **Memory Usage**: Large parsers require significant memory
- **Output Format**: Output format depends on configuration
- **Documentation Quality**: Quality depends on parser documentation

## Examples

### Display help
**Args:** `python -c "import sphinxargparse; help(sphinxargparse)"`
**Explanation:** Shows module documentation.

### Basic documentation
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram`
**Explanation:** Document argparse parser in Sphinx.

### With nested parsers
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :nested: full`
**Explanation:** Document nested subparsers.

### With descriptions
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :description: My program description`
**Explanation:** Add program description.

### With usage examples
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :usage: myprogram [options]`
**Explanation:** Add usage examples.

### Output detailed documentation
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :detail: full`
**Explanation:** Output detailed documentation.

### Output help text
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :help: full`
**Explanation:** Output help text.

### Output statistics
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :stats: true`
**Explanation:** Output parser statistics.

### Generate report
**Args:** `.. argparse:: :module: mymodule :func: main :prog: myprogram :report: true`
**Explanation:** Generate documentation report.
---
name: gcen
category: expression
description: GCEN: an easy-to-use toolkit for Gene Co-Expression Network analysis and lncRNAs annotation.
tags: [gcen, expression]
author: oxo-call-community
source_url: "https://www.biochen.org/gcen"
---

## Concepts
- **Tool Overview**: GCEN is a command-line toolkit that allows biologists to easily build gene co-expression network and predict gene function, especially in RNA-Seq research or lncRNAs annotation. GCEN is primarily designed to be used in lncRNAs annotation, but is not limited to those scenarios. It is an efficient and easy-to-use solution that will allow everyone to perform gene co-expression network analysis without sophisticated programming skills. The recommended pipeline consists of four parts: data pretreatment, network construction, module identification, and function annotation. A README file and sample data are included in the software package. Because of its modular design, the GCEN can be easily integrated into another pipeline. Also, the multithreaded implementation of GCEN makes it fast and efficient for RNA-Seq data.
- **Core Function**: GCEN: an easy-to-use toolkit for Gene Co-Expression Network analysis and lncRNAs annotation.
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda gcen`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.

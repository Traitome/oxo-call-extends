---
name: export2graphlan
category: formatting
description: Conversion software tool for annotating tree with GraPhlAn
tags: [export2graphlan, formatting, visualization, metagenomics, phylogenetic-tree]
author: oxo-call-community
source_url: "https://github.com/segatalab/export2graphlan"
---

## Concepts

- **Tool Overview**: export2graphlan is a conversion tool for producing annotation and tree files for GraPhlAn visualization software.
- **Core Function**: Automatically generates input files for GraPhlAn from various bioinformatics tools' outputs.
- **Input/Output**: Input: MetaPhlAn, LEfSe, or HUMAnN output, BIOM format files. Output: GraPhlAn tree and annotation files.
- **Algorithm**: Parses input files and converts them into GraPhlAn-compatible format with automatic clade highlighting.
- **Key Features**: Multi-tool support, automatic annotation generation, clade highlighting, BIOM format support, batch processing.
- **Installation**: `conda install -c bioconda export2graphlan`

## Pitfalls

- **Tool Compatibility**: Requires specific input formats from supported tools.
- **Tree Quality**: Results depend on input tree quality.
- **Annotation Complexity**: Complex annotations may produce cluttered visualizations.
- **Version Compatibility**: Options may vary between versions.
- **Dependency**: Requires GraPhlAn for visualization.

## Examples

### Basic conversion from MetaPhlAn
**Args:** `export2graphlan_annotate.py -i metaphlan_output.txt -o annotation.txt`
**Explanation:** Converts MetaPhlAn output to GraPhlAn annotation format.

### Generate tree file
**Args:** `export2graphlan_tree.py -i metaphlan_output.txt -o tree.txt`
**Explanation:** Generates tree file from MetaPhlAn output.

### Combined annotation and tree
**Args:** `export2graphlan.py -i metaphlan_output.txt --tree tree.txt --annot annotation.txt -o graphlan_input/`
**Explanation:** Generates both tree and annotation files.

### From BIOM format
**Args:** `export2graphlan_annotate.py -i otu_table.biom -o annotation.txt --biom`
**Explanation:** Converts BIOM format to GraPhlAn annotation.

### With LEfSe output
**Args:** `export2graphlan_annotate.py -i lefse_output.txt -o annotation.txt --lefse`
**Explanation:** Converts LEfSe output to GraPhlAn annotation format.
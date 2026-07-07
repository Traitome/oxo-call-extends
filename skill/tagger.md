---
name: tagger
category: text-mining
description: Tag a corpus of documents with search terms for entities like proteins, species, diseases.
tags: [tagger, text-mining, bioinformatics, entity-recognition]
author: oxo-call-community
source_url: "https://github.com/larsjuhljensen/tagger/blob/1.1/README.md"
---

## Concepts

- **Tool Overview**: tagger (v1.1) tags documents with search terms.
- **Core Function**: Identifies entities in text documents.
- **Algorithm**: Uses dictionary-based entity recognition.
- **Input/Output**: Input: Text documents; Output: Tagged entities.
- **Applications**: Literature mining, entity recognition, text analysis.
- **Installation**: `conda install -c bioconda tagger` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large corpora require significant memory.
- **Dictionary Size**: Large dictionaries affect performance.
- **Ambiguity**: Same term may refer to multiple entities.
- **False Positives**: May incorrectly tag non-entity terms.
- **Case Sensitivity**: May miss lowercase/uppercase variations.
- **Performance**: Processing large documents can be slow.

## Examples

### Display help
**Args:** `tagger --help`
**Explanation:** Shows available options and usage information.

### Basic tagging
**Args:** `tagger -i documents.txt -d dictionary.txt -o tagged.txt`
**Explanation:** Tag documents using dictionary.

### With multiple dictionaries
**Args:** `tagger -i documents.txt -d proteins.txt -d diseases.txt -o tagged.txt`
**Explanation:** Use multiple dictionaries for tagging.

### Verbose mode
**Args:** `tagger -i documents.txt -d dictionary.txt -o tagged.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tagger -i documents.txt -d dictionary.txt -o tagged.txt --stats`
**Explanation:** Generate statistics about tagging.

### Batch processing
**Args:** `for f in docs/*.txt; do tagger -i $f -d dictionary.txt -o tagged/${f%.txt}_tagged.txt; done`
**Explanation:** Process multiple documents.

### Case insensitive
**Args:** `tagger -i documents.txt -d dictionary.txt -o tagged.txt -c`
**Explanation:** Case insensitive matching.

### Include context
**Args:** `tagger -i documents.txt -d dictionary.txt -o tagged.txt -w 5`
**Explanation:** Include 5 words of context around each tag.

### Generate report
**Args:** `tagger -i documents.txt -d dictionary.txt -o tagged.txt --report`
**Explanation:** Generate comprehensive tagging report.

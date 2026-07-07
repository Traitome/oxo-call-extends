---
name: crazydoc
category: formatting
description: Python library to parse DNA sequences from stylized MS Word documents and convert to Biopython records, GenBanks, or FASTA
tags: [crazydoc, docx, biopython, DNA-sequences, sequence-format-conversion, MS-Word, genetic-sequences, sequence-annotation]
author: oxo-call-community
source_url: "https://github.com/Edinburgh-Genome-Foundry/crazydoc"
---

## Concepts

- **Tool Overview**: crazydoc (v0.2.2) - A Python library to parse DNA sequences from colorful and styled MS Word documents (.docx) and convert them to standard bioinformatics formats.
- **Core Function**: Parses styled MS Word documents containing DNA sequence representations, recognizing sequence annotations based on text formatting (highlight color, bold, underline, italics, case changes). Returns Biopython SeqRecord objects with features corresponding to the various formatting annotations.
- **Algorithm**: Uses python-docx to extract document formatting information, identifies sequence regions based on capitalization and styling patterns, maps formatting annotations to Biopython record features.
- **Input**: MS Word documents (.docx) containing DNA or protein sequences with styling annotations.
- **Output**: Biopython SeqRecord objects, which can be saved as GenBank, FASTA, or plotted using dna_features_viewer.
- **Application**: Converting legacy MS Word sequence documents to standard formats, extracting annotated sequences from publications or collaboration documents, batch conversion of sequence collections in Word format.
- **Installation**: `pip install crazydoc` or `conda install -c bioconda crazydoc`

## Pitfalls

- **Python Version**: Requires Python >= 3.9
- **Dependencies**: Requires biopython, python-docx, and dna_features_viewer. Ensure these are installed.
- **Docx Format Only**: Only works with .docx format, not older .doc format
- **Sequence Format Requirements**: Sequences in Word documents should follow standard DNA/Protein notation with consistent formatting
- **GenBank Name Truncation**: records_to_genbank() truncates record names to 20 characters to fit GenBank format requirements
- **Filename Character Restrictions**: Slashes (/ ) in record names are replaced with hyphens (-) in output filenames
- **Color Detection**: Some printers/scanners may not preserve exact color information when printing documents

## Examples

### Parse docx file to Biopython records
**Args:** `from crazydoc import CrazydocParser; parser = CrazydocParser(['highlight_color', 'bold', 'underline']); records = parser.parse_doc_file("sequences.docx")`
**Explanation:** Import CrazydocParser and create parser that recognizes highlight color, bold, and underline annotations. Parse a Word document containing styled DNA sequences and return as Biopython SeqRecord objects.

### Parse protein sequences
**Args:** `parser.parse_doc_file("proteins.docx", is_protein=True)`
**Explanation:** Parse a Word document containing protein sequences by passing is_protein=True. Returns protein SeqRecords which will be saved with .gp extension.

### Convert to GenBank format
**Args:** `from crazydoc import records_to_genbank; records_to_genbank(records)`
**Explanation:** Convert Biopython records to GenBank format files. Each record becomes a separate .gbk file with annotations preserved.

### Convert to GenBank with custom extension
**Args:** `records_to_genbank(records, extension='embl')`
**Explanation:** Save records as EMBL format files instead of GenBank by specifying a different extension.

### Plot sequences with annotations
**Args:** `from crazydoc import CrazydocSketcher; sketcher = CrazydocSketcher(); sketch = sketcher.translate_record(record); sketch.plot()`
**Explanation:** Create a visual plot of the annotated sequence using dna_features_viewer. Generates a graphical representation showing sequence features and annotations.

### Save annotated sequence back to Word
**Args:** `from crazydoc import write_crazydoc; write_crazydoc(seq_record, 'product', 'annotated.docx')`
**Explanation:** Write an annotated Biopython SeqRecord back to a Word document. The qualifier key ('product') determines which feature annotation to highlight in the output document.

### Extract and save multiple sequences
**Args:** `records = parser.parse_doc_file("multi_sequence.docx"); from Bio import SeqIO; SeqIO.write(records, "output.fasta", "fasta")`
**Explanation:** Parse a document with multiple sequences, then save all records to a single FASTA file using Biopythin's SeqIO.

### Custom parsing with different annotation types
**Args:** `parser = CrazydocParser(['italic', 'case_change', 'strikethrough']); records = parser.parse_doc_file("styled_seqs.docx")`
**Explanation:** Create parser with different annotation detection modes to handle documents using various formatting styles for sequence annotation.

### Programmatic usage in Python script
**Args:** `from crazydoc import CrazydocParser; parser = CrazydocParser(); records = parser.parse_doc_file("sequences.docx"); print(f"Found {len(records)} sequences")`
**Explanation:** Basic Python script to parse a docx file and report how many sequences were extracted. Useful for batch processing multiple documents.

### Batch process multiple documents
**Args:** `import glob; from crazydoc import CrazydocParser; parser = CrazydocParser(); [parser.parse_doc_file(f) for f in glob.glob("*.docx")]`
**Explanation:** Process all Word documents in current directory to extract sequences from multiple files at once.

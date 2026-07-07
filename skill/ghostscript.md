---
name: ghostscript
category: document-processing
description: ghostscript - PostScript interpreter and PDF processor.
tags: [ghostscript, document-processing, PDF, PostScript]
author: oxo-call-community
source_url: "http://ghostscript.com/"
---

## Concepts
- **PostScript Processing**: Interprets PostScript language.
- **PDF Processing**: Processes PDF documents.
- **Format Conversion**: Converts between formats.
- **Image Processing**: Processes images in documents.
- **Text Extraction**: Extracts text from documents.

## Pitfalls
- **Memory Usage**: Large documents require memory.
- **Font Handling**: May have font compatibility issues.
- **Version Differences**: Options vary between versions.
- **Security**: PostScript can contain malicious code.
- **Performance**: Large files may be slow.

## Examples
### Convert PDF to PS
**Args:** `ps2pdf input.ps output.pdf`
**Explanation:** Converts PostScript to PDF.

### Convert PDF to images
**Args:** `gs -sDEVICE=png16m -r300 -o output-%03d.png input.pdf`
**Explanation:** Converts PDF to PNG images.

### Extract text
**Args:** `pdftotext input.pdf output.txt`
**Explanation:** Extracts text from PDF.

### Compress PDF
**Args:** `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -o output.pdf input.pdf`
**Explanation:** Compresses PDF file.

### Merge PDFs
**Args:** `gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=merged.pdf file1.pdf file2.pdf`
**Explanation:** Merges multiple PDF files.
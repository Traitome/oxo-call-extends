---
name: tesseract
category: utility
description: Tesseract - Legacy optical character recognition (OCR) engine (not a bioinformatics tool).
tags: [tesseract, ocr, image, text-recognition, legacy]
author: oxo-call-community
source_url: "https://github.com/tesseract-ocr/tesseract"
---

## Concepts

- **Tool Overview**: Tesseract - A highly capable OCR (Optical Character Recognition) engine originally developed by HP and now maintained by Google. It is NOT a bioinformatics tool.
- **Core Function**: Converts images containing text into machine-readable text data.
- **Key Features**: Supports multiple languages, various image formats, and provides high accuracy text recognition.
- **Installation**: `apt-get install tesseract-ocr` (Linux) or download installers from GitHub
- **Note**: This is a general-purpose OCR tool. In bioinformatics, it may be used indirectly for digitizing printed documents or reading printed text from images.

## Pitfalls

- **Not a bioinformatics tool**: Cannot be used directly for biological data analysis.
- **Image Quality**: OCR accuracy depends heavily on input image quality.
- **Layout**: Complex page layouts may reduce accuracy.

## Examples

### Basic OCR
**Args:** `tesseract image.png output_text.txt`
**Explanation:** Recognize text from image and save to text file.

### Specific language
**Args:** `tesseract image.png output -l eng+spa`
**Explanation:** Use English and Spanish language models for recognition.

### Page segmentation mode
**Args:** `tesseract document.jpg text_output --psm 6`
**Explanation:** Use page segmentation mode 6 (uniform block of text).

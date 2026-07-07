---
name: gocr
category: utility
description: GOCR is a command-line optical character recognition (OCR) tool that extracts text from image files.
tags: [gocr, OCR, image-processing, text-extraction, utility]
author: oxo-call-community
source_url: "https://jocr.sourceforge.net"
---

## Concepts

- **Optical Character Recognition**: GOCR analyzes image files to recognize and extract text characters using pattern recognition algorithms.

- **Image Format Support**: Supports multiple image formats including PNG, JPEG, GIF, TIFF, and PBM/PGM/PPM formats.

- **Language Support**: Capable of recognizing text in multiple languages with appropriate training data.

- **Output Formats**: Generates plain text output with optional bounding box information for each recognized character.

- **Batch Processing**: Supports processing multiple image files in a single run, enabling automated text extraction workflows.

- **Preprocessing Options**: Provides options for image preprocessing including thresholding, scaling, and noise reduction.

## Pitfalls

- **Image Quality**: Recognition accuracy depends heavily on image quality. Blurry, skewed, or low-contrast images may produce poor results.

- **Font Limitations**: Works best with standard fonts. Handwritten text or highly stylized fonts may not be recognized correctly.

- **Language Limitations**: Default configuration may not support non-Latin scripts without additional training data.

- **Layout Complexity**: Complex document layouts with multiple columns or overlapping text may confuse the recognition algorithm.

- **Output Format**: Default output may include extraneous characters or spacing issues that require post-processing.

## Examples

### Basic OCR on an image
**Args:** `gocr input.png`
**Explanation:** Extracts text from input.png and prints the result to standard output.

### Save output to file
**Args:** `gocr input.jpg -o output.txt`
**Explanation:** Extracts text from input.jpg and saves the result to output.txt.

### Batch process multiple images
**Args:** `gocr image1.png image2.png image3.png -o results.txt`
**Explanation:** Processes multiple image files and combines results into a single output file.

### Set language
**Args:** `gocr -l eng input.png`
**Explanation:** Specifies English language for OCR recognition. Use appropriate language codes for other languages.

### Include bounding box information
**Args:** `gocr -b input.png`
**Explanation:** Outputs bounding box coordinates for each recognized character, useful for positioning information.

### Adjust threshold
**Args:** `gocr -t 50 input.png`
**Explanation:** Sets a custom threshold value (0-255) for image binarization, useful for improving recognition on low-contrast images.

### Scale image before processing
**Args:** `gocr -s 2 input.png`
**Explanation:** Scales the image by a factor of 2 before processing, which can improve recognition of small text.
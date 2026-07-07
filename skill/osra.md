---
name: osra
category: formatting
description: OSRA converts graphical chemical structures to SMILES or SDF formats.
tags: [osra, formatting, chemistry, structure-recognition]
author: oxo-call-community
source_url: "http://cactus.nci.nih.gov/osra/"
---

## Concepts

- **Tool Overview**: OSRA extracts chemical structures from images.
- **Core Function**: Converts graphical representations to chemical formats.
- **Algorithm**: Uses optical structure recognition.
- **Input Format**: Accepts image files (PNG, JPEG, TIFF).
- **Output**: Produces SMILES or SDF format.
- **Use Case**: Cheminformatics, patent analysis, and structure digitization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Image Quality**: Results depend on input image quality.
- **Complex Structures**: May fail on complex molecules.
- **Ambiguity**: Some structures may be ambiguous.
- **OCR Errors**: Optical recognition may have errors.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `osra --help`
**Explanation:** Shows available options and usage instructions.

### Convert image to SMILES
**Args:** `osra structure.png -o structure.smi`
**Explanation:** Converts image to SMILES format.

### Output SDF
**Args:** `osra structure.png -o structure.sdf --sdf`
**Explanation:** Outputs in SDF format.

### Multiple images
**Args:** `osra *.png -o structures/`
**Explanation:** Processes multiple image files.

### Verbose mode
**Args:** `osra structure.png -v -o structure.smi`
**Explanation:** Runs with verbose output.

### Quality threshold
**Args:** `osra structure.png -q 0.9 -o structure.smi`
**Explanation:** Sets confidence threshold.

### Batch processing
**Args:** `osra -d images/ -o structures/`
**Explanation:** Processes all images in directory.
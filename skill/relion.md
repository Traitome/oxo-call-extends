---
name: relion
category: utility
description: RELION is image-processing software for cryo-electron microscopy for 3D structure determination.
tags: [relion, utility, cryo-em, 3d-reconstruction]
author: oxo-call-community
source_url: "https://relion.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: relion reconstructs structures.
- **Core Function**: 3D reconstruction.
- **Algorithm**: Uses maximum likelihood methods.
- **Input Format**: Accepts EM images.
- **Output**: Produces 3D models.
- **Use Case**: Structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Image Quality**: Affects reconstruction.
- **Parameters**: Must be configured.
- **Runtime**: Reconstruction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `relion --help`
**Explanation:** Shows available options and usage instructions.

### Run reconstruction
**Args:** `relion_refine --i particles.star --o reconstruction --auto_refine`
**Explanation:** Runs 3D auto-refinement.

### With parameters
**Args:** `relion_refine --i particles.star --o reconstruction --par params.conf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `relion_refine --verbose --i particles.star --o reconstruction`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `relion_refine --j 4 --i particles.star --o reconstruction`
**Explanation:** Uses 4 threads for parallel processing.

### Classify particles
**Args:** `relion_classify3d --i particles.star --o classes --K 4`
**Explanation:** Performs 3D classification.

### Generate report
**Args:** `relion_refine --i particles.star --o reconstruction --report report.html`
**Explanation:** Generates HTML report.
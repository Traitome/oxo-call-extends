---
name: fiji-max_inscribed_circles
category: image-analysis
description: "ImageJ/Fiji plugin implementing an iterative Largest Inscribed Circle algorithm using a euclidean distance map for finding maximum non-overlapping circles in binary images."
tags: [fiji-max_inscribed_circles, image-analysis, ImageJ, Fiji, plugin, binary-image, euclidean-distance-map, circles, java, bioinformatics]
author: oxo-call-community
source_url: "https://imagej.net/plugins/max-inscribed-circles"
---

## Concepts

- **Tool Overview**: Max Inscribed Circles is an ImageJ/Fiji plugin that implements an iterative Largest Inscribed Circle algorithm using a euclidean distance map. It finds the maximum number of non-overlapping circles that can fit within a binary image or selection.
- **Core Function**: Uses a Local Maxima Finder to efficiently identify multiple circles of varying sizes in a single pass, placing larger circles first and continuing until the minimum diameter is reached.
- **Input/Output**: Input: 8-bit binary image or selection. Output: Circles added to ROI Manager as individual ROIs.
- **Algorithm**: Rewritten in 2016 with a faster algorithm that uses distance transform. Instead of calculating one distance map per circle, it finds all non-overlapping circles of the same size simultaneously.
- **Key Features**: Fast multi-circle detection, ROI Manager integration, macro recordable, spine detection (optional), Groovy/Java API for scripting, Fiji update site installation.
- **Installation**: Install via FIJI's BIOP update site (Plugins > BIOP > Image Analysis > Binary > Max Inscribed Circles).

## Pitfalls

- **Not a Standalone CLI Tool**: This is an ImageJ/Fiji plugin, not a standalone command-line tool. It must be run within ImageJ or Fiji, or via ImageJ macro/script.
- **Input Must Be Binary**: The plugin requires an 8-bit binary image (black and white). Non-binary images must be thresholded first using Image > Adjust > Threshold.
- **Accuracy Limitation**: Accuracy is limited by the finite resolution of the distance map. Circles larger than 2 pixels in diameter should be sufficiently accurate for most applications.
- **Minimum Diameter Setting**: Setting minimum diameter to 0 returns only the single largest inscribed circle.
- **Overlapping Circles**: The algorithm ensures circles do not overlap, but this may not be desired for all applications.

## Examples

### Via ImageJ GUI
**Args:** `Plugins > BIOP > Image Analysis > Binary > Max Inscribed Circles`
**Explanation:** Open ImageJ, load your binary image, then go to Plugins > BIOP > Image Analysis > Binary > Max Inscribed Circles. Set minimum disk diameter and click OK.

### Via ImageJ Macro
**Args:** `run("Max Inscribed Circles...", "minimum=20");`
**Explanation:** Macro command to run the plugin with a minimum circle diameter of 20 pixels. Results are added to the ROI Manager.

### Via Groovy Script (Builder Pattern)
**Args:**
```
MaxInscribedCircles mic = MaxInscribedCircles.builder(imp)
  .minimumDiameter(5)
  .useSelectionOnly(true)
  .getSpine(true)
  .spineClosenessTolerance(20)
  .spineMinimumSimilarity(0.3)
  .build()
mic.process()
```
**Explanation:** Uses the builder pattern for more control over parameters including minimum diameter, selection-only mode, spine detection, and naming options.

### Static Method Call
**Args:** `MaxInscribedCircles.getMaxInscribedCircles(imp, 5)`
**Explanation:** For programmatic use in Java or Groovy, the static method provides a simple interface to get all circles as an ArrayList of Roi objects.

### Finding Single Largest Circle
**Args:** `run("Max Inscribed Circles...", "minimum=0")`
**Explanation:** Set Minimum Disk Diameter to 0 in the plugin dialog to return only the single largest inscribed circle, useful for measuring maximum vessel width or similar metrics.

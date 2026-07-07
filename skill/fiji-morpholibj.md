---
name: fiji-morpholibj
category: image-analysis
description: "MorphoLibJ is a collection of mathematical morphology methods and plugins for ImageJ/Fiji, providing 2D/3D image segmentation, filtering, and analysis capabilities."
tags: [fiji-morpholibj, image-analysis, ImageJ, Fiji, MorphoLibJ, morphology, segmentation, plugin, Java, visualization, bioinformatics, microscopy]
author: oxo-call-community
source_url: "https://imagej.net/plugins/morpholibj"
---

## Concepts

- **Tool Overview**: MorphoLibJ is a collection of mathematical morphology methods and plugins for ImageJ/Fiji, created at INRA-IJPB Modeling and Digital Imaging lab. It extends ImageJ with essential morphological operations that were missing in the base installation.
- **Core Function**: Provides comprehensive morphological image analysis including filtering, reconstruction, segmentation, and measurements for 2D and 3D grayscale and binary images.
- **Input/Output**: Input: Various image formats (TIFF, PNG, JPEG, LSM, etc.) supported by ImageJ. Output: Processed images, label maps, ROI sets, measurement tables, and 3D visualizations.
- **Algorithm**: Java-based implementation of mathematical morphology operations including erosion, dilation, opening, closing, top-hat transforms, watershed segmentation, and morphological reconstruction.
- **Key Features**: Morphological filtering (2D/3D, binary/grayscale), regional and extended minima/maxima detection, watershed segmentation with dams, 2D/3D measurements (volume, surface area, inertia ellipse), binary/label image utilities, and comprehensive macro/scripting support.
- **Installation**: `conda install -c bioconda fiji-morpholibj` or add IJPB-plugins update site in Fiji (Help > Update > Manage update sites > Activate IJPB-plugins)

## Pitfalls

- **Fiji Dependency**: The conda package `fiji-morpholibj` requires Fiji as a dependency. Ensure Fiji is properly installed and configured before using MorphoLibJ functions.
- **Memory Usage**: 3D morphological operations can consume significant RAM. For large 3D stacks, ensure adequate memory allocation via Fiji > Edit > Options > Memory & Threads.
- **Image Type Requirements**: Watershed segmentation expects high-intensity boundaries (gradient images). Using "Object Image" mode on border images produces poor results.
- **Tolerance Parameter Sensitivity**: The tolerance value is image-type dependent. A tolerance of 10 works for 8-bit images but may need to increase to ~2000 for 16-bit images.
- **Macro vs GUI**: Some advanced operations may require macro scripting. Familiarize yourself with ImageJ macro language for batch processing.

## Examples

### Install MorphoLibJ via conda
**Args:** `conda install -c bioconda fiji-morpholibj`
**Explanation:** Installs MorphoLibJ along with its Fiji dependency using Bioconda. Requires Fiji to be launchable from the command line after installation.

### Install via Fiji update site
**Args:** `Help > Update > Manage update sites > IJPB-plugins`
**Explanation:** In Fiji GUI, select Help > Update to open the updater. Click "Manage update sites", find "IJPB-plugins" in the list, activate it, then click "Apply changes" and restart Fiji. This gives you the most current version.

### Open an image and apply grayscale erosion
**Args:** `Process > Filters > Morphological Operations > Erosion`
**Explanation:** In Fiji, open your image (File > Open), then run the morphological filter: Process > Filters > Morphological Operations. Select "Erosion" as the operation type and adjust the structuring element size (default is 1 pixel/voxel radius).

### Segment objects using watershed
**Args:** `Plugins > MorphoLibJ > Morphological Segmentation`
**Explanation:** Use the Morphological Segmentation plugin (Plugins > MorphoLibJ > Morphological Segmentation). Load a grayscale image, select "Border Image" if edges are highlighted or "Object Image" to let the plugin compute gradient. Adjust tolerance (start with 10 for 8-bit) and click "Run" to perform watershed segmentation.

### Extract largest connected component
**Args:** `Plugins > MorphoLibJ > Binary > Keep Largest & Fill Holes`
**Explanation:** Use Plugins > MorphoLibJ > Binary > Keep Largest & Fill Holes. This operation removes all but the largest connected component in a binary image and fills holes within the retained object.

### Measure 3D object properties
**Args:** `Plugins > MorphoLibJ > Analyze > 3D Measurements`
**Explanation:** After segmentation (creating a label image), use Plugins > MorphoLibJ > Analyze > 3D Measurements. Select your label image and a reference grayscale image if intensity measurements are needed. The plugin outputs volume, surface area, centroid, and intensity statistics for each label.

### Batch processing with ImageJ macro
**Args:**
```python
inputDir = getDirectory("Choose Input Directory");
outputDir = getDirectory("Choose Output Directory");
list = getFileList(inputDir);
for (i = 0; i < list.length; i++) {
    open(inputDir + list[i]);
    run("Morphological Filters", "operation=Opening element=Square radius=1");
    saveAs("TIFF", outputDir + list[i]);
    close();
}
```
**Explanation:** Write a macro to process multiple files.

### Compute end-point distance transform
**Args:** `Plugins > MorphoLibJ > Binary > Distance Map`
**Explanation:** Use Plugins > MorphoLibJ > Binary > Distance Map. This creates an image where each pixel value represents its distance to the nearest background pixel (for binary images) or computes end-point distance transform for skeleton analysis.

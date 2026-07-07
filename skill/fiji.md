---
name: fiji
category: image-analysis
description: "Fiji is an image processing package—a 'batteries-included' distribution of ImageJ with bundled plugins for scientific image analysis."
tags: [fiji, image-analysis, ImageJ, Fiji, image-processing, plugin, Java, visualization, bioinformatics, microscopy]
author: oxo-call-community
source_url: "https://imagej.net/software/fiji"
---

## Concepts

- **Tool Overview**: Fiji (Fiji Is Just ImageJ) is an image processing package that bundles ImageJ with a comprehensive collection of scientific image analysis plugins. It is designed for biological image analysis including microscopy, cell counting, and fluorescence analysis.
- **Core Function**: Provides a extensible platform for image processing, analysis, and visualization through both GUI interactions and scripting (macros, Python, Java).
- **Input/Output**: Input: Various image formats (TIFF, PNG, JPEG, LSM, etc.). Output: Processed images, ROIs, measurements tables, and batch results.
- **Algorithm**: Java-based image processing with 2D/3D analysis capabilities, integrated ImageJ plugins, and Fiji-specific extensions.
- **Key Features**: Bundled plugins (150+), 3D viewers, macro recording, headless batch processing, Python/Jython scripting support, Fiji update site for additional plugins.
- **Installation**: `conda install -c bioconda fiji` or download from https://imagej.net/software/fiji

## Pitfalls

- **Memory Management**: Fiji can consume significant RAM with large images or 3D data. Use `--mem` flag to set memory limits (e.g., `fiji --mem=4g`).
- **Headless Mode Limitations**: Some plugins that require GUI components will fail in headless mode. Test scripts in GUI mode first before batch processing.
- **Plugin Compatibility**: Not all ImageJ plugins are compatible with Fiji's bundled Java version. Check plugin documentation for requirements.
- **Scripting Complexity**: Advanced automation may require learning ImageJ macro language, Jython, or Beanshell syntax.
- **Updater Auto-Check**: In headless cluster environments, disable the updater auto-check to prevent unnecessary server connections: `-Dimagej.updater.disableAutocheck=true`

## Examples

### Open an image
**Args:** `fiji --open /path/to/image.tif`
**Explanation:** Opens an image file directly from the command line into the Fiji GUI.

### Run a macro in headless mode
**Args:** `fiji --headless -macro /path/to/process.ijm`
**Explanation:** Runs an ImageJ macro script in headless mode without GUI, suitable for batch processing on servers or clusters.

### Run a Python script with parameters
**Args:** `fiji --headless --run /path/to/script.py 'param1=value1,param2=value2'`
**Explanation:** Executes a Python script (Jython) with script parameters in headless mode. Script must use @Parameter annotations.

### Display help
**Args:** `fiji --help`
**Explanation:** Shows all available command-line options including memory settings, headless mode, and script interpreter flags.

### Dry run to see Java command
**Args:** `fiji --dry-run`
**Explanation:** Shows the actual Java command that would be executed without running Fiji. Useful for debugging launcher issues.

### Batch process with memory limit
**Args:** `fiji --mem=8g --headless -macro /path/to/batch.ijm`
**Explanation:** Runs batch processing with 8GB memory limit. Adjust based on image sizes and available system RAM.

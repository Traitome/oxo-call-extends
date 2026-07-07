---
name: nmrglue
category: programming
description: NMRGlue is a Python module for working with NMR spectroscopy data.
tags: [nmrglue, programming, python, nmr]
author: oxo-call-community
source_url: "http://www.nmrglue.com"
---

## Concepts

- **Tool Overview**: NMRGlue provides tools for processing and analyzing NMR data in Python.
- **Core Function**: Reads, writes, and processes NMR data files.
- **Algorithm**: Implements various NMR data processing algorithms.
- **Input Format**: Accepts NMR data formats (VnmrJ, Bruker, NMRPipe).
- **Output**: Produces processed NMR data and analysis results.
- **Use Case**: NMR data analysis, peak picking, and spectral processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **File Compatibility**: Requires specific NMR data formats.
- **Memory Usage**: Large spectra require memory.
- **Dependency**: Requires Python and related scientific libraries.
- **Documentation**: Limited documentation for some features.
- **Performance**: May have performance considerations for large datasets.

## Examples

### Install package
**Args:** `pip install nmrglue`
**Explanation:** Installs NMRGlue package.

### Import module
**Args:** `import nmrglue as ng`
**Explanation:** Imports NMRGlue module in Python.

### Read NMR data
**Args:** `dic, data = ng.bruker.read('fid/')`
**Explanation:** Reads Bruker NMR data.

### Process FID
**Args:** `data_proc = ng.proc_base.fft(data)`
**Explanation:** Applies FFT to FID data.

### Save processed data
**Args:** `ng.bruker.write('proc/', dic, data_proc, overwrite=True)`
**Explanation:** Saves processed NMR data.

### Peak picking
**Args:** `peaks = ng.peakpick.pick(data_proc, pthres=0.1)`
**Explanation:** Detects peaks in NMR spectrum.

### Documentation
**Args:** `pydoc nmrglue`
**Explanation:** Shows documentation for NMRGlue.
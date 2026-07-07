---
name: test-glibc
category: utility
description: Conda virtual package for detecting GNU C Library (glibc) version on Linux systems.
tags: [test-glibc, glibc, conda, virtual-package, utility]
author: oxo-call-community
source_url: "https://conda.org/learn/ceps/cep-0030"
---

## Concepts

- **Tool Overview**: test-glibc is a Conda virtual package that exposes the system's glibc version to the Conda solver for compatibility checking.
- **Core Function**: Enables Conda packages to declare dependencies on minimum glibc versions, ensuring packages only install on compatible systems.
- **Virtual Package**: Virtual packages are synthetic packages that represent host capabilities; they are never installed but detected automatically.
- **Version Format**: glibc version is reported as major.minor (e.g., 2.38), constrained to first two components.
- **Platform**: Only available on Linux systems; not present on macOS or Windows.
- **Detection**: Conda automatically detects glibc version from the system, typically via `ldd --version` or system library inspection.

## Pitfalls

- **Non-Linux Systems**: test-glibc is only relevant on Linux; it will not be detected on macOS or Windows.
- **Version Override**: Setting CONDA_OVERRIDE_GLIBC may allow installation of incompatible packages, causing runtime errors.
- **Forward Compatibility**: Packages built against older glibc (e.g., 2.17) work on newer systems, but not vice versa.
- **Docker Containers**: glibc version in containers depends on the base image; ensure compatibility with your base image.
- **Cross-Compilation**: When cross-compiling, ensure target system's glibc version meets package requirements.

## Examples

### Check detected glibc version
**Args:** `conda info | grep -A 5 "virtual packages"`
**Explanation:** Display the virtual packages detected by Conda, including __glibc version on Linux systems.

### Install package requiring specific glibc version
**Args:** `CONDA_OVERRIDE_GLIBC=2.17 conda install some-package`
**Explanation:** Override glibc detection for troubleshooting or testing compatibility with older systems.

### List virtual packages
**Args:** `conda info --json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('virtual_packages',{}), indent=2))"`
**Explanation:** Use JSON output to programmatically inspect virtual packages including __glibc.

### Build package with glibc constraint
**Args:** `conda-build --no-test --override-channels -c conda-forge -c bioconda recipe/`
**Explanation:** Build a conda package that may declare __glibc >=2.17 as a run requirement for Linux compatibility.

### Check system glibc directly
**Args:** `ldd --version | head -1`
**Explanation:** Directly check the system's glibc version using the ldd command.
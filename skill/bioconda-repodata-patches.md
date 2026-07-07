---
name: bioconda-repodata-patches
category: containerization
description: Generate tweaks to index metadata, hosted separately from anaconda.org index
tags: [bioconda, repodata, patching, metadata]
author: oxo-call-community
source_url: "https://github.com/bioconda/bioconda-repodata-patches"
---

## Concepts

- **Tool Overview**: bioconda-repodata-patches provides a mechanism for patching Bioconda repository metadata (repodata) to fix issues like incorrect dependency pinning without rebuilding packages.
- **Repodata**: JSON files containing package metadata (dependencies, versions, etc.) used by conda/mamba for package resolution.
- **Patch Application**: Patches are applied to repodata.json files for each architecture (linux-64, osx-64, noarch, etc.).
- **Use Case**: Fixing dependency issues in already-published packages, such as adding version constraints to broken dependencies.

## Pitfalls

- **Version Specificity**: Patches are versioned and may need updates when new package versions are released.
- **Architecture Coverage**: Patches must be applied to all relevant architectures.
- **Testing Required**: Always test patches with `show_diff.py` before deployment.

## Examples

### Generate patch JSON
**Args:** `python gen_patch_json.py`
**Explanation:** Generates patch instructions JSON from patch YAML files.

### View patch differences
**Args:** `python show_diff.py`
**Explanation:** Shows changes that would be made to repodata if patches were applied.
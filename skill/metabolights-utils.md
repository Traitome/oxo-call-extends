---
name: metabolights-utils
category: utility
description: Command line interface for MetaboLights metabolomics data repository.
tags: [metabolights-utils, metabolomics, data-management]
author: oxo-call-community
source_url: "https://github.com/EBI-Metabolights/metabolights-utils"
---

## Concepts

- **Tool Overview**: MetaboLights-utils provides CLI for MetaboLights repository.
- **Core Function**: Metabolomics data management and access.
- **Data Upload**: Uploads data to MetaboLights.
- **Data Download**: Downloads data from repository.
- **Metadata Handling**: Manages metadata for studies.
- **Installation**: `conda install -c bioconda metabolights-utils`

## Pitfalls

- **Network Requirements**: Requires internet access.
- **Authentication**: Needs MetaboLights account.
- **Data Format**: Strict format requirements.
- **Rate Limiting**: Subject to API rate limits.
- **Dependency Issues**: May have conflicting dependencies.
- **Version Compatibility**: API changes may break tools.

## Examples

### Upload data
**Args:** `ml-upload -i study_dir/ -s MTBLS123`
**Explanation:** Uploads study to MetaboLights.

### Download data
**Args:** `ml-download -s MTBLS123 -o study_dir/`
**Explanation:** Downloads study from MetaboLights.

### Validate metadata
**Args:** `ml-validate -i metadata.tsv`
**Explanation:** Validates metadata format.

### List studies
**Args:** `ml-list --search "cancer"`
**Explanation:** Searches for studies.

### Help documentation
**Args:** `ml-utils --help`
**Explanation:** Displays available options.

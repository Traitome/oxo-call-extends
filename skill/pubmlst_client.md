---
name: pubmlst_client
category: utility
description: pubmlst_client lists and downloads MLST schemes from pubMLST.org database.
tags: [pubmlst_client, utility, MLST, sequence-typing]
author: oxo-call-community
source_url: "https://github.com/Public-Health-Bioinformatics/pubmlst_client"
---

## Concepts

- **Tool Overview**: pubmlst_client accesses MLST databases.
- **Core Function**: MLST scheme management.
- **Algorithm**: Uses web API queries.
- **Input Format**: Accepts query parameters.
- **Output**: Produces scheme data.
- **Use Case**: Bacterial typing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Dependency**: Requires internet access.
- **Data Quality**: Results depend on database.
- **API Rate Limits**: May affect downloads.
- **Runtime**: Downloads may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pubmlst_client --help`
**Explanation:** Shows available options and usage instructions.

### List schemes
**Args:** `pubmlst_client list`
**Explanation:** Lists available MLST schemes.

### Download scheme
**Args:** `pubmlst_client download -s scheme_name -o output_dir`
**Explanation:** Downloads specified MLST scheme.

### With parameters
**Args:** `pubmlst_client download -s scheme_name -p params.yaml -o output_dir`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pubmlst_client -v download -s scheme_name -o output_dir`
**Explanation:** Runs with verbose output.

### Update schemes
**Args:** `pubmlst_client update -o output_dir`
**Explanation:** Updates all local schemes.

### Generate report
**Args:** `pubmlst_client download -s scheme_name -o output_dir --report report.html`
**Explanation:** Generates HTML report.
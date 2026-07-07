---
name: planemo
category: utility
description: planemo assists in building tools for the Galaxy project.
tags: [planemo, utility, galaxy, tools]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/planemo"
---

## Concepts

- **Tool Overview**: planemo builds Galaxy tools.
- **Core Function**: Galaxy tool development utilities.
- **Algorithm**: Uses workflow management methods.
- **Input Format**: Accepts tool configuration files.
- **Output**: Produces Galaxy tool definitions.
- **Use Case**: Galaxy tool development, testing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex workflows require memory.
- **Configuration Errors**: May have setup issues.
- **Galaxy Compatibility**: Requires Galaxy framework.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `planemo --help`
**Explanation:** Shows available options and usage instructions.

### Run tool tests
**Args:** `planemo test -t tool.xml`
**Explanation:** Tests Galaxy tool definition.

### With parameters
**Args:** `planemo test -t tool.xml -p params.yaml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `planemo test -v -t tool.xml`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `planemo test -t 4 -t tool.xml`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `planemo test -t tool.xml -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `planemo test -t tool.xml --report report.html`
**Explanation:** Generates HTML report.
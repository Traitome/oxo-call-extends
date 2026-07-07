---
name: pytest-marks
category: utility
description: pytest-marks provides decorators for setting marks on pytest test methods.
tags: [pytest-marks, utility, testing, pytest]
author: oxo-call-community
source_url: "https://github.com/adamgoucher/pytest-marks"
---

## Concepts

- **Tool Overview**: pytest-marks decorates tests.
- **Core Function**: Test marking.
- **Algorithm**: Uses pytest API.
- **Input Format**: Accepts test files.
- **Output**: Produces marked tests.
- **Use Case**: Test organization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Many tests require memory.
- **Mark Conflicts**: May occur.
- **Test Discovery**: Must work.
- **Runtime**: Testing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pytest-marks --help`
**Explanation:** Shows available options and usage instructions.

### Run tests
**Args:** `pytest-marks run -i tests/ -o results.xml`
**Explanation:** Runs marked tests.

### With parameters
**Args:** `pytest-marks run -i tests/ -p params.yaml -o results.xml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pytest-marks -v run -i tests/ -o results.xml`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pytest-marks -t 4 run -i tests/ -o results.xml`
**Explanation:** Uses 4 threads for parallel processing.

### List marks
**Args:** `pytest-marks list -i tests/`
**Explanation:** Lists available marks.

### Generate report
**Args:** `pytest-marks run -i tests/ -o results.xml --report report.html`
**Explanation:** Generates HTML report.
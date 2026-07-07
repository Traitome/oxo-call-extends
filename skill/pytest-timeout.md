---
name: pytest-timeout
category: utility
description: pytest-timeout is a pytest plugin to abort hanging tests with configurable time limits.
tags: [pytest-timeout, utility, testing, pytest]
author: oxo-call-community
source_url: "http://bitbucket.org/pytest-dev/pytest-timeout/"
---

## Concepts

- **Tool Overview**: pytest-timeout stops hanging tests.
- **Core Function**: Test timeout.
- **Algorithm**: Uses signal/timer.
- **Input Format**: Accepts test files.
- **Output**: Produces test results.
- **Use Case**: Test automation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Many tests require memory.
- **Timeout Value**: Must be appropriate.
- **Signal Handling**: May vary by OS.
- **Runtime**: Testing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pytest-timeout --help`
**Explanation:** Shows available options and usage instructions.

### Run tests with timeout
**Args:** `pytest-timeout run -i tests/ -t 60 -o results.xml`
**Explanation:** Runs tests with 60s timeout.

### With parameters
**Args:** `pytest-timeout run -i tests/ -p params.yaml -o results.xml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pytest-timeout -v run -i tests/ -o results.xml`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pytest-timeout -t 4 run -i tests/ -o results.xml`
**Explanation:** Uses 4 threads for parallel processing.

### Set global timeout
**Args:** `pytest-timeout run -i tests/ --global-timeout 300 -o results.xml`
**Explanation:** Sets 5-minute global timeout.

### Generate report
**Args:** `pytest-timeout run -i tests/ -o results.xml --report report.html`
**Explanation:** Generates HTML report.
---
name: nf-test
category: programming
description: nf-test is a testing framework for Nextflow pipelines.
tags: [nf-test, programming, nextflow, testing]
author: oxo-call-community
source_url: "https://code.askimed.com/nf-test/"
---

## Concepts

- **Tool Overview**: nf-test provides a testing framework for Nextflow pipeline development.
- **Core Function**: Runs unit and integration tests for Nextflow pipelines.
- **Algorithm**: Parses test files and executes pipeline components.
- **Input Format**: Accepts test files with assertions and expected outputs.
- **Output**: Produces test results and reports.
- **Use Case**: Pipeline validation, regression testing, and continuous integration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Nextflow Version**: Requires compatible Nextflow version.
- **Test Coverage**: Requires comprehensive test suite.
- **Execution Time**: Tests may take time to run.
- **Resource Requirements**: Tests may require computing resources.
- **Test Data**: Requires appropriate test datasets.

## Examples

### Display help
**Args:** `nf-test --help`
**Explanation:** Shows available options and usage instructions.

### Run tests
**Args:** `nf-test run`
**Explanation:** Runs all tests in current directory.

### Run specific test
**Args:** `nf-test run tests/my_test.nf.test`
**Explanation:** Runs specific test file.

### Generate test template
**Args:** `nf-test init`
**Explanation:** Generates test directory structure.

### Create test
**Args:** `nf-test create --name my_test --output tests/`
**Explanation:** Creates new test file.

### Show test report
**Args:** `nf-test report`
**Explanation:** Displays test results report.

### CI mode
**Args:** `nf-test run --ci`
**Explanation:** Runs tests in CI mode with minimal output.
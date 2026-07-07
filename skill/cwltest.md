---
name: cwltest
category: programming
description: Common workflow language testing framework
tags: [cwltest, programming, CWL, testing, workflow]
author: oxo-call-community
source_url: "https://github.com/common-workflow-language/cwltest"
---

## Concepts

- **Tool Overview**: cwltest (v2.2.20220521103021+) is a testing framework for Common Workflow Language (CWL) workflows and tools.
- **Core Function**: Validates CWL workflows and tools against test cases, ensuring they produce expected outputs.
- **Input/Output**: Input: CWL workflow/tool files, test case YAML files. Output: Test results, pass/fail reports.
- **Key Features**: Runs CWL workflows with specified inputs, compares outputs against expected results, generates test reports.
- **Installation**: `conda install -c bioconda cwltest`

## Pitfalls

- **CWL Version**: Ensure test cases match the CWL version supported by the workflow.
- **Environment Setup**: Requires CWL runner (e.g., cwltool) to be installed and configured.
- **Test Case Format**: Test YAML files must follow the cwltest specification.
- **File Paths**: Relative paths in test cases may cause issues; use absolute paths or adjust working directory.
- **Performance**: Running many test cases can be time-consuming for complex workflows.

## Examples

### Run tests for CWL workflow
**Args:** `cwltest --test test_cases.yaml --tool cwltool`
**Explanation:** Run test cases against CWL workflow using cwltool as the executor.

### Run single test
**Args:** `cwltest --test test_cases.yaml --tool cwltool --index 0`
**Explanation:** Run only the first test case from the test file.

### Generate JUnit report
**Args:** `cwltest --test test_cases.yaml --tool cwltool --junit-report results.xml`
**Explanation:** Run tests and generate JUnit-style XML report.

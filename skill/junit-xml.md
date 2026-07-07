---
name: junit-xml
category: utility
description: Creates JUnit XML test result documents that can be read by tools such as Jenkins.
tags: [junit-xml, utility, testing, CI/CD, reporting]
author: oxo-call-community
source_url: "https://github.com/kyrus/python-junit-xml"
---

## Concepts

- **Tool Overview**: junit-xml (v1.8) - A Python library for creating JUnit XML test result documents.
- **JUnit Format**: Generates test results in JUnit XML format.
- **CI/CD Integration**: Works with Jenkins, GitHub Actions, and other CI/CD tools.
- **Test Reporting**: Generates comprehensive test reports.
- **Python Integration**: Integrates with Python test frameworks.
- **Multiple Test Cases**: Supports multiple test cases and suites.

## Pitfalls

- **XML Validity**: Generated XML must be valid JUnit format.
- **Encoding Issues**: Character encoding can affect XML parsing.
- **Test Naming**: Test names must follow JUnit conventions.
- **Version Compatibility**: Different CI tools may require specific formats.
- **Special Characters**: Special characters in test names need escaping.
- **Report Size**: Very large test suites can produce large reports.

## Examples

### Create simple test result
**Args:** `python -c "from junit_xml import TestSuite, TestCase; tc = TestCase('test1'); print(TestSuite.to_xml_string([TestSuite('suite', [tc])]))"`
**Explanation:** Creates and prints JUnit XML from Python.

### Add test failure
**Args:** `python -c "from junit_xml import TestCase; tc = TestCase('test'); tc.add_failure('failed'); print(tc.to_xml())"`
**Explanation:** Creates test case with failure.

### Multiple test suites
**Args:** `python -c "from junit_xml import TestSuite; suites = [TestSuite('suite1', cases1), TestSuite('suite2', cases2)]; TestSuite.to_file('results.xml', suites)"`
**Explanation:** Writes multiple test suites to file.

### Add error to test
**Args:** `python -c "from junit_xml import TestCase; tc = TestCase('test'); tc.add_error('error message'); print(tc.to_xml())"`
**Explanation:** Creates test case with error.

### Add test properties
**Args:** `python -c "from junit_xml import TestCase; tc = TestCase('test', {'version': '1.0'}); print(tc.to_xml())"`
**Explanation:** Adds custom properties to test case.

### Generate report from pytest
**Args:** `pytest --junitxml=results.xml`
**Explanation:** Runs pytest and generates JUnit XML report.
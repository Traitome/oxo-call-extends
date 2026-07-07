---
name: sure
category: programming
description: Utility belt for automated testing in Python with fluent assertions.
tags: [sure, python-testing, assertions, unit-testing]
author: oxo-call-community
source_url: "http://github.com/gabrielfalcao/sure"
---

## Concepts

- **Tool Overview**: sure (v2.0.1) is a utility library for fluent assertions in Python testing.
- **Core Function**: Provides human-readable assertions for unit testing.
- **Algorithm**: Implements fluent assertion methods for Python objects.
- **Input/Output**: Input: Python objects; Output: Assertion results.
- **Applications**: Unit testing, test-driven development, Python development.
- **Installation**: `conda install -c bioconda sure` or pip install.

## Pitfalls

- **Version Compatibility**: May not work with all Python versions.
- **Learning Curve**: Requires learning fluent assertion syntax.
- **Error Messages**: May have cryptic error messages.
- **Performance**: May be slower than native assertions.
- **Integration**: Requires integration with test frameworks.
- **Documentation**: Limited documentation for advanced features.

## Examples

### Display help
**Args:** `python -c "import sure; help(sure)"`
**Explanation:** Shows available options and usage information.

### Basic assertion
**Args:** `python -c "from sure import expect; expect([1, 2, 3]).to.have.length_of(3)"`
**Explanation:** Use fluent assertions in Python.

### Chain assertions
**Args:** `python -c "from sure import expect; expect('hello').to.contain('ll').and_not.contain('zz')"`
**Explanation:** Chain multiple assertions together.

### Verbose mode
**Args:** `python -c "from sure import expect; expect(actual).to.equal(expected).verbose()"`
**Explanation:** Get verbose assertion output.

### Testing with pytest
**Args:** `pytest test_file.py -v`
**Explanation:** Run tests with pytest and sure assertions.

### Batch testing
**Args:** `python -c "from sure import expect; [expect(x).to.be.true for x in results]"`
**Explanation:** Test multiple values together.

### Filter results
**Args:** `python -c "from sure import expect; expect(list(filter(lambda x: x > 0, values))).to.not_be.empty"`
**Explanation:** Use with filter operations.

### Include type checks
**Args:** `python -c "from sure import expect; expect(result).to.be.a(dict)"`
**Explanation:** Check object type.

### Generate report
**Args:** `pytest test_file.py --html=report.html`
**Explanation:** Generate HTML test report.

---
name: backports.unittest_mock
category: utility
description: backports.unittest_mock - Backport of unittest.mock for Python 2/3 compatibility
tags: [backports.unittest_mock, utility, testing, mock, python2]
author: oxo-call-community
source_url: "https://github.com/jaraco/backports.unittest_mock"
---

## Concepts

- **Tool Overview**: backports.unittest_mock is a backport of Python 3's unittest.mock module for use in Python 2 environments. Version 1.3.
- **Core Function**: Provides Python 3 unittest.mock functionality to Python 2, enabling consistent mocking across Python versions.
- **Mock Objects**: Allows creation of mock objects for testing purposes.
- **Patch Decorators**: Supports patch, patch.object, and patch.dict decorators for replacing objects during tests.
- **MagicMock**: Provides mock objects with all magic methods pre-configured.
- **Python 2/3 Compatibility**: Enables the same testing code to run on both Python 2 and Python 3.
- **Installation**: `conda install -c bioconda backports.unittest_mock` or `pip install backports.unittest_mock`.

## Pitfalls

- **Python 2 Deprecation**: Python 2 is no longer supported. Migrate to Python 3 if possible.
- **Version Compatibility**: Different Python versions may have slightly different mock behavior.
- **Mocking Complex Objects**: Mocking complex objects requires careful setup to avoid unexpected behavior.
- **Side Effects**: Incorrectly configured side effects can lead to confusing test failures.

## Examples

### Basic mock usage
**Args:** `python -c "from backports.unittest_mock import Mock; m = Mock(); m.return_value = 42; print(m())"`
**Explanation:** Creates a basic mock object that returns 42 when called.

### Patch decorator
**Args:** `python -c "from backports.unittest_mock import patch; @patch('__main__.func') def test(mock_func): mock_func.return_value = 'mocked'; print(func())"`
**Explanation:** Uses patch decorator to replace function with mock during test.

### MagicMock usage
**Args:** `python -c "from backports.unittest_mock import MagicMock; m = MagicMock(); m.__iter__.return_value = iter([1, 2, 3]); print(list(m))"`
**Explanation:** Creates MagicMock with magic methods for iteration.

### Mock with side effect
**Args:** `python -c "from backports.unittest_mock import Mock; m = Mock(side_effect=[1, 2, 3]); print(m(), m(), m())"`
**Explanation:** Configures mock to return different values on successive calls.

### Patch object method
**Args:** `python -c "from backports.unittest_mock import patch; class MyClass: def method(self): return 'original'; obj = MyClass(); with patch.object(obj, 'method', return_value='patched'): print(obj.method())"`
**Explanation:** Patches a specific method on an object instance.

### Mock assert calls
**Args:** `python -c "from backports.unittest_mock import Mock; m = Mock(); m('arg1', key='value'); m.assert_called_once_with('arg1', key='value')"`
**Explanation:** Verifies mock was called with specific arguments.

### Patch dictionary
**Args:** `python -c "from backports.unittest_mock import patch; d = {'key': 'original'}; with patch.dict(d, {'key': 'patched'}): print(d['key'])"`
**Explanation:** Temporarily modifies a dictionary during test.
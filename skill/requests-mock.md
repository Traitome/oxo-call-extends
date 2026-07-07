---
name: requests-mock
category: containerization
description: Requests-mock mocks responses from the requests package for testing.
tags: [requests-mock, containerization, testing, python]
author: oxo-call-community
source_url: "https://github.com/jamielennox/requests-mock"
---

## Concepts

- **Tool Overview**: requests-mock mocks HTTP requests.
- **Core Function**: HTTP response mocking.
- **Algorithm**: Uses intercept methods.
- **Input Format**: Accepts URL patterns.
- **Output**: Produces mock responses.
- **Use Case**: Testing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Pattern Complexity**: Affects mocking.
- **Response Data**: Must be prepared.
- **Parameters**: Must be configured.
- **Runtime**: Mocking may have overhead.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import requests_mock; help(requests_mock)"`
**Explanation:** Shows available options and usage instructions.

### Basic mock
**Args:** `with requests_mock.Mocker() as m: m.get('http://example.com', text='data')`
**Explanation:** Mocks HTTP GET request.

### Decorator usage
**Args:** `@requests_mock.Mocker(kw='mock')`
**Explanation:** Uses decorator for mocking.

### Multiple URLs
**Args:** `m.get([url1, url2], text='response')`
**Explanation:** Mocks multiple URLs.

### Status code
**Args:** `m.get(url, status_code=404)`
**Explanation:** Returns custom status code.

### JSON response
**Args:** `m.get(url, json={'key': 'value'})`
**Explanation:** Returns JSON response.

### Real requests
**Args:** `m.get(url, real_http=True)`
**Explanation:** Falls back to real request.
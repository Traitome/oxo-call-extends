---
name: httpretty
category: programming
description: HTTPretty is a Python library for mocking HTTP requests in unit tests, allowing developers to test HTTP clients without real network connections.
tags: [httpretty, programming, testing, HTTP, mock]
author: oxo-call-community
source_url: "http://github.com/gabrielfalcao/httpretty"
---

## Concepts

- **Tool Overview**: HTTPretty is a Python mocking library that intercepts HTTP requests during testing.
- **Request Mocking**: Allows defining expected HTTP responses for specific URLs.
- **Response Customization**: Supports custom status codes, headers, and response bodies.
- **Request Recording**: Records all HTTP requests made during tests for verification.
- **Framework Integration**: Works with popular Python testing frameworks like pytest and unittest.
- **Installation**: `conda install -c bioconda httpretty` or `pip install httpretty`

## Pitfalls

- **Python Version**: Compatibility may vary between Python versions.
- **Async Support**: Limited support for asynchronous HTTP clients.
- **SSL/TLS**: Mocking HTTPS requests may require additional configuration.
- **Request Matching**: URL matching can be tricky with complex query parameters.
- **Cleanup**: Requires proper cleanup between tests to avoid state leakage.
- **Third-Party Libraries**: May not work with all HTTP client libraries.

## Examples

### Basic mock setup
**Args:** `@httpretty.activate`
**Explanation:** Decorator to activate HTTP mocking for a test function.

### Mock a simple GET request
**Args:** `httpretty.register_uri(httpretty.GET, "http://example.com/api", body='{"status": "ok"}')`
**Explanation:** Registers a mock response for GET requests to the specified URL.

### Mock with custom status code
**Args:** `httpretty.register_uri(httpretty.POST, "http://example.com/submit", status=400, body='{"error": "bad request"}')`
**Explanation:** Mocks a POST request returning a 400 status code with error body.

### Verify request was made
**Args:** `assert httpretty.last_request().method == "GET"`
**Explanation:** Verifies the method of the last intercepted HTTP request.

### Mock JSON response
**Args:** `httpretty.register_uri(httpretty.GET, "http://example.com/data", body=json.dumps({"items": [1, 2, 3]}), content_type="application/json")`
**Explanation:** Registers a mock returning JSON data with proper content type.
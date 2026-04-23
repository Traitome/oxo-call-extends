---
name: bleach
category: utility
description: Whitelist-based HTML sanitizing tool for Python
tags: [bleach, html, sanitization, security]
author: oxo-call-community
source_url: "https://github.com/jsocol/bleach"
---

## Concepts

- **Tool Overview**: Bleach is an HTML sanitization library using whitelist-based filtering.
- **Core Function**: Sanitizes HTML input by removing potentially dangerous content.
- **Features**: Tag whitelisting, attribute filtering, and link sanitization.
- **Application**: Web application security and user input sanitization.
- **Installation**: Install via bioconda: `conda install -c bioconda bleach`

## Pitfalls

- **Python Only**: Python library, not a command-line tool.
- **Whitelist Approach**: Only allowed tags/attributes are preserved.
- **XSS Prevention**: Helps prevent cross-site scripting attacks.

## Examples

### Sanitize HTML
**Args:** `python -c "import bleach; print(bleach.clean('<script>alert(1)</script><b>Hello</b>'))"`
**Explanation:** Sanitizes HTML, removing script tags while preserving safe content.

### Allow specific tags
**Args:** `python -c "import bleach; print(bleach.clean('<b>Hello</b><i>World</i>', tags=['b']))"`
**Explanation:** Allows only bold tags, removing italic tags.

### Strip all tags
**Args:** `python -c "import bleach; print(bleach.clean('<b>Hello</b>', tags=[]))"`
**Explanation:** Removes all HTML tags, returning plain text.

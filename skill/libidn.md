---
name: libidn
category: programming
description: Internationalized Domain Name (IDN) library
tags: [libidn, programming, IDN, domain-names, internationalization]
author: oxo-call-community
source_url: "https://www.gnu.org/software/libidn/"
---

## Concepts

- **IDN Support**: Internationalized Domain Name handling
- **Punycode**: Punycode encoding/decoding
- **Unicode**: Unicode domain name support
- **Normalization**: String normalization for IDN
- **Validation**: Domain name validation
- **Encoding**: Conversion between Unicode and ASCII-compatible encoding

## Pitfalls

- **Encoding Issues**: Proper encoding handling required
- **Normalization**: Different normalization forms
- **Compatibility**: Older systems may not support IDN
- **Security**: IDN homograph attacks possible
- **Error Handling**: Requires careful validation
- **Version Compatibility**: API may change between versions

## Examples

### Encode domain
**Args:** `idn encode -i www.测试.com -o encoded.txt`
**Explanation:** Encodes internationalized domain name.

### Decode domain
**Args:** `idn decode -i xn--0zwm56d -o decoded.txt`
**Explanation:** Decodes Punycode to Unicode.

### Validate domain
**Args:** `idn validate -i www.example.com`
**Explanation:** Validates domain name format.

### Convert to ASCII
**Args:** `idn toascii -i www.测试.com`
**Explanation:** Converts Unicode domain to ASCII-compatible encoding.

### Convert to Unicode
**Args:** `idn tounicode -i xn--0zwm56d`
**Explanation:** Converts ASCII-compatible encoding to Unicode.

### Check IDN support
**Args:** `idn check -i www.example.com`
**Explanation:** Checks if domain uses IDN.
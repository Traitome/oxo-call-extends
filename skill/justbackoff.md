---
name: justbackoff
category: programming
description: Simple backoff algorithm implementation in Python.
tags: [justbackoff, programming, backoff, retry, algorithm]
author: oxo-call-community
source_url: "https://github.com/admiralobvious/justbackoff"
---

## Concepts

- **Tool Overview**: justbackoff (v0.4.0) - A simple and flexible backoff algorithm implementation for Python.
- **Exponential Backoff**: Implements exponential backoff for retry logic.
- **Configurable**: Supports configurable backoff parameters.
- **Jitter Support**: Includes jitter to prevent thundering herd.
- **Max Retries**: Supports configurable maximum retry attempts.
- **Decorator Pattern**: Can be used as a decorator for functions.

## Pitfalls

- **Infinite Loops**: Without max retries, can loop indefinitely.
- **Timeout Handling**: Does not handle timeouts automatically.
- **Exception Handling**: Requires proper exception handling.
- **State Management**: Backoff state needs proper management.
- **Concurrency**: Multiple concurrent retries may still cause issues.
- **Performance**: Excessive retries can impact performance.

## Examples

### Create backoff instance
**Args:** `from justbackoff import Backoff; b = Backoff(min_wait=1, max_wait=60)`
**Explanation:** Creates backoff with 1-60 second wait range.

### Use as decorator
**Args:** `@Backoff(max_tries=5)`
**Explanation:** Decorates function with backoff retry logic.

### Manual backoff
**Args:** `b = Backoff(); b.wait()`
**Explanation:** Manually waits with exponential backoff.

### With jitter
**Args:** `b = Backoff(jitter=True)`
**Explanation:** Enables jitter for randomness in wait times.

### Custom backoff function
**Args:** `b = Backoff(backoff_func=lambda n: n * 2)`
**Explanation:** Uses custom backoff function.

### Reset backoff
**Args:** `b = Backoff(); b.reset()`
**Explanation:** Resets backoff state to initial values.
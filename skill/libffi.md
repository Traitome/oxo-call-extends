---
name: libffi
category: programming
description: Portable Foreign Function Interface library for cross-language calls
tags: [libffi, programming, FFI, cross-language, foreign-function]
author: oxo-call-community
source_url: "https://sourceware.org/libffi/"
---

## Concepts

- **Foreign Function Interface**: Enables calling functions across languages
- **Cross-language Calls**: Call C functions from other languages
- **Dynamic Linking**: Load and call shared libraries
- **Function Pointers**: Create and use function pointers
- **ABI Compatibility**: Handles different calling conventions
- **Type Conversion**: Converts types between languages

## Pitfalls

- **Type Safety**: No compile-time type checking
- **Memory Management**: Manual memory handling required
- **Platform Compatibility**: Different platforms have different ABIs
- **Error Handling**: Requires careful error checking
- **Performance Overhead**: FFI calls have performance cost
- **Thread Safety**: Not thread-safe by default

## Examples

### Load library
**Args:** `ffi_load -l libexample.so`
**Explanation:** Loads shared library.

### Call function
**Args:** `ffi_call -f function_name -a arg1,arg2`
**Explanation:** Calls function with arguments.

### Get symbol
**Args:** `ffi_symbol -l libexample.so -s function_name`
**Explanation:** Retrieves function pointer.

### Create closure
**Args:** `ffi_closure -c callback_function`
**Explanation:** Creates callback function.

### Set argument types
**Args:** `ffi_types -i int,float -o int`
**Explanation:** Specifies argument and return types.

### Call with struct
**Args:** `ffi_struct -f function -s struct_def -d data`
**Explanation:** Calls function with struct argument.
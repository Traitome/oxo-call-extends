---
name: aenum
category: programming
description: Advanced Enumerations (compatible with Python's stdlib Enum), NamedTuples, and NamedConstants
tags: [aenum, python, enumeration, enum, namedtuple, constant]
author: oxo-call-community
source_url: "https://github.com/ethanfurman/aenum"
---

## Concepts

- **Tool Overview**: aenum is a Python library providing advanced enumerations, NamedTuples, and NamedConstants that extend Python's standard library `enum` module.
- **Core Function**: Provides enhanced enum functionality including auto-numbering, ordered comparisons, unique values, flags, and class-based NamedTuples.
- **Main Features**: Enum, IntEnum, StrEnum, AutoNumberEnum, OrderedEnum, UniqueEnum, Flag, IntFlag, NamedTuple, NamedConstant.
- **Backward Compatibility**: Fully compatible with Python's standard library Enum, making it easy to upgrade existing code.
- **Installation**: Install via conda: `conda install -c bioconda aenum` or via pip: `pip install aenum`
- **Python Support**: Python 3.6+ with latest features in Python 3.11+

## Pitfalls

- **Version Differences**: aenum includes features later added to Python's stdlib enum (like StrEnum in 3.11). Check which features require which Python version.
- **Import Conflicts**: Avoid importing from both `enum` and `aenum` in the same module to prevent confusion.
- **AutoNumbering**: AutoNumberEnum automatically assigns integer values starting from 1 by default.
- **Flag Combinations**: Flag members can be combined using bitwise operators without losing their Flag membership.

## Examples

### Basic Enum definition
**Args:**
```python
from aenum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)        # Color.RED
print(Color.RED.name)   # 'RED'
print(Color.RED.value)  # 1
```
**Explanation:** Defines a simple enumeration with named constants. Members have both name and value attributes.

### Auto-numbering enumeration
**Args:**
```python
from aenum import AutoNumberEnum

class Direction(AutoNumberEnum):
    NORTH = ()
    EAST = ()
    SOUTH = ()
    WEST = ()

print(Direction.NORTH.value)  # 1
print(Direction.EAST.value)   # 2
```
**Explanation:** Automatically assigns incrementing integer values starting from 1.

### Ordered enumeration
**Args:**
```python
from aenum import OrderedEnum

class Size(OrderedEnum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

print(Size.SMALL < Size.LARGE)  # True
```
**Explanation:** Supports comparison operators (<, <=, >, >=) between members.

### Flag enumeration
**Args:**
```python
from aenum import Flag

class Permissions(Flag):
    READ = 1
    WRITE = 2
    EXECUTE = 4

user_perms = Permissions.READ | Permissions.WRITE
print(Permissions.READ in user_perms)   # True
print(Permissions.EXECUTE in user_perms) # False
```
**Explanation:** Supports bitwise operations for combining multiple flags.

### NamedTuple definition
**Args:**
```python
from aenum import NamedTuple

class Point(NamedTuple):
    x: int
    y: int
    z: int = 0

p = Point(10, 20)
print(p.x, p.y, p.z)  # 10 20 0
```
**Explanation:** Creates class-based NamedTuples with type hints and default values.

### Unique values enforcement
**Args:**
```python
from aenum import UniqueEnum

class Status(UniqueEnum):
    ACTIVE = 1
    INACTIVE = 2
    # PENDING = 1  # Would raise ValueError for duplicate value
```
**Explanation:** Ensures all enum values are unique, raising ValueError on duplicates.

### Creating enum from sequence
**Args:**
```python
from aenum import Enum

Fruit = Enum('Fruit', ['APPLE', 'BANANA', 'CHERRY'])
print(Fruit.APPLE)  # Fruit.APPLE
```
**Explanation:** Functional API for creating enums from sequences or mappings.
# Day 01 – Mutability vs Immutability in Python

## Definition

**Mutable objects** can change their internal data
without changing their memory identity.

**Immutable objects** cannot be changed once created.
Any modification creates a new object.

---

## Common Examples

### Mutable
- list
- dict
- set

### Immutable
- int
- str
- tuple

---

## Mental Model

Python variables do not store values.
They store references to objects.

Changing a mutable object modifies the same object.
Changing an immutable object creates a new object.

---

## Why Immutability Exists
- Predictability
- Thread safety
- Hashing support
- Safe dictionary keys

## Full Medium Article
https://medium.com/@hirdyanshpandeyy/one-day-one-learning-day-1-3344d26e2178


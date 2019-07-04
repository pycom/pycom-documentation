---
title: "gc"
aliases:
    - firmwareapi/micropython/gc.html
    - firmwareapi/micropython/gc.md
    - chapter/firmwareapi/micropython/gc
---

## Methods

#### gc.enable()

Enable automatic garbage collection.

#### gc.disable()

Disable automatic garbage collection. Heap memory can still be allocated, and garbage collection can still be initiated manually using `gc.collect()`.

#### gc.collect()

Run a garbage collection.

#### gc.mem\_alloc()

Return the number of bytes of heap RAM that are allocated.

#### gc.mem\_free()

Return the number of bytes of available heap RAM.


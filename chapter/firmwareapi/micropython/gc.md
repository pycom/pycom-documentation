# gc – Garbage Collector

### Functions

#####<function>gc.enable()</function>

Enable automatic garbage collection.

#####<function>gc.disable()</function>

Disable automatic garbage collection. Heap memory can still be allocated, and garbage collection can still be initiated manually using <function>gc.collect()</function>.

#####<function>gc.collect()</function>

Run a garbage collection.

#####<function>gc.mem_alloc()</function>

Return the number of bytes of heap RAM that are allocated.

#####<function>gc.mem_free()</function>

Return the number of bytes of available heap RAM.

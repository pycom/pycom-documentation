# class micropython – MicroPython Internals Controls

### Functions
#####<function>micropython.alloc_emergency_exception_buf(size)</function>  

Allocate size bytes of RAM for the emergency exception buffer (a good size
is around 100 bytes). The buffer is used to create exceptions in cases when
normal RAM allocation would fail (eg within an interrupt handler) and
therefore give useful traceback information in these situations.

A good way to use this function is to place it at the start of a main script
(e.g. `boot.py` or `main.py`) and then the emergency exception buffer will be
active for all the code following it.

#####<function>micropython.const(expr)</function>  

Used to declare that the expression is a constant so that the compile can
optimise it. The use of this function should be as follows:  

```python  
from micropython import const  

CONST_X = const(123)
CONST_Y = const(2 * CONST_X + 1)
```

Constants declared this way are still accessible as global variables from
outside the module they are declared in.  On the other hand, if a constant
begins with an underscore then it is hidden, it is not available as a global
variable, and does not take up any memory during execution.

This const function is recognised directly by the MicroPython parser and is
provided as part of the `micropython` module mainly so that scripts can be
written which run under both CPython and MicroPython, by following the above
pattern.  

#####<function>micropython.opt_level([level])</function>  

If `level` is given then this function sets the optimisation level for subsequent
compilation of scripts, and returns `None`. Otherwise it returns the current
optimisation level.  

#####<function>micropython.mem_info([verbose])</function>   

Print information about currently used memory. If the `verbose` argument
is given then extra information is printed.

The information that is printed is implementation dependent, but currently
includes the amount of stack and heap used. In verbose mode it prints out
the entire heap indicating which blocks are used and which are free.

#####<function>micropython.qstr_info([verbose])</function>

Print information about currently interned strings. If the `verbose`
argument is given then extra information is printed.  

The information that is printed is implementation dependent, but currently
includes the number of interned strings and the amount of RAM they use.  In
verbose mode it prints out the names of all RAM-interned strings.

#####<function>micropython.stack_use()</function>  

Return an integer representing the current amount of stack that is being
used. The absolute value of this is not particularly useful, rather it
should be used to compute differences in stack usage at different points.

#####<function>micropython.heap_lock()</function>  
#####<function>micropython.heap_unlock()</function>  

Lock or unlock the heap. When locked no memory allocation can occur and a
`MemoryError` will be raised if any heap allocation is attempted.  

These functions can be nested, i.e. `heap_lock()` can be called multiple times
in a row and the lock-depth will increase, and then `heap_unlock()` must be
called the same number of times to make the heap available again.

#####<function>micropython.kbd_intr(chr)</function>  

Set the character that will raise a `KeyboardInterrupt` exception. By
default this is set to 3 during script execution, corresponding to `Ctrl-C`.
Passing `-1` to this function will disable capture of `Ctrl-C`, and passing `3`
will restore it.  

This function can be used to prevent the capturing of `Ctrl-C` on the
incoming stream of characters that is usually used for the REPL, in case
that stream is used for other purposes.

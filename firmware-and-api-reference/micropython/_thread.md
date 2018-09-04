# \_thread

This module provides low-level primitives for working with multiple threads \(also called light-weight processes or tasks\) — multiple threads of control sharing their global data space. For synchronisation, simple locks \(also called mutexes or binary semaphores\) are provided.

When a thread specific error occurs a `RuntimeError` exception is raised.

## Quick Usage Example

```python
import _thread
import time

def th_func(delay, id):
    while True:
        time.sleep(delay)
        print('Running thread %d' % id)

for i in range(2):
    _thread.start_new_thread(th_func, (i + 1, i))
```

## Methods

#### \_thread.start\_new\_thread\(function, args\[, kwargs\]\)

Start a new thread and return its identifier. The thread executes the function with the argument list args \(which must be a tuple\). The optional `kwargs` argument specifies a dictionary of keyword arguments. When the function returns, the thread silently exits. When the function terminates with an unhandled exception, a stack trace is printed and then the thread exits \(but other threads continue to run\).

#### \_thread.exit\(\)

Raise the `SystemExit` exception. When not caught, this will cause the thread to exit silently.

#### \_thread.allocate\_lock\(\)

Return a new lock object. Methods of locks are described below. The lock is initially unlocked.

#### \_thread.get\_ident\(\)

Return the `thread identifier` of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created.

#### \_thread.stack\_size\(\[size\]\)

Return the thread stack size \(in bytes\) used when creating new threads. The optional size argument specifies the stack size to be used for subsequently created threads, and must be `0` \(use platform or configured default\) or a positive integer value of at least `4096` \(4KiB\). 4KiB is currently the minimum supported stack size value to guarantee sufficient stack space for the interpreter itself.

## Objects

#### \_thread.LockType

This is the type of lock objects.

## class Lock

Used for synchronisation between threads

### Methods

Lock objects have the following methods:

#### lock.acquire\(waitflag=1, timeout=-1\)

Without any optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread \(only one thread at a time can acquire a lock — that’s their reason for existence\).

If the integer `waitflag` argument is present, the action depends on its value: if it is zero, the lock is only acquired if it can be acquired immediately without waiting, while if it is nonzero, the lock is acquired unconditionally as above.

If the floating-point timeout argument is present and positive, it specifies the maximum wait time in seconds before returning. A negative timeout argument specifies an unbounded wait. You cannot specify a timeout if `waitflag` is zero.

The return value is `True` if the lock is acquired successfully, `False` if not.

#### lock.release\(\)

Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread.

#### lock.locked\(\)

Return the status of the lock: `True` if it has been acquired by some thread, `False` if not.

In addition to these methods, lock objects can also be used via the with statement, e.g.:

```python
import _thread

a_lock = _thread.allocate_lock()

with a_lock:
    print("a_lock is locked while this executes")
```


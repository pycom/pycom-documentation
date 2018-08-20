# uos

The `uos` module contains functions for filesystem access and `urandom` function.

## Port Specifics

The filesystem has `/` as the root directory and the available physical drives are accessible from here. They are currently:

* `/flash` – the internal flash filesystem
* `/sd` – the SD card \(if it exists\)

## Methods

#### uos.uname\(\)

Return information about the system, firmware release version, and MicroPython interpreter version.

#### uos.chdir\(path\)

Change current directory.

#### uos.getcwd\(\)

Get the current directory.

#### uos.listdir\(\[dir\]\)

With no argument, list the current directory. Otherwise list the given directory.

#### uos.mkdir\(path\)

Create a new directory.

#### uos.remove\(path\)

Remove a file.

#### uos.rmdir\(path\)

Remove a directory.

#### uos.rename\(old\_path, new\_path\)

Rename a file.

#### uos.stat\(path\)

Get the status of a file or directory.

The return value is a tuple with the following 10 values, in order:

* `st_mode`: protection bits.
* `st_ino`: `inode` number. \(not implemented, returns 0\)
* `st_dev`: device. \(not implemented, returns 0\)
* `st_nlink`: number of hard links. \(not implemented, returns 0\)
* `st_uid`: user id of owner. \(not implemented, returns 0\)
* `st_gid`: group id of owner. \(not implemented, returns 0\)
* `st_size`: size of file in bytes.
* `st_atime`: time of most recent access.
* `st_mtime`: time of most recent content modification.
* `st_ctime`: time of most recent metadata change.

#### uos.getfree\(path\)

Returns the free space \(in KiB\) in the drive specified by path.

#### uos.sync\(\)

Sync all filesystems.

#### uos.urandom\(n\)

Return a bytes object with n random bytes.

#### uos.unlink\(path\)

Alias for the `remove()` method.

#### uos.mount\(block\_device, mount\_point, \* , readonly=False\)

Mounts a block device \(like an SD object\) in the specified mount point. Example:

```python
os.mount(sd, '/sd')
uos.unmount(path)
```

Unmounts a previously mounted block device from the given path.

#### uos.mkfs\(block\_device or path\)

Formats the specified path, must be either `/flash` or `/sd`. A block device can also be passed like an SD object before being mounted.

#### uos.dupterm\(stream\_object\)

Duplicate the terminal \(the REPL\) on the passed stream-like object. The given object must at least implement the `read()` and `write()` methods.

## Constants

* `uos.sep`: Separation character used in paths


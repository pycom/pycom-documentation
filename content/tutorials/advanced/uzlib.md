---
title: "Compressed files"
---
The Pycom firmware includes the [`uzlib`](/firmwareapi/micropython/uzlib/) module by default, which supports the decompression of files and streams. Below, two usage examples are highlighted:
* [Decompressing a zlib file](decompressing-a-zlib-file)
* [Decompressing a gzip file](#decompressing-a-gzip-file)

## Decompressing a zlib file
While the micropython firmware does not support the compression of a file, the equivalent Python library does. You can use the following snippet in Python to compress a file:
```python
# run this with python3 on the computer
# then upload test.txt.z to the pycom device (adjust 'Project settings' in Pymakr)
import zlib
import os

s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n'
b = bytes(s, "utf-8")
z = zlib.compress(b)
with open('test.txt.z', 'wb') as f:
    f.write(z)
print('ratio', len(z)/len(s))
```
This will create a file called `test.txt.z` with some content. Paste this file in your project and adjust the Pymakr settings to allow the uploading of this file type (Pymakr Settings --> Global settings --> Upload file types, add `.z` in the list). On your device, you can use the following example to decompress the file and print its contents:
```python
import zlib
import os

# verify that the file has been uploaded
file = 'test.txt.z'
print('dir', os.listdir())
print(file, os.stat(file))

# read contents, decompress and print
with open(file, 'r') as f:
    z = f.read()
b = zlib.decompress(z)
s = b.decode('utf-8')
print('ratio', len(z)/len(s))
print(s)
```

## Decompressing a gzip file
A `gzip` archive (not to be confused with a `zip` or `zlib` file) can be generated using the terminal in Linux or macOS. You can use the following commands to create and gzip a file in the terminal:
```bash
echo "Hello world" > test.txt
gzip test.txt
```
This generates the file `test.txt.gz`. Now, you can copy the file over to your project and allow pymakr to upload the `.gz` file (Pymakr Settings --> Global settings --> Upload file types, add `.gz` in the list). On your device, you can run the following to decompress the file:
```python
import zlib
import os

#verify the presence of the file
file = 'test.txt.gz'
print('dir', os.listdir())
print(file, os.stat(file))

with open('test.txt.gz', 'r') as file:
    data = zlib.DecompIO(file, 31)
    #use data.readline() to read a single line
    print(data.read())
```

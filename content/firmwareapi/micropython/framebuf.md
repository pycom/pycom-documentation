---
title: "Framebuf"
---

Frame buffer manipulation

Quick example:
```python
import framebuf
fbuf = framebuf.FrameBuffer(bytearray(10*100*2), 10, 100, framebuf.RGB565)

fbuf.fill(0)
fbuf.text('Pycom!', 10,10, 0xffff)
fbuf.hline(0, 20, 96, 0xffff)

```

## Constructor

### framebuf.FrameBuffer(buffer, width, height, format [, stride=width])

Constructs a FrameBuffer object with parameters
* `framebuffer`: A bytearray object large enough to contain every pixel
* `width`: The width of the FrameBuffer in pixels
* `height`: The height of the FrameBuffer in pixels
* `format`: The type of pixel used in the Framebuffer and can be one of the following constants:
    * `framebuf.GS2_HMSB`: 2-bt grayscale
    * `framebuf.GS4_HMSB`: 4-bit grayscale
    * `framebuf.GS8`: 8-bit grayscale
    * `framebuf.MONO_HLSB`: monochrome, horizontally mapped, LSB
    * `framebuf.MONO_HMSB`: monochrome, horizontally mapped, MSB
    * `framebuf.MONO_VLSB`: monochrhome, vertically mapped, LSB
    * `framebuf.MVLSB`: Same as `MONO_VLSB`
    * `framebuf.RGB565`: 16-bit RGB color (5 bits red, 6 bits blue, 5 buts green)
* `stride`: The number of pixels between each horizontal line of pixels in the FrameBuffer.


The coordinates in the following methods are defined with `(0, 0)` in the upper left-hand corner, with `x` on the horizontal axis, and `y` on the vertical axis.
The color arguments is a small int that depends the `format` color order. 

### framebuf.FrameBuffer1(buffer, width, height, format)

Provides compatibility with the legacy FrameBuffer class. 

## Methods

### fbuf.fill(c)

Fills the entire FrameBuffer with the specified color

### fbuf.pixel(x, y [, c])

Gets or sets the color at the specified pixel. 

### fbuf.hline(x, y, w, c)

Draws a 1-pixel wide horizontal line starting at `x, y` with width `w` and color `c`

### fbuf.vline(x, y, h, c)

Draws a 1-pixel wide vertical line starting at `x, y` with height `h` and color `c`

### fbuf.line(x1, y1, x2, y2, c)

Draws a 1-pixel wide line starting at `x1, y1` to `x2, y2` with color `c`

### fbuf.rect(x, y, w, y, c)

Draws a 1-pixel rectangle outline with starting corner `x, y`, width `w`, height `h` and color `c`

### fbuf.fill_rect(x, y, w, h, c)

Draws a colored rectangle with starting corner `x, y`, width `w`, height `h` and color `c`

### fbuf.text(s, x, y, [, c = 1])

Write text to the FrameBuffer with characters of 8 by 8 pixels, with `x, y` in the top left hand corner and `c` as the color.
At the moment, it is not possible to change either the font, or its size.

### fbuf.scroll(xstep, ystep)

Shifts the contents of the FrameBuffer by the given step size in x and y. The pixels will **not** roll around to the other side.

### fbuf.blit(fbuf, x, y [, key])

Draw another FrameBuffer on top of the current one at the given coordinates. If a `key` is specified, the passed FrameBuffer will be considered transparent for that color. All pixels of that color will not be drawn. 

## Constants
format: `GS2_HMSB`, `GS4_HMSB`, `GS8`, `MONO_HLSB`, `MONO_HMSB`, `MONO_VLSB`, `MVLSB`, `RGB565`
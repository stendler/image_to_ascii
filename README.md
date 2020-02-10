# Image to ASCII

This program converts images and gifs to ASCII <br>
It can also display them in the terminal

![demo](https://github.com/yattsu/image_to_ascii/blob/master/demo.gif)
![demo2](https://github.com/yattsu/image_to_ascii/blob/master/demo2.gif)
![demo3](https://github.com/yattsu/image_to_ascii/blob/master/demo3.png)

## Prerequisites

Python==3.8.1 <br>
Pillow==7.0.0 <br>
Requests==2.22.0 <br>

## Usage

### ascii.py

It accepts images and gifs. You can specify the path or link (ending in .jpg/.png/.gif ...) <br>
Example: `python ascii.py /path/to/file.png` / `python ascii.py https://site.domain/file.gif` <br>

You can specify the `scale` and `reverse` arguments <br>
`scale {integer}` - scales the source file to the integer specified <br>
Example: `python ascii.py /path/to/file.gif scale 75` <br>
`reverse` - swaps black&white for the given file <br>
Example: `python ascii.py /path/to/file.gif reverse scale 10` <br>

### show.py

Displays the image/gif in the terminal. For gifs, it will infinitely loop through the frames <br>
Example: `python show.py` <br>

You can specify the `s` argument to specify the delay between frames <br>
`s {float}` - delay between frames, default is 0.07 seconds
Example: `python show.py s 0.3` <br>

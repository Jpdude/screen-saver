## About

[![Screen Shot][screen-screenshot]](https://github.com/Jpdude/screen-saver/blob/main/Images/Screenshot%202025-02-09%20093942.png)

[![Screen Shot][screen-screenshot]](https://github.com/Jpdude/screen-saver/blob/main/Images/Screenshot%202025-02-09%20093853.png)
[![Screen Shot][screen-screenshot]](https://github.com/Jpdude/screen-saver/blob/main/Images/Screenshot%202025-02-09%20093638.png)
Just a side project I was working on for personal use. Decided to post it on GitHub because I wanted to , in some way, "Immortalize" it as i have lost a lot of my projects in the past due to corrupt hardrives and unforseen cicumstances.
Plus the fact other people can use and contribute to what ive made is cool too.
It is a cli and GUI application that allows you to programmatically set up timers , stopwatches or just the regular time and options to show a static picture or multiple after certain intervals all in fullscreen(or not ) on your monitors.
It also gives you some Information about the monitors that are connected to your system (your main display included if you are on a pc) and alows you to tweak some settings without physically touching them. Currently porting to java as python isn't as cross platform reliable

## Installation
```sh
git clone https://github.com/Jpdude/screen-saver
```
## Usage
```sh
ScreenSaver.py --display 0 --mode df
```
cli version seems really buggy right now I suggest you try the GUI version. Just move to the directory where it's located and run this code:
```sh
ScreenGui.py
```
## Known Issues
* CLI not fully integrated and really buggy
* Trying to change to change the contrast and/or brightness is sometimes erratic

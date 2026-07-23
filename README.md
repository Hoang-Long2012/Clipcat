# Clipcat

**Clipcat** is a lightweight Windows command-line utility that prints Unicode text from the clipboard to standard output.

It is designed for use in scripts, command pipelines, and automation.

## Features

* Reads Unicode text directly from the Windows clipboard.
* Writes clipboard contents to standard output.
* Suitable for scripting and command-line automation.

## Installation

## From release

Download latest Clipcat version to [latest release page](https://github.com/Hoang-Long2012/Clipcat/release/latest), extract and enjoy.

### From source

```
git clone https://github.com/Hoang-Long2012/Clipcat.git
cd Clipcat
python clipcat.py
```

### Build a standalone executable

```
pip install pyinstaller
pyinstaller --onefile clipcat.py
```

## Usage

```
clipcat [options]
```

### Options

| Option            | Description                           |
| ----------------- | ------------------------------------- |
| `-v`, `--version` | Display the program version and exit. |
| `-h`, `--help`    | Show the help message and exit.       |

## Examples

Print the clipboard:

```
clipcat
```

Redirect clipboard contents to a file:

```
clipcat > notes.txt
```

Pipe clipboard contents to another command:

```
clipcat | findstr "Python"
```

## Exit Codes

| Code | Meaning                                                 |
| ---: | ------------------------------------------------------- |
|  `0` | Clipboard text printed successfully.                    |
|  `1` | Clipboard contains only whitespace or is empty.         |
|  `2` | Failed to access the clipboard or no text is available. |

## Notes

* Only Unicode text (`CF_UNICODETEXT`) is supported.
* Non-text clipboard formats such as images, files, or HTML are ignored.
* This utility is intended for Windows only.

## Why Clipcat?

Windows includes the `clip` command for copying text **to** the clipboard, but it does not provide a simple way to read clipboard contents from the command line.

Clipcat fills that gap by acting like the Unix `cat` command, except its input source is the Windows clipboard.

## License

This project is licensed under the [MIT License.](LICENSE)

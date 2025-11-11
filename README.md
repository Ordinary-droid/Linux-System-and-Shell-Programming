# Filesystem Crawler (CLI)

A simple command-line tool that scans a directory and prints inode, link count, file type, size, timestamps, and symlink targets.

## Features

* Recursively walks a directory (like `find`)
* Shows inode + hard link count
* Distinguishes file / directory / symlink


## Usage

Run on any directory:

```bash
python3 crawler.py /path/to/scan
```


## Hard Links

Hard links are shown as normal files. Detect by:

* Same inode
* `nlink > 1`

## Requirements

* Python 3.7+
* Linux / WSL / macOS


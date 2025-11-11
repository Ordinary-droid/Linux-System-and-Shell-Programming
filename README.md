# Filesystem Crawler (CLI)

A simple command-line tool that scans a directory and prints inode, link count, file type, size, timestamps, and symlink targets.

## Features

* Recursively walks a directory (like `find`)
* Shows inode + hard link count
* Distinguishes file / directory / symlink
* Outputs clean tab-separated rows
* Safe: uses `lstat()` to avoid following symlinks

## Usage

Run on any directory:

```bash
python3 crawler.py /path/to/scan
```

Save to file:

```bash
python3 crawler.py testfs > report.tsv
```

## Example Output

```
inode   nlink   type    size    mtime                 path            target
12885   1       file    12      2025-11-10T14:20:03   testfs/a.txt
12886   2       file    12      2025-11-10T14:20:03   testfs/a_hard
12887   1       symlink 7       2025-11-10T14:22:00   testfs/a_link   ../a.txt
```

## Test Directory Setup

```bash
mkdir -p testfs/dirA testfs/dirB

echo "hello" > testfs/dirA/a.txt
ln testfs/dirA/a.txt testfs/dirB/a_hard
ln -s ../dirA/a.txt testfs/dirB/a_link
```

## Hard Links

Hard links are shown as normal files. Detect by:

* Same inode
* `nlink > 1`

## Requirements

* Python 3.7+
* Linux / WSL / macOS

## License

MIT

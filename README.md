# Filesystem Crawler (CLI)

A simple command‑line tool that scans a directory and prints inode, link count, file type, size, timestamps, and symlink targets.

## Features

* Recursively walks a directory (like `find`)
* Shows inode + hard link count
* Distinguishes file / directory / symlink

Run on any directory:

```bash
python3 crawler.py /path/to/scan
```

Save to file:

```bash
python3 crawler.py testfs > report.tsv
```

## Hard Links

Hard links are shown as normal files. Detect by:

* Same inode
* `nlink > 1`

## Searching the Output
### Search by inode

```bash
python3 crawler.py testfs | grep "12885"
```

### Search by file type

```bash
python3 crawler.py testfs | grep "symlink"
```

### Search by size (e.g., files 1024 bytes)

```bash
python3 crawler.py testfs | awk '$4 == 1024'
```

### Search by path fragment

```bash
python3 crawler.py testfs | grep "dirA"
```

### Combine filters

```bash
python3 crawler.py testfs | grep "file" | awk '$4 > 500'
```


## Requirements

* Python 3.7+
* Linux / WSL / macOS

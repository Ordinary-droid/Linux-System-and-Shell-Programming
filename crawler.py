#!/usr/bin/env python3

import os
import stat
import argparse
from datetime import datetime


def classify(mode):
    if stat.S_ISREG(mode):
        return "file"
    if stat.S_ISDIR(mode):
        return "directory"
    if stat.S_ISLNK(mode):
        return "symlink"
    return "other"


def crawl(base):
    # Print headers once
    print("inode\tnlink\ttype\tsize\tmtime\tpath\ttarget")

    for root, dirs, files in os.walk(base, followlinks=False):
        for name in dirs + files:
            path = os.path.join(root, name)

            try:
                st = os.lstat(path)
            except Exception:
                continue

            ftype = classify(st.st_mode)
            inode = st.st_ino
            nlink = st.st_nlink
            size = st.st_size
            mtime = datetime.fromtimestamp(st.st_mtime).isoformat()

            target = ""
            if ftype == "symlink":
                try:
                    target = os.readlink(path)
                except Exception:
                    target = ""

            print(f"{inode}\t{nlink}\t{ftype}\t{size}\t{mtime}\t{path}\t{target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI filesystem crawler with inode/link info")
    parser.add_argument("path", help="Directory path to scan")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Path does not exist: {args.path}")
        raise SystemExit(1)

    crawl(args.path)

#!/data/data/com.termux/files/usr/bin/bash
find audits -type f ! -name "sha256_manifest.txt" -exec sha256sum {} \; > audits/checksums/sha256_manifest.txt

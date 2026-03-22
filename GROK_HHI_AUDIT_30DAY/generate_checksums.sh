#!/data/data/com.termux/files/usr/bin/bash
set -e
cd "$(dirname "$0")"
find . -type f \( ! -name "checksums.sha256" \) -print0 | sort -z | xargs -0 sha256sum > checksums.sha256
echo "checksums.sha256 generated"

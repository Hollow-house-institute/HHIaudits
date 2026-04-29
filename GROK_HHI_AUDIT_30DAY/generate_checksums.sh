#!/bin/bash
sha256sum $(find . -type f ! -name "*.sha256") > checksums.sha256

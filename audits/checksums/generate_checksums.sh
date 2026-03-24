find . -type f \
  ! -path "./.git/*" \
  ! -name "*CHECKSUMS.sha256" \
  | sed 's|^\./||' \
  | sort \
  | while read -r file; do
    sha256sum "$file"
  done

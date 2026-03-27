#!/usr/bin/env bash
set -euo pipefail

SPEC_FILE="packaging/coova-chilli.spec"
TOPDIR="$HOME/rpmbuild"

if [[ ! -f "$SPEC_FILE" ]]; then
  echo "Spec file not found: $SPEC_FILE" >&2
  exit 1
fi

mkdir -p "$TOPDIR"/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

# Keep rpm macros explicit so the build is reproducible in CI.
cat > "$HOME/.rpmmacros" <<EOF
%_topdir $TOPDIR
EOF

cp "$SPEC_FILE" "$TOPDIR/SPECS/"

echo "Building SRPM and binary RPM from $SPEC_FILE"
rpmbuild -bs "$TOPDIR/SPECS/$(basename "$SPEC_FILE")"
yum-builddep -y "$TOPDIR/SPECS/$(basename "$SPEC_FILE")"
rpmbuild -ba "$TOPDIR/SPECS/$(basename "$SPEC_FILE")"

echo "Build completed. RPMS are under: $TOPDIR/RPMS"
find "$TOPDIR/RPMS" -type f -name "*.rpm" -print
find "$TOPDIR/SRPMS" -type f -name "*.src.rpm" -print

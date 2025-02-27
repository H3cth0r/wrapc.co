# Steps to build and test nixpkg

## Build
```sh
echo '(import <nixpkgs> {}).python3Packages.callPackage ./default.nix {}' > shell.nix
nix-build shell.nix
```

## In case fix hash mismatch
```
nix-build -E 'with import <nixpkgs> {}; callPackage ./default.nix {}'
```

## Test in shell
```
nix-shell -E 'with import <nixpkgs> {}; mkShell { buildInputs = [ (python3.withPackages (ps: [ (ps.callPackage ./default.nix {}) ])) ]; }'
```

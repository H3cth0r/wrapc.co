# Steps to build and test nixpkg

## Get correct hash
```
nix-build -E 'with import <nixpkgs> {}; python3Packages.callPackage ./wrapcco/default.nix {}'
```

## Build
```sh
nix-build -E 'with import <nixpkgs> {}; python3.pkgs.callPackage ./wrapcco/default.nix {}'
```

## Test in shell
```
nix-shell

python
>> import wrapcco
```


## Add package
```
pkgs/development/python-modules/wrapcco/default.nix
```

**Add reference**
```
# pkgs/top-level/python-packages.nik

wrapcco = callPackage ../development/python-modules/wrapcco { };
```

## Build on nixpkgs
```
nix-build -A python3Packages.wrapcco
```

## Commit and PR
```
git checkout -b add-wrapcko
git add .
git commit -m "pythonPackages.wrapcko: init at 0.1.3"
git push origin add-wrapcko
```

Make PR to master

## Format
Create a shell wit this package:
```
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.nixfmt-rfc-style
  ];
}
```
Run this command:
```
nixfmt 'pkgs/development/python-modules/wrapcco/default.nix'
```

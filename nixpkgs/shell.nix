with import <nixpkgs> {};
let
  mywrapcco = python3.pkgs.callPackage ./wrapcco/default.nix {};
in
mkShell {
  packages = [ mywrapcco ];
}

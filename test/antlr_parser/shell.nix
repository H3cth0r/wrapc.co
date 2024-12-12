with import <nixpkgs> {};

let
  python = python311;
  antlr4Python = stdenv.mkDerivation rec {
    pname = "antlr4-python3-runtime";
    version = "4.13.1";
    src = fetchurl {
      url = "https://www.antlr.org/download/antlr-${version}-complete.jar";
      # sha256 = "0g1n7qrqhd5qxkx4c9i01zfk2rkhlvhkf2nj3vszzw7bvwrk9qa5";
      sha256 = "vBOpxXqN19UZaIghHl7eZXy2SjzpaGCGl+T2aCUahIc=";
    };
    nativeBuildInputs = [ makeWrapper ];
    dontUnpack = true;
    installPhase = ''
      mkdir -p $out/bin
      mkdir -p $out/lib

      cp $src $out/lib/antlr-${version}-complete.jar

      makeWrapper ${jre}/bin/java $out/bin/antlr4 \
        --add-flags "-jar $out/lib/antlr-${version}-complete.jar"
    '';
  };
in
mkShell {
  name = "antlr-python-env";
  buildInputs = [
    zlib
    python
    antlr4Python
    openjdk
  ];
  shellHook = ''
    export CLASSPATH="$CLASSPATH:${antlr4Python}/lib/antlr-4.13.1-complete.jar"
    export PYTHONPATH="${python.pkgs.pybindgen}/lib/${python.pkgs.python.libPrefix}/site-packages:${antlr4Python}/${python.sitePackages}"
    export LD_LIBRARY_PATH="${zlib}/lib"
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
          pkgs.stdenv.cc.cc
          zlib
    ]}
  '';
}

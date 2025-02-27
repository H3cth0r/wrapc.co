{ lib
, buildPythonPackage
, fetchPypi
, numpy
, setuptools
}:
buildPythonPackage rec {
  pname = "wrapcco";
  version = "0.1.0";
  format = "setuptools";
  src = fetchPypi {
    inherit pname version;
    sha256 = "sha256-wFyRIsJjW9AJwXJ/85q3U5JwsWOdb05qH7GOz4GNrrM=";
  };
  nativeBuildInputs = [ setuptools ];
  propagatedBuildInputs = [ numpy setuptools ];
  meta = with lib; {
    description = "Supercharge Python with C++ extensions! Automate boilerplate, crush Numpy arrays at native speed, and code what matters—zero wrapper headaches. 🚀";
    homepage = "https://github.com/H3cth0r/wrapc.co";
    license = licenses.mit;
    maintainers = with maintainers; [ h3cth0r ];
  };
}

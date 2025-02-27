# setup.py
from setuptools import setup, find_packages

setup(
    name="wrapcco",
    version="0.1.3",
    author="Hector Miranda",
    author_email="hector.miranda@zentinel.mx",
    description="A Python module to wrap C/C++ code and generate Python extensions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/H3cth0r/wrapc.co",  # Update with your repository URL
    packages=find_packages(include=["wrapcco", "wrapcco.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "Programming Language :: C++",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "setuptools"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "flake8>=6.0", 
        ]
    },
    entry_points={
        "console_scripts": [
            "wrapcco=wrapcco:_main",
        ]
    },
    include_package_data=True,
    package_data={
        "wrapcco.resources": ["*.hpp"],
    },
    zip_safe=False,
)

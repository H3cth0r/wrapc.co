from setuptools import setup, find_packages

setup(
    name="wrapcco",
    version="0.1.0",
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
        "antlr4-python3-runtime>=4.10", 
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "flake8>=6.0", 
        ]
    },
    # entry_points={
    #     "console_scripts": [
    #         "wrapcco=wrapcco.__main__:main",  # CLI entry point, if applicable
    #     ]
    # },
    include_package_data=True,
    package_data={
        "wrapcco.grammars": ["*.g4"],  # Include grammar files
    },
    zip_safe=False,
)

from setuptools import setup, find_packages

setup(
        name="wrapcco",
        version="0.1.0",
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'wrapcco=wrapcco:main',
            ],
        },
        author="h3cth0r",
        author_email="hector.miranda@zentinel.mx",
        description="A tool to generate Python C extensions from C header and source files",
        long_description=open("./README.md").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/H3cth0r/wrapc.co",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independient",
        ],
        python_requires=">=3.6",
)

from wrapcco.tools import Extension

import argparse
import sys
import os
from setuptools import Distribution
from setuptools.command.build_ext import build_ext
from setuptools import Extension as stExtension

from typing import List

__version__ = "0.1.0"
def show_version() -> None: print(f"wrapcco version {__version__}")

def run_build(extensions: List[stExtension]) -> None:
    dist = Distribution({'ext_modules': extensions})
    dist.parse_config_files()
    cmd = build_ext(dist)
    cmd.inplace =  True
    cmd.ensure_finalized()
    cmd.run()

def _main() -> None:
    parser = argparse.ArgumentParser(
            description='Generate Python C extensions from hpp files'
    )
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show program version'
    )
    group.add_argument(
        '--help-examples',
        action='store_true',
        help='Show usage examples'
    )

    # Main arguments
    parser.add_argument('library_file', help='Path to the hpp file', nargs='?')
    parser.add_argument(
            '--module-name', 
            default='outmod',
            help='Name output module', 
    )
    parser.add_argument(
            '--save-script', 
            default='false',
            help='true or false to save extension cpp file', 
    )
    parser.add_argument(
            '--output-path', 
            default='./',
            help='Path where you want to save module', 
    )

    args = parser.parse_args()

    # handle version display
    if args.version:
        show_version()
        return

    # handle examples display
    if args.help_examples:
        print("""
Usage Examples:
--------------
1. Basic usage:
   wrapcco <library>.hpp --module-name <modulename> --save-script <true/false> --output-path "./"
        """)
        return

    # check if required arguments are provided
    if not all([args.library_file]):
        parser.print_help()
        sys.exit(1)

    # validate file extensions
    if not args.library_file.endswith('.hpp'):
        print("Error: Header file must have .hpp extension")
        sys.exit(1)

    # validate save script is boolean
    if args.save_script not in ("true", "false"):
        print(f"Error: --save-script should be either true/false")
        sys.exit(1)
    
    # validate file existence
    if not os.path.exists(args.library_file):
        print(f"Error: Header file '{args.library_file}' not found")
        sys.exit(1)
    if not os.path.exists(args.output_path):
        print(f"Error: Source file '{args.output_path}' not found")
        sys.exit(1)

    os.makedirs(args.output_path, exist_ok=True)

    try:
        extension = Extension(
                module_name=args.module_name,
                filepaths=args.library_file,
                save=True if args.save_script == "true" else False,
                output_path=args.output_path,
                extra_compile_args=['-std=c++17'],
        )
        extension.build()
        st_extension = extension.extension
        if not st_extension: raise RuntimeError("Failed to create setuptools Extension.")
        run_build([st_extension])
        
        print(f"Successfully generated extension: {args.output_path}{args.module_name}.cpp")
        
    except Exception as e:
        print(f"Error generating extension: {str(e)}")
        sys.exit(1)

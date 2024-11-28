from .wrapper import Wrapper
from typing import List
import sys
import os
import argparse

__version__ = "0.1.0"
def show_version(): print(f"wrapcco version {__version__}")

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Generate Python C extensions from C header and source files'
    )
    
    # create a group for commands that are mutually exclusive
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

    # main arguments
    parser.add_argument('header_file', help='Path to the header file (.h)', nargs='?')
    parser.add_argument('source_file', help='Path to the source file (.c)', nargs='?')
    parser.add_argument('output_name', help='Name for the output extension', nargs='?')
    parser.add_argument(
        '--methods',
        nargs='+',
        help='List of methods to include (default: all)',
        default=[]
    )
    parser.add_argument(
        '--output-path',
        default='./',
        help='Output directory path (default: current directory)'
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
   wrapcco header.h source.c output_name

2. Specify methods to include:
   wrapcco header.h source.c output_name --methods function1 function2 function3

3. Specify output path:
   wrapcco header.h source.c output_name --output-path ./build/

4. Combine methods and output path:
   wrapcco header.h source.c output_name --methods add multiply --output-path ./build/

5. Show version:
   wrapcco --version

6. Show this help:
   wrapcco --help-examples
        """)
        return

    # check if required arguments are provided
    if not all([args.header_file, args.source_file, args.output_name]):
        parser.print_help()
        sys.exit(1)

    # validate file extensions
    if not args.header_file.endswith('.h'):
        print("Error: Header file must have .h extension")
        sys.exit(1)
    if not args.source_file.endswith('.c'):
        print("Error: Source file must have .c extension")
        sys.exit(1)

    # validate file existence
    if not os.path.exists(args.header_file):
        print(f"Error: Header file '{args.header_file}' not found")
        sys.exit(1)
    if not os.path.exists(args.source_file):
        print(f"Error: Source file '{args.source_file}' not found")
        sys.exit(1)

    os.makedirs(args.output_path, exist_ok=True)

    try:
        wrapper = Wrapper(
            header_file=args.header_file,
            source_file=args.source_file,
            methods_to_include=args.methods,
            output_name=args.output_name,
            output_path=args.output_path
        )
        
        wrapper.parse_header()
        wrapper.generate_c_extention_functions()
        wrapper.generate_c_extension()
        wrapper.save_extension_file()
        
        print(f"Successfully generated extension: {args.output_path}{args.output_name}.c")
        
    except Exception as e:
        print(f"Error generating extension: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()

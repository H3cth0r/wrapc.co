from wrapcco.wrapper import CExtensionGenerator

methods_to_include = [
    # "print_buffer_size",
    # "is_code_block_delimeter",
    # "get_language_spec",
    # "process_code_block",
    # "base64_encode",
    # "file_to_base64",
    # "process_image_block",
    # "process_inline_formatting",
    # "parse_markdown_line",
    "process_markdown_file"
]

base_path = "/home/h3cth0r/Documents/notes.co/notesco/c_src/"

ceg = CExtensionGenerator(
    header_file=base_path + "markdown_to_html.h",
    source_file=base_path + "markdown_to_html.c",
    methods_to_include=methods_to_include,
    output_name="my_markdown_extension",
    output_path=base_path
)
ceg.parse_header()
ceg.generate_c_extention_functions()
ceg.generate_c_extension()
ceg.save_extension_file()

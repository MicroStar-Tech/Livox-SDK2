import glob
import sys

from os import system
from pathlib import Path


def get_filepaths():
    all_filepaths = glob.glob("**/*.hpp", recursive=True)
    all_filepaths += glob.glob("**/*.cpp", recursive=True)
    all_filepaths += glob.glob("**/*.tcc", recursive=True)
    all_filepaths += glob.glob("**/*.h", recursive=True)

    filtered_filepaths = []
    for filepath in all_filepaths:
        if not filepath.startswith("submodule") and not filepath.startswith("lib") and not filepath.startswith("build"):
            filtered_filepaths.append(filepath)
    return filtered_filepaths

# usage : python3 clang_formatter.py <my_local_clang_format>
# replace <my_local_clang_format> with the local clang format
# alias on your system path. For example, if you have clang-format-12
# on the system then the usage is,
# eg : python3 clang_formatter.py clang-format-12


def main():
    formatter = "clang-format"
    if len(sys.argv) == 2:
        formatter = sys.argv[1]
    cwd = Path()    # current working directory
    format_filepaths = get_filepaths()
    command = formatter + " --sort-includes --style=file -i "
    for format_filepath in format_filepaths:
        command += str(format_filepath) + ' '
    print(command)
    system(command)  # execute command in terminal


if __name__ == '__main__':
    main()

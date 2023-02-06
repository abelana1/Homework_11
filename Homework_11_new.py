import argparse

def read_file(input_file):
    """We open and read the file. Then we get as a result the content as a list."""

    with open(input_file, encoding='utf-8', mode='r') as file:
        content = file.readlines()
        return content

def capitalize_string(list_of_strings):
    return [string.upper() for string in list_of_strings ]


def write_file(input_list, file_name):
    with open(file_name, encoding='utf-8', mode='w') as file:
        file.writelines(input_list)
       

parser = argparse.ArgumentParser(description='argparse greeting')
parser.add_argument('input_file', default=None, help=("Input file to read"))
parser.add_argument('output_file', default=None, help=("Output file to write"))
parser.add_argument('capitalize', default=None, help=("Shall it capitalize or not?"), nargs='?')
args = parser.parse_args()
if args.capitalize is not None : #is not None is not compulsory
    write_file(capitalize_string(read_file(args.input_file)), args.output_file)
else :
    write_file(read_file(args.input_file), args.output_file)


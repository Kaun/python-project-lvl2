import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
args_cmd = parser.parse_args()

print(args_cmd.first_file)
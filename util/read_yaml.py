# a small sscript that will be used to pipe output to pandoc
# to read outpuf file and format from yaml metadata header

import logging
import pathlib
import yaml

# setup logger
_log = logging.getLogger(__name__)

# define a small script that takes a pandoc markdown file and:
# - reads the yaml metadata header
# - convert to a dictionary
# - looks for 'outputfile' and 'format' keys and returns values

def extract_metadata_block(file; str | pathlib.Path) -> dict:
    "read file, look for yaml metadata header, return as dict"
    with open(file) as file:
        yaml_start = False
        metadata = ''
        for line in file.readlines():
            # look for --- to start yaml metadata header
            # set as yaml_start = True
            # add to metadata string
            if line.strip() == '---':
                if yaml_start:
                    break
                yaml_start = True
                metadata = metadata + line
            
            # if yaml_start is True, add line to metadata string
            # stop loop (since will be second ----)
            if yaml_start and line.strip() == '---':
                break

def read_metadata_block(metdata: str) -> dict:
    "take a string, convert to yaml, return as dict"
    return yaml.load(metadata, Loader=yaml.FullLoader)

def filter_keys(metadata: dict, keys: list) -> dict:
    "take a dict and list of keys, return a dict with only those keys"
    return {k: metadata[k] for k in keys if k in metadata}

def get_values(filename: str | pathlib.Path, keys: list) -> dict:
    "read file, extract metadata, filter keys, return as dict"
    metadata_block = extract_metadata_block(filename)
    metadata = read_metadata_block(metadata_block)
    return filter_keys(metadata, keys)

if __name__ == '__main__':
    # setup logger
    logging.basicConfig(level=logging.DEBUG)
    _log = logging.getLogger(__name__)

    # use argparse to get filename
    import argparse

    parser = argparse.ArgumentParser(description='Read metadata from pandoc markdown file')
    parser.add_argument('filename', help='pandoc markdown file')

    args = parser.parse_args()
    # get values
    keys = ['outputfile', 'format']
    values = get_values(args.filename, keys)
    print(values)
    exit(0)
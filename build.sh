#!/usr/bin/env bash

set +x

# declare a map of input files and a array of output file name and format
declare -A output_files=(
    ["sample.md"]="sample_output.md"
)

declare -A formats=(
    ["sample.md"]="gfm"
)

# create a list of files in ./src directory
files=$(ls ./src)

# loop through list of files, file filename matches a string,
# run pandoc in form of:
# pandoc -s <filename> -o <string_match_filename>
# else run pandoc in form of:
# pandoc -s <filename> -o <filename>
for file in $files
do
    # check if file is in the map
    if [[ -n ${output_files[$file]} ]]; then
        # run pandoc with output file name and format
        pandoc -s -t ${formats[$file]} src/$file -o output/${output_files[$file]}
    else
        # run pandoc with output file name and format
        pandoc -s -t gfm src/$file -o output/$file
    fi
done
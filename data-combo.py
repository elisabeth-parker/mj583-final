import glob
import json

# thanks to stackexchange user Jonas Kölker for an original version of this code, which I edited for python 3

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        first = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if first:
                    outfile.write('[')
                    first = False
                else:
                    outfile.write(',')
                outfile.write(infile.read())
        outfile.write(']')

cat_json('merged_theaters.json', ['formatted-ch.json', 'formatted-durham.json', 'formatted-raleigh.json'])

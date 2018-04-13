import json

# def clean_json(output_filename, input_filename):
#     with open(output_filename, "w") as outfile:
#         with open(input_filename) as infile:
#             data = json.load(infile)
#             for o in data:
#                 del o["address2"]
#
#             outfile.write(theaters)

def clean_json(output_filename, input_filename):
    with open(output_filename, "w") as outfile:
        with open(input_filename) as infile:
            data = json.load(infile)
            new_data = []
            for o in data:
                

            outfile.write(theaters)

clean_json('merged00.json', 'merged_theaters.json')

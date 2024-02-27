import os
import json
import csv

# Directory containing JSON files
json_directory = '.'
json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]

# Data structures to hold the results
types_slices = {}
all_slices = {}

def find_slices(data, json_file):
    if isinstance(data, dict):
        if data.get("type") == "Slices":
            process_slices(data, json_file)
        for value in data.values():
            find_slices(value, json_file)
    elif isinstance(data, list):
        for item in data:
            find_slices(item, json_file)

def process_slices(slices_obj, json_file):
    choices = slices_obj.get("config", {}).get("choices", {})
    for slice_id in choices.keys():
        # Update the type's slices list
        type_name = json_file.replace('.json', '')
        if type_name in types_slices:
            types_slices[type_name].add(slice_id)
        else:
            types_slices[type_name] = {slice_id}

        # Update the slice's types list
        if slice_id in all_slices:
            all_slices[slice_id].add(type_name)
        else:
            all_slices[slice_id] = {type_name}

# Process each JSON file
for json_file in json_files:
    file_path = os.path.join(json_directory, json_file)
    with open(file_path, 'r') as file:
        data = json.load(file)
        find_slices(data, json_file)

# Write Types CSV
with open('types.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Type', 'Slices'])
    for type_name, slices in types_slices.items():
        writer.writerow([type_name, ', '.join(sorted(slices))])  # Sort slices for consistent ordering

# Write Slices CSV
with open('slices.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Slice ID', 'Types'])
    for slice_id, types in all_slices.items():
        writer.writerow([slice_id, ', '.join(sorted(types))])  # Sort types for consistent ordering

print("CSV files generated successfully.")

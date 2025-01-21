import json

# Load JSON data
with open('output_updated.json', 'r') as json_file:
    data = json.load(json_file)

# Default value for customuser_id
default_customuser_id = 1  # Change this to the appropriate default value

# Update JSON data to include customuser_id if it's missing
for table_name, rows in data.items():
    if table_name == 'auto_parts_cart':
        for row in rows:
            if 'customuser_id' not in row:
                row['customuser_id'] = default_customuser_id

# Save the updated JSON data
with open('output_updated.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file has been updated.")

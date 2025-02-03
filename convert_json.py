# Convert data.json from UTF-16 to UTF-8
input_file = 'data.json'  # Your source file
output_file = 'data_utf8.json'  # Your target file

# Read the original file in UTF-16 and write it out in UTF-8
with open(input_file, 'r', encoding='utf-16') as f:
    content = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Converted '{input_file}' to '{output_file}' in UTF-8 format.")
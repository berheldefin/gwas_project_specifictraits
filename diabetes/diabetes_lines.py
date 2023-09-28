# Specify the input and output file paths
input_file_path = "gwas_catalog_v1.0-associations_e110_r2023-09-10.tsv" 
output_file_path = "diabetes_lines.tsv"  # Choose a name for the output TSV file

# Open the input file for reading and the output file for writing
with open(input_file_path, "r", encoding="utf-8") as input_file, \
     open(output_file_path, "w", encoding="utf-8") as output_file:
    # Read the first line (header) from the input file
    header = input_file.readline()
    # Write the header to the output file
    output_file.write(header)

    # Read each line in the input file
    for line in input_file:
        # If the line contains "diabet"(case-insensitive)
        if "diabetes" in line.lower():
            output_file.write(line)

# Inform the user that the operation is complete
print("Lines containing 'diabetes' (case-insensitive) have been saved to", output_file_path)

#içinde bir sürü no diabetes araştırmaları var bunları çıkarmak için:
# Specify the input file path
input_file_path = "diabetes_lines.tsv"

# Open the input file for reading and store the lines without "no diabetes" in a list
filtered_lines = []
with open(input_file_path, "r", encoding="utf-8") as input_file:
    for line in input_file:
        # If the line does not contain "no diabetes" (case-insensitive)
        if "no diabetes" not in line.lower():
            filtered_lines.append(line)

# Open the input file again for writing (overwrite mode) and write the filtered lines back
with open(input_file_path, "w", encoding="utf-8") as input_file:
    input_file.writelines(filtered_lines)

# Inform the user that the operation is complete
print("Lines containing 'no diabetes' (case-insensitive) have been removed from the file.")





# daha sonrasında diabetes journalında yayınlanmış ama direkt diabet araştırması olmayanları çıkarmam gerekebilir. journal sütunu diabetes olduğu yerde study ya da disease/trait sütununda diabetes yoksa silersin.


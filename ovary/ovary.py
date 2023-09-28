# Specify the input and output file paths, ovarian, ovary, ovarium kısaca ovar ile belki aratabilirim.
input_file_path = "gwas_catalog_v1.0-associations_e110_r2023-09-10.tsv"
output_file_path = "ovary.tsv"  # Choose a name for the output TSV file

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
        if "ovary" in line.lower() or "ovarian" in line.lower():
            output_file.write(line)

# Inform the user that the operation is complete
print("Lines containing 'ovary' (case-insensitive) have been saved to", output_file_path)

# First, extract rows that contains colon cancer yazanlarda colorectal yazmıyor or colorectal yazanlarda da colon yazmıyor hiç o yüzden veya ararabilirim
# Specify the input and output file paths
input_file_path = "gwas_catalog_v1.0-associations_e110_r2023-09-10.tsv"
output_file_path = "colorectal_cancer_lines.tsv"  # Choose a name for the output TSV file

# Open the input file for reading and the output file for writing
with open(input_file_path, "r", encoding="utf-8") as input_file, \
     open(output_file_path, "w", encoding="utf-8") as output_file:
     # Read the first line (header) from the input file
    header = input_file.readline()
    # Write the header to the output file
    output_file.write(header)

    # Read each line in the input file
    for line in input_file:
        # If the line contains "colon cancer" or "colorectal" (case-insensitive)
        if "colon cancer" in line.lower() or "colorectal" in line.lower() or "carcinoembryonic" in line.lower() or "fetoprotein" in line.lower() or "cytokeratin" in line.lower() or "cancer antigen" in line.lower():
            # Write this line to the output file
            output_file.write(line)

# Inform the user that the operation is complete
print("Lines containing 'colon cancer' or 'colorectal' (case-insensitive) have been saved to", output_file_path)

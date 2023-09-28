# First, extract rows that contains prostate, Specify the input and output file paths
input_file_path = "gwas_catalog_v1.0-associations_e110_r2023-09-10.tsv"
output_file_path = "prostate_lines.tsv"  # Choose a name for the output TSV file

# Open the input file for reading and the output file for writing
with open(input_file_path, "r", encoding="utf-8") as input_file, \
     open(output_file_path, "w", encoding="utf-8") as output_file:
    # Read the first line (header) from the input file
    header = input_file.readline()
    # Write the header to the output file
    output_file.write(header)

    # Read each line in the input file
    for line in input_file:
        # If the line contains the word "prostate" (case-insensitive)
        if "prostate" in line.lower():
            # Write this line to the output file
            output_file.write(line)

# Inform the user that the operation is complete
print("Lines containing 'prostate' (case-insensitive) have been saved to", output_file_path)

# eliminate the ones not related with prostate cancer
import pandas as pd

# Specify the file name and path
file_path = "prostate_lines.tsv"

# Load the TSV file into a DataFrame
df = pd.read_csv(file_path, sep='\t', encoding='utf-8')

# Select rows where "prostate cancer" appears in the 7th, 8th, or 9th column
prostate_cancer_rows = df[df.iloc[:, 6:9].apply(lambda row: 'prostate cancer' in ' '.join(row), axis=1)]

# Save the results to another TSV file if desired
prostate_cancer_rows.to_csv("prostate_cancer_lines.tsv", sep='\t', index=False, encoding='utf-8')

# Display a message indicating the completion of the operation
print("Rows containing 'prostate cancer' in the 7th, 8th, or 9th column have been saved to 'prostate_cancer_lines.tsv'.")

import pandas as pd

# Specify the file name and path
file_path = "ovary.tsv"

# Load the TSV file into a DataFrame
df = pd.read_csv(file_path, sep='\t', encoding='utf-8')

# Select rows where "cancer" or "carcinoma" appears in the 7th, 8th, or 9th column
ovarian_cancer_rows = df[df.iloc[:, 6:9].apply(lambda row: any(keyword in ' '.join(row).lower() for keyword in ['cancer', 'carcinoma']), axis=1)]

# Save the results to another TSV file if desired
ovarian_cancer_rows.to_csv("ovarian_cancerlines.tsv", sep='\t', index=False, encoding='utf-8')

# Display a message indicating the completion of the operation
print("'ovarian_cancerlines.tsv' is created.")

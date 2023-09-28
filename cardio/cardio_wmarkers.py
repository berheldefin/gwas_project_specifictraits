import pandas as pd

# Verileri oku
df = pd.read_csv('cardio.tsv', sep='\t')

# 'DISEASE/TRAIT' sütununu kontrol et ve içinde marker olanları seç, şimdilik klinik kimya kısmına baktım, geri kalanlara sonra bakacağım.
filtered_df = df[df['DISEASE/TRAIT'].str.contains('blood cell|antigen|cytokeratin|fetoprotein|carbohydrate|carcinoembryonic|cancer antigen|erythroid|sodium|magnesium|potassium|calcium|chloride|amylase|lipase|creatine kinase|glucose|urea|creatinine|uric acid|protein|albumin|bilirubin|triglyceride|cholesterol|alanine aminotransferase|aspartate aminotransferase|gamma-glutamyl transferase|HbA1c|insulin|erythroid|hemoglobin|hematocrit|platelet|blood cell|energy|lymphocyte|leukocyte|neutrophil|monocyte|eosinophile|basophil|thrombocyte', case=False, regex=True)]

# Sonuçları diabetes_lines_wmarkers.tsv dosyasına kaydet
filtered_df.to_csv('cardio_wmarkers.tsv', sep='\t', index=False)

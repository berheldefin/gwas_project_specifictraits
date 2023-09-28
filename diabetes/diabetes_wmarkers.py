import pandas as pd

# Verileri oku
df = pd.read_csv('diabetes_lines.tsv', sep='\t')

# 'DISEASE/TRAIT' sütununu kontrol et ve içinde marker olanları seç, şimdilik klinik kimya kısmına baktım, geri kalanlara sonra bakacağım.
filtered_df = df[df['DISEASE/TRAIT'].str.contains('glucose|urea|creatinine|uric acid|protein|albumin|bilirubin|triglyceride|cholesterol|alanine aminotransferase|aspartate aminotransferase|gamma-glutamyl transferase|HbA1c|insulin|erythroid|hemoglobin|hematocrit|platelet|blood cell|energy|lymphocyte|leukocyte|neutrophil|monocyte|eosinophile|basophil|thrombocyte', case=False, regex=True)]

# Sonuçları diabetes_lines_wmarkers.tsv dosyasına kaydet
filtered_df.to_csv('diabetes_lines_wmarkers.tsv', sep='\t', index=False)

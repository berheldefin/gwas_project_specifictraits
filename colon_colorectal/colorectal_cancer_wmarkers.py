import pandas as pd

# Verileri oku
df = pd.read_csv('colorectal_cancer_lines.tsv', sep='\t')

# 'DISEASE/TRAIT' ve 'STUDY' sütunlarını kontrol et ve içinde marker olanları seç
filtered_df = df[df['DISEASE/TRAIT'].str.contains('protein|calcium|hematocrit|platelet|blood cell|antigen|cytokeratin|fetoprotein|carbohydrate|carcinoembryonic|cancer antigen|erythroid|hemoglobin|hematocrit|platelet|blood cell|energy|lymphocyte|leukocyte|neutrophil|monocyte|eosinophile|basophil|thrombocyte', case=False, regex=True) | df['STUDY'].str.contains('protein|calcium|hematocrit|platelet|blood cell|antigen|cytokeratin|fetoprotein|carbohydrate|carcinoembryonic|cancer antigen|erythroid|hemoglobin|hematocrit|platelet|blood cell|energy|lymphocyte|leukocyte|neutrophil|monocyte|eosinophile|basophil|thrombocyte|CA 125|CA 19|CA 15', case=False, regex=True)]

# Sonuçları colorectal_cancer_wmarkers.tsv dosyasına kaydet
filtered_df.to_csv('colorectal_cancer_wmarkers.tsv', sep='\t', index=False)


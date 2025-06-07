import pandas as pd

# Contoh data frame dengan beberapa nilai hilang
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, None, None, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [None, 2, None, 4, None]
}

df = pd.DataFrame(data)

# Menampilkan data frame awal
print("Data frame awal:")
print(df)

# Menghitung persentase nilai hilang per kolom
missing_percentage = df.isnull().mean()

# Menghapus kolom yang memiliki lebih dari 50% nilai hilang
threshold = 0.5
columns_to_drop = missing_percentage[missing_percentage > threshold].index
df_cleaned = df.drop(columns=columns_to_drop)

# Menampilkan data frame setelah penghapusan kolom
print("\nData frame setelah menghapus kolom dengan >50% nilai hilang:")
print(df_cleaned)

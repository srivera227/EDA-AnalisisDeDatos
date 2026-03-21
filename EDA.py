import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import kagglehub
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt

#Carga del dataset
df = pd.read_csv('datos.csv')
# ==========================================
# 1. INFORMACIÓN DEL DATASET
# ==========================================
print("=" * 60)
print(" " * 18 + "INFORMACIÓN DEL DATASET")
print("=" * 60)
df.info() # No need to use print() because df.info() automatically prints to console
print("\n")

# ==========================================
# 2. DESCRIPCIÓN ESTADISTICA
# ==========================================
print("=" * 60)
print(" " * 18 + "DESCRIPCIÓN ESTADISTICA")
print("=" * 60)
display(df.describe())
print("\n")

# ==========================================
# 3. VALORES NULOS
# ==========================================
print("=" * 60)
print(" " * 22 + "VALORES NULOS")
print("=" * 60)
print(df.isnull().sum())
print("\n")

# ==========================================
# 4. FILAS DUPLICADAS
# ==========================================
print("=" * 60)
print(" " * 22 + "FILAS DUPLICADAS")
print("=" * 60)
print(f"Total duplicated rows found: {df.duplicated().sum()}")
print("\n")
# ==========================================
# 5. TRATAMIENTO DE LOS VALORES NULOS
# ==========================================
#Eliminar valores nulos
df = df.dropna()
print(df.isnull().sum())


# ==========================================
# 5. DETECCIÓN DE VALORES ATÍPICOS (BOXPLOT)
# ==========================================
sns.boxplot(x=df["salary"])
plt.title("Boxplot de salario")
plt.show()


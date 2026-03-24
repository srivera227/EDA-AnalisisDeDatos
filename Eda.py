import matplotlib
matplotlib.use("TkAgg")

from Imputaciones import imputacionMediana
from Exploracion import exploracion
import pandas as pd
import kagglehub
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# ==========================================
# EXPLORACIÓN DEL DATASET
# ==========================================
df = exploracion()

# ==========================================
# TRATAMIENTO DE LOS VALORES NULOS
# ==========================================
print("=" * 60)
print(" " * 22 + "TRATAMIENTO, IMPUTACIÓN Y ELIMINACIÓN")
print("=" * 60)
df_procesado = imputacionMediana(df,"job_title", "salary")
# ==========================================
# VALIDACIÓN TRATAMIENTO DE LOS VALORES NULOS
# ==========================================
print("=" * 60)
print(" " * 22 + "VALIDACIÓN TRATAMIENTO DE LOS VALORES NULOS")
print("=" * 60)
print(df_procesado.isnull().sum())
# ==========================================
# DETECCIÓN DE VALORES ATÍPICOS (BOXPLOT)
# ==========================================
print("=" * 60)
print(" " * 22 + "DETECCIÓN DE VALORES ATÍPICOS (BOXPLOT)")
print("=" * 60)
sns.boxplot(x=df_procesado["salary"])
plt.title("Boxplot de salario")
plt.show()
#ALE LO PEGAS ACA


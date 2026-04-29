import matplotlib
matplotlib.use("TkAgg")

from Entrega2.Imputaciones import imputacionMediana
from Entrega2.Exploracion import exploracion
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

Q1 = df_procesado["salary"].quantile(0.25)
Q3 = df_procesado["salary"].quantile(0.75)
IQR = Q3 - Q1
limite_superior = Q3 + 1.5 * IQR
limite_inferior = Q1 - 1.5 * IQR
outliersSuperiores = df_procesado[df_procesado["salary"] > limite_superior]
outliersInferiores = df_procesado[df_procesado["salary"] < limite_inferior]
print("=" * 60)
print(" " * 22 + "OUTLIERS BOXPLOT")
print("=" * 60)
print(" " * 22 + "OUTLIERS INFERIORES")
print(outliersInferiores)
print(" " * 22 + "OUTLIERS SUPERIORES")
print(outliersSuperiores)
# ==========================================
# DETECCIÓN DE VALORES ATÍPICOS (Z-SCRORE)
# ==========================================

df_procesado["z_score_salary"] = zscore(df_procesado["salary"])
outliers_z = df_procesado[
    (df_procesado["z_score_salary"] > 3) |
    (df_procesado["z_score_salary"] < -3)
]

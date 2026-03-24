import matplotlib
matplotlib.use("TkAgg")

from Imputaciones import imputacionMediana
import pandas as pd
import kagglehub
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# CARGA  DEL DATASET
# ==========================================
df = pd.read_csv('datos.csv')

# ==========================================
# INFORMACIÓN DEL DATASET
# ==========================================

def exploracion():

    print("=" * 60)
    print(" " * 18 + "INFORMACIÓN DEL DATASET")
    print("=" * 60)
    df.info() # No need to use print() because df.info() automatically prints to console
    print("\n")
    # ==========================================
    # DESCRIPCIÓN ESTADISTICA
    # ==========================================
    print("=" * 60)
    print(" " * 18 + "DESCRIPCIÓN ESTADISTICA")
    print("=" * 60)
    display(df.describe())
    print("\n")
    # ==========================================
    # INDICADORES - VALORES NULOS
    # ==========================================
    print("=" * 60)
    print(" " * 22 + "VALORES NULOS")
    print("=" * 60)
    print(df.isnull().sum())
    print("\n")
    # ==========================================
    # FILAS DUPLICADAS
    # ==========================================
    print("=" * 60)
    print(" " * 22 + "FILAS DUPLICADAS")
    print("=" * 60)
    print(f"Total filas duplicadas: {df.duplicated().sum()}")
    print("\n")
    return df 
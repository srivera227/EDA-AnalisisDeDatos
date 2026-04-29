import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10,6)

# =========================
# 1. CARGA DE DATOS
# =========================
df = pd.read_csv("StudentsPerformance.csv")

# Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("=== DATASET ORIGINAL ===")
print("Shape:", df.shape)
print(df.info())
print(df.describe())

# =========================
# 2. VALIDACIÓN DE CALIDAD
# =========================
print("\n=== VALIDACIÓN ===")

# Nulos
print("\nValores nulos:")
print(df.isnull().sum())

# Duplicados
print("\nDuplicados:", df.duplicated().sum())

# Tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# =========================
# 3. LIMPIEZA DE DATOS
# =========================
print("\n=== LIMPIEZA ===")

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar nulos (por seguridad)
df = df.dropna()

# Validar rangos (scores deben estar entre 0 y 100)
df = df[
    (df['math_score'].between(0,100)) &
    (df['reading_score'].between(0,100)) &
    (df['writing_score'].between(0,100))
]

print("Shape después de limpieza:", df.shape)

# =========================
# 4. FEATURE ENGINEERING
# =========================
df['average_score'] = df[['math_score','reading_score','writing_score']].mean(axis=1)

df['performance'] = pd.cut(
    df['average_score'],
    bins=[0, 60, 75, 100],
    labels=['Low', 'Medium', 'High']
)

# =========================
# 5. EDA (RESUMIDO)
# =========================

scores = ['math_score', 'reading_score', 'writing_score']

# Distribución
df[scores].hist(bins=20)
plt.suptitle("Distribución de puntajes")
plt.show()

# Correlación
corr = df[scores].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlación entre variables")
plt.show()

# Boxplot curso preparación
sns.boxplot(data=df, x='test_preparation_course', y='average_score')
plt.title("Impacto del curso de preparación")
plt.show()

# Boxplot lunch
sns.boxplot(data=df, x='lunch', y='average_score')
plt.title("Impacto del tipo de almuerzo")
plt.show()

# =========================
# 6. DATASET LIMPIO FINAL
# =========================
df_clean = df.copy()

print("\n=== DATASET LIMPIO ===")
print(df_clean.shape)
print(df_clean.head())

# =========================
# 7. EXPORTAR DATASET
# =========================
df_clean.to_csv("students_performance_clean.csv", index=False)

print("\n✅ Dataset limpio guardado como: students_performance_clean.csv")
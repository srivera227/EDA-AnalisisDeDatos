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
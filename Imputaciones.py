import pandas as pd
import numpy as np

def imputacionMediana(df,columna_job, columna_salario):
    """
    Imputa valores nulos en salary usando la mediana por job_title
    Solo imputa si el registro tiene job_title con datos
    """
    
    print("="*60)
    print(" " * 22 + "IMPUTACIÓN DE SALARIOS POR EMPLEO")
    print("="*60)
    
    # PASO 1: Detectar nulos en salary
    nulos_salary = df[columna_salario].isna()
    total_nulos_inicial = nulos_salary.sum()
    print(f"\nTotal de salarios nulos: {total_nulos_inicial}")
    
    # PASO 2 y 3: Filtrar nulos que tienen job_title con datos
    nulos_con_job = nulos_salary & df[columna_job].notna()
    registros_a_imputar = nulos_con_job.sum()
    print(f"Registros con job_title y que se pueden imputar: {registros_a_imputar}")
    
    if registros_a_imputar == 0:
        print("\nNo hay registros para imputar")
        return df
    
    # PASO 4: Calcular medianas por job
    print(f"Calculando medianas por job...")
    jobs_unicos = df[df[columna_salario].notna()][columna_job].unique()
    medianas = {}
    
    for job in jobs_unicos:
        salarios = df[(df[columna_job] == job) & (df[columna_salario].notna())][columna_salario]
        if len(salarios) > 0:
            medianas[job] = salarios.median()
            print(f"   {job:20} → mediana: {medianas[job]:>12,.2f} (n={len(salarios)})")
    
    # PASO 5: Imputar
    print(f"Imputando valores...")
    imputados = 0
    
    for idx in df[nulos_con_job].index:
        job = df.loc[idx, columna_job]
        if job in medianas:
            df.loc[idx, columna_salario] = medianas[job]
            imputados += 1
    
    # PASO 6: Resultados
    print(f"\n" + "="*60)
    print("RESULTADOS FINALES:")
    print("="*60)
    print(f"Imputados correctamente: {imputados}")
    print(f"Nulos que quedan (sin job_title): {df[columna_salario].isna().sum()}")
    print(f"Porcentaje imputado: {(imputados/total_nulos_inicial*100) if total_nulos_inicial>0 else 0:.1f}%")
    
    return df


    

    
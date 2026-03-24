# EDA-AnalisisDeDatos
Análisis exploratorio de datos para descubrir patrones, tendencias y validar hipótesis. Este repositorio contiene scripts en Python:
Visualizaciones, limpieza de datos. 
Estadísticas descriptivas para obtener insights accionables.

Informe – Análisis Exploratorio de Datos (EDA)
1. Descripción del conjunto de datos

El conjunto de datos contiene información relacionada con salarios en el sector tecnológico.
Las variables disponibles son:

job_title: cargo del empleado
experience_years: años de experiencia
education_level: nivel educativo
skills_count: número de habilidades
industry: industria
company_size: tamaño de la empresa
location: país
remote_work: modalidad de trabajo
certifications: número de certificaciones
salary: salario anual

El objetivo del análisis exploratorio es comprender la estructura de los datos, detectar valores faltantes, identificar valores atípicos y analizar posibles relaciones entre variables, especialmente aquellas que influyen en el salario.

2. Revisión de valores faltantes

Se realizó una verificación para identificar valores nulos en el conjunto de datos.

Ejemplo en Python:

df_procesado.isnull().sum()

Se encontró que la variable experience_years presenta valores faltantes.

Los valores faltantes pueden afectar el análisis, por lo que se deben tratar antes de realizar modelos o conclusiones.

Posibles estrategias:

eliminar registros incompletos
imputar con la media o mediana
crear indicadores de datos faltantes

En este análisis se decidió mantener los datos y considerarlos en la interpretación.

3. Estadísticas descriptivas

Se calcularon estadísticas básicas para la variable salary.

df_procesado["salary"].describe()

Estas estadísticas permiten observar:

valor mínimo
valor máximo
media
mediana
desviación estándar
cuartiles

Se observa que existe una amplia dispersión en los salarios, lo que sugiere la posible presencia de valores atípicos.

4. Análisis gráfico – Boxplot

Se realizó un diagrama de caja para visualizar la distribución del salario.

plt.boxplot(df_procesado["salary"])
plt.show()

El boxplot permite observar:

mediana del salario
rango intercuartílico
valores extremos

Resultados observados:

La mediana se encuentra aproximadamente en el centro del rango.
La mayoría de los salarios se concentra en un intervalo intermedio.
Se detectan varios valores atípicos, especialmente en la parte superior.

Interpretación:

Los valores atípicos pueden corresponder a empleados con alta experiencia, cargos especializados o empresas grandes, aunque también podrían indicar errores en los datos.

5. Diagrama de dispersión

Se realizó un diagrama de dispersión entre experiencia y salario.

plt.scatter(df_procesado["experience_years"], df_procesado["salary"])
plt.show()

Este gráfico permite observar la relación entre variables.

Resultados:

Existe una tendencia general a que el salario aumente con la experiencia.
Se observan puntos alejados del patrón, lo que indica posibles outliers.

Interpretación:

La experiencia parece influir en el salario, pero existen casos que no siguen la tendencia general.

6. Detección de valores atípicos con IQR

Se utilizó el método del rango intercuartílico para detectar valores extremos.

Q1 = df_procesado["salary"].quantile(0.25)
Q3 = df_procesado["salary"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df_procesado[
    (df_procesado["salary"] < limite_inferior) |
    (df_procesado["salary"] > limite_superior)
]

Resultado:

Se detectaron valores que superan los límites establecidos, considerados outliers.

Interpretación:

Estos valores representan salarios inusualmente altos o bajos en comparación con el resto de los datos.

7. Detección de valores atípicos con Z-Score

También se aplicó el método estadístico Z-score.

from scipy.stats import zscore

df_procesado["z_score_salary"] = zscore(df_procesado["salary"])

outliers_z = df_procesado[
    (df_procesado["z_score_salary"] > 3) |
    (df_procesado["z_score_salary"] < -3)
]

Criterio:

Valores con |z| > 3 se consideran atípicos.

Resultados:

Se identificaron registros con valores extremos en el salario.

Interpretación:

Estos datos pueden corresponder a casos especiales o errores.

8. Relación entre variables

Se analizó la relación entre salario y otras variables.

Relaciones evaluadas:

salario vs experiencia
salario vs educación
salario vs tamaño de empresa
salario vs número de habilidades
salario vs certificaciones

Se observa que:

mayor experiencia suele asociarse con mayor salario
empresas grandes tienden a pagar más
más certificaciones pueden relacionarse con salarios mayores
algunos cargos presentan salarios más altos
9. Discusión sobre los valores atípicos

Los valores atípicos pueden tener varias causas:

empleados con mucha experiencia
cargos de alto nivel
empresas grandes
errores en el registro
datos faltantes

Por esta razón, no se eliminaron automáticamente.

En un análisis posterior se podría decidir si eliminarlos o mantenerlos.

10. Conclusiones

El análisis exploratorio permitió comprender la estructura del conjunto de datos.

Principales hallazgos:

existen valores faltantes en algunas variables
el salario presenta alta variabilidad
se detectaron valores atípicos mediante boxplot, IQR y z-score
la experiencia parece influir en el salario
el tamaño de la empresa y el cargo también pueden afectar el salario

El EDA confirma que el dataset es adecuado para realizar análisis más avanzados, aunque se recomienda tratar los valores faltantes y revisar los outliers antes de aplicar modelos estadísticos o de machine learning.

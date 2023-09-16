1. **Importar NumPy**:

   Antes de comenzar, asegúrate de importar NumPy en tu script:

   ```python
   import numpy as np
   ```

2. **Generación de datos de muestra**:

   Vamos a crear un conjunto de datos de muestra para realizar operaciones estadísticas:

   ```python
   data = np.array([12, 15, 17, 18, 22, 24, 25, 28, 30, 35])
   ```

3. **Media (promedio)**:

   ```python
   # Calcular la media de los datos
   mean = np.mean(data)
   ```

4. **Mediana**:

   ```python
   # Calcular la mediana de los datos
   median = np.median(data)
   ```

5. **Moda**:

   ```python
   from scipy import stats

   # Calcular la moda de los datos
   mode = stats.mode(data)
   ```

6. **Desviación estándar y varianza**:

   ```python
   # Calcular la desviación estándar de los datos
   std_deviation = np.std(data)

   # Calcular la varianza de los datos
   variance = np.var(data)
   ```

7. **Percentiles**:

   ```python
   # Calcular el percentil 25 (primer cuartil)
   percentile_25 = np.percentile(data, 25)

   # Calcular el percentil 75 (tercer cuartil)
   percentile_75 = np.percentile(data, 75)
   ```

8. **Rango intercuartil (IQR)**:

   ```python
   # Calcular el rango intercuartil (IQR)
   iqr = np.percentile(data, 75) - np.percentile(data, 25)
   ```

9. **Correlación entre dos conjuntos de datos**:

   Supongamos que tienes dos conjuntos de datos `x` e `y`:

   ```python
   x = np.array([1, 2, 3, 4, 5])
   y = np.array([2, 4, 6, 8, 10])
   ```

   Puedes calcular la correlación entre ellos:

   ```python
   correlation = np.corrcoef(x, y)
   ```

10. **Generación de números aleatorios**:

    Puedes generar números aleatorios utilizando las funciones de NumPy. Por ejemplo, para generar 5 números aleatorios distribuidos uniformemente entre 0 y 1:

    ```python
    random_numbers = np.random.rand(5)
    ```

11. **Regresión lineal simple**:

   Puedes utilizar NumPy para realizar una regresión lineal simple en un conjunto de datos. Supongamos que tienes conjuntos de datos `x` e `y`:

   ```python
   import numpy as np

   x = np.array([1, 2, 3, 4, 5])
   y = np.array([2, 4, 6, 8, 10])
   ```

   Puedes calcular la pendiente (`m`) e intercepto (`b`) de la línea de regresión utilizando NumPy:

   ```python
   m, b = np.polyfit(x, y, 1)
   ```

12. **Análisis de correlación avanzado**:

   Puedes calcular la matriz de correlación entre múltiples variables en un conjunto de datos:

   ```python
   import numpy as np

   data = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

   correlation_matrix = np.corrcoef(data, rowvar=False)
   ```

   Esto te dará una matriz de correlación entre las columnas de `data`.

13. **Estadísticas descriptivas avanzadas**:

   Puedes utilizar NumPy y SciPy para calcular estadísticas descriptivas avanzadas, como la asimetría y la curtosis:

   ```python
   from scipy.stats import skew, kurtosis

   data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

   # Calcular la asimetría
   skewness = skew(data)

   # Calcular la curtosis
   kurt = kurtosis(data)
   ```

14. **Análisis de componentes principales (PCA)**:

   NumPy también se puede utilizar en el análisis de componentes principales para reducir la dimensionalidad de los datos:

   ```python
   from sklearn.decomposition import PCA

   data = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

   pca = PCA(n_components=2)
   pca.fit(data)

   # Obtener los componentes principales
   principal_components = pca.components_
   ```

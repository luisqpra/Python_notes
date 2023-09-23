1. **Interpolar**:
   - **Explicación**: El método `interpolate()` se utiliza para rellenar valores faltantes en una serie o DataFrame mediante la interpolación entre los valores cercanos. Puedes especificar el método de interpolación, como lineal, polinomial, etc.
   - **Ejemplo**:
     ```python
     df['columna'].interpolate(method='linear', inplace=True)
     ```

2. **Negation (~)**:
   - **Explicación**: El operador `~` se utiliza para la negación de valores booleanos en una Serie o DataFrame. Cambia `True` a `False` y viceversa.
   - **Ejemplo**:
     ```python
     df['columna_bool_negada'] = ~df['columna_bool']
     ```

3. **Arange**:
   - **Explicación**: El método `pd.arange()` genera una secuencia de valores numéricos entre un inicio y un final especificados, con un intervalo determinado.
   - **Ejemplo**:
     ```python
     secuencia = pd.arange(start=1, stop=10, step=2)
     ```

4. **iloc**:
   - **Explicación**: El método `iloc` se utiliza para acceder a filas y columnas en un DataFrame por su posición de índice, utilizando números enteros.
   - **Ejemplo**:
     ```python
     valor = df.iloc[0, 2]
     ```

5. **loc**:
   - **Explicación**: El método `loc` se utiliza para acceder a filas y columnas en un DataFrame por etiquetas de índice, utilizando etiquetas o condiciones booleanas.
   - **Ejemplo**:
     ```python
     valor = df.loc[0, 'columna']
     ```

6. **info**:
   - **Explicación**: El método `info()` proporciona información sobre un DataFrame, incluyendo el número de filas, columnas, tipos de datos y uso de memoria.
   - **Ejemplo**:
     ```python
     df.info()
     ```

7. **describe**:
   - **Explicación**: El método `describe()` genera estadísticas descriptivas para columnas numéricas en un DataFrame, como media, desviación estándar y cuartiles.
   - **Ejemplo**:
     ```python
     estadisticas = df.describe() # -> Campos numericos (inlcude=[np.number])
     estadisticas = df.describe(include=object) # -> Campos categoricos
     estadisticas = df.describe(include=All) # -> Todos los campos
     ```

8. **dtypes**:
   - **Explicación**: El atributo `dtypes` muestra los tipos de datos de cada columna en un DataFrame.
   - **Ejemplo**:
     ```python
     tipos_de_datos = df.dtypes
     ```

9. **memory_usage**:
   - **Explicación**: El método `memory_usage()` muestra la cantidad de memoria utilizada por cada columna en un DataFrame.
   - **Ejemplo**:
     ```python
     uso_de_memoria = df.memory_usage(deep=True)
     ```

10. **date_range**:
    - **Explicación**: El método `pd.date_range()` se utiliza para generar un rango de fechas en una Serie de tiempo.
    - **Ejemplo**:
      ```python
      fechas = pd.date_range(start='2023-01-01', end='2023-01-10')
      ```

11. **melt**:
   - **Explicación**: El método `melt` se utiliza para transformar un DataFrame de formato ancho (wide) a formato largo (long) al desenrollar columnas en filas. Esto es útil para reorganizar datos cuando se tienen múltiples columnas que representan variables.
   - **Ejemplo**:
     ```python
     df_melted = pd.melt(df, id_vars=['ID'], value_vars=['Variable1', 'Variable2'])
     ```
     En este ejemplo, estamos derritiendo el DataFrame `df` para mantener la columna `ID` como identificador y desenrollar las columnas `Variable1` y `Variable2` en filas.

12. **apply**:
   - **Explicación**: El método `apply` se utiliza para aplicar una función personalizada a una columna o fila en un DataFrame. Puedes utilizarlo para realizar operaciones más complejas en los datos.
   - **Ejemplo**:
     ```python
     def funcion_personalizada(x):
         return x * 2

     df['nueva_columna'] = df['columna'].apply(funcion_personalizada)
     ```
     En este ejemplo, estamos aplicando la función `funcion_personalizada` a la columna `columna` del DataFrame `df` para crear una nueva columna llamada `nueva_columna` que contiene el resultado de la función aplicada a cada elemento de la columna.

Claro, aquí tienes algunos ejemplos de cómo usar la biblioteca NumPy en Python para realizar operaciones de álgebra lineal básicas:

1. **Importar NumPy**:

   Antes de utilizar NumPy, asegúrate de importarlo en tu script o entorno de Python:

   ```python
   import numpy as np
   ```

2. **Creación de matrices**:

   Puedes crear matrices NumPy utilizando la función `np.array()` o funciones especiales como `np.zeros()`, `np.ones()`, `np.eye()` y `np.random` para matrices aleatorias.

   ```python
   import numpy as np

   # Crear una matriz
   A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

   # Crear una matriz de ceros
   zeros_matrix = np.zeros((3, 3))

   # Crear una matriz de unos
   ones_matrix = np.ones((2, 2))

   # Crear una matriz identidad
   identity_matrix = np.eye(4)

   # Crear una matriz aleatoria
   random_matrix = np.random.rand(3, 3)
   ```

3. **Operaciones de álgebra lineal**:

   a. **Multiplicación de matrices**:

   ```python
   import numpy as np

   A = np.array([[1, 2], [3, 4]])
   B = np.array([[5, 6], [7, 8]])

   # Multiplicación de matrices
   C = np.dot(A, B)
   # También puedes usar A @ B para multiplicación de matrices en Python 3.5+
   ```

   b. **Determinante de una matriz**:

   ```python
   import numpy as np

   A = np.array([[1, 2], [3, 4]])

   # Calcular el determinante de A
   det_A = np.linalg.det(A)
   ```

   c. **Inversa de una matriz**:

   ```python
   import numpy as np

   A = np.array([[1, 2], [3, 4]])

   # Calcular la inversa de A
   inv_A = np.linalg.inv(A)
   ```

   d. **Resolución de sistemas de ecuaciones lineales**:

   ```python
   import numpy as np

   A = np.array([[2, 3], [1, -2]])
   b = np.array([5, 1])

   # Resolver el sistema Ax = b
   x = np.linalg.solve(A, b)
   ```

Estos son solo algunos ejemplos básicos de cómo NumPy se utiliza en álgebra lineal en Python. NumPy proporciona muchas más funciones y capacidades para operaciones avanzadas de álgebra lineal.
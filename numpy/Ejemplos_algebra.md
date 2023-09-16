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

4. **Descomposiciones de matrices**:

   a. **Descomposición LU**:

   ```python
   import numpy as np

   A = np.array([[2, 3], [1, 4]])

   # Descomposición LU
   P, L, U = scipy.linalg.lu(A)
   ```

   b. **Descomposición QR**:

   ```python
   import numpy as np

   A = np.array([[2, -1], [1, 2], [1, 2]])

   # Descomposición QR
   Q, R = np.linalg.qr(A)
   ```

5. **Valores y vectores propios**:

   ```python
   import numpy as np

   A = np.array([[4, -2], [1, 1]])

   # Calcular valores y vectores propios
   eigenvalues, eigenvectors = np.linalg.eig(A)
   ```

6. **Factorización de matrices**:

   a. **Factorización de valores singulares (SVD)**:

   ```python
   import numpy as np

   A = np.array([[1, 2, 3], [4, 5, 6]])

   # Factorización SVD
   U, S, V = np.linalg.svd(A)
   ```

   b. **Factorización de Cholesky**:

   ```python
   import numpy as np

   A = np.array([[4, 6, 8], [6, 13, 17], [8, 17, 30]])

   # Factorización de Cholesky
   L = np.linalg.cholesky(A)
   ```

7. **Funciones para matrices especiales**:

   a. **Matriz de Hilbert**:

   ```python
   import numpy as np

   n = 4

   # Matriz de Hilbert
   H = np.linalg.hilbert(n)
   ```

   b. **Matriz de Vandermonde**:

   ```python
   import numpy as np

   x = np.array([1, 2, 3, 4])

   # Matriz de Vandermonde
   V = np.vander(x)
   ```

8. **Cálculos avanzados de matrices**:

   a. **Normas matriciales**:

   ```python
   import numpy as np

   A = np.array([[1, 2], [3, 4]])

   # Norma Frobenius
   norm_frobenius = np.linalg.norm(A, 'fro')

   # Norma de Frobenius al cuadrado
   norm_frobenius_squared = np.linalg.norm(A, 'fro')**2
   ```

   b. **Rango de una matriz**:

   ```python
   import numpy as np

   A = np.array([[1, 2], [3, 4], [5, 6]])

   # Calcular el rango de A
   rank_A = np.linalg.matrix_rank(A)
   ```
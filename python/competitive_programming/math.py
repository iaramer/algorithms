import numpy as np

A = np.array([
    [3, 1, 2, 1],
    [1, 2, 1, 1],
    [1, 0, 3, 2],
    [1, 1, 2, 0]
])

# Matrix trace
np.trace(A)
A.trace()

# Matrix rank
np.linalg.matrix_rank(A)

# Matrix determinant
np.linalg.det(A)

# Inverse matrix
B = np.linalg.inv(A)

# Eigenvalues and eigenvectors
np.linalg.eig(A)  # both
np.linalg.eigvals(A)  # only eigenvalues

# Matrix multiplication
A @ B

# Solve linear equation (find X vector of unknown)
b = [1, 1, 1]
np.linalg.solve(A, b)  # Matrix should not have determinant = 0

import random

random.choice([2, 5, 9])

random.randint(0, 1)

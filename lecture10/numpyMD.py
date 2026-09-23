import numpy as np

random_martrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 Matrix:\n", random_martrix)

martrix_sum = np.sum(random_martrix)
print(f"\nSum of all element: {martrix_sum}")

martrix_mean = np.mean(random_martrix)
print(f"\nMean of the matrix: {martrix_mean:2.2f}")

transposed_matrix = np.transpose(random_martrix)
print("\nTranspose Matrix:\n", transposed_matrix)

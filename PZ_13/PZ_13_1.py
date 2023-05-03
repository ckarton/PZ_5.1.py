# В матрице найти минимальный элемент в предпоследнем столбце

def find_min_element(matrix):
  min_element = matrix[0][-2]
  for row in matrix:
    if row[-2] < min_element:
      min_element = row[-2]
  return min_element

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]
print("Минимальный элемент в предпоследнем столбце:", find_min_element(matrix))
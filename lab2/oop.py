from typing import List, Union
from numbers import Number


class Matrix:
    """Матрица в ООП стиле"""

    def __init__(self, data: List[List[float]]) -> None:
        self._validate_matrix(data)
        self._data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def _validate_matrix(self, data: List[List[float]]) -> None:
        if not data:
            return
        cols = len(data[0])
        for i, row in enumerate(data):
            if len(row) != cols:
                raise ValueError(
                    f"All rows must have the same length. Row {i} has {len(row)} elements, expected {cols}")

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Сложение матриц"""
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = [
            [self._data[i][j] + other._data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other: Union['Matrix', Number]) -> 'Matrix':
        """Умножение матриц или на скаляр"""
        if isinstance(other, Number):
            # Умножение на скаляр
            result = [
                [self._data[i][j] * other for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        elif isinstance(other, Matrix):
            # Умножение матриц
            if self.cols != other.rows:
                raise ValueError("Number of columns in first matrix must equal number of rows in second")

            result = [[0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result[i][j] += self._data[i][k] * other._data[k][j]
            return Matrix(result)
        else:
            return NotImplemented

    def __rmul__(self, other: Number) -> 'Matrix':
        """Умножение скаляра на матрицу"""
        if isinstance(other, Number):
            return self * other
        return NotImplemented

    def transpose(self) -> 'Matrix':
        """Транспонирование матрицы"""
        result = [
            [self._data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(result)

    def determinant(self) -> float:
        """Вычисление определителя матрицы"""
        if self.rows != self.cols:
            raise ValueError("Determinant is defined only for square matrices")

        if self.rows == 1:
            return self._data[0][0]
        elif self.rows == 2:
            return self._data[0][0] * self._data[1][1] - self._data[0][1] * self._data[1][0]
        elif self.rows == 3:
            # Правило Саррюса для матрицы 3x3
            a, b, c = self._data[0]
            d, e, f = self._data[1]
            g, h, i = self._data[2]
            return a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h
        else:
            # Рекурсивное вычисление для матриц большего порядка
            det = 0
            for j in range(self.cols):
                minor = []
                for i in range(1, self.rows):
                    row = []
                    for k in range(self.cols):
                        if k != j:
                            row.append(self._data[i][k])
                    minor.append(row)
                det += ((-1) ** j) * self._data[0][j] * Matrix(minor).determinant()
            return det

    def __str__(self) -> str:
        return '\n'.join([' '.join(f'{elem:6.1f}' for elem in row) for row in self._data])

    def __repr__(self) -> str:
        return f"Matrix({self._data})"



if __name__ == "__main__":
    print("=== ООП реализация матриц ===")

    m1 = Matrix([[1, 2], [2, 3]])
    m2 = Matrix([[2, 5], [7, 9]])

    print("m1 =", m1._data)
    print("m2 =", m2._data)

    m3 = m1 + m2
    m4 = m1 * m2
    m5 = m1.transpose()
    det = m1.determinant()

    print("\n--- Результаты операций ---")
    print("m1 + m2 =", m3._data)
    print("m1 * m2 =", m4._data)
    print("m1.transpose() =", m5._data)
    print("m1.determinant() =", det)


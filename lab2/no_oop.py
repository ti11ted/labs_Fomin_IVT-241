from typing import List, Union
from numbers import Number


def create_matrix(data: List[List[float]]) -> List[List[float]]:
    """Создать матрицу"""
    _validate_matrix(data)
    return [row[:] for row in data]


def _validate_matrix(data: List[List[float]]) -> None:
    if not data:
        return
    cols = len(data[0])
    for i, row in enumerate(data):
        if len(row) != cols:
            raise ValueError(f"All rows must have the same length. Row {i} has {len(row)} elements, expected {cols}")


def matrix_add(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Сложение матриц"""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matrix_multiply(a: List[List[float]], b: Union[List[List[float]], Number]) -> List[List[float]]:
    """Умножение матриц или на скаляр"""
    if isinstance(b, Number):
        # Умножение на скаляр
        return [
            [a[i][j] * b for j in range(len(a[0]))]
            for i in range(len(a))
        ]
    else:
        # Умножение матриц
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in first matrix must equal number of rows in second")

        result = [[0] * len(b[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    result[i][j] += a[i][k] * b[k][j]
        return result


def matrix_transpose(a: List[List[float]]) -> List[List[float]]:
    """Транспонирование матрицы"""
    return [
        [a[j][i] for j in range(len(a))]
        for i in range(len(a[0]))
    ]


def matrix_determinant(a: List[List[float]]) -> float:
    """Вычисление определителя матрицы"""
    if len(a) != len(a[0]):
        raise ValueError("Determinant is defined only for square matrices")

    n = len(a)
    if n == 1:
        return a[0][0]
    elif n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    elif n == 3:
        # Правило Саррюса для матрицы 3x3
        return (a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1]
                - a[0][2] * a[1][1] * a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1])
    else:
        # Рекурсивное вычисление для матриц большего порядка
        det = 0
        for j in range(n):
            minor = []
            for i in range(1, n):
                row = []
                for k in range(n):
                    if k != j:
                        row.append(a[i][k])
                minor.append(row)
            det += ((-1) ** j) * a[0][j] * matrix_determinant(minor)
        return det



if __name__ == "__main__":
    print("=== Функциональная реализация матриц ===")


    m1 = create_matrix([[1, 2], [2, 3]])
    m2 = create_matrix([[2, 5], [7, 9]])

    print("m1 =", m1)
    print("m2 =", m2)

    m3 = matrix_add(m1, m2)
    m4 = matrix_multiply(m1, m2)
    m5 = matrix_transpose(m1)
    det = matrix_determinant(m1)

    print("\n--- Результаты операций ---")
    print("matrix_add(m1, m2) =", m3)
    print("matrix_multiply(m1, m2) =", m4)
    print("matrix_transpose(m1) =", m5)
    print("matrix_determinant(m1) =", det)


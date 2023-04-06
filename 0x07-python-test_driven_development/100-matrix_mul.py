#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a (list): a list of lists of integers or floats.
        m_b (list): a list of lists of integers or floats.

    Returns:
        A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError: if m_a or m_b is not a list or a list of lists, or if an element in the lists is not an integer or a float, or if each row of m_a or m_b is not of the same size.
        ValueError: if m_a or m_b is empty or if m_a and m_b cannot be multiplied.
    """
    # Validate input matrices
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(val, (int, float)) for row in m_a for val in row) or not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Compute matrix product
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = 0
            for k in range(len(m_b)):
                val += m_a[i][k] * m_b[k][j]
                row.append(val)
                result.append(row)
                return result

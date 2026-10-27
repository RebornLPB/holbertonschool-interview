# Rotate 2D Matrix

## Description
This project rotates an `n x n` 2D matrix **90 degrees clockwise, in place**: the matrix is edited directly instead of returning a new one. The solution transposes the matrix (swapping `matrix[i][j]` with `matrix[j][i]`), then reverses each row.

The script targets **Python 3.8+**.

## 📝 Learning Objectives
* Manipulate a 2D list and swap elements without extra memory.
* Understand a rotation as a **transpose + row reversal**.
* Modify a mutable argument in place (the function returns nothing).

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** Code is meant to follow the PEP 8 style guide (check with `pycodestyle`).
* **Prototype:** `def rotate_2d_matrix(matrix)`
* **Constraint:** The matrix is assumed to be a valid square matrix; it must be edited in place (no new matrix allocated).

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-rotate_2d_matrix.py` | Rotate 2D Matrix | `rotate_2d_matrix(matrix)` rotates a square matrix 90° clockwise in place. |

---

## 🚀 Execution & PEP 8 Testing

```bash
python3 -c "
from importlib import util
spec = util.spec_from_file_location('r', '0-rotate_2d_matrix.py')
m = util.module_from_spec(spec)
spec.loader.exec_module(m)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m.rotate_2d_matrix(matrix)
print(matrix)   # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
"
```

```bash
pycodestyle 0-rotate_2d_matrix.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

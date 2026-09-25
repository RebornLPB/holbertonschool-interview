# Pascal's Triangle

## Description
This project builds **Pascal's Triangle** as a list of lists of integers, where each row is derived from the previous one by summing adjacent pairs.

The script targets **Python 3.8+** and follows the **PEP 8** style guide.

## 📝 Learning Objectives
* Generate a data structure incrementally, row by row, from a base case.
* Manipulate nested lists (list of lists) in Python.
* Handle edge cases such as `n <= 0`.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Prototype:** `def pascal_triangle(n)`

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-pascal_triangle.py` | Pascal's Triangle | `pascal_triangle(n)` returns a list of lists of integers representing Pascal's Triangle of `n` rows (an empty list if `n <= 0`). |

---

## 🚀 Execution & PEP 8 Testing

```bash
python3 -c "
from importlib import util
spec = util.spec_from_file_location('pt', '0-pascal_triangle.py')
m = util.module_from_spec(spec)
spec.loader.exec_module(m)
print(m.pascal_triangle(5))
"
```

```bash
pycodestyle 0-pascal_triangle.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

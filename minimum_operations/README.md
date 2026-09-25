# Minimum Operations

## Description
This project solves the **"Copy & Paste"** interview problem: starting with a single `H` character on a notepad, and using only `Copy All` and `Paste` operations, find the fewest operations needed to reach exactly `n` `H` characters. This is equivalent to summing the prime factors of `n` (with multiplicity).

The script targets **Python 3.8+** and follows the **PEP 8** style guide.

## 📝 Learning Objectives
* Reduce a seemingly combinatorial problem to prime factorization.
* Implement trial division to factorize an integer.
* Handle base cases (`n <= 1` requires 0 operations).

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Prototype:** `def minOperations(n)`

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-minoperations.py` | Minimum Operations | `minOperations(n)` returns the fewest `Copy All`/`Paste` operations needed to reach `n` characters, computed as the sum of the prime factors of `n`. |

---

## 🚀 Execution & PEP 8 Testing

```bash
python3 -c "
from importlib import util
spec = util.spec_from_file_location('mo', '0-minoperations.py')
m = util.module_from_spec(spec)
spec.loader.exec_module(m)
print(m.minOperations(9))
"
```

```bash
pycodestyle 0-minoperations.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

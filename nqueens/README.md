# N Queens

## Description
This project solves the classic **N queens puzzle**: place `N` non-attacking queens on an `N x N` chessboard. The program is run with `N` as argument and prints **every** solution, one per line, as a list of `[row, column]` coordinates. It uses **backtracking**: queens are placed row by row, and a column is rejected if it shares a column or a diagonal with a queen already placed.

The script targets **Python 3.8+**.

## 📝 Learning Objectives
* Solve a constraint-satisfaction problem with **recursion and backtracking**.
* Detect column and diagonal conflicts (`abs(c - col) == abs(r - row)`).
* Validate command-line arguments and exit with the right status.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** Code is meant to follow the PEP 8 style guide (check with `pycodestyle`).
* **Usage:** `./0-nqueens.py N`
* **Errors (exit status `1`):**
  * Wrong number of arguments → `Usage: nqueens N`
  * `N` is not an integer → `N must be a number`
  * `N` is smaller than 4 → `N must be at least 4`

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-nqueens.py` | N queens | Prints all the solutions of the N queens problem as lists of `[row, column]` pairs. |

---

## 🚀 Execution & PEP 8 Testing

```bash
chmod +x 0-nqueens.py
./0-nqueens.py 4
```

Expected output:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
pycodestyle 0-nqueens.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

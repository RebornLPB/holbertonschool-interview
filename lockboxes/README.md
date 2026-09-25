# Lockboxes

## Description
This project solves the classic **"can you open every box?"** interview problem: given a list of boxes, each containing keys to other boxes, determine whether every box can eventually be unlocked starting from box `0` (which is always unlocked).

The script targets **Python 3.8+** and follows the **PEP 8** style guide.

## 📝 Learning Objectives
* Model a reachability problem as a graph/BFS traversal using sets and a queue-like list.
* Reason about time complexity when every box and every key must be visited.
* Handle edge cases: an empty list of boxes, or keys pointing outside the valid range.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Prototype:** `def canUnlockAll(boxes)`

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-lockboxes.py` | Lockboxes | `canUnlockAll(boxes)` returns `True` if all boxes can be opened starting from box `0`, `False` otherwise. |

---

## 🚀 Execution & PEP 8 Testing

```bash
python3 -c "
from importlib import util
spec = util.spec_from_file_location('lockboxes', '0-lockboxes.py')
m = util.module_from_spec(spec)
spec.loader.exec_module(m)
print(m.canUnlockAll([[1], [2], [3], []]))
"
```

```bash
pycodestyle 0-lockboxes.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

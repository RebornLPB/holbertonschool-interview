# UTF-8 Validation

## Description
This project checks whether a list of integers is a valid **UTF-8** encoding. A character can span 1 to 4 bytes: a leading byte announces how many bytes the character uses (`0xxxxxxx`, `110xxxxx`, `1110xxxx`, `11110xxx`) and every following byte must start with the bits `10`. Only the 8 least significant bits of each integer are considered.

The script targets **Python 3.8+**.

## 📝 Learning Objectives
* Understand how UTF-8 encodes characters on 1 to 4 bytes.
* Use bitwise operators (`&`, `>>`) to inspect the leading bits of a byte.
* Track state across a loop (number of continuation bytes still expected).
* Handle edge cases: invalid leading bytes (`10xxxxxx`, more than 4 bytes) and truncated sequences.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** Code is meant to follow the PEP 8 style guide (check with `pycodestyle`).
* **Prototype:** `def validUTF8(data)`

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-validate_utf8.py` | UTF-8 Validation | `validUTF8(data)` returns `True` if `data` is a valid UTF-8 sequence, `False` otherwise. |

---

## 🚀 Execution & PEP 8 Testing

```bash
python3 -c "
from importlib import util
spec = util.spec_from_file_location('v', '0-validate_utf8.py')
m = util.module_from_spec(spec)
spec.loader.exec_module(m)
print(m.validUTF8([65]))                    # True
print(m.validUTF8([229, 65, 127, 256]))     # False
print(m.validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]))  # True
"
```

```bash
pycodestyle 0-validate_utf8.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

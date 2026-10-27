# Log Parsing

## Description
This project reads an access log from standard input, line by line, and computes metrics: the **total file size** and the **number of lines per HTTP status code**. Statistics are printed every 10 lines and once more at the end of the input or when the program is interrupted with `CTRL + C`.

Each line is expected to end with `<status code> <file size>`, e.g.:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

The script targets **Python 3.8+**.

## 📝 Learning Objectives
* Process a stream from `sys.stdin` line by line.
* Parse text with `str.split` and ignore malformed lines (`ValueError`, `IndexError`).
* Aggregate values in a dictionary and print them sorted by key.
* Handle `KeyboardInterrupt` to print final statistics on `CTRL + C`.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** Code is meant to follow the PEP 8 style guide (check with `pycodestyle`).
* **Status codes tracked:** `200`, `301`, `400`, `401`, `403`, `404`, `405`, `500` (only codes with at least one occurrence are printed).
* **Output format:** `File size: <total>` followed by `<status code>: <number>` lines in ascending order.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-stats.py` | Log parsing | Reads log lines from `stdin`, sums the file sizes, counts the status codes, and prints the statistics every 10 lines and on exit / `CTRL + C`. |

---

## 🚀 Execution & PEP 8 Testing

```bash
printf '1.2.3.4 - [2024-01-01] "GET /projects/260 HTTP/1.1" 200 512\n' | ./0-stats.py
```

Or feed it a generated log:

```bash
./0-stats.py < access.log
```

```bash
pycodestyle 0-stats.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)

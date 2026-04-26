# SQL Guide: Code-Along repository

Course: "Learn SQL: The Hands-on Guide with interactive exercises"

Link: https://www.udemy.com/course/sql-guide/

Author: Jannis Seemann

---

# Using PostgreSQL from Python

## Use a virtual environment (venv)

Create new Virtual Environment:

```bash
python3 -m venv ./.venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

After this, we can install Python packages using "pip".

## Using `psycopg`

Package Documentation: https://www.psycopg.org/psycopg3/

Install using PIP:

```bash
pip install "psycopg[binary,pool]"
```

Then run `pip freeze` to mention dependencies in a .txt file:

```bash
pip freeze > requirements.txt
```
